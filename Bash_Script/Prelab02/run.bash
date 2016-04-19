#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-25 23:52:04 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab02/run.bash $
#$Revision: 86880 $

[[ $# != 2 ]] && echo "usage: run.bash <filename> <filename>" && exit 1

gcc $1 -o quick_sim

[[ $? != 0 ]] && echo "error: quick_sim could not be compiled!" && exit 2

ofile=$2
while [[ -e $ofile ]]
do
    read -p "$ofile exists.  Would you like to delete it? " decision
    if [[ $decision == "n" ]] 
    then
        read -p "Enter a new filename: " ofile
    elif [[ $decision == "y" ]]
    then
        rm -f $ofile
    fi
done       

for s in 1 2 4 8 16 32
do
    for w in 1 2 4 8 16
    do
        gcc $1 -o quick_sim
        quick_sim $s $w a | cut -d ":" -f 2,4,6,8,10 >> $ofile
        gcc $1 -o quick_sim 
        quick_sim $s $w i | cut -d ":" -f 2,4,6,8,10 >> $ofile
    done
done

exec 3< $ofile
read line <&3
min=$(echo $line | cut -d ":" -f5)
while read line 
do
    tim=$(echo $line | cut -d ":" -f5)
    if ((tim < min))
    then
        minline=$(echo $line)
        ((min = tim))
    fi 
done < $ofile
name=$(echo $minline | cut -d ":" -f1)
s=$(echo $minline | cut -d ":" -f2)
w=$(echo $minline | cut -d ":" -f3)
echo "Fastest run time achieved by $name with cache size $s and issue width $w was $min"

#cut -d ":" -f 1,2,3,4,5 $ofile --output-delimiter "," > "${ofile}.tmp"  && mv "${ofile}.tmp" $ofile
#sort -n number; -k colum; -r reverse; -t delimiter

