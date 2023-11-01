#!/bin/bash
echo "id|title|total_books_count" 
cat series.json | jq -r '. as $parent | .works[] | [$parent.id, $parent.title, .books_count] | join("|")' | awk -F'|' '{a[$1"|"$2]+=$3} END{for (i in a) print i"| "a[i]}' | sort -t'|' -k3nr | head -5