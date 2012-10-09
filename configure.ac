AC_INIT([leveldb], [0.1], [leveldb@googlegroups.com])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])
m4_ifdef([AM_PROG_AR], [AM_PROG_AR])
AC_PROG_CC
AC_PROG_CXX
AC_PROG_LIBTOOL
AC_LANG_CPLUSPLUS
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([
  Makefile
])

AC_MSG_CHECKING(whether compiler supports C++11 cstdatomic)
OLD_CXXFLAGS="$CXXFLAGS"
CXXFLAGS="$CXXFLAGS -std=c++0x"
AC_COMPILE_IFELSE([AC_LANG_SOURCE([
#include <cstdatomic>
int main() {}
])], [
     AC_MSG_RESULT(yes)
     has_cstdatomic=yes
   ],
   [
     AC_MSG_RESULT(no)
     has_cstdatomic=no
   ])
CXXFLAGS="$OLD_CXXFLAGS"

if test "x$has_cstdatomic" = "xyes"
then
  CSTDATOMIC="1"
else
  CSTDATOMIC=""
fi

# tcmalloc?
AC_ARG_WITH([tcmalloc],
	    [AS_HELP_STRING([--without-tcmalloc], [disable tcmalloc for memory allocations])],
	    [],
	    [with_tcmalloc=yes])
TCMALLOC=
AS_IF([test "x$with_tcmalloc" != xno],
	    [AC_CHECK_LIB([tcmalloc], [malloc],
	     [AC_SUBST([LIBTCMALLOC], ["-ltcmalloc"])
	       AC_DEFINE([HAVE_LIBTCMALLOC], [1],
	       		 [Define if you have tcmalloc])
	       HAVE_LIBTCMALLOC=1
	     ],
	    [AC_MSG_FAILURE(
		  [no tcmalloc found (use --without-tcmalloc to disable)])])])
AM_CONDITIONAL(WITH_TCMALLOC, [test "$HAVE_LIBTCMALLOC" = "1"])
AM_CONDITIONAL(CSTDATOMIC, [test "$CSTDATOMIC" = "1"])

AC_OUTPUT
