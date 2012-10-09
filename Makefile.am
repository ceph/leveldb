#-----------------------------------------------
# Uncomment exactly one of the lines labelled (A), (B), and (C) below
# to switch between compilation modes.

OPT ?= -O2 -DNDEBUG       # (A) Production use (optimized mode)
# OPT ?= -g2              # (B) Debug mode, w/ full line-level debugging symbols
# OPT ?= -O2 -g2 -DNDEBUG # (C) Profiling mode: opt, but w/debugging symbols
#-----------------------------------------------

# TODO maybe support android & chromium platforms via automake too?

AM_CFLAGS = -I$(srcdir)/include $(OPT) -pthread -fno-builtin-memcmp -DLEVELDB_PLATFORM_POSIX

AM_CXXFLAGS = -I$(srcdir)/include $(OPT) -pthread -fno-builtin-memcmp -DLEVELDB_PLATFORM_POSIX
if CSTDATOMIC
AM_CXXFLAGS += -DLEVELDB_CSTDATOMIC_PRESENT -std=c++0x
endif
AM_LDFLAGS = -pthread

if WITH_TCMALLOC
AM_LDFLAGS += -ltcmalloc
endif

# items will be appended to this
check_PROGRAMS = $(TESTS)

# tests to actually run on "make check"; if you need extra, non-test,
# executables built, you need to replace this with manual assignments
# target by target
TESTS =

noinst_LIBRARIES = libleveldb.a
noinst_HEADERS = \
  ./util/random.h \
	./util/coding.h \
	./util/logging.h \
	./util/posix_logger.h \
	./util/hash.h \
	./util/crc32c.h \
	./util/histogram.h \
	./util/mutexlock.h \
	./util/testutil.h \
	./util/testharness.h \
	./util/arena.h \
	./port/win/stdint.h \
	./port/port_example.h \
	./port/port_posix.h \
	./port/port.h \
	./port/atomic_pointer.h \
	./port/port_android.h \
	./table/format.h \
	./table/two_level_iterator.h \
	./table/iterator_wrapper.h \
	./table/block.h \
	./table/block_builder.h \
	./table/merger.h \
	./doc/bench \
	./include/leveldb/options.h \
	./include/leveldb/cache.h \
	./include/leveldb/table.h \
	./include/leveldb/status.h \
	./include/leveldb/c.h \
	./include/leveldb/comparator.h \
	./include/leveldb/env.h \
	./include/leveldb/write_batch.h \
	./include/leveldb/db.h \
	./include/leveldb/slice.h \
	./include/leveldb/iterator.h \
	./include/leveldb/table_builder.h \
	./config.h \
	./helpers/memenv/memenv.h \
	./db/db_iter.h \
	./db/table_cache.h \
	./db/builder.h \
	./db/memtable.h \
	./db/snapshot.h \
	./db/dbformat.h \
	./db/log_writer.h \
	./db/version_set.h \
	./db/skiplist.h \
	./db/write_batch_internal.h \
	./db/log_format.h \
	./db/filename.h \
	./db/db_impl.h \
	./db/log_reader.h \
	./db/version_edit.h

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

TESTUTIL = util/testutil.cc
TESTHARNESS = util/testharness.cc $(TESTUTIL)

c_test_SOURCES = db/c_test.c $(TESTHARNESS)
c_test_LDADD = libleveldb.a
TESTS += c_test

coding_test_SOURCES = util/coding_test.cc $(TESTHARNESS)
coding_test_LDADD = libleveldb.a
TESTS += coding_test

db_bench_SOURCES = db/db_bench.cc $(TESTUTIL)
db_bench_LDADD = libleveldb.a
check_PROGRAMS += db_bench

#db_bench_sqlite3_SOURCES = doc/bench/db_bench_sqlite3.cc $(TESTUTIL)
#db_bench_sqlite3_LDADD = libleveldb.a
#TESTS += db_bench_sqlite3

#db_bench_tree_db_SOURCES = doc/bench/db_bench_tree_db.cc $(TESTUTIL)
#db_bench_tree_db_LDADD = libleveldb.a
#TESTS += db_bench_tree_db

arena_test_SOURCES = util/arena_test.cc $(TESTHARNESS)
arena_test_LDADD = libleveldb.a
TESTS += arena_test

cache_test_SOURCES = util/cache_test.cc $(TESTHARNESS)
cache_test_LDADD = libleveldb.a
TESTS += cache_test

corruption_test_SOURCES = db/corruption_test.cc $(TESTHARNESS)
corruption_test_LDADD = libleveldb.a
TESTS += corruption_test

crc32c_test_SOURCES = util/crc32c_test.cc $(TESTHARNESS)
crc32c_test_LDADD = libleveldb.a
TESTS += crc32c_test

db_test_SOURCES = db/db_test.cc $(TESTHARNESS)
db_test_LDADD = libleveldb.a
TESTS += db_test

dbformat_test_SOURCES = db/dbformat_test.cc $(TESTHARNESS)
dbformat_test_LDADD = libleveldb.a
TESTS += dbformat_test

env_test_SOURCES = util/env_test.cc $(TESTHARNESS)
env_test_LDADD = libleveldb.a
TESTS += env_test

filename_test_SOURCES = db/filename_test.cc $(TESTHARNESS)
filename_test_LDADD = libleveldb.a
TESTS += filename_test

log_test_SOURCES = db/log_test.cc $(TESTHARNESS)
log_test_LDADD = libleveldb.a
TESTS += log_test

table_test_SOURCES = table/table_test.cc $(TESTHARNESS)
table_test_LDADD = libleveldb.a
TESTS += table_test

skiplist_test_SOURCES = db/skiplist_test.cc $(TESTHARNESS)
skiplist_test_LDADD = libleveldb.a
TESTS += skiplist_test

version_edit_test_SOURCES = db/version_edit_test.cc $(TESTHARNESS)
version_edit_test_LDADD = libleveldb.a
TESTS += version_edit_test

version_set_test_SOURCES = db/version_set_test.cc $(TESTHARNESS)
version_set_test_LDADD = libleveldb.a
TESTS += version_set_test

write_batch_test_SOURCES = db/write_batch_test.cc $(TESTHARNESS)
write_batch_test_LDADD = libleveldb.a
TESTS += write_batch_test
