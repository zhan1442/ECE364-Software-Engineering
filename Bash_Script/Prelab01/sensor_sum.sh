#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-17 04:09:52 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab01/sensor_sum.sh $
#$Revisioni$

(( ! $# == 1 )) && echo "usage: sensor_sum.sh" && exit 0
[[ ! -r $1 ]] && echo "error: $1 is not a readable file!" && exit 0

#while read line
#do
#    id=$(echo "$line" | cut -d - -f 1)
#    val1=$(echo $line | cut -d " " -f 2)
#    val2=$(echo $line | cut -d " " -f 3)
#    val3=$(echo $line | cut -d " " -f 4)
#    ((sum= val1 + val2 + val3))
#    echo $id $sum
#done < $1

echo "======"

while read id val1 val2 val3
do
    ((sum=val1 + val2 + val3))
    id=$(echo $id | cut -d - -f 1)
    echo "$id $sum"
done < $1



exit 0


