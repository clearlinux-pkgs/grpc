PKG_NAME := grpc
URL = https://github.com/grpc/grpc/archive/v1.24.2.tar.gz
ARCHIVES = https://github.com/google/benchmark/archive/090faecb454fbd6e6e17a75ef8146acb037118d4.tar.gz third_party/benchmark https://github.com/c-ares/c-ares/archive/e982924acee7f7313b4baa4ee5ec000c5e373c30.tar.gz third_party/cares/cares https://github.com/gflags/gflags/archive/28f50e0fed19872e0fd50dd23ce2ee8cd759338e.tar.gz third_party/gflags https://github.com/protocolbuffers/protobuf/archive/09745575a923640154bcf307fba8aedff47f240a.tar.gz third_party/protobuf https://github.com/google/boringssl/archive/b29b21a81b32ec273f118f589f46d56ad3332420.tar.gz third_party/boringssl https://github.com/madler/zlib/archive/cacf7f1d4e3d44d871b605da3b647f07d718623f.tar.gz third_party/zlib https://github.com/protocolbuffers/upb/archive/931bbecbd3230ae7f22efa5d203639facc47f719.tar.gz third_party/upb

include ../common/Makefile.common
