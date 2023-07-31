import vk
import settings
import time
api = vk.API(access_token=settings.token, v=5.131)
print('ssssssssssssssssssssssssuuuuuuuuuuuupeeeeeeeerapi=',api)
while True:
    application = api.groups.getRequests(group_id=settings.club_id, v=5.131)
    listapp = (application.get('items'))
    print(listapp)
    if listapp != []:
        for prayer in listapp:
            api.groups.approveRequest(group_id=settings.club_id, user_id=(prayer),v=5.131) 
            time.sleep(1) 
        print('all prayers приняты')
    else:
        print('ты никому не нужен')  
    time.sleep(settings.sleep_time)
