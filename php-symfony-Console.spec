%define		package	Console
%define		php_min_version 8.2
Summary:	Symfony Console Component
Summary(pl.UTF-8):	Komponent Symfony Console
Name:		php-symfony-Console
Version:	7.2.9
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/console/archive/v%{version}/console-%{version}.tar.gz
# Source0-md5:	76af0ca344159f6c783c3ce8a3969426
URL:		https://symfony.com/doc/current/components/console.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Requires:	php-symfony-ServiceContracts >= 2.5
Requires:	php-symfony-String >= 6.4
Obsoletes:	php-symfony2-Console < 3
Suggests:	php-symfony-EventDispatcher >= 6.4
Suggests:	php-symfony-Process >= 6.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Console component eases the creation of beautiful and testable
command line interfaces.

%description -l pl.UTF-8
Komponent Console ułatwia tworzenie pięknych i testowalnych
interfejsów linii poleceń.

%prep
%setup -q -n console-%{version}

%build
phpab -n -e '*/Tests/*' -e '*/CI/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
# CI helpers not needed at runtime
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/CI
# Windows binary
rm $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Resources/bin/hiddeninput.exe

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Console
%{php_data_dir}/Symfony/Component/Console/*.php
%{php_data_dir}/Symfony/Component/Console/Attribute
%{php_data_dir}/Symfony/Component/Console/Command
%{php_data_dir}/Symfony/Component/Console/CommandLoader
%{php_data_dir}/Symfony/Component/Console/Completion
%{php_data_dir}/Symfony/Component/Console/DataCollector
%{php_data_dir}/Symfony/Component/Console/Debug
%{php_data_dir}/Symfony/Component/Console/DependencyInjection
%{php_data_dir}/Symfony/Component/Console/Descriptor
%{php_data_dir}/Symfony/Component/Console/Event
%{php_data_dir}/Symfony/Component/Console/EventListener
%{php_data_dir}/Symfony/Component/Console/Exception
%{php_data_dir}/Symfony/Component/Console/Formatter
%{php_data_dir}/Symfony/Component/Console/Helper
%{php_data_dir}/Symfony/Component/Console/Input
%{php_data_dir}/Symfony/Component/Console/Logger
%{php_data_dir}/Symfony/Component/Console/Messenger
%{php_data_dir}/Symfony/Component/Console/Output
%{php_data_dir}/Symfony/Component/Console/Question
%{php_data_dir}/Symfony/Component/Console/Resources
%{php_data_dir}/Symfony/Component/Console/SignalRegistry
%{php_data_dir}/Symfony/Component/Console/Style
%{php_data_dir}/Symfony/Component/Console/Tester
