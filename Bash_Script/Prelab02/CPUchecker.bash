#! /bin/bash
#
#$Author$
#$Date$
#$HeadURL$
#$Revision$

[[ $# != 1 ]] && echo "usage: .bash <filename>" && exit 1

[[ ! -r $1 ]] && echo "$1 is not readable" && exit 2

max_avg=0
while read -a Data
do
    sum=0
    var=0
    loop=0
    mul=0.9
    t_num=$(( ${#Data[*]} -1 ))
    h_num=$(( ${#Data[*]} -3 ))
    for I in ${Data[*]}
    do
        if (( $I != ${Data[0]} && $I != ${Data[1]} && $I !=  ${Data[$t_num]} ))
        then
            sum=$(($sum+$I))
        fi
    done
    sum=$(($sum/$h_num))
    #echo "$sum"
    for I in ${Data[*]}
    do
        if (( $I != ${Data[0]} && $I != ${Data[1]} && $I != ${Data[$t_num]} ))
        then
            loop=$(( $loop + 1 ))
            if (( $I < $(( ( 9 * $sum)/10 )) ))
            then
                echo "Run $loop for ${Data[0]} ${Data[1]} with score $I was 90% less than average"
            fi
        fi
    done

    echo "${Data[0]} ${Data[1]} scored an average of $sum"
    av=$(( $sum / ${Data[$t_num]} ))
    #echo "$av"
    if (( $av > $max_avg ))
    then
        proc=${Data[0]}
        speed=${Data[1]}
        watt=${Data[$t_num]}
        max_avg=$av
        # echo "$proc $spees $watt "
    fi
done < $1
echo "The best performance per watt was achieved by $proc $speed at $max_avg"
