import json

profit_sum = 0
firms_dict = {}
profit_firms_count = 0

with open("in.txt", "r") as f_in:
    while True:
        line = f_in.readline()
        if line == "":
            break

        words_in_line = line.split(" ")
        firm_name = words_in_line[0]
        earning = float(words_in_line[2])
        costs = float(words_in_line[3])
        profit = earning - costs
        if profit > 0:
            profit_sum += profit
            profit_firms_count += 1
        firms_dict[firm_name] = profit

new_list = [firms_dict, {"average_profit":profit_sum/profit_firms_count}]

with open("out.json", "w") as f_out:
    json.dump(new_list, f_out)
