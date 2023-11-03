#!/bin/bash
echo "id|title|total_books_count"
jq -r '. as $parent | .works[] | [$parent.id, $parent.title, .books_count] | join("|")' series.json | awk -F'|' '{a[$1"|"$2]+=$3} END{for (i in a) print i"| "a[i]}' | sort -t'|' -k3nr | head -5
