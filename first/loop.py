data_list = ["apple", "banana", "cherry", "kiwi", "mango"]
data_dic = {
  "a": 'hello',
  "b": 'welcome'
}

list_contain_a = []

for x in data_list:
  if "a" in x:
    list_contain_a.append(x)

for x in data_dic:
  print(x)
