cc=dict()
while 1:
    aa=input("请输入指令")
    bb=int(aa)
    if bb==2 :
        dd=input("输入姓名")
        if dd not in cc:
            ee=input("电话")
            cc[dd]=ee
        else:
            print("已存在")
            gg=input("是否修改")
            if gg=="yes":
                hh=input("输入电话")
                cc[dd]=hh
    elif bb==1:
        ff=input("输入姓名")
        print("查询结果："+cc[ff])
    elif bb==4:
        break