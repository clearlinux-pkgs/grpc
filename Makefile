PKG_NAME := grpc
URL = https://github.com/grpc/grpc/archive/v1.24.2.tar.gz
ARCHIVES = https://github.com/google/benchmark/tarball/090faecb454fbd6e6e17a75ef8146acb037118d4 third_party/benchmark https://github.com/c-ares/c-ares/tarball/e982924acee7f7313b4baa4ee5ec000c5e373c30 third_party/cares/cares https://github.com/gflags/gflags/tarball/28f50e0fed19872e0fd50dd23ce2ee8cd759338e third_party/gflags https://github.com/protocolbuffers/protobuf/tarball/09745575a923640154bcf307fba8aedff47f240a third_party/protobuf https://github.com/google/boringssl/tarball/b29b21a81b32ec273f118f589f46d56ad3332420 third_party/boringssl https://github.com/madler/zlib/tarball/cacf7f1d4e3d44d871b605da3b647f07d718623f third_party/zlib https://github.com/protocolbuffers/upb/tarball/931bbecbd3230ae7f22efa5d203639facc47f719 third_party/upb

include ../common/Makefile.common
