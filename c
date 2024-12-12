#!/bin/bash

day=$1
fn=c$day.py
if [ -f $fn ]; then
  echo "Day $day code already exists!"
  exit 1
fi

cat <<EOF >> $fn
import common
from collections import defaultdict
data = common.ReadInput($day)
w = len(data[0])
h = len(data)
EOF

code $fn