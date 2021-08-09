#!/bin/sh
echo "  NAME                        PID        SWAP"
for PID in /proc/[0-9]*
do
  if stat $PID/status >/dev/null
  then
    # get name of process
    procname=`grep 'Name:' $PID/status | awk -e '{ print $2 };'`
    # get amount of swap in use by that process
    procswap=`grep 'VmSwap:' $PID/status | awk -e '{ print $2 };'`

    printf "%-21s %11d %11d\n" $procname `basename $PID` $procswap
  fi
done
