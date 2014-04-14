Summary:	Open Source Command-Line RTMP Client
Name:		flvstreamer
Version:	2.1c1
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://download.savannah.gnu.org/releases/flvstreamer/source/%{name}-%{version}.tar.gz
# Source0-md5:	4866387328ad89c957af90a2478e5556
Patch0:		optflags.patch
URL:		http://savannah.nongnu.org/projects/flvstreamer
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
flvstreamer is an open source command-line RTMP client intended to
stream audio or video content from all types of flash or rtmp servers.
Forked from rtmpdump v1.6 with encrypted rtmp and swf verification
support removed.

This tool provides free interoperability with the previously
undocumented adobe RTMP protocol so widely in use on the internet
today. It was developed entirely by reverse engineering methods and
without access to any proprietary or restrictive-license protocol
specifications.

%prep
%setup -q -n %{name}
%patch0

%build
%{__make} posix \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p flvstreamer $RPM_BUILD_ROOT%{_bindir}/flvstreamer
install -p rtmpsrv $RPM_BUILD_ROOT%{_bindir}/rtmpsrv
install -p rtmpsuck $RPM_BUILD_ROOT%{_bindir}/rtmpsuck
install -p streams $RPM_BUILD_ROOT%{_bindir}/streams

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog
%attr(755,root,root) %{_bindir}/flvstreamer
%attr(755,root,root) %{_bindir}/rtmpsrv
%attr(755,root,root) %{_bindir}/rtmpsuck
%attr(755,root,root) %{_bindir}/streams
