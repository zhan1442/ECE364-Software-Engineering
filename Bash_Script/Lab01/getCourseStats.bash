#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-25 18:31:45 -0500 (Mon, 25 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Lab01/getCourseStats.bash $
#$Revision: 86783 $

[[ $# != 1 ]] && echo "usage: ./getFinalScores.bash <filename>" && exit 1
if [[ $1 != "ece364" && $1 != "ece337" && $1 != "ece468" ]]
then
    echo "Error: course $1 is not a valid option."
    exit 5
fi

files=$(ls gradebooks/$1*)
num=0
tots=0
max=0

for file in $files 
do
   ./getFinalScores.bash $file > /dev/null
   (( $? != 0 )) && echo "STDOUT: 'Error while running getFinalScores.bash'" && exit 3 
   output=$(echo $file | cut -d . -f 1)
   output=$(echo ${output}.out)
   while read student
   do
        ((num++))
        score=$(echo $student | cut -d , -f 2)
        if (( $score >= $max ))
        then
            ((max = $score))
            maxname=$(echo $student | cut -d , -f 1)
        fi  
        ((tots = $tots + $score))
    done < $output
done

echo "Total students: $num"
((avg= tots/num))
echo "Average score: $avg"
echo "$maxname had the highest score of $max"
