Name:           erigon_proxy
Version:        1.0.1
Release:        %autorelease
Summary:        A simple proxy for Erigon
License:        MIT
URL:            https://github.com/lemenkov/erigon_proxy
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       python3-aiohttp

%description
%{summary}.

%prep
%autosetup -p1

%build
# Nothing to build

%install
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 0644 %{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
%autochangelog
