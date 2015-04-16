{ pkgs ? import <nixpkgs> {} }:

let
pytoml = pkgs.python34Packages.buildPythonPackage {
  name = "pytoml-0.1.2";
  basename = "pytoml";
  version = "0.1.2";
  src = pkgs.fetchurl {
    url = "https://pypi.python.org/packages/source/p/pytoml/pytoml-0.1.2.zip";
    md5 = "183a829b7b05cd65eebc94f7d02d32d8";
  };
};
pdfkit = pkgs.python34Packages.buildPythonPackage rec {
  name = "pdfkit-0.5.0";
  propagatedBuildInputs = with pkgs.python34Packages; [  ];
  src = pkgs.fetchurl {
    url = "https://pypi.python.org/packages/source/p/pdfkit/pdfkit-0.5.0.zip";
    md5 = "5cbe42c43d463f0794272a01e37a553f";
  };
  doCheck = false;
  meta = with pkgs.stdenv.lib; {
    description = "Python-PDFKit: HTML to PDF wrapper";
    license = licenses.mit;
  };
};

in
pkgs.python34Packages.buildPythonPackage {
  name = "proppy-0.01";
  srcs = ./.;
  propagatedBuildInputs = [
    pkgs.wkhtmltopdf
    pytoml
    pdfkit
    pkgs.python34Packages.jinja2
    pkgs.cairo
  ];
}
