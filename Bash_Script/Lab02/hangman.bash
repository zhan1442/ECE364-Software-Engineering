#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-28 22:59:11 -0500 (Thu, 28 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Lab02/hangman.bash $
#$Revision: 87276 $

[[ $# != 0 ]] && echo "usage: hangman.bash <filename>" && exit 1

str=(banana parsimonious sesquipedalian)

s="$(echo ${str[(($RANDOM % 3))]})"
i=0
while [[ ${s:$i:1} != "" ]]
do
    sc[$i]=${s:$i:1}
    ((i++))
done
 
len=${#sc[*]}

for (( i=0; i < ${#sc[*]}; i++))
do
    sg[$i]="."
done

echo Your word is ${#sc[*]} letters long.

cnt=0
while true
do
    printf "Word is:  "

    for ind in ${sg[*]}
    do
        printf "$ind "
    done
    echo
    read -p "  Make a guess: " letter
    found=0
    for (( i=0; i < ${#sc[*]}; i++ ))
    do
        if [[ ${sc[$i]} == $letter && ${sg[$i]} == "." ]]
        then
            sg[$i]=${sc[$i]}
            ((cnt++))
            found=1
        fi
    done
    
    [[ $found == 1 ]] && echo "  Good going!"
    [[ $found == 0 ]] && echo "  Sorry, try again."
    
    echo
    (( $cnt == $len )) && echo "Congratulations! You guessed the word: $s" && exit 0
done
echo


