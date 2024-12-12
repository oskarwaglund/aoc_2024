#!/bin/bash


function run()
{
  day=$1

  echo ""
  echo "Day $day:"
  python3 c$day.py
}

function runAll()
{
for day in {1..25}; do
  if [ -f c$day.py ]; then
    time run $day
  fi
done
}

if [ $1 == "a" ]; then
  time ( runAll && echo "" && echo "Total time:" )
else
  time run $1
fi
