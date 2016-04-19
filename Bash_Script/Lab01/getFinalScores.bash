#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-25 18:32:08 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Lab01/getFinalScores.bash $
#$Revision: 86784 $

[[ $# != 1 ]] && echo "usage: ./getFinalScores.bash <filename>" && exit 1

if [[ ! -e $1 ]]
then
    echo "Error reading input file: $1"
    exit 2
fi

output=$(echo $1 | cut -d . -f 1)
output=$(echo ${output}.out)
[[ -e $output ]] && echo Output file ${output} already exists && exit 3 

while read line 
do
    name=$(echo $line | cut -d , -f 1)
    ass=$(echo $line | cut -d , -f 2)
    mid1=$(echo $line | cut -d , -f 3)
    mid2=$(echo $line | cut -d , -f 4)
    proj=$(echo $line | cut -d , -f 5)
    ((final= 15*$ass/100 + 30*$mid1/100 + 30*$mid2/100 + 25*$proj/100))
    echo "$name,$final"
    echo "$name,$final" >> $output

done < $1
