runner_1 = int(input())
runner_2 = int(input())
runner_3 = int(input())

sub_total = runner_1 + runner_2 + runner_3
min_total = sub_total // 60
sec_total = sub_total % 60

if sec_total <= 9:
    print(f"{min_total}:0{sec_total}")
else:
    print(f"{min_total}:{sec_total}")
