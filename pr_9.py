"""
table number up to 20

"""
num=int(input('enter the number for table:'))
for t in range(1,21):
    m_num=t*num
    print(f'{t} * {num} = {m_num}')