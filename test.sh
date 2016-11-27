for t in `ls`; do
    echo ${t}
done


for skill in Ada Coffe Action Java; do
        echo "I am good at ${skill}Script"
    done


myUrl="http://www.w3cschool.cc"
#readonly myUrl
echo $myUrl

echo 'asdfdf${myUrl}'
your_name='qinjx'
str="Hello, I know your are \"$your_name\"! \n"
echo $str

your_name="qinjx"
greeting="hello你好, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting $greeting_1
echo ${#greeting}


array=(1 3 4 5)
echo ${array[*]}
echo ${#array}


echo ${1}

echo "$#"
echo "$@"
echo "$*"

for t in "$@"; do
    echo $t
done


for t in "$*"; do
    echo $t
done

my_array[2]=2
#my_array=(A B "C" D)

echo ${my_array[*]}
echo ${#my_array[*]}

my_array[1]=1

echo ${my_array[*]}
echo ${#my_array[*]}

echo ${my_array[0]}


var=`expr ${my_array[1]}${my_array[2]} + 2`
echo $var





