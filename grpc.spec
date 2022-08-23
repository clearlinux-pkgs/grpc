#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grpc
Version  : 1.24.2
Release  : 31
URL      : https://github.com/grpc/grpc/archive/v1.24.2.tar.gz
Source0  : https://github.com/grpc/grpc/archive/v1.24.2.tar.gz
Source1  : https://github.com/c-ares/c-ares/archive/e982924acee7f7313b4baa4ee5ec000c5e373c30.tar.gz
Source2  : https://github.com/gflags/gflags/archive/28f50e0fed19872e0fd50dd23ce2ee8cd759338e.tar.gz
Source3  : https://github.com/google/benchmark/archive/090faecb454fbd6e6e17a75ef8146acb037118d4.tar.gz
Source4  : https://github.com/google/boringssl/archive/b29b21a81b32ec273f118f589f46d56ad3332420.tar.gz
Source5  : https://github.com/madler/zlib/archive/cacf7f1d4e3d44d871b605da3b647f07d718623f.tar.gz
Source6  : https://github.com/protocolbuffers/protobuf/archive/09745575a923640154bcf307fba8aedff47f240a.tar.gz
Source7  : https://github.com/protocolbuffers/upb/archive/931bbecbd3230ae7f22efa5d203639facc47f719.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSL-1.0 MIT OpenSSL
Requires: grpc-bin = %{version}-%{release}
Requires: grpc-data = %{version}-%{release}
Requires: grpc-lib = %{version}-%{release}
Requires: grpc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-qmake
BuildRequires : c-ares-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi(coverage)
BuildRequires : pypi(cython)
BuildRequires : pypi(enum34)
BuildRequires : pypi(protobuf)
BuildRequires : pypi(six)
BuildRequires : pypi(wheel)
Patch1: 0001-Update-Makefile-for-linking-issue.patch

%description
The status.proto file is copied from
https://github.com/googleapis/googleapis/blob/master/google/rpc/status.proto.

%package bin
Summary: bin components for the grpc package.
Group: Binaries
Requires: grpc-data = %{version}-%{release}
Requires: grpc-license = %{version}-%{release}

%description bin
bin components for the grpc package.


%package data
Summary: data components for the grpc package.
Group: Data

%description data
data components for the grpc package.


%package dev
Summary: dev components for the grpc package.
Group: Development
Requires: grpc-lib = %{version}-%{release}
Requires: grpc-bin = %{version}-%{release}
Requires: grpc-data = %{version}-%{release}
Provides: grpc-devel = %{version}-%{release}
Requires: grpc = %{version}-%{release}

%description dev
dev components for the grpc package.


%package lib
Summary: lib components for the grpc package.
Group: Libraries
Requires: grpc-data = %{version}-%{release}
Requires: grpc-license = %{version}-%{release}

%description lib
lib components for the grpc package.


%package license
Summary: license components for the grpc package.
Group: Default

%description license
license components for the grpc package.


