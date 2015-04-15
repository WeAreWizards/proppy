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
  name = "proppy";
  srcs = ./.;
  propagatedBuildInputs = [
    deps.weasyprint
    deps.pytoml
    pkgs.python34Packages.jinja2
  ] ++ deps.weasyprint.installRequires;
  shellHook = ''
      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.cairo}/lib:${pkgs.glib}/lib:${pkgs.pango}/lib
  '';
}
