{ lib, buildPythonPackage, python }:

buildPythonPackage rec {
  pname = "unicode-clock";
  version = "0.1";

  src = ./.;

  format = "other";
  phases = [ "unpackPhase" "installPhase" "fixupPhase" ];

  installPhase = ''
    mkdir -p $out/bin
    install -Dm755 unicode_clock/__init__.py $out/${python.sitePackages}/unicode_clock/__init__.py
    install -Dm644 README.md $out/share/doc/unicode-clock/README.md
    ln -s $out/${python.sitePackages}/unicode_clock/__init__.py $out/bin/unicode-clock
  '';

  postFixup = "patchShebangs $out/${python.sitePackages}/unicode_clock/";

  meta = with lib; {
    description = "Get unicode clock symbol for a time";
    license = licenses.gpl3;
    maintainers = [ maintainers.sternenseemann ];
  };
}

