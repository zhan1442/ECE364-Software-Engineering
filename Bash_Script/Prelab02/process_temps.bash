#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-25 21:53:07 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab02/process_temps.bash $
#$Revision: 86841 $

[[ $# != 1 ]] && echo "usage: process_temps.bash <input file>" && exit 1

[[ ! -r $1 ]] && echo "Error: $1 is not a readable file." && exit 2

exec 3< $1
read line <&3
while read t data
do
    arr=($data)
    num=${#arr[*]}
    tot=0
    for i in ${arr[*]}
    do
        ((tot += i))
    done
    ((avg = tot / num))
    echo "Average temperature for time $t was $avg C."
done <&3
