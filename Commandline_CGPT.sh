#!/bin/bash

if [ ! -f "series.json" ]; then
  echo "Error: 'series.json' file not found."
  exit 1
fi

jq -r '. as $parent | .works[] | [$parent.id, $parent.title, .books_count] | join("|")' series.json | awk -F'|' '{a[$1"|"$2]+=$3} END{for (i in a) print i"| "a[i]}' | sort -t'|' -k3nr | head -n 5
