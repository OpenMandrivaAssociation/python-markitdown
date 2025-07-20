%define module markitdown

Name:		python-markitdown
Version:	0.1.2
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

%description
Python tool for converting files and office documents to Markdown. 

%prep
%autosetup -p1 -n %{module}-%{version}

%files
