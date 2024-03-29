#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v5
# autospec commit: c02b2fe
#
Name     : htslib
Version  : 1.19
Release  : 5
URL      : https://github.com/samtools/htslib/releases/download/1.19/htslib-1.19.tar.bz2
Source0  : https://github.com/samtools/htslib/releases/download/1.19/htslib-1.19.tar.bz2
Summary  : C library for high-throughput sequencing data formats
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: htslib-bin = %{version}-%{release}
Requires: htslib-lib = %{version}-%{release}
Requires: htslib-license = %{version}-%{release}
Requires: htslib-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : curl-dev
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
HTSlib is an implementation of a unified C library for accessing common file
formats, such as SAM, CRAM, VCF, and BCF, used for high-throughput sequencing
data.  It is the core library used by samtools and bcftools.

%package bin
Summary: bin components for the htslib package.
Group: Binaries
Requires: htslib-license = %{version}-%{release}

%description bin
bin components for the htslib package.


%package dev
Summary: dev components for the htslib package.
Group: Development
Requires: htslib-lib = %{version}-%{release}
Requires: htslib-bin = %{version}-%{release}
Provides: htslib-devel = %{version}-%{release}
Requires: htslib = %{version}-%{release}

%description dev
dev components for the htslib package.


%package lib
Summary: lib components for the htslib package.
Group: Libraries
Requires: htslib-license = %{version}-%{release}

%description lib
lib components for the htslib package.


%package license
Summary: license components for the htslib package.
Group: Default

%description license
license components for the htslib package.


%package man
Summary: man components for the htslib package.
Group: Default

%description man
man components for the htslib package.


%prep
%setup -q -n htslib-1.19
cd %{_builddir}/htslib-1.19
pushd ..
cp -a htslib-1.19 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711738409
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-lzma
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-lzma
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711738409
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/htslib
cp %{_builddir}/htslib-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/htslib/ea8a4f5c9e6ea3725e9c4b0399bdd26094d531f7 || :
cp %{_builddir}/htslib-%{version}/htscodecs/LICENSE.md %{buildroot}/usr/share/package-licenses/htslib/6c4957c5b4497597ff61a6a6cef7b08eacbc7731 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/annot-tsv
/V3/usr/bin/bgzip
/V3/usr/bin/htsfile
/V3/usr/bin/tabix
/usr/bin/annot-tsv
/usr/bin/bgzip
/usr/bin/htsfile
/usr/bin/tabix

%files dev
%defattr(-,root,root,-)
/usr/include/htslib/bgzf.h
/usr/include/htslib/cram.h
/usr/include/htslib/faidx.h
/usr/include/htslib/hfile.h
/usr/include/htslib/hts.h
/usr/include/htslib/hts_defs.h
/usr/include/htslib/hts_endian.h
/usr/include/htslib/hts_expr.h
/usr/include/htslib/hts_log.h
/usr/include/htslib/hts_os.h
/usr/include/htslib/kbitset.h
/usr/include/htslib/kfunc.h
/usr/include/htslib/khash.h
/usr/include/htslib/khash_str2int.h
/usr/include/htslib/klist.h
/usr/include/htslib/knetfile.h
/usr/include/htslib/kroundup.h
/usr/include/htslib/kseq.h
/usr/include/htslib/ksort.h
/usr/include/htslib/kstring.h
/usr/include/htslib/regidx.h
/usr/include/htslib/sam.h
/usr/include/htslib/synced_bcf_reader.h
/usr/include/htslib/tbx.h
/usr/include/htslib/thread_pool.h
/usr/include/htslib/vcf.h
/usr/include/htslib/vcf_sweep.h
/usr/include/htslib/vcfutils.h
/usr/lib64/libhts.so
/usr/lib64/pkgconfig/htslib.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libhts.so.1.19
/usr/lib64/libhts.so.1.19
/usr/lib64/libhts.so.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/htslib/6c4957c5b4497597ff61a6a6cef7b08eacbc7731
/usr/share/package-licenses/htslib/ea8a4f5c9e6ea3725e9c4b0399bdd26094d531f7

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/annot-tsv.1
/usr/share/man/man1/bgzip.1
/usr/share/man/man1/htsfile.1
/usr/share/man/man1/tabix.1
/usr/share/man/man5/faidx.5
/usr/share/man/man5/sam.5
/usr/share/man/man5/vcf.5
/usr/share/man/man7/htslib-s3-plugin.7
