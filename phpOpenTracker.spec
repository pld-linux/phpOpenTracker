# ToDo:
#  - placement of files - not so sure if they should go to php_pear_dir
Summary:	phpOpenTracker - Website traffic analysis framework
Summary(pl):	phpOpenTracker - Abstrakcyjna warstwa analizatora ruchu na stronach WWW
Name:		phpOpenTracker
Version:	1.4.1
Release:	0.1
License:	Apache Software License, Version 2.0
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/phpopencounter/%{name}-%{version}.tgz
# Source0-md5:	e3a66b99137f0bb05782ddffa5a23eb8
Patch0:		%{name}-config.patch
URL:		http://phpopentracker.de/
Requires:	jpgraph
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phpOpenTracker is a framework solution for the analysis of website
traffic and visitor analysis.

%description -l pl
phpOpenTracker jest abstrakcyjn± warstw± s³u¿±c± do analizowania ruchu
oraz ¶ledzenia u¿ytkowników na stronach WWW

%prep
%setup -q -c
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{php_pear_dir}/%{name}/{API,API/plugins,DB,LoggingEngine,conf}}

install %{name}-%{version}/%{name}.php   $RPM_BUILD_ROOT%{php_pear_dir}/
install %{name}-%{version}/%{name}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/
install %{name}-%{version}/%{name}/API/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/API/
install %{name}-%{version}/%{name}/API/plugins/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/API/plugins
install %{name}-%{version}/%{name}/DB/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/DB/
install %{name}-%{version}/%{name}/LoggingEngine/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/LoggingEngine/
install %{name}-%{version}/%{name}/conf/* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/phpOpenTracker.php.dist $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/phpOpenTracker.php
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/lock.ini.dist $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/lock.ini

for i in `ls $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/*` ; do
ln -sf %{_sysconfdir}/%{name}/`basename $i` $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/conf/
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Remember to create database and customize configuration in" >&2
echo "%{_sysconfdir}/%{name}/phpOpenTracker.php file !" >&2

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/%{name}/docs/*
%{php_pear_dir}/%{name}
%{php_pear_dir}/*.php
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/*
