#!/bin/sh
#
# See README for up to date usage examples.
# vim: syntax=sh noexpandtab
#

umask 022
cd "$(dirname "$0")/.."
TOP="$(pwd)"

. build/nano_env
. build/functions.sh
. build/repos.sh

. build/nanobsd/nanobsd_funcs.sh

# File descriptor 3 is used for logging output, see pprint
exec 3>&1

NANO_STARTTIME=`date +%s`
pprint 1 "NanoBSD image ${NANO_NAME} build starting"

trap on_exit EXIT

# Number of jobs to pass to make. Only applies to src so far.
MAKE_JOBS=$(( 2 * $(sysctl -n kern.smp.cpus) + 1 ))
if [ ${MAKE_JOBS} -gt 10 ]; then
        MAKE_JOBS=10
fi
export MAKE_JOBS

NANO_PMAKE="${NANO_PMAKE} -j ${MAKE_JOBS}"

mkdir -p ${MAKEOBJDIRPREFIX}
printenv > ${MAKEOBJDIRPREFIX}/_.env
make_conf_build
build_world
build_kernel

mkdir -p ${NANO_OBJ} ${NANO_WORLDDIR}
printenv > ${NANO_OBJ}/_.env
make_conf_install
install_world
install_etc
setup_nanobsd_etc
install_kernel

