%define		_class		Tree
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.3.7
Release:	1
Summary:	Generic tree management
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Tree/
Source0:	http://download.pear.php.net/package/Tree-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-5mdv2011.0
+ Revision: 667644
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-4mdv2011.0
+ Revision: 607159
- rebuild

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.4-3mdv2010.1
+ Revision: 466331
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3.4-2mdv2010.0
+ Revision: 426671
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.3.4-1mdv2009.1
+ Revision: 368277
- Update php pear Tree to version 0.3.4

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-2mdv2009.1
+ Revision: 321916
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.3-1mdv2009.0
+ Revision: 272599
- 0.3.3

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-3mdv2009.0
+ Revision: 224887
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-2mdv2008.1
+ Revision: 178541
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdv2008.0
+ Revision: 54560
- 0.3.1

* Sun Jun 03 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-1mdv2008.0
+ Revision: 34816
- 0.3.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-7mdv2007.0
+ Revision: 82779
- Import php-pear-Tree

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.4-1mdk
- initial Mandriva package (PLD import)