%prep
%setup -q -n grpc-1.24.2
cd %{_builddir}
tar xf %{_sourcedir}/090faecb454fbd6e6e17a75ef8146acb037118d4.tar.gz
cd %{_builddir}
tar xf %{_sourcedir}/e982924acee7f7313b4baa4ee5ec000c5e373c30.tar.gz
cd %{_builddir}
tar xf %{_sourcedir}/28f50e0fed19872e0fd50dd23ce2ee8cd759338e.tar.gz
cd %{_builddir}
tar xf %{_sourcedir}/09745575a923640154bcf307fba8aedff47f240a.tar.gz
cd %{_builddir}
tar xf %{_sourcedir}/b29b21a81b32ec273f118f589f46d56ad3332420.tar.gz
cd %{_builddir}
tar xf %{_sourcedir}/cacf7f1d4e3d44d871b605da3b647f07d718623f.tar.gz
cd %{_builddir}
tar xf %{_sourcedir}/931bbecbd3230ae7f22efa5d203639facc47f719.tar.gz
cd %{_builddir}/grpc-1.24.2
mkdir -p third_party/benchmark
cp -r %{_builddir}/benchmark-090faecb454fbd6e6e17a75ef8146acb037118d4/* %{_builddir}/grpc-1.24.2/third_party/benchmark
mkdir -p third_party/cares/cares
cp -r %{_builddir}/c-ares-e982924acee7f7313b4baa4ee5ec000c5e373c30/* %{_builddir}/grpc-1.24.2/third_party/cares/cares
mkdir -p third_party/gflags
cp -r %{_builddir}/gflags-28f50e0fed19872e0fd50dd23ce2ee8cd759338e/* %{_builddir}/grpc-1.24.2/third_party/gflags
mkdir -p third_party/protobuf
cp -r %{_builddir}/protobuf-09745575a923640154bcf307fba8aedff47f240a/* %{_builddir}/grpc-1.24.2/third_party/protobuf
mkdir -p third_party/boringssl
cp -r %{_builddir}/boringssl-b29b21a81b32ec273f118f589f46d56ad3332420/* %{_builddir}/grpc-1.24.2/third_party/boringssl
mkdir -p third_party/zlib
cp -r %{_builddir}/zlib-cacf7f1d4e3d44d871b605da3b647f07d718623f/* %{_builddir}/grpc-1.24.2/third_party/zlib
mkdir -p third_party/upb
cp -r %{_builddir}/upb-931bbecbd3230ae7f22efa5d203639facc47f719/* %{_builddir}/grpc-1.24.2/third_party/upb
%patch1 -p1
pushd ..
cp -a grpc-1.24.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656119361
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
make  %{?_smp_mflags}

pushd ../buildavx2
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1656119361
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grpc
cp %{_builddir}/benchmark-090faecb454fbd6e6e17a75ef8146acb037118d4/LICENSE %{buildroot}/usr/share/package-licenses/grpc/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/boringssl-b29b21a81b32ec273f118f589f46d56ad3332420/LICENSE %{buildroot}/usr/share/package-licenses/grpc/2c4bc817e0d969875f7c241e9ccfa02d0a7751f0
cp %{_builddir}/boringssl-b29b21a81b32ec273f118f589f46d56ad3332420/third_party/android-cmake/LICENSE %{buildroot}/usr/share/package-licenses/grpc/6ddaf91c4bdcc84506b4652937b40776c504d41e
cp %{_builddir}/boringssl-b29b21a81b32ec273f118f589f46d56ad3332420/third_party/fiat/LICENSE %{buildroot}/usr/share/package-licenses/grpc/b71c498e7e934dcfb176710d4f42e18b9e86fe85
cp %{_builddir}/boringssl-b29b21a81b32ec273f118f589f46d56ad3332420/third_party/googletest/LICENSE %{buildroot}/usr/share/package-licenses/grpc/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/c-ares-e982924acee7f7313b4baa4ee5ec000c5e373c30/LICENSE.md %{buildroot}/usr/share/package-licenses/grpc/e9c597f9b6cf935773ee731d4170b0c2ba142dbb
cp %{_builddir}/gflags-28f50e0fed19872e0fd50dd23ce2ee8cd759338e/COPYING.txt %{buildroot}/usr/share/package-licenses/grpc/b2d4ab17f1b8ef9e0646ba932dce81efe3b852ab
cp %{_builddir}/grpc-1.24.2/LICENSE %{buildroot}/usr/share/package-licenses/grpc/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/grpc-1.24.2/src/php/ext/grpc/LICENSE %{buildroot}/usr/share/package-licenses/grpc/7d96a2516756ac02b4f9c984bb0dc09773200a99
cp %{_builddir}/grpc-1.24.2/third_party/address_sorting/LICENSE %{buildroot}/usr/share/package-licenses/grpc/aa0f4491c1110db68dd4e054555e255fd470d4f6
cp %{_builddir}/grpc-1.24.2/third_party/rake-compiler-dock/LICENSE.txt %{buildroot}/usr/share/package-licenses/grpc/88c9733ea42866741711462cb513b74d2d4555e8
cp %{_builddir}/protobuf-09745575a923640154bcf307fba8aedff47f240a/LICENSE %{buildroot}/usr/share/package-licenses/grpc/1b5a14d06dd784e88dadc5c68344be2dc13875b6
cp %{_builddir}/upb-931bbecbd3230ae7f22efa5d203639facc47f719/LICENSE %{buildroot}/usr/share/package-licenses/grpc/62a84576412fd902600dc53e00d37e3607865dae
cp %{_builddir}/upb-931bbecbd3230ae7f22efa5d203639facc47f719/third_party/lunit/LICENSE %{buildroot}/usr/share/package-licenses/grpc/fdd1d72fcc979c32a5ab8ae278a2dfd967faf820
cp %{_builddir}/zlib-cacf7f1d4e3d44d871b605da3b647f07d718623f/contrib/dotzlib/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/grpc/892b34f7865d90a6f949f50d95e49625a10bc7f0
pushd ../buildavx2/
%make_install_v3 prefix=%{buildroot}/usr
popd
%make_install prefix=%{buildroot}/usr
## install_append content
mkdir -p %{buildroot}/usr/lib64/haswell
rm -rf %{buildroot}/usr/lib/*.*
pushd ../buildavx2/
%make_install_avx2 prefix=%{buildroot}/usr
popd
mv %{buildroot}/usr/lib/*.* %{buildroot}/usr/lib64/haswell
%make_install prefix=%{buildroot}/usr
mv %{buildroot}/usr/lib/*.* %{buildroot}/usr/lib64/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/grpc_cpp_plugin
/usr/bin/grpc_csharp_plugin
/usr/bin/grpc_node_plugin
/usr/bin/grpc_objective_c_plugin
/usr/bin/grpc_php_plugin
/usr/bin/grpc_python_plugin
/usr/bin/grpc_ruby_plugin
/usr/bin/haswell/grpc_cpp_plugin
/usr/bin/haswell/grpc_csharp_plugin
/usr/bin/haswell/grpc_node_plugin
/usr/bin/haswell/grpc_objective_c_plugin
/usr/bin/haswell/grpc_php_plugin
/usr/bin/haswell/grpc_python_plugin
/usr/bin/haswell/grpc_ruby_plugin

%files data
%defattr(-,root,root,-)
/usr/share/grpc/roots.pem

%files dev
%defattr(-,root,root,-)
/usr/include/grpc++/alarm.h
/usr/include/grpc++/channel.h
/usr/include/grpc++/client_context.h
/usr/include/grpc++/completion_queue.h
/usr/include/grpc++/create_channel.h
/usr/include/grpc++/create_channel_posix.h
/usr/include/grpc++/ext/health_check_service_server_builder_option.h
/usr/include/grpc++/ext/proto_server_reflection_plugin.h
/usr/include/grpc++/generic/async_generic_service.h
/usr/include/grpc++/generic/generic_stub.h
/usr/include/grpc++/grpc++.h
/usr/include/grpc++/health_check_service_interface.h
/usr/include/grpc++/impl/call.h
/usr/include/grpc++/impl/channel_argument_option.h
/usr/include/grpc++/impl/client_unary_call.h
/usr/include/grpc++/impl/codegen/async_stream.h
/usr/include/grpc++/impl/codegen/async_unary_call.h
/usr/include/grpc++/impl/codegen/byte_buffer.h
/usr/include/grpc++/impl/codegen/call.h
/usr/include/grpc++/impl/codegen/call_hook.h
/usr/include/grpc++/impl/codegen/channel_interface.h
/usr/include/grpc++/impl/codegen/client_context.h
/usr/include/grpc++/impl/codegen/client_unary_call.h
/usr/include/grpc++/impl/codegen/completion_queue.h
/usr/include/grpc++/impl/codegen/completion_queue_tag.h
/usr/include/grpc++/impl/codegen/config.h
/usr/include/grpc++/impl/codegen/config_protobuf.h
/usr/include/grpc++/impl/codegen/core_codegen.h
/usr/include/grpc++/impl/codegen/core_codegen_interface.h
/usr/include/grpc++/impl/codegen/create_auth_context.h
/usr/include/grpc++/impl/codegen/grpc_library.h
/usr/include/grpc++/impl/codegen/metadata_map.h
/usr/include/grpc++/impl/codegen/method_handler_impl.h
/usr/include/grpc++/impl/codegen/proto_utils.h
/usr/include/grpc++/impl/codegen/rpc_method.h
/usr/include/grpc++/impl/codegen/rpc_service_method.h
/usr/include/grpc++/impl/codegen/security/auth_context.h
/usr/include/grpc++/impl/codegen/serialization_traits.h
/usr/include/grpc++/impl/codegen/server_context.h
/usr/include/grpc++/impl/codegen/server_interface.h
/usr/include/grpc++/impl/codegen/service_type.h
/usr/include/grpc++/impl/codegen/slice.h
/usr/include/grpc++/impl/codegen/status.h
/usr/include/grpc++/impl/codegen/status_code_enum.h
/usr/include/grpc++/impl/codegen/string_ref.h
/usr/include/grpc++/impl/codegen/stub_options.h
/usr/include/grpc++/impl/codegen/sync_stream.h
/usr/include/grpc++/impl/codegen/time.h
/usr/include/grpc++/impl/grpc_library.h
/usr/include/grpc++/impl/method_handler_impl.h
/usr/include/grpc++/impl/rpc_method.h
/usr/include/grpc++/impl/rpc_service_method.h
/usr/include/grpc++/impl/serialization_traits.h
/usr/include/grpc++/impl/server_builder_option.h
/usr/include/grpc++/impl/server_builder_plugin.h
/usr/include/grpc++/impl/server_initializer.h
/usr/include/grpc++/impl/service_type.h
/usr/include/grpc++/resource_quota.h
/usr/include/grpc++/security/auth_context.h
/usr/include/grpc++/security/auth_metadata_processor.h
/usr/include/grpc++/security/credentials.h
/usr/include/grpc++/security/server_credentials.h
/usr/include/grpc++/server.h
/usr/include/grpc++/server_builder.h
/usr/include/grpc++/server_context.h
/usr/include/grpc++/server_posix.h
/usr/include/grpc++/support/async_stream.h
/usr/include/grpc++/support/async_unary_call.h
/usr/include/grpc++/support/byte_buffer.h
/usr/include/grpc++/support/channel_arguments.h
/usr/include/grpc++/support/config.h
/usr/include/grpc++/support/error_details.h
/usr/include/grpc++/support/slice.h
/usr/include/grpc++/support/status.h
/usr/include/grpc++/support/status_code_enum.h
/usr/include/grpc++/support/string_ref.h
/usr/include/grpc++/support/stub_options.h
/usr/include/grpc++/support/sync_stream.h
/usr/include/grpc++/support/time.h
/usr/include/grpc/byte_buffer.h
/usr/include/grpc/byte_buffer_reader.h
/usr/include/grpc/census.h
/usr/include/grpc/compression.h
/usr/include/grpc/fork.h
/usr/include/grpc/grpc.h
/usr/include/grpc/grpc_cronet.h
/usr/include/grpc/grpc_posix.h
/usr/include/grpc/grpc_security.h
/usr/include/grpc/grpc_security_constants.h
/usr/include/grpc/impl/codegen/atm.h
/usr/include/grpc/impl/codegen/atm_gcc_atomic.h
/usr/include/grpc/impl/codegen/atm_gcc_sync.h
/usr/include/grpc/impl/codegen/atm_windows.h
/usr/include/grpc/impl/codegen/byte_buffer.h
/usr/include/grpc/impl/codegen/byte_buffer_reader.h
/usr/include/grpc/impl/codegen/compression_types.h
/usr/include/grpc/impl/codegen/connectivity_state.h
/usr/include/grpc/impl/codegen/fork.h
/usr/include/grpc/impl/codegen/gpr_slice.h
/usr/include/grpc/impl/codegen/gpr_types.h
/usr/include/grpc/impl/codegen/grpc_types.h
/usr/include/grpc/impl/codegen/log.h
/usr/include/grpc/impl/codegen/port_platform.h
/usr/include/grpc/impl/codegen/propagation_bits.h
/usr/include/grpc/impl/codegen/slice.h
/usr/include/grpc/impl/codegen/status.h
/usr/include/grpc/impl/codegen/sync.h
/usr/include/grpc/impl/codegen/sync_custom.h
/usr/include/grpc/impl/codegen/sync_generic.h
/usr/include/grpc/impl/codegen/sync_posix.h
/usr/include/grpc/impl/codegen/sync_windows.h
/usr/include/grpc/load_reporting.h
/usr/include/grpc/slice.h
/usr/include/grpc/slice_buffer.h
/usr/include/grpc/status.h
/usr/include/grpc/support/alloc.h
/usr/include/grpc/support/atm.h
/usr/include/grpc/support/atm_gcc_atomic.h
/usr/include/grpc/support/atm_gcc_sync.h
/usr/include/grpc/support/atm_windows.h
/usr/include/grpc/support/cpu.h
/usr/include/grpc/support/log.h
/usr/include/grpc/support/log_windows.h
/usr/include/grpc/support/port_platform.h
/usr/include/grpc/support/string_util.h
/usr/include/grpc/support/sync.h
/usr/include/grpc/support/sync_custom.h
/usr/include/grpc/support/sync_generic.h
/usr/include/grpc/support/sync_posix.h
/usr/include/grpc/support/sync_windows.h
/usr/include/grpc/support/thd_id.h
/usr/include/grpc/support/time.h
/usr/include/grpc/support/workaround_list.h
/usr/include/grpcpp/alarm.h
/usr/include/grpcpp/alarm_impl.h
/usr/include/grpcpp/channel.h
/usr/include/grpcpp/channel_impl.h
/usr/include/grpcpp/client_context.h
/usr/include/grpcpp/completion_queue.h
/usr/include/grpcpp/completion_queue_impl.h
/usr/include/grpcpp/create_channel.h
/usr/include/grpcpp/create_channel_impl.h
/usr/include/grpcpp/create_channel_posix.h
/usr/include/grpcpp/create_channel_posix_impl.h
/usr/include/grpcpp/ext/channelz_service_plugin.h
/usr/include/grpcpp/ext/channelz_service_plugin_impl.h
/usr/include/grpcpp/ext/health_check_service_server_builder_option.h
/usr/include/grpcpp/ext/proto_server_reflection_plugin.h
/usr/include/grpcpp/ext/proto_server_reflection_plugin_impl.h
/usr/include/grpcpp/generic/async_generic_service.h
/usr/include/grpcpp/generic/generic_stub.h
/usr/include/grpcpp/generic/generic_stub_impl.h
/usr/include/grpcpp/grpcpp.h
/usr/include/grpcpp/health_check_service_interface.h
/usr/include/grpcpp/health_check_service_interface_impl.h
/usr/include/grpcpp/impl/call.h
/usr/include/grpcpp/impl/channel_argument_option.h
/usr/include/grpcpp/impl/client_unary_call.h
/usr/include/grpcpp/impl/codegen/async_generic_service.h
/usr/include/grpcpp/impl/codegen/async_stream.h
/usr/include/grpcpp/impl/codegen/async_stream_impl.h
/usr/include/grpcpp/impl/codegen/async_unary_call.h
/usr/include/grpcpp/impl/codegen/async_unary_call_impl.h
/usr/include/grpcpp/impl/codegen/byte_buffer.h
/usr/include/grpcpp/impl/codegen/call.h
/usr/include/grpcpp/impl/codegen/call_hook.h
/usr/include/grpcpp/impl/codegen/call_op_set.h
/usr/include/grpcpp/impl/codegen/call_op_set_interface.h
/usr/include/grpcpp/impl/codegen/callback_common.h
/usr/include/grpcpp/impl/codegen/channel_interface.h
/usr/include/grpcpp/impl/codegen/client_callback.h
/usr/include/grpcpp/impl/codegen/client_callback_impl.h
/usr/include/grpcpp/impl/codegen/client_context.h
/usr/include/grpcpp/impl/codegen/client_context_impl.h
/usr/include/grpcpp/impl/codegen/client_interceptor.h
/usr/include/grpcpp/impl/codegen/client_unary_call.h
/usr/include/grpcpp/impl/codegen/completion_queue.h
/usr/include/grpcpp/impl/codegen/completion_queue_impl.h
/usr/include/grpcpp/impl/codegen/completion_queue_tag.h
/usr/include/grpcpp/impl/codegen/config.h
/usr/include/grpcpp/impl/codegen/config_protobuf.h
/usr/include/grpcpp/impl/codegen/core_codegen.h
/usr/include/grpcpp/impl/codegen/core_codegen_interface.h
/usr/include/grpcpp/impl/codegen/create_auth_context.h
/usr/include/grpcpp/impl/codegen/delegating_channel.h
/usr/include/grpcpp/impl/codegen/grpc_library.h
/usr/include/grpcpp/impl/codegen/intercepted_channel.h
/usr/include/grpcpp/impl/codegen/interceptor.h
/usr/include/grpcpp/impl/codegen/interceptor_common.h
/usr/include/grpcpp/impl/codegen/message_allocator.h
/usr/include/grpcpp/impl/codegen/metadata_map.h
/usr/include/grpcpp/impl/codegen/method_handler_impl.h
/usr/include/grpcpp/impl/codegen/proto_buffer_reader.h
/usr/include/grpcpp/impl/codegen/proto_buffer_writer.h
/usr/include/grpcpp/impl/codegen/proto_utils.h
/usr/include/grpcpp/impl/codegen/rpc_method.h
/usr/include/grpcpp/impl/codegen/rpc_service_method.h
/usr/include/grpcpp/impl/codegen/security/auth_context.h
/usr/include/grpcpp/impl/codegen/serialization_traits.h
/usr/include/grpcpp/impl/codegen/server_callback.h
/usr/include/grpcpp/impl/codegen/server_callback_impl.h
/usr/include/grpcpp/impl/codegen/server_context.h
/usr/include/grpcpp/impl/codegen/server_context_impl.h
/usr/include/grpcpp/impl/codegen/server_interceptor.h
/usr/include/grpcpp/impl/codegen/server_interface.h
/usr/include/grpcpp/impl/codegen/service_type.h
/usr/include/grpcpp/impl/codegen/slice.h
/usr/include/grpcpp/impl/codegen/status.h
/usr/include/grpcpp/impl/codegen/status_code_enum.h
/usr/include/grpcpp/impl/codegen/string_ref.h
/usr/include/grpcpp/impl/codegen/stub_options.h
/usr/include/grpcpp/impl/codegen/sync.h
/usr/include/grpcpp/impl/codegen/sync_stream.h
/usr/include/grpcpp/impl/codegen/sync_stream_impl.h
/usr/include/grpcpp/impl/codegen/time.h
/usr/include/grpcpp/impl/grpc_library.h
/usr/include/grpcpp/impl/method_handler_impl.h
/usr/include/grpcpp/impl/rpc_method.h
/usr/include/grpcpp/impl/rpc_service_method.h
/usr/include/grpcpp/impl/serialization_traits.h
/usr/include/grpcpp/impl/server_builder_option.h
/usr/include/grpcpp/impl/server_builder_option_impl.h
/usr/include/grpcpp/impl/server_builder_plugin.h
/usr/include/grpcpp/impl/server_initializer.h
/usr/include/grpcpp/impl/server_initializer_impl.h
/usr/include/grpcpp/impl/service_type.h
/usr/include/grpcpp/resource_quota.h
/usr/include/grpcpp/resource_quota_impl.h
/usr/include/grpcpp/security/auth_context.h
/usr/include/grpcpp/security/auth_metadata_processor.h
/usr/include/grpcpp/security/auth_metadata_processor_impl.h
/usr/include/grpcpp/security/credentials.h
/usr/include/grpcpp/security/credentials_impl.h
/usr/include/grpcpp/security/server_credentials.h
/usr/include/grpcpp/security/server_credentials_impl.h
/usr/include/grpcpp/server.h
/usr/include/grpcpp/server_builder.h
/usr/include/grpcpp/server_builder_impl.h
/usr/include/grpcpp/server_context.h
/usr/include/grpcpp/server_impl.h
/usr/include/grpcpp/server_posix.h
/usr/include/grpcpp/server_posix_impl.h
/usr/include/grpcpp/support/async_stream.h
/usr/include/grpcpp/support/async_stream_impl.h
/usr/include/grpcpp/support/async_unary_call.h
/usr/include/grpcpp/support/async_unary_call_impl.h
/usr/include/grpcpp/support/byte_buffer.h
/usr/include/grpcpp/support/channel_arguments.h
/usr/include/grpcpp/support/channel_arguments_impl.h
/usr/include/grpcpp/support/client_callback.h
/usr/include/grpcpp/support/client_callback_impl.h
/usr/include/grpcpp/support/client_interceptor.h
/usr/include/grpcpp/support/config.h
/usr/include/grpcpp/support/error_details.h
/usr/include/grpcpp/support/error_details_impl.h
/usr/include/grpcpp/support/interceptor.h
/usr/include/grpcpp/support/message_allocator.h
/usr/include/grpcpp/support/proto_buffer_reader.h
/usr/include/grpcpp/support/proto_buffer_writer.h
/usr/include/grpcpp/support/server_callback.h
/usr/include/grpcpp/support/server_callback_impl.h
/usr/include/grpcpp/support/server_interceptor.h
/usr/include/grpcpp/support/slice.h
/usr/include/grpcpp/support/status.h
/usr/include/grpcpp/support/status_code_enum.h
/usr/include/grpcpp/support/string_ref.h
/usr/include/grpcpp/support/stub_options.h
/usr/include/grpcpp/support/sync_stream.h
/usr/include/grpcpp/support/sync_stream_impl.h
/usr/include/grpcpp/support/time.h
/usr/include/grpcpp/support/validate_service_config.h
/usr/lib64/haswell/libaddress_sorting.so
/usr/lib64/haswell/libgpr.so
/usr/lib64/haswell/libgrpc++.so
/usr/lib64/haswell/libgrpc++_error_details.so
/usr/lib64/haswell/libgrpc++_reflection.so
/usr/lib64/haswell/libgrpc++_unsecure.so
/usr/lib64/haswell/libgrpc.so
/usr/lib64/haswell/libgrpc_cronet.so
/usr/lib64/haswell/libgrpc_unsecure.so
/usr/lib64/haswell/libgrpcpp_channelz.so
/usr/lib64/libaddress_sorting.so
/usr/lib64/libgpr.so
/usr/lib64/libgrpc++.so
/usr/lib64/libgrpc++_error_details.so
/usr/lib64/libgrpc++_reflection.so
/usr/lib64/libgrpc++_unsecure.so
/usr/lib64/libgrpc.so
/usr/lib64/libgrpc_cronet.so
/usr/lib64/libgrpc_unsecure.so
/usr/lib64/libgrpcpp_channelz.so
/usr/lib64/pkgconfig/gpr.pc
/usr/lib64/pkgconfig/grpc++.pc
/usr/lib64/pkgconfig/grpc++_unsecure.pc
/usr/lib64/pkgconfig/grpc.pc
/usr/lib64/pkgconfig/grpc_unsecure.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libaddress_sorting.so.8
/usr/lib64/haswell/libaddress_sorting.so.8.0.0
/usr/lib64/haswell/libgpr.so.8
/usr/lib64/haswell/libgpr.so.8.0.0
/usr/lib64/haswell/libgrpc++.so.1
/usr/lib64/haswell/libgrpc++.so.1.24.2
/usr/lib64/haswell/libgrpc++_error_details.so.1
/usr/lib64/haswell/libgrpc++_error_details.so.1.24.2
/usr/lib64/haswell/libgrpc++_reflection.so.1
/usr/lib64/haswell/libgrpc++_reflection.so.1.24.2
/usr/lib64/haswell/libgrpc++_unsecure.so.1
/usr/lib64/haswell/libgrpc++_unsecure.so.1.24.2
/usr/lib64/haswell/libgrpc.so.8
/usr/lib64/haswell/libgrpc.so.8.0.0
/usr/lib64/haswell/libgrpc_cronet.so.8
/usr/lib64/haswell/libgrpc_cronet.so.8.0.0
/usr/lib64/haswell/libgrpc_unsecure.so.8
/usr/lib64/haswell/libgrpc_unsecure.so.8.0.0
/usr/lib64/haswell/libgrpcpp_channelz.so.1
/usr/lib64/haswell/libgrpcpp_channelz.so.1.24.2
/usr/lib64/libaddress_sorting.so.8
/usr/lib64/libaddress_sorting.so.8.0.0
/usr/lib64/libgpr.so.8
/usr/lib64/libgpr.so.8.0.0
/usr/lib64/libgrpc++.so.1
/usr/lib64/libgrpc++.so.1.24.2
/usr/lib64/libgrpc++_error_details.so.1
/usr/lib64/libgrpc++_error_details.so.1.24.2
/usr/lib64/libgrpc++_reflection.so.1
/usr/lib64/libgrpc++_reflection.so.1.24.2
/usr/lib64/libgrpc++_unsecure.so.1
/usr/lib64/libgrpc++_unsecure.so.1.24.2
/usr/lib64/libgrpc.so.8
/usr/lib64/libgrpc.so.8.0.0
/usr/lib64/libgrpc_cronet.so.8
/usr/lib64/libgrpc_cronet.so.8.0.0
/usr/lib64/libgrpc_unsecure.so.8
/usr/lib64/libgrpc_unsecure.so.8.0.0
/usr/lib64/libgrpcpp_channelz.so.1
/usr/lib64/libgrpcpp_channelz.so.1.24.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grpc/1b5a14d06dd784e88dadc5c68344be2dc13875b6
/usr/share/package-licenses/grpc/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/grpc/2c4bc817e0d969875f7c241e9ccfa02d0a7751f0
/usr/share/package-licenses/grpc/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/grpc/62a84576412fd902600dc53e00d37e3607865dae
/usr/share/package-licenses/grpc/6ddaf91c4bdcc84506b4652937b40776c504d41e
/usr/share/package-licenses/grpc/7d96a2516756ac02b4f9c984bb0dc09773200a99
/usr/share/package-licenses/grpc/88c9733ea42866741711462cb513b74d2d4555e8
/usr/share/package-licenses/grpc/892b34f7865d90a6f949f50d95e49625a10bc7f0
/usr/share/package-licenses/grpc/aa0f4491c1110db68dd4e054555e255fd470d4f6
/usr/share/package-licenses/grpc/b2d4ab17f1b8ef9e0646ba932dce81efe3b852ab
/usr/share/package-licenses/grpc/b71c498e7e934dcfb176710d4f42e18b9e86fe85
/usr/share/package-licenses/grpc/e9c597f9b6cf935773ee731d4170b0c2ba142dbb
/usr/share/package-licenses/grpc/fdd1d72fcc979c32a5ab8ae278a2dfd967faf820
