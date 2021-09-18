from db import DB
room_id = '613b2db387708d9551acee3b'
user_id = 'al09952090529302' 
room_id_u = '613c84fdceee2ab59d44dee8'
user_ddd = 'lkdl049092098509292'
roomff = '6145aec5285e4a18402073b1'

# print(DB.write("roomz",
#                {
# user    6145fc9a285e4a18402074f4 ------ 6145f987285e4a18402074eb
#                    'name': 'Room2',
#                    'url': 'ws://'
# org 6145eee9285e4a18402074cd
#                }))

print(DB.read("dm_messages", {}))
# 6146140b547b462ecf519478
# 614fc9a285e4a
#print(DB.send_centrifugo_data(room=room_id, data=response_output))
