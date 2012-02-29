#-----------------------------------------------
# Uncomment exactly one of the lines labelled (A), (B), and (C) below
# to switch between compilation modes.

OPT ?= -O2 -DNDEBUG       # (A) Production use (optimized mode)
# OPT ?= -g2              # (B) Debug mode, w/ full line-level debugging symbols
# OPT ?= -O2 -g2 -DNDEBUG # (C) Profiling mode: opt, but w/debugging symbols
#-----------------------------------------------

# TODO maybe support android & chromium platforms via automake too?
CFLAGS = -I$(srcdir)/include $(OPT) -pthread -fno-builtin-memcmp -DLEVELDB_PLATFORM_POSIX -DLEVELDB_CSTDATOMIC_PRESENT
CXXFLAGS = -I$(srcdir)/include $(OPT) -pthread -fno-builtin-memcmp -DLEVELDB_PLATFORM_POSIX -DLEVELDB_CSTDATOMIC_PRESENT -std=c++0x
LDFLAGS = -pthread

if WITH_TCMALLOC
LDFLAGS += -ltcmalloc
endif

# items will be appended to this
check_PROGRAMS =

# tests to actually run on "make check"; if you need extra, non-test,
# executables built, you need to replace this with manual assignments
# target by target
TESTS = $(check_PROGRAMS)

noinst_LIBRARIES = libleveldb.a
libleveldb_a_SOURCES = \
	./db/builder.cc \
	./db/c.cc \
	./db/db_impl.cc \
	./db/db_iter.cc \
	./db/filename.cc \
	./db/dbformat.cc \
	./db/log_reader.cc \
	./db/log_writer.cc \
	./db/memtable.cc \
	./db/repair.cc \
	./db/table_cache.cc \
	./db/version_edit.cc \
	./db/version_set.cc \
	./db/write_batch.cc \
	./port/port_posix.cc \
	./table/block.cc \
	./table/block_builder.cc \
	./table/format.cc \
	./table/iterator.cc \
	./table/merger.cc \
	./table/table.cc \
	./table/table_builder.cc \
	./table/two_level_iterator.cc \
	./util/arena.cc \
	./util/cache.cc \
	./util/coding.cc \
	./util/comparator.cc \
	./util/crc32c.cc \
	./util/env.cc \
	./util/env_posix.cc \
	./util/hash.cc \
	./util/histogram.cc \
	./util/logging.cc \
	./util/options.cc \
	./util/status.cc

c_test_SOURCES = db/c_test.c util/testharness.cc util/testutil.cc
c_test_LDADD = libleveldb.a
check_PROGRAMS += c_test

coding_test_SOURCES = util/coding_test.cc util/testharness.cc util/testutil.cc
coding_test_LDADD = libleveldb.a
check_PROGRAMS += coding_test
