import random

def get_big_num(n):
    x = list()
    st = ""
    for i in range(n):
        x.append(str(random.randint(0,9)))
    return int(st.join(x))

if __name__ == "__main__":
    n = 55
    num1 = get_big_num(n)
    num2 = get_big_num(n)
    print(num1*num2)
