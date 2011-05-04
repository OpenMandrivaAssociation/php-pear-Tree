%define		_class		Tree
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.3.4
Release:	%mkrel 5
Summary:	Generic tree management
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Tree/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Provides methods to read and manipulate trees, which are stored in the
DB or an XML file. The trees can be stored in the DB either as nested
trees or as simple trees ('brain dead method'), which use
parentId-like structure. Currently XML data can only be read from a
file and accessed. The package offers a big number of methods to
access and manipulate trees. For example methods like: getRoot,
getChild[ren], getParent, getPath and many more. There are two ways of
retrieving the data from the place where they are stored, one is by
reading the entire tree into the memory - the Memory way. The other is
reading the tree nodes as needed (very useful in combination with huge
trees and the nested set model). The package is designed that way that
it is possible to convert/copy tree data from either structure to
another (from XML into DB).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
