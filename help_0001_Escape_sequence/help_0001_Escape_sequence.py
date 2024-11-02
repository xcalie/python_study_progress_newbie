

from time import sleep

'''
因为python的print的末尾自带换行
这里通过end = ...
将末尾的换行修改了
'''
for i  in range(5):
    print(i,end = ' ')
'''
这里其实对于计算机只输出了
1 2 3 4 5
空格也是字符
'''

print(end = '\n')  
'''
到这里是
1 2 3 4 5 \n
到\n就发生了换行
'''
sleep(1)

print('y',end = '')
print(end = '\n')
sleep(1)
'''
到这里是
1 2 3 4 5 \ny\n
到\n就发生了换行
计算机在处理的时候会自动识别 \ 然后识别下一个字符，下一个为n
就会输出\n 既换行
'''

for i  in range(5):
    print(i,end = ' ')
print(end = '\n')
sleep(1)

'''
到这里是
1 2 3 4 5 \ny\n1 2 3 4 5 
'''

sleep(1);

for i  in range(5):
    print(i,end = ' ');
print(end = '\n');


'''
到这里是
1 2 3 4 5 \ny\n1 2 3 4 5 \n1 2 3 4 5 \n
也就是说对于计算机来说它看到的只有一行字符
而我们看到的就是经过处理的画面
'''

