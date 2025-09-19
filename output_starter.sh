#!/bin/bash
source "/srv/monitoring/bin/activate"
result=$(timeout -k 50 45 python3 "/srv/monitoring/$1.py")

if [ -z "${result}" ]
then
    echo "{}"
else
    echo "$result"
fi

exit 0