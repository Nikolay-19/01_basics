fuel_type = str(input())
fuel_qt = float(input())
club_card = str(input())

gasoline_pr = 2.22
diesel_pr = 2.33
gas_pr = 0.93
gasoline_dst = gasoline_pr - 0.18
diesel_dst = diesel_pr - 0.12
gas_dst = gas_pr - 0.08
small_dst = 0.08
big_dst = 0.1

if fuel_type == "Gasoline":
    if club_card == "No":
        if fuel_qt < 20:
            total = fuel_qt * gasoline_pr
            print(f"{total:.2f} lv.")
        if 20 <= fuel_qt <= 25:
            total = fuel_qt * gasoline_pr - (fuel_qt * gasoline_pr * small_dst)
            print(f"{total:.2f} lv.")
        if fuel_qt > 25:
            total = fuel_qt * gasoline_pr - (fuel_qt * gasoline_pr * big_dst)
            print(f"{total:.2f} lv.")
    if club_card == "Yes":
        sub_total = fuel_qt * gasoline_dst
        if fuel_qt < 20:
            total = sub_total
            print(f"{total:.2f} lv.")
        if 20 <= fuel_qt <= 25:
            total = sub_total - (sub_total * small_dst)
            print(f"{total:.2f} lv.")
        if fuel_qt > 25:
            total = sub_total - (sub_total * big_dst)
            print(f"{total:.2f} lv.")

if fuel_type == "Diesel":
    if club_card == "No":
        if fuel_qt <= 20:
            total = fuel_qt * diesel_pr
            print(f"{total:.2f} lv.")
        if 20 <= fuel_qt <= 25:
            total = fuel_qt * diesel_pr - (fuel_qt * diesel_pr * small_dst)
            print(f"{total:.2f} lv.")
        if fuel_qt > 25:
            total = fuel_qt * diesel_pr - (fuel_qt * diesel_pr * big_dst)
            print(f"{total:.2f} lv.")
    if club_card == "Yes":
        sub_total = fuel_qt * diesel_dst
        if fuel_qt < 20:
            total = sub_total
            print(f"{total:.2f} lv.")
        if 20 <= fuel_qt <= 25:
            total = sub_total - (sub_total * small_dst)
            print(f"{total:.2f} lv.")
        if fuel_qt > 25:
            total = sub_total - (sub_total * big_dst)
            print(f"{total:.2f} lv.")

if fuel_type == "Gas":
    if club_card == "No":
        if fuel_qt <= 20:
            total = fuel_qt * gas_pr
            print(f"{total:.2f} lv.")
        if 20 <= fuel_qt <= 25:
            total = fuel_qt * gas_pr - (fuel_qt * gas_pr * small_dst)
            print(f"{total:.2f} lv.")
        if fuel_qt > 25:
            total = fuel_qt * gas_pr - (fuel_qt * gas_pr * big_dst)
            print(f"{total:.2f} lv.")
    if club_card == "Yes":
        sub_total = fuel_qt * gas_dst
        if fuel_qt < 20:
            total = sub_total
            print(f"{total:.2f} lv.")
        if 20 <= fuel_qt <= 25:
            total = sub_total - (sub_total * small_dst)
            print(f"{total:.2f} lv.")
        if fuel_qt > 25:
            total = sub_total - (sub_total * big_dst)
            print(f"{total:.2f} lv.")