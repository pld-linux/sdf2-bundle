Summary:	SDF2 syntax definition formalism
Name:		sdf2-bundle
Version:	2.4
Release:	1
License:	LGPL
Group:		Development/Languages
Source0:	http://ftp.strategoxt.org/pub/stratego/StrategoXT/strategoxt-0.17/%{name}-%{version}.tar.gz
# Source0-md5:	8aa110d790c4a8bf7bc8b884590d7bee
URL:		http://www.syntax-definition.org/
BuildRequires:	atermlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDF2 syntax definition formalism.

%prep
%setup -q

%build
CFLAGS="-D__NO_CTYPE"
%configure \
	--disable-static \
	--with-aterm=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/addPosInfo
%attr(755,root,root) %{_bindir}/ambtracker
%attr(755,root,root) %{_bindir}/apply-function
%attr(755,root,root) %{_bindir}/comparePT
%attr(755,root,root) %{_bindir}/dump-actions
%attr(755,root,root) %{_bindir}/dump-gotos
%attr(755,root,root) %{_bindir}/dump-priorities
%attr(755,root,root) %{_bindir}/dump-productions
%attr(755,root,root) %{_bindir}/error-diff
%attr(755,root,root) %{_bindir}/error-support
%attr(755,root,root) %{_bindir}/error-support-config
%attr(755,root,root) %{_bindir}/filterPT
%attr(755,root,root) %{_bindir}/flattenPT
%attr(755,root,root) %{_bindir}/implodePT
%attr(755,root,root) %{_bindir}/lift-error
%attr(755,root,root) %{_bindir}/liftPT
%attr(755,root,root) %{_bindir}/lower-error
%attr(755,root,root) %{_bindir}/parse-sdf2
%attr(755,root,root) %{_bindir}/parsetablegen
%attr(755,root,root) %{_bindir}/removevarsyntax
%attr(755,root,root) %{_bindir}/restorebrackets
%attr(755,root,root) %{_bindir}/sdf-modules
%attr(755,root,root) %{_bindir}/sdf-renaming
%attr(755,root,root) %{_bindir}/sdf2table
%attr(755,root,root) %{_bindir}/sdfchecker
%attr(755,root,root) %{_bindir}/sglr
%attr(755,root,root) %{_bindir}/tbunpack
%attr(755,root,root) %{_bindir}/unparsePT
%attr(755,root,root) %{_bindir}/unparseProd
%{_mandir}/man1/sdf2table.1
%{_mandir}/man1/sglr.1
%{_mandir}/man3/sglr-api.3
%{_includedir}/ASFME*.h
%{_includedir}/Error*.h
%{_includedir}/Location*.h
%{_includedir}/MEPT*.h
%{_includedir}/PT2SDF.h
%{_includedir}/PTMEPT*.h
%{_includedir}/Parsed*.h
%{_includedir}/SDF2PT.h
%{_includedir}/SDFME*.h
%{_includedir}/TA*.h
%{_includedir}/asc-*.h
%{_includedir}/atb-tool.h
%{_includedir}/builtin-common.h
%{_includedir}/parse-table.h
%{_includedir}/sglr.h
%{_includedir}/tide*.h
%attr(755,root,root) %{_libdir}/libASFME.so
%attr(755,root,root) %{_libdir}/libATB.so
%attr(755,root,root) %{_libdir}/libErrorAPI.so
%attr(755,root,root) %{_libdir}/libLocationAPI.so
%attr(755,root,root) %{_libdir}/libPT2SDF.so
%attr(755,root,root) %{_libdir}/libPTMEPT.so
%attr(755,root,root) %{_libdir}/libSDF2PT.so
%attr(755,root,root) %{_libdir}/libSDFME.so
%attr(755,root,root) %{_libdir}/libasc-support-me.so
%attr(755,root,root) %{_libdir}/libmept.so
%attr(755,root,root) %{_libdir}/libsglr.so
%attr(755,root,root) %{_libdir}/libtide-adapter.so
%{_pkgconfigdir}/asc-support.pc
%{_pkgconfigdir}/asf-support.pc
%{_pkgconfigdir}/error-support.pc
%{_pkgconfigdir}/pgen.pc
%{_pkgconfigdir}/pt-support.pc
%{_pkgconfigdir}/sdf-library.pc
%{_pkgconfigdir}/sdf-support.pc
%{_pkgconfigdir}/sdf2-bundle.pc
%{_pkgconfigdir}/sglr.pc
%{_pkgconfigdir}/tide-support.pc
%{_pkgconfigdir}/toolbuslib.pc
%{_datadir}/error-support
%{_datadir}/pgen
%{_datadir}/pt-support
%{_datadir}/sdf-library
%{_datadir}/sdf-support
%{_datadir}/sglr
%{_datadir}/tide-support
