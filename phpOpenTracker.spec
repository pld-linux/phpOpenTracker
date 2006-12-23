# TODO:
#  - placement of files - not so sure if they should go to php_pear_dir
Summary:	phpOpenTracker - website traffic analysis framework
Summary(pl):	phpOpenTracker - abstrakcyjna warstwa analizatora ruchu na stronach WWW
Name:		phpOpenTracker
Version:	1.5.2
Release:	1
License:	Apache Software License, Version 2.0
Group:		Development/Languages/PHP
Source0:	http://download.berlios.de/phpopentracker/%{name}-%{version}.tgz
# Source0-md5:	6e28c979f66b4b53e3fa97052376db34
URL:		http://phpopentracker.de/
Requires:	jpgraph
Requires:	php-pear
Requires:	php-pear-Cache_Lite
Requires:	php-pear-Image_GraphViz
Requires:	php-pear-XML_Tree
Requires:	webserver(php) >= 4.2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		php_pear_dir	%{_datadir}/pear

%description
phpOpenTracker is a framework solution for the analysis of website
traffic and visitor analysis. Requires one if MySQL, PostgreSQL or
Oracle database.

%description -l pl
phpOpenTracker jest abstrakcyjn± warstw± s³u¿±c± do analizowania ruchu
oraz ¶ledzenia u¿ytkowników na stronach WWW. Do dzia³ania wymaga
jednej z baz danych: MySQL, PostgreSQL lub Oracle.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{php_pear_dir}/%{name}/{API,API/plugins,DB,LoggingEngine,conf}}

install %{name}-%{version}/%{name}.php			$RPM_BUILD_ROOT%{php_pear_dir}
install %{name}-%{version}/%{name}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{name}
install %{name}-%{version}/%{name}/API/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{name}/API
install %{name}-%{version}/%{name}/API/plugins/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{name}/API/plugins
install %{name}-%{version}/%{name}/DB/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{name}/DB
install %{name}-%{version}/%{name}/LoggingEngine/*.php	$RPM_BUILD_ROOT%{php_pear_dir}/%{name}/LoggingEngine
install %{name}-%{version}/%{name}/conf/*		$RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/phpOpenTracker.php.dist $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/phpOpenTracker.php
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/lock.ini.dist $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/lock.ini

for i in `ls $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/*` ; do
ln -sf %{_sysconfdir}/%{name}/`basename $i` $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/conf
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Remember to create database and customize configuration in"
echo "%{_sysconfdir}/%{name}/phpOpenTracker.php file !"

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/%{name}/docs/*
%dir %{_sysconfdir}/%{name}
%{php_pear_dir}/%{name}
%{php_pear_dir}/*.php
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
