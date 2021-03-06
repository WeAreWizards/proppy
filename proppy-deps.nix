### DO NOT EDIT BY HAND! this package was auto generated by pypi2nix ####
### For more info go to: https://www.github.com/offlinehacker/pypi2nix

{ pkgs, python, buildPythonPackage, self, overrides }:
  with pkgs.lib;
let
  isPy26 = python.majorVersion == "2.6";
  isPy27 = python.majorVersion == "2.7";
  isPy33 = python.majorVersion == "3.3";
  isPy34 = python.majorVersion == "3.4";
  isPyPy = python.executable == "pypy";

  # Unique python version identifier
  pythonName =
    if isPy26 then "python26" else
    if isPy27 then "python27" else
    if isPy33 then "python33" else
    if isPy34 then "python34" else
    if isPyPy then "pypy" else "";

  fetchurl = pkgs.fetchurl;

  callOverride = pkg: override:
    if (isFunction override) then (override pkg) else override;

  attrByPathAlternatives = alt: default: e:
    if alt==[] then default else
      attrByPath (head alt) (attrByPathAlternatives (drop 1 alt) default e) e;

  overridablePythonPackage = pkg: buildPythonPackage (
    pkg // (callOverride pkg (
      attrByPathAlternatives ([[pkg.basename] [pkg.name]]) {} overrides)
    )
  );

  callPythonPackage = args@ { name, installRequires, extra ? {}, ... }: use_extra:
    overridablePythonPackage ((args // {extra="";}) // {
      propagatedBuildInputs =
        installRequires ++
        (map (ex: attrByPath [ex] [] extra) use_extra);
      name = name +
        (optionalString (use_extra!=[]) "-") +
        (concatStringsSep "_" use_extra);
    });

in {}
############### Aliases #####################################################

// (optionalAttrs (pythonName == "python34") {
    "pytoml" = self.by-version."pytoml-0.1.2" [];
    generated."pytoml" = self.by-version."pytoml-0.1.2" [];
    by-extra."default"."pytoml" = self.by-version."pytoml-0.1.2" [];

    "weasyprint" = self.by-version."weasyprint-0.23" [];
    generated."weasyprint" = self.by-version."weasyprint-0.23" [];
    by-extra."default"."weasyprint" = self.by-version."weasyprint-0.23" [];

  })


############### Packages ####################################################
// {}

