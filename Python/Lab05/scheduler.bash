#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-02-16 17:18:41 -0500 (Tue, 16 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Lab05/scheduler.bash $
#$Revision: 88281 $

[[ $# != 1 ]] && echo "usage: scheduler.bash <filename>" && exit 1

[[ ! -r $1 ]] && echo "$1 is not readable" && exit 2

#[[ -e schedule.out ]] && echo "scheduler.out already exists." && exit 3

name=$(cut $1 -d " " -f1)
echo $name

echo "        07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00" > schedule.out

count_arr=(0 0 0 0 0 0 0 0 0 0 0)

while read line
do
    array=(- - - - - - - - - - -)
    for ((i=1; i < 12; i++))
    do
        x=""
        x=$(echo $line | cut -d " " -f2 | cut -d "," -f $i)
        if [[ $x = 07:00 || $x = 08:00||$x = 09:00||$x = 10:00||$x = 11:00|| $x = 12:00|| $x = 13:00|| $x = 14:00|| $x = 15:00|| $x = 16:00|| $x = 17:00 ]] 
        then
            s=$(echo $x | cut -d ":" -f1)
            if [[ $s == 7 || $s == 8 || $s == 9 ||$s == 10 ||$s == 11 ||$s == 12 ||$s == 13 ||$s == 14 ||$s == 15 ||$s == 16 || $s == 17 ]]
            then
                ((ind = s - 7))
                array[$ind]=$(echo Y)
            fi
        fi
        echo $array
    done
    echo
done < $1

