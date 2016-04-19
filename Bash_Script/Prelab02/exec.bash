#! /bin/bash
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$

#[[ $# != 1 ]] && echo "usage: .bash <filename>" && exit 1

#[[ ! -r $1 ]] && echo "$1 is not readable" && exit 2

cd c-files

for line in $(ls *.c)
do
    echo Attemping to compile $line
    gcc -Wall -Werror $line 2>/dev/null
    if (($? == 1))
    then
        echo Compiling file $line... Error: Compilation failed.

    else
        echo Compiling file $line... Compilation succeeded.
        file=$line
        filename=$(echo $file | cut -d '.' -f 1)
        a.out > $filename.out
    fi
done 

