#!/bin/sh

BASE_REL=$(dpkg-parsechangelog 2>/dev/null | sed -ne 's/Version: \([0-9]\)\+.*/\1/p')
OLDDIR=${PWD}
GOS_DIR=${OLDDIR}/get-orig-source
GIT_COMMIT='git log --no-color -1 --oneline | cut -d" " -f1'
GIT_DATE='git log --no-color -1 --date=iso | sed -ne "s/Date:\s\+\(.*\).*/\1/p" | cut -d" " -f1 | tr -d "-"'

if [ -z ${BASE_REL} ]; then
	echo 'Please run this script from the sources root directory.'
	exit 1
fi


rm -rf ${GOS_DIR}
mkdir ${GOS_DIR} && cd ${GOS_DIR}
git clone https://code.google.com/p/leveldb/ leveldb
cd leveldb/
LEVELDB_GIT_COMMIT=$(eval "${GIT_COMMIT}")
LEVELDB_GIT_DATE=$(eval "${GIT_DATE}")
cd .. && tar cjf \
	${OLDDIR}/leveldb_${BASE_REL}+${LEVELDB_GIT_DATE}.git${LEVELDB_GIT_COMMIT}.orig.tar.bz2 \
	leveldb --exclude-vcs
rm -rf ${GOS_DIR}
