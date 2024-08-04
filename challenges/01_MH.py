d = {
    "MH|Others": 345324,
    "MH|MUM": 6543242,
    "MH|PUNE": 544234,
    "MH|NAG": 534,
    "MH|JAL": 5678908765,
    "TN|Others": 567890876,
    "TN|COI": 34532,
    "TN|MADU": 45678976,
    "TN|OOTY": 6543,
    "TN|CHN": 3927634,
    "UP|BANARAS": 42342,
    "UP|AYODHYA": 4567898
}
ls = list(d.values())

for i in range(len(ls)):
    for j in range(i+1, len(ls)):
        if ls[i] >= ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print(ls)

for i, j in d.items():
    if j == ls[-1]:
        print(i.split('|')[0])
