Summary:	GRBL controller application
Name:           candle
Version:        1.1
Release:        1
License:        GPLv2+
Group:          Monitoring
Url:            https://github.com/Denvi/Candle
Source0:	https://github.com/Denvi/Candle/archive/v%{version}.tar.gz
Patch0:		translation.patch

BuildRequires:	cmake(Qt5SerialPort)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5OpenGL)

%description
GRBL controller application with G-Code visualizer written in Qt.

Supported functions:

Controlling GRBL-based cnc-machine via console commands,
buttons on form, numpad. Monitoring cnc-machine state.
Loading, editing, saving and sending of G-code files to cnc-machine.
Visualizing G-code files.

%prep
%setup -qn Candle-%{version}
%apply_patches

%build
pushd src
%qmake_qt5
%make
popd

%install
pushd src
%makeinstall_std

install -d %{buildroot}/%{_datadir}/%{name}/translations/
install -m 0644 translations/*.qm %{buildroot}/%{_datadir}/%{name}/translations/
install -d %{buildroot}/%{_bindir}
install -m 0755 Candle %{buildroot}/%{_bindir}/candle
install -d %{buildroot}/%{_datadir}/%{name}/images/
popd

%find_lang candle --with-qt

%files -f %{name}.lang
%{_bindir}/%{name}
