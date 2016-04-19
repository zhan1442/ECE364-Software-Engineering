#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-25 23:38:08 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab02/yards.bash $
#$Revision: 86877 $

[[ $# != 1 ]] && echo "usage: yards.bash <filename>" && exit 1

[[ ! -r $1 ]] && echo "Error: $1 is not readable" && exit 2 

max=0
while read line
do
    name=$(echo $line | cut -d " " -f1)
    arr=($(echo $line | cut -d " " -f2-))
    num=${#arr[*]}
    tot=0
    totvar=0
    for i in ${arr[*]}
    do
        ((tot += i))
    done
    ((avg = tot / num))
    ((avg > max)) && ((max = avg))
    for i in ${arr[*]}
    do
        ((totvar += (i - avg)*(i - avg)))
    done
    ((var = totvar / num))
    echo "$name schools averaged $avg yards receiving with a variance of $var"
done < $1
    echo "The largest average yardage was $max"
