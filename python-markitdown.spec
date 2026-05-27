%undefine _debugsource_packages
%define module markitdown

Name:		python-markitdown
Version:	0.1.6
Release:	1
Summary:	Python tool for converting files and office documents to Markdown
License:	MIT
Group:		Development/Python
URL:		https://github.com/microsoft/markitdown
Source0:	https://files.pythonhosted.org/packages/source/m/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

#Optional:
Recommends: python%{pyver}dist(lxml)
Recommends: python%{pyver}dist(youtube-transcript-api)
#FIXME. It require a lot of optional python stuff. Lets add it in near future.

%description
%{module} is a Python package and command-line utility for converting various
files to Markdown (e.g., for indexing, text analysis, etc).

%prep -a
# try relax dependencies
sed -i 's/magika~=0\.6\.1/magika>=1.0.1/' pyproject.toml

%files
%doc README.md
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
