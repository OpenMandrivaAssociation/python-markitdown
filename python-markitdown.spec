%undefine _debugsource_packages
%define module markitdown

Name:		python-markitdown
Version:	0.1.3
Release:	1
Summary:	Python tool for converting files and office documents to Markdown. 
URL:		https://github.com/microsoft/markitdown
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/m/markitdown/markitdown-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:  python-hatchling

Requires: python3dist(magika)
Requires: python3dist(requests)
Requires: python3dist(markdownify)
Requires: python3dist(charset-normalizer)
Requires: python3dist(defusedxml)
Requires: python3dist(onnxruntime)

#Optional:
Requires: python3dist(lxml)
Requires: python3dist(youtube-transcript-api)
#FIXME. It require a lot of optional python stuff. Lets add it in near future.

%description
Python tool for converting files and office documents to Markdown. 

%prep
%autosetup -p1 -n %{module}-%{version}

# try relax dependencies
sed -i 's/magika~=0\.6\.1/magika>=1.0.1/' pyproject.toml

%files
%{_bindir}/markitdown
%{python_sitelib}/markitdown-%{version}.dist-info
%{python_sitelib}/markitdown
