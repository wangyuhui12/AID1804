

# 银行业务：
#     存钱：
#         savemoney
#     取钱：
#         withdraw
#         

# 1.添加一个余额变动提醒短信息功能
def messend_send(fn):
    def fx(name, x):
        print("发送消息", name, "来银行办理业务...")
        fn(name, x)
        print("发送消息：", name, "办了", x, "元的业务，短信已发出..")
    return fx

# 2.加一个权限验证功能
def privileged_check(fn):
    def fx(name, x):
        print("正在检查权限..")
        if True:
            fn(name, x)
    return fx


@privileged_check
@messend_send
def savemoney(name, x):
    print(name, "存钱",x,'元')

@messend_send
def withdraw(name, x):
    print(name, '取钱', x, '元')

# 以下调用者小张定的程序
savemoney('小李', 200)
# savemoney('小赵', 500)
print()
# withdraw('小王', 300)
