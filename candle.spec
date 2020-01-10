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
%autopatch -p1

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
install -d %{buildroot}/%{_datadir}/icons/hicolor
install -m 0644 images/candle_256.png %{buildroot}/%{_datadir}/icons/candle.png
popd

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Candle
GenericName=Candle
Comment=GRBL controller application with G-Code visualizer written in Qt.
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
EOF

%find_lang candle --with-qt

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/icons/candle.png
%{_datadir}/applications/%{name}.desktop
