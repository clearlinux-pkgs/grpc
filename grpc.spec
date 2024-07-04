#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v13
# autospec commit: dc0ff31
#
Name     : grpc
Version  : 1.65.0
Release  : 59
URL      : https://github.com/grpc/grpc/archive/v1.65.0/grpc-1.65.0.tar.gz
Source0  : https://github.com/grpc/grpc/archive/v1.65.0/grpc-1.65.0.tar.gz
Source1  : https://github.com/census-instrumentation/opencensus-proto/archive/v0.3.0/opencensus-proto-0.3.0.tar.gz
Summary  : @PC_DESCRIPTION@
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
BuildRequires : abseil-cpp-dev
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : llvm
BuildRequires : ninja
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libcares)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(protobuf)
BuildRequires : pkgconfig(re2)
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The status.proto file is copied from
https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto.

%prep
%setup -q -n grpc-1.65.0
cd %{_builddir}
tar xf %{_sourcedir}/opencensus-proto-0.3.0.tar.gz
cd %{_builddir}/grpc-1.65.0
mkdir -p third_party/opencensus-proto
cp -r %{_builddir}/opencensus-proto-0.3.0/* %{_builddir}/grpc-1.65.0/third_party/opencensus-proto
pushd ..
cp -a grpc-1.65.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719964628
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CLEAR_INTERMEDIATE_CFLAGS=${CLEAR_ORIG_CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CLEAR_INTERMEDIATE_CXXFLAGS=${CLEAR_ORIG_CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DgRPC_ABSL_PROVIDER:STRING='package' \
-DgRPC_CARES_PROVIDER:STRING='package' \
-DgRPC_SSL_PROVIDER:STRING='package' \
-DgRPC_ZLIB_PROVIDER:STRING='package' \
-DgRPC_RE2_PROVIDER:STRING='package' \
-DgRPC_PROTOBUF_PROVIDER:STRING='package' \
-DgRPC_INSTALL:BOOL=ON \
-DgRPC_INSTALL_BINDIR:PATH=/usr/bin \
-DgRPC_INSTALL_LIBDIR:PATH=/usr/lib64 \
-DgRPC_INSTALL_INCLUDEDIR:PATH=/usr/include \
-DgRPC_INSTALL_CMAKEDIR:PATH=/usr/lib64/cmake/grpc \
-DgRPC_INSTALL_SHAREDIR:PATH=/usr/share/grpc \
-DBUILD_SHARED_LIBS=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CLEAR_INTERMEDIATE_CFLAGS=${CLEAR_ORIG_CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CLEAR_INTERMEDIATE_CXXFLAGS=${CLEAR_ORIG_CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DgRPC_ABSL_PROVIDER:STRING='package' \
-DgRPC_CARES_PROVIDER:STRING='package' \
-DgRPC_SSL_PROVIDER:STRING='package' \
-DgRPC_ZLIB_PROVIDER:STRING='package' \
-DgRPC_RE2_PROVIDER:STRING='package' \
-DgRPC_PROTOBUF_PROVIDER:STRING='package' \
-DgRPC_INSTALL:BOOL=ON \
-DgRPC_INSTALL_BINDIR:PATH=/usr/bin \
-DgRPC_INSTALL_LIBDIR:PATH=/usr/lib64 \
-DgRPC_INSTALL_INCLUDEDIR:PATH=/usr/include \
-DgRPC_INSTALL_CMAKEDIR:PATH=/usr/lib64/cmake/grpc \
-DgRPC_INSTALL_SHAREDIR:PATH=/usr/share/grpc \
-DBUILD_SHARED_LIBS=ON  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CLEAR_INTERMEDIATE_CFLAGS=${CLEAR_ORIG_CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CLEAR_INTERMEDIATE_CXXFLAGS=${CLEAR_ORIG_CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719964628
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grpc
cp %{_builddir}/grpc-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/grpc/242ec6abfdd8c114f2e803b84934469c299348fc || :
cp %{_builddir}/grpc-%{version}/src/php/ext/grpc/LICENSE %{buildroot}/usr/share/package-licenses/grpc/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/grpc-%{version}/third_party/address_sorting/LICENSE %{buildroot}/usr/share/package-licenses/grpc/aa0f4491c1110db68dd4e054555e255fd470d4f6 || :
cp %{_builddir}/grpc-%{version}/third_party/toolchains/rbe_ubuntu2004/LICENSE %{buildroot}/usr/share/package-licenses/grpc/0590bc7a4e55e5f4d7b94045ee76e35914bcb614 || :
cp %{_builddir}/grpc-%{version}/third_party/toolchains/rbe_windows_bazel_6.3.2_vs2019/LICENSE %{buildroot}/usr/share/package-licenses/grpc/0590bc7a4e55e5f4d7b94045ee76e35914bcb614 || :
cp %{_builddir}/grpc-%{version}/third_party/utf8_range/LICENSE %{buildroot}/usr/share/package-licenses/grpc/252c7fd154ca740ae6f765d206fbd9119108a0e3 || :
cp %{_builddir}/grpc-%{version}/third_party/xxhash/LICENSE %{buildroot}/usr/share/package-licenses/grpc/d6cf8b65815efff8a46def3ec4c74c57033d25fa || :
cp %{_builddir}/opencensus-proto-0.3.0/LICENSE %{buildroot}/usr/share/package-licenses/grpc/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3 prefix=%{buildroot}/usr || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install prefix=%{buildroot}/usr
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
