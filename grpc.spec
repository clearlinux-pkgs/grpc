#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v7
# autospec commit: f56f1fa
#
Name     : grpc
Version  : 1.64.0
Release  : 56
URL      : https://github.com/grpc/grpc/archive/v1.64.0/grpc-1.64.0.tar.gz
Source0  : https://github.com/grpc/grpc/archive/v1.64.0/grpc-1.64.0.tar.gz
Source1  : https://github.com/census-instrumentation/opencensus-proto/archive/v0.3.0/opencensus-proto-0.3.0.tar.gz
Summary  : @PC_DESCRIPTION@
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause MIT
Requires: grpc-bin = %{version}-%{release}
Requires: grpc-data = %{version}-%{release}
Requires: grpc-lib = %{version}-%{release}
Requires: grpc-license = %{version}-%{release}
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
%setup -q -n grpc-1.64.0
cd %{_builddir}
tar xf %{_sourcedir}/opencensus-proto-0.3.0.tar.gz
cd %{_builddir}/grpc-1.64.0
mkdir -p third_party/opencensus-proto
cp -r %{_builddir}/opencensus-proto-0.3.0/* %{_builddir}/grpc-1.64.0/third_party/opencensus-proto

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1717005991
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
-DBUILD_SHARED_LIBS=ON
make  %{?_smp_mflags}
popd
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
-DBUILD_SHARED_LIBS=ON
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1717005991
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
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3 prefix=%{buildroot}/usr || :
popd
GOAMD64=v2
pushd clr-build
%make_install prefix=%{buildroot}/usr
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/grpc_cpp_plugin
/V3/usr/bin/grpc_csharp_plugin
/V3/usr/bin/grpc_node_plugin
/V3/usr/bin/grpc_objective_c_plugin
/V3/usr/bin/grpc_php_plugin
/V3/usr/bin/grpc_python_plugin
/V3/usr/bin/grpc_ruby_plugin
/usr/bin/grpc_cpp_plugin
/usr/bin/grpc_csharp_plugin
/usr/bin/grpc_node_plugin
/usr/bin/grpc_objective_c_plugin
/usr/bin/grpc_php_plugin
/usr/bin/grpc_python_plugin
/usr/bin/grpc_ruby_plugin

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
/usr/include/grpc++/impl/codegen/create_auth_context.h
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
/usr/include/grpc/credentials.h
/usr/include/grpc/event_engine/endpoint_config.h
/usr/include/grpc/event_engine/event_engine.h
/usr/include/grpc/event_engine/extensible.h
/usr/include/grpc/event_engine/internal/memory_allocator_impl.h
/usr/include/grpc/event_engine/internal/slice_cast.h
/usr/include/grpc/event_engine/memory_allocator.h
/usr/include/grpc/event_engine/memory_request.h
/usr/include/grpc/event_engine/port.h
/usr/include/grpc/event_engine/slice.h
/usr/include/grpc/event_engine/slice_buffer.h
/usr/include/grpc/fork.h
/usr/include/grpc/grpc.h
/usr/include/grpc/grpc_audit_logging.h
/usr/include/grpc/grpc_crl_provider.h
/usr/include/grpc/grpc_posix.h
/usr/include/grpc/grpc_security.h
/usr/include/grpc/grpc_security_constants.h
/usr/include/grpc/impl/call.h
/usr/include/grpc/impl/channel_arg_names.h
/usr/include/grpc/impl/codegen/atm.h
/usr/include/grpc/impl/codegen/atm_gcc_atomic.h
/usr/include/grpc/impl/codegen/atm_gcc_sync.h
/usr/include/grpc/impl/codegen/atm_windows.h
/usr/include/grpc/impl/codegen/byte_buffer.h
/usr/include/grpc/impl/codegen/byte_buffer_reader.h
/usr/include/grpc/impl/codegen/compression_types.h
/usr/include/grpc/impl/codegen/connectivity_state.h
/usr/include/grpc/impl/codegen/fork.h
/usr/include/grpc/impl/codegen/gpr_types.h
/usr/include/grpc/impl/codegen/grpc_types.h
/usr/include/grpc/impl/codegen/log.h
/usr/include/grpc/impl/codegen/port_platform.h
/usr/include/grpc/impl/codegen/propagation_bits.h
/usr/include/grpc/impl/codegen/slice.h
/usr/include/grpc/impl/codegen/status.h
/usr/include/grpc/impl/codegen/sync.h
/usr/include/grpc/impl/codegen/sync_abseil.h
/usr/include/grpc/impl/codegen/sync_custom.h
/usr/include/grpc/impl/codegen/sync_generic.h
/usr/include/grpc/impl/codegen/sync_posix.h
/usr/include/grpc/impl/codegen/sync_windows.h
/usr/include/grpc/impl/compression_types.h
/usr/include/grpc/impl/connectivity_state.h
/usr/include/grpc/impl/grpc_types.h
/usr/include/grpc/impl/propagation_bits.h
/usr/include/grpc/impl/slice_type.h
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
/usr/include/grpc/support/json.h
/usr/include/grpc/support/log.h
/usr/include/grpc/support/log_windows.h
/usr/include/grpc/support/metrics.h
/usr/include/grpc/support/port_platform.h
/usr/include/grpc/support/string_util.h
/usr/include/grpc/support/sync.h
/usr/include/grpc/support/sync_abseil.h
/usr/include/grpc/support/sync_custom.h
/usr/include/grpc/support/sync_generic.h
/usr/include/grpc/support/sync_posix.h
/usr/include/grpc/support/sync_windows.h
/usr/include/grpc/support/thd_id.h
/usr/include/grpc/support/time.h
/usr/include/grpc/support/workaround_list.h
/usr/include/grpcpp/alarm.h
/usr/include/grpcpp/channel.h
/usr/include/grpcpp/client_context.h
/usr/include/grpcpp/completion_queue.h
/usr/include/grpcpp/create_channel.h
/usr/include/grpcpp/create_channel_binder.h
/usr/include/grpcpp/create_channel_posix.h
/usr/include/grpcpp/ext/call_metric_recorder.h
/usr/include/grpcpp/ext/channelz_service_plugin.h
/usr/include/grpcpp/ext/health_check_service_server_builder_option.h
/usr/include/grpcpp/ext/proto_server_reflection_plugin.h
/usr/include/grpcpp/ext/server_metric_recorder.h
/usr/include/grpcpp/generic/async_generic_service.h
/usr/include/grpcpp/generic/generic_stub.h
/usr/include/grpcpp/grpcpp.h
/usr/include/grpcpp/health_check_service_interface.h
/usr/include/grpcpp/impl/call.h
/usr/include/grpcpp/impl/call_hook.h
/usr/include/grpcpp/impl/call_op_set.h
/usr/include/grpcpp/impl/call_op_set_interface.h
/usr/include/grpcpp/impl/channel_argument_option.h
/usr/include/grpcpp/impl/channel_interface.h
/usr/include/grpcpp/impl/client_unary_call.h
/usr/include/grpcpp/impl/codegen/async_generic_service.h
/usr/include/grpcpp/impl/codegen/async_stream.h
/usr/include/grpcpp/impl/codegen/async_unary_call.h
/usr/include/grpcpp/impl/codegen/byte_buffer.h
/usr/include/grpcpp/impl/codegen/call.h
/usr/include/grpcpp/impl/codegen/call_hook.h
/usr/include/grpcpp/impl/codegen/call_op_set.h
/usr/include/grpcpp/impl/codegen/call_op_set_interface.h
/usr/include/grpcpp/impl/codegen/callback_common.h
/usr/include/grpcpp/impl/codegen/channel_interface.h
/usr/include/grpcpp/impl/codegen/client_callback.h
/usr/include/grpcpp/impl/codegen/client_context.h
/usr/include/grpcpp/impl/codegen/client_interceptor.h
/usr/include/grpcpp/impl/codegen/client_unary_call.h
/usr/include/grpcpp/impl/codegen/completion_queue.h
/usr/include/grpcpp/impl/codegen/completion_queue_tag.h
/usr/include/grpcpp/impl/codegen/config.h
/usr/include/grpcpp/impl/codegen/config_protobuf.h
/usr/include/grpcpp/impl/codegen/create_auth_context.h
/usr/include/grpcpp/impl/codegen/delegating_channel.h
/usr/include/grpcpp/impl/codegen/intercepted_channel.h
/usr/include/grpcpp/impl/codegen/interceptor.h
/usr/include/grpcpp/impl/codegen/interceptor_common.h
/usr/include/grpcpp/impl/codegen/message_allocator.h
/usr/include/grpcpp/impl/codegen/metadata_map.h
/usr/include/grpcpp/impl/codegen/method_handler.h
/usr/include/grpcpp/impl/codegen/method_handler_impl.h
/usr/include/grpcpp/impl/codegen/proto_buffer_reader.h
/usr/include/grpcpp/impl/codegen/proto_buffer_writer.h
/usr/include/grpcpp/impl/codegen/proto_utils.h
/usr/include/grpcpp/impl/codegen/rpc_method.h
/usr/include/grpcpp/impl/codegen/rpc_service_method.h
/usr/include/grpcpp/impl/codegen/security/auth_context.h
/usr/include/grpcpp/impl/codegen/serialization_traits.h
/usr/include/grpcpp/impl/codegen/server_callback.h
/usr/include/grpcpp/impl/codegen/server_callback_handlers.h
/usr/include/grpcpp/impl/codegen/server_context.h
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
/usr/include/grpcpp/impl/codegen/time.h
/usr/include/grpcpp/impl/completion_queue_tag.h
/usr/include/grpcpp/impl/create_auth_context.h
/usr/include/grpcpp/impl/delegating_channel.h
/usr/include/grpcpp/impl/grpc_library.h
/usr/include/grpcpp/impl/intercepted_channel.h
/usr/include/grpcpp/impl/interceptor_common.h
/usr/include/grpcpp/impl/metadata_map.h
/usr/include/grpcpp/impl/method_handler_impl.h
/usr/include/grpcpp/impl/proto_utils.h
/usr/include/grpcpp/impl/rpc_method.h
/usr/include/grpcpp/impl/rpc_service_method.h
/usr/include/grpcpp/impl/serialization_traits.h
/usr/include/grpcpp/impl/server_builder_option.h
/usr/include/grpcpp/impl/server_builder_plugin.h
/usr/include/grpcpp/impl/server_callback_handlers.h
/usr/include/grpcpp/impl/server_initializer.h
/usr/include/grpcpp/impl/service_type.h
/usr/include/grpcpp/impl/status.h
/usr/include/grpcpp/impl/sync.h
/usr/include/grpcpp/resource_quota.h
/usr/include/grpcpp/security/alts_context.h
/usr/include/grpcpp/security/alts_util.h
/usr/include/grpcpp/security/audit_logging.h
/usr/include/grpcpp/security/auth_context.h
/usr/include/grpcpp/security/auth_metadata_processor.h
/usr/include/grpcpp/security/authorization_policy_provider.h
/usr/include/grpcpp/security/binder_credentials.h
/usr/include/grpcpp/security/binder_security_policy.h
/usr/include/grpcpp/security/credentials.h
/usr/include/grpcpp/security/server_credentials.h
/usr/include/grpcpp/security/tls_certificate_provider.h
/usr/include/grpcpp/security/tls_certificate_verifier.h
/usr/include/grpcpp/security/tls_credentials_options.h
/usr/include/grpcpp/security/tls_crl_provider.h
/usr/include/grpcpp/server.h
/usr/include/grpcpp/server_builder.h
/usr/include/grpcpp/server_context.h
/usr/include/grpcpp/server_interface.h
/usr/include/grpcpp/server_posix.h
/usr/include/grpcpp/support/async_stream.h
/usr/include/grpcpp/support/async_unary_call.h
/usr/include/grpcpp/support/byte_buffer.h
/usr/include/grpcpp/support/callback_common.h
/usr/include/grpcpp/support/channel_arguments.h
/usr/include/grpcpp/support/client_callback.h
/usr/include/grpcpp/support/client_interceptor.h
/usr/include/grpcpp/support/config.h
/usr/include/grpcpp/support/error_details.h
/usr/include/grpcpp/support/interceptor.h
/usr/include/grpcpp/support/message_allocator.h
/usr/include/grpcpp/support/method_handler.h
/usr/include/grpcpp/support/proto_buffer_reader.h
/usr/include/grpcpp/support/proto_buffer_writer.h
/usr/include/grpcpp/support/server_callback.h
/usr/include/grpcpp/support/server_interceptor.h
/usr/include/grpcpp/support/slice.h
/usr/include/grpcpp/support/status.h
/usr/include/grpcpp/support/status_code_enum.h
/usr/include/grpcpp/support/string_ref.h
/usr/include/grpcpp/support/stub_options.h
/usr/include/grpcpp/support/sync_stream.h
/usr/include/grpcpp/support/time.h
/usr/include/grpcpp/support/validate_service_config.h
/usr/include/grpcpp/version_info.h
/usr/include/grpcpp/xds_server_builder.h
/usr/lib64/cmake/grpc/gRPCConfig.cmake
/usr/lib64/cmake/grpc/gRPCConfigVersion.cmake
/usr/lib64/cmake/grpc/gRPCPluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/grpc/gRPCPluginTargets.cmake
/usr/lib64/cmake/grpc/gRPCTargets-relwithdebinfo.cmake
/usr/lib64/cmake/grpc/gRPCTargets.cmake
/usr/lib64/cmake/grpc/modules/Findc-ares.cmake
/usr/lib64/cmake/grpc/modules/Findre2.cmake
/usr/lib64/cmake/grpc/modules/Findsystemd.cmake
/usr/lib64/libaddress_sorting.so
/usr/lib64/libgpr.so
/usr/lib64/libgrpc++.so
/usr/lib64/libgrpc++_alts.so
/usr/lib64/libgrpc++_error_details.so
/usr/lib64/libgrpc++_reflection.so
/usr/lib64/libgrpc++_unsecure.so
/usr/lib64/libgrpc.so
/usr/lib64/libgrpc_authorization_provider.so
/usr/lib64/libgrpc_plugin_support.so
/usr/lib64/libgrpc_unsecure.so
/usr/lib64/libgrpcpp_channelz.so
/usr/lib64/libupb_base_lib.so
/usr/lib64/libupb_json_lib.so
/usr/lib64/libupb_mem_lib.so
/usr/lib64/libupb_message_lib.so
/usr/lib64/libupb_textformat_lib.so
/usr/lib64/libutf8_range_lib.so
/usr/lib64/pkgconfig/gpr.pc
/usr/lib64/pkgconfig/grpc++.pc
/usr/lib64/pkgconfig/grpc++_unsecure.pc
/usr/lib64/pkgconfig/grpc.pc
/usr/lib64/pkgconfig/grpc_unsecure.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libaddress_sorting.so.41.0.0
/V3/usr/lib64/libgpr.so.41.0.0
/V3/usr/lib64/libgrpc++.so.1.64.0
/V3/usr/lib64/libgrpc++_alts.so.1.64.0
/V3/usr/lib64/libgrpc++_error_details.so.1.64.0
/V3/usr/lib64/libgrpc++_reflection.so.1.64.0
/V3/usr/lib64/libgrpc++_unsecure.so.1.64.0
/V3/usr/lib64/libgrpc.so.41.0.0
/V3/usr/lib64/libgrpc_authorization_provider.so.1.64.0
/V3/usr/lib64/libgrpc_plugin_support.so.1.64.0
/V3/usr/lib64/libgrpc_unsecure.so.41.0.0
/V3/usr/lib64/libgrpcpp_channelz.so.1.64.0
/V3/usr/lib64/libupb_base_lib.so.41.0.0
/V3/usr/lib64/libupb_json_lib.so.41.0.0
/V3/usr/lib64/libupb_mem_lib.so.41.0.0
/V3/usr/lib64/libupb_message_lib.so.41.0.0
/V3/usr/lib64/libupb_textformat_lib.so.41.0.0
/V3/usr/lib64/libutf8_range_lib.so.41.0.0
/usr/lib64/libaddress_sorting.so.41
/usr/lib64/libaddress_sorting.so.41.0.0
/usr/lib64/libgpr.so.41
/usr/lib64/libgpr.so.41.0.0
/usr/lib64/libgrpc++.so.1.64
/usr/lib64/libgrpc++.so.1.64.0
/usr/lib64/libgrpc++_alts.so.1.64
/usr/lib64/libgrpc++_alts.so.1.64.0
/usr/lib64/libgrpc++_error_details.so.1.64
/usr/lib64/libgrpc++_error_details.so.1.64.0
/usr/lib64/libgrpc++_reflection.so.1.64
/usr/lib64/libgrpc++_reflection.so.1.64.0
/usr/lib64/libgrpc++_unsecure.so.1.64
/usr/lib64/libgrpc++_unsecure.so.1.64.0
/usr/lib64/libgrpc.so.41
/usr/lib64/libgrpc.so.41.0.0
/usr/lib64/libgrpc_authorization_provider.so.1.64
/usr/lib64/libgrpc_authorization_provider.so.1.64.0
/usr/lib64/libgrpc_plugin_support.so.1.64
/usr/lib64/libgrpc_plugin_support.so.1.64.0
/usr/lib64/libgrpc_unsecure.so.41
/usr/lib64/libgrpc_unsecure.so.41.0.0
/usr/lib64/libgrpcpp_channelz.so.1.64
/usr/lib64/libgrpcpp_channelz.so.1.64.0
/usr/lib64/libupb_base_lib.so.41
/usr/lib64/libupb_base_lib.so.41.0.0
/usr/lib64/libupb_json_lib.so.41
/usr/lib64/libupb_json_lib.so.41.0.0
/usr/lib64/libupb_mem_lib.so.41
/usr/lib64/libupb_mem_lib.so.41.0.0
/usr/lib64/libupb_message_lib.so.41
/usr/lib64/libupb_message_lib.so.41.0.0
/usr/lib64/libupb_textformat_lib.so.41
/usr/lib64/libupb_textformat_lib.so.41.0.0
/usr/lib64/libutf8_range_lib.so.41
/usr/lib64/libutf8_range_lib.so.41.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grpc/0590bc7a4e55e5f4d7b94045ee76e35914bcb614
/usr/share/package-licenses/grpc/242ec6abfdd8c114f2e803b84934469c299348fc
/usr/share/package-licenses/grpc/252c7fd154ca740ae6f765d206fbd9119108a0e3
/usr/share/package-licenses/grpc/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/grpc/aa0f4491c1110db68dd4e054555e255fd470d4f6
/usr/share/package-licenses/grpc/d6cf8b65815efff8a46def3ec4c74c57033d25fa
