
"""
#  While Loop in List

dev_list = ['Sadi', 'Hammad', 'Ashraf', 'Athik', 'Nasir']

start_index=0
while start_index < len(dev_list):
    print(dev_list[start_index])
    start_index = start_index + 1
"""

"""
#  While Loop in a String
simple_word = 'Hello World'
start_index=0
while start_index < len(simple_word):
    print(simple_word[start_index])
    start_index +=1

"""

#  Break, Continue in while loop
"""
strt_index = 0
end_index = 10
while strt_index < end_index:
    # Break
    # if strt_index == 5:
    #     break
    
    # Continue
    if strt_index == 4:
        strt_index +=1
        continue
    print(strt_index)
    strt_index +=1
"""



"""
#  While Loop in Dictionaries
dev_info ={"name": "Saadi", "age": 18, "isCompleted": True, "district": "Sunamganj"}
dev_keys = list(dev_info.keys())
start_index =0
while start_index < len(dev_keys):
    each_key = dev_keys[start_index]
    print(each_key, dev_info[each_key])
    start_index +=1
"""

#  While Loop in Set
set_list ={ 1,2,3,4,5,6,7,8}
set_key = list(set_list)
start_index = 0
while start_index < len(set_key):
    print(set_key[start_index])
    start_index +=1











