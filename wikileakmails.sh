#!/bin/bash

mkdir dwikileakmails
cd dwikileakmails
for i in `seq 1 30000`
do
wget https://wikileaks.org/dnc-emails//get/$i
done