// (optionalAttrs (pythonName == "python34") {

  by-version."cffi-0.9.2" = callPythonPackage {
    name = "cffi-0.9.2";
    basename = "cffi";
    version = "0.9.2";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/c/cffi/cffi-0.9.2.tar.gz";
        md5 = "b1bf4625ae07a8a932f2f1a2eb200c54";
    };

    doCheck =false;

    buildInputs = [ pkgs.libffi ];
    installRequires = [(self.by-version."pycparser-2.10" []) ];
    extra = {

    };
  };

  by-version."pyphen-0.9.1" = callPythonPackage {
    name = "pyphen-0.9.1";
    basename = "pyphen";
    version = "0.9.1";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/P/Pyphen/Pyphen-0.9.1.tar.gz";
        md5 = "024fe88b78e7b65f02cba1c3165223e6";
    };

    doCheck =false;

    buildInputs = [];
    installRequires = [];
    extra = {

    };
  };

  by-version."lxml-3.4.2" = callPythonPackage {
    name = "lxml-3.4.2";
    basename = "lxml";
    version = "3.4.2";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/l/lxml/lxml-3.4.2.tar.gz";
        md5 = "429e5e771c4be0798923c04cb9739b4e";
    };

    doCheck =false;

    buildInputs = [ pkgs.libxml2 pkgs.libxslt ];
    installRequires = [];
    extra = {

    };
  };

  by-version."pycparser-2.10" = callPythonPackage {
    name = "pycparser-2.10";
    basename = "pycparser";
    version = "2.10";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/p/pycparser/pycparser-2.10.tar.gz";
        md5 = "d87aed98c8a9f386aa56d365fe4d515f";
    };

    doCheck =false;

    buildInputs = [];
    installRequires = [];
    extra = {

    };
  };

  by-version."html5lib-0.999" = callPythonPackage {
    name = "html5lib-0.999";
    basename = "html5lib";
    version = "0.999";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/h/html5lib/html5lib-0.999.tar.gz";
        md5 = "acb8ba4d6db5637360a07859192eb7f8";
    };

    doCheck =false;

    buildInputs = [];
    installRequires = [(self.by-version."six-1.8.0" []) ];
    extra = {

    };
  };

  by-version."cairocffi-0.6" = callPythonPackage {
    name = "cairocffi-0.6";
    basename = "cairocffi";
    version = "0.6";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/c/cairocffi/cairocffi-0.6.tar.gz";
        md5 = "af0e93b31be42a8f2be23b1234336496";
    };

    doCheck =false;

    buildInputs = [ pkgs.cairo ];
    installRequires = [(self.by-version."cffi-0.9.2" []) ];
    extra = {

    };
  };

  by-version."six-1.8.0" = callPythonPackage {
    name = "six-1.8.0";
    basename = "six";
    version = "1.8.0";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/s/six/six-1.8.0.tar.gz";
        md5 = "1626eb24cc889110c38f7e786ec69885";
    };

    doCheck =false;

    buildInputs = [];
    installRequires = [];
    extra = {

    };
  };

  by-version."tinycss-0.3" = callPythonPackage {
    name = "tinycss-0.3";
    basename = "tinycss";
    version = "0.3";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/t/tinycss/tinycss-0.3.tar.gz";
        md5 = "13999e54453d4fbc9d1539f4b95d235e";
    };

    doCheck =false;

    buildInputs = [];
    installRequires = [];
    extra = {

    };
  };

  by-version."cairosvg-1.0.13" = callPythonPackage {
    name = "cairosvg-1.0.13";
    basename = "cairosvg";
    version = "1.0.13";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/C/CairoSVG/CairoSVG-1.0.13.tar.gz";
        md5 = "d8bcbaa71962f0595546274c3f15eb09";
    };

    doCheck =false;

    buildInputs = [];
    installRequires = [(self.by-version."cairocffi-0.6" []) ];
    extra = {

    };
  };

  by-version."pytoml-0.1.2" = callPythonPackage {
    name = "pytoml-0.1.2";
    basename = "pytoml";
    version = "0.1.2";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/p/pytoml/pytoml-0.1.2.zip";
        md5 = "183a829b7b05cd65eebc94f7d02d32d8";
    };

    doCheck =true;

    buildInputs = [];
    installRequires = [];
    extra = {

    };
  };


  by-version."weasyprint-0.23" =
  callPythonPackage {
    name = "weasyprint-0.23";
    basename = "weasyprint";
    version = "0.23";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/W/WeasyPrint/WeasyPrint-0.23.tar.gz";
        md5 = "4b66302fa685f5e183a5f912eccb02e0";
    };

    doCheck = false;

    buildInputs = [ pkgs.cairo pkgs.glib pkgs.pango ];
    preBuild = ''
      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.cairo}/lib:${pkgs.glib}/lib:${pkgs.pango}/lib
    '';
    installRequires = [(self.by-version."cffi-0.9.2" []) (self.by-version."cairosvg-1.0.13" []) (self.by-version."cssselect-0.9.1" []) (self.by-version."cairocffi-0.6" []) (self.by-version."lxml-3.4.2" []) (self.by-version."tinycss-0.3" []) (self.by-version."pyphen-0.9.1" []) (self.by-version."html5lib-0.999" []) ];
    extra = {

    };
  };

  by-version."cssselect-0.9.1" = callPythonPackage {
    name = "cssselect-0.9.1";
    basename = "cssselect";
    version = "0.9.1";

    src = fetchurl {
        url = "https://pypi.python.org/packages/source/c/cssselect/cssselect-0.9.1.tar.gz";
        md5 = "c74f45966277dc7a0f768b9b0f3522ac";
    };

    doCheck =false;

    buildInputs = [];
    installRequires = [];
    extra = {

    };
  };

})
