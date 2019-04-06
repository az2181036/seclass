import random as rd

op = ['+','-','×','÷'] # 算数符数组

def get_factor(num):
    lst = [1]
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            lst.append(i)
    lst.append(num)
    return lst

def calculate( num_1, num_2, op , flag):
    """
    :param num_1:  数字1
    :param num_2:  数字2
    :param op:  操作符
    :param flag: 判断是否为第二次计算
    :return:
    """
    if op == 0:
        while(num_1+ num_2 > 100): # 和大于一百 重新随机生成
            if flag is False: # 第一次计算
                num_1 = rd.randint(0,100)
                num_2 = rd.randint(0,100)
            else: # 第二次计算 num_1 为一个计算好的值，无法改变，只改变num_2，随机取0-(100-num_1),确保和小于100
                num_2 = rd.randint(0,100-num_1)
        return num_1,num_2,num_1 + num_2
    elif op == 1:
        while (num_1 - num_2 < 0): # 差值为负数，重新生成
            if flag is False: # 第一次计算，交换两个数
                tmp = num_1
                num_1 = num_2
                num_2 = tmp
            else: # 随机生成一个 小于等于num_1的整数
                num_2 = rd.randint(0, num_1)
        return num_1,num_2,num_1 - num_2
    elif op == 2:
        while (num_1 * num_2 > 100): # 乘积大于100
            # 不管第一次还是第二次,都锁定num_1
            num_2 = rd.randint(0, int(100/num_1))
        return num_1, num_2, num_1 * num_2
    else:
        if num_1 == 0:
            return num_1,num_2, 0
        if num_2 == 0 or num_1 % num_2 != 0: # 除数为0， 商不是整数
            # 同样的，锁定num_1
            _lst = get_factor(num_1) #
            num_2 = _lst[rd.randint(0,len(_lst)-1)] # 去因子列表中的某个数获取因子列表
        return num_1,num_2,int(num_1 / num_2)

def set_formula( a, b, c, op1, op2, flag):
    if flag is True:
        eqt = '('+ str(a) + op[op1] + str(b) + ')' + op[op2] + str(c) + "="
    else:
        eqt = str(a) + op[op1] + str(b) + op[op2] + str(c) + "="
    return eqt

def main():
    print("请输入出题数目：")
    n = int(input())    # 出题数目
    print("是否直接显示答案？ 0：不显示， 1：显示")
    v = int(input())
    lst = set()
    f_lst = list()

    while(True):
        # 集合中的数是否有N个
        if len(lst) == n:
            break
        op1_index = rd.randint(0,3) # 随机算数符1
        op2_index = rd.randint(0,3) # 随机算数符2

        # 随机生成3个数
        num_1 = rd.randint(0,100)
        num_2 = rd.randint(0,100)
        num_3 = rd.randint(0,100)

        # 计算前两个数
        num_1, num_2, sum_12 = calculate(num_1, num_2, op1_index, False)
        # 计算和与第三个数
        sum_12, num_3, sum_123 = calculate(sum_12, num_3, op2_index, True)

        # 由于我首先计算了前两个数的和，所以可能出现+，*等组成，需要加（）
        flag = False # 不需要加括号
        if op1_index < 2 and op2_index > 1: # 算数符1是+，- 并且 算数符2是 *,/
            flag = True

        # 生成算式
        eqt = set_formula(num_1,num_2,num_3, op1_index, op2_index, flag)
        # 判断算式 是否重复，不重复加入集合
        if eqt not in lst:
            lst.add(eqt)
            f_lst.append([eqt,sum_123])
            if v == 0:
                print(eqt)
            else:
                print(eqt,end="")
                print(sum_123)

if __name__ == "__main__":
    main()
