# 数値微分を定義
def numerical_diff(f,x):
    h = 1e-4
    return  (f(x+h) - f(x-h)) / (2*h)

# 2変数関数function_2を定義
def function_2(x):
    return x[0]**2 + x[1]**2

# function_2の変数x1=4としたとき
def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

# function_2の変数x0=3としたとき
def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

# x0=3,x1=4 としたときの x0 に対する偏微分を出力
print(numerical_diff(function_tmp1, 3.0))     # 6.00000000000378


# x0=3,x1=4 としたときの x1 に対する偏微分を出力
print(numerical_diff(function_tmp2, 4.0))     # 7.999999999999119

