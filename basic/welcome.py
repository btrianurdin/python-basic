data_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
data_tuples = ("apple", "banana", "cherry", "orange", "kiwi", 9)
data_set = {"apple", "banana", "cherry", "orange", "kiwi", 3}
data_dic = {
  ('a',7): 'hello',
  ('b', 8): 'welcome'
}

data_list2 = data_list.copy()

data_list[0] = "grape"

print("data_list: ", type(data_list))
