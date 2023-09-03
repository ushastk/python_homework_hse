phone_trans_money = {}
def get_transactions(params):

    if params == "print_it":
        print("Вывод")
        for trans, vals in phone_trans_money.items():
            print(str(vals[0]), str(trans), str(vals[1]), sep=' ')
    else:
        phone_trans_and_money = params.split(":")
        money = int(phone_trans_and_money[1])
        phone_and_trans = phone_trans_and_money[0].split("-")
        phone = phone_and_trans[0]
        trans = phone_and_trans[1]
        if trans in phone_trans_money:
            phone_trans_money[trans] = [phone_trans_money[trans][0]+1, phone_trans_money[trans][1]+money]
        else:
            phone_trans_money[trans] = [1, money]


get_transactions('880005553535-перевод:100')
get_transactions('111111111-перевод:1000')
get_transactions('880005553535-оплата_жкх:10000')
get_transactions('89065664312-перевод:50000000')
get_transactions('print_it')