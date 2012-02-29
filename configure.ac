AC_INIT([leveldb], [0.1], [leveldb@googlegroups.com])
AM_INIT_AUTOMAKE([-Wall -Werror foreign])
m4_ifdef([AM_SILENT_RULES],[AM_SILENT_RULES([yes])])
AC_PROG_CC
AC_PROG_CXX
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([
  Makefile
])
AC_PROG_RANLIB

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

AC_OUTPUT
