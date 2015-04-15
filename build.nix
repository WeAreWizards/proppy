{ pkgs ? import <nixpkgs> {} }:
let
deps = pkgs.callPackage ./proppy-deps.nix {
         python = pkgs.python34;
         buildPythonPackage = pkgs.python34Packages.buildPythonPackage;
         self = deps;
         overrides = "";
       };
in
pkgs.python34Packages.buildPythonPackage {
  name = "proppy-0.01";
  srcs = ./.;
  propagatedBuildInputs = [
    deps.weasyprint
    deps.pytoml
    pkgs.python34Packages.jinja2
    pkgs.cairo
  ] ++ deps.weasyprint.installRequires;

  # weasyprint uses a terrible system to load SOs
  postInstall = ''
    wrapProgram $out/bin/proppy \
      --prefix LD_LIBRARY_PATH : ${pkgs.cairo}/lib:${pkgs.cairo}/lib:${pkgs.glib}/lib:${pkgs.pango}/lib
  '';

}
