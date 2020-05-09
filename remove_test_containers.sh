#!/bin/bash

i=1

while :
do
  docker container rm parletorecritmenttask_web_run_$i || exit
  i=$((i + 1))
done