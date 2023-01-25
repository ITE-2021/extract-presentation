#!/bin/bash
cd frames/
rename 'unless (/0+[0-9]{5}.bmp/) {s/^([0-9]{1,4}\.bmp)$/0000$1/g;s/0*([0-9]{5}\..*)/$1/}' *
