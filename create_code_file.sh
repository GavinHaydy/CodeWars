if [ $# != 2 ];
then
    echo "参数个数错误"
    exit 1
fi

array=(1
2
3
4
5
6
7
8
)

lau=(
    .ts
    .go
    .java
    .js
    .py
    .md
)

found=false
for element in "${array[@]}"; do
    if [ "$element" == "$1" ]; then
        found=true
        break
    fi
done

if [ "$found" = true ]; then
    cd $1ku && mkdir $2
    for filename in "${lau[@]}";do
        touch "$2/$2$filename"
    done
else
    echo "$1ku文件夹不存在"
    exit
fi


val="# url\n
[$2]()\n
# Chinese\n
\`\`\` shell\n\n
\`\`\`\n\n
# English\n
\`\`\` shell\n\n
\`\`\` 
"

go_java_js_ts="/*\tbest\n*/"

py_doc="\"\"\" best\n
\"\"\"
"

echo $val >> $2/$2.md

for element in "${lau[@]}"; do
    if [ "$element" == ".md" ];then
        echo 1
        continue
    elif [ "$element" == ".py" ];then
        echo 2
        echo $py_doc >> $2/$2.py
    else
        echo 3
        echo $go_java_js_ts >> $2/$2$element    
    fi
done