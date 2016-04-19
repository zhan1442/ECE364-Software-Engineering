#! /bin/bash
#
#$Author: ee364c07 $
#$Date: 2016-01-17 02:38:39 -0500 (Sun, 17 Jan 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364c07/Prelab01/svncheck.bash $
#$Revision: 85273 $

while read line
do
    sta=$(svn status $line | head -c 1)
    if [[ $sta == "?" && -e $line ]]
    then
        if [[ ! -x $line ]]
        then
            echo "Would you like to make $line executable?"
            read decision
            [[ $decision == "y" ]] && chmod +x $line
        fi
        svn add $line
    elif [[ ! -e $line ]]
    then 
        echo "Error: File $line appears to not exist here or in svn"
    elif [[ $status == "" && ! -x $line ]]
    then
        svn propset svn:executable ON $line
    fi
done < file_list
svn commit
echo "Auto-commiting code"
exit 0
