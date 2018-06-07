import commands
import time

print "###############################################################################################################"
print "please source your openstack cred. file , if not sourced just press Ctrl+c and source it 1st"
print "###############################################################################################################"
print "this script usages 'openstack endpoint group list' which is only in latest 'python-openstackclient' package"
print "###############################################################################################################"
v1 = commands.getoutput("openstack endpoint group list --endpointgroup 28a6b4f533a245a88a86a0df5f8cb070  -f value")
v2 = v1.split('\n')
i=0
project_id_list= []
list_user_id= []
list_user_name= []
list_trial_type_user= []
list_community_type_user= []
list_trial_started_at= []
list_community_started_at= []

all_community_users_inline = commands.getoutput("openstack role  assignment list --role 23a17930700f44bfa527818bd41765ef -c User -f value")
all_trial_users_inline = commands.getoutput("openstack role  assignment list --role 7698be72802342cdb2a78f89aa55d8ac -c User -f value")
all_community_users= all_community_users_inline.split('\n')
all_trial_users= all_trial_users_inline.split('\n')
while i<len(v2):
	v3= v2[i]
	v9= v3.split(' ')
	v4= v9[0]
	project_id_list.append(v4)
	v5 =  commands.getoutput("openstack user list --project " + v4 + " -f value")
	v6 = v5.split(" ")
	v7= v6[0]
	v8= v6[1]
	list_user_id.append(v7)
	list_user_name.append(v8)
	i= i+1
print project_id_list
print list_user_id
print list_user_name

j=0
while j<len(list_user_id):
	user_id= list_user_id[j]
	user_name= list_user_name[j]
	if user_id in all_trial_users:
		print(user_name + " trial_user")
		list_trial_type_user.append("True")
	else:
		list_trial_type_user.append("False")


	if user_id in all_community_users:
		print(user_name + " community_user")
		list_community_type_user.append("True")
	else:
		list_community_type_user.append("False")

	v10 =commands.getoutput("openstack user show "+list_user_id[j] +"   -f shell")
	v13= v10.split('\n')
	if 'trial_started_at' in v10:
		k=0
		while k<len(v13):
			if 'trial_started_at' in v13[k]:
				v14= v13[k]
				v15= v14.split('=')
				v16 = v15[1]
				v17 = v16[1:-1]
				list_trial_started_at.append(v17)
			k= k+1
	else:
		list_trial_started_at.append("None")


	if 'community_started_at' in v10:
		m=0
		while m<len(v13):
			if 'community_started_at' in v13[m]:
				v19= v13[m]
				v20= v19.split('=')
				v21= v20[1]
				v22= v21[1:-1]
				if 'community_started_at:' in v22:
					v23 = v22.split(":")
					v24 = v23[1]
					list_community_started_at.append(v24)
				else:
					list_community_started_at.append(v22)
			m= m+1
	else:
		list_community_started_at.append("None")

	j= j+1

user_names = list_user_name
project_ids = project_id_list
com_user = list_community_type_user
trail_user = list_trial_type_user
com_date = list_community_started_at
trail_date = list_trial_started_at

#print list_community_type_user
#print list_trial_type_user
#print list_community_started_at
#print list_trial_started_at
print "Now lenth \n"
print len(list_community_type_user)
print len(list_trial_type_user)
print len(list_user_id)
print len(project_id_list)
print len(list_community_started_at)
print len(list_trial_started_at)


if len(list_user_id) == len(project_id_list)  and len(list_community_type_user)  == len(list_user_id)  and len(list_trial_type_user) == len(list_user_id) and len(list_user_name) == len(list_trial_started_at) and len(list_community_started_at) == len(project_id_list):
    print "lenth of all lists containing information is equal ====>>> So creating csv from data."
    print "###############################################################################################################"
else:
    print "lenth of all lists containing information is equal ====>>> Please contact find out error , why lenth of list not equal. "
    print "###############################################################################################################"
    quit()
print "creating users_data.csv file at current directory."
print "###############################################################################################################"
date1 = time.strftime("%d%m%Y")
filename = "users_data_"+date1+".csv"
csvfile = commands.getoutput("touch  "+  filename)
csvfile2 =  commands.getoutput(">"+filename)

#csvfile = "my.csv"

#user_names1 = user_names.insert(0,'Username')
#project_ids1 = project_ids.insert(0,'Project_ID')
#com_user1 = list_community_type_user.insert(0,'Community_type_user')
#trail_user1 = list_trial_type_user.insert(0,'Trial_type_user')
#com_date1 = list_community_started_at.insert(0,'Community_started_at')
#trail_date1 = list_trial_started_at.insert(0,'Trial_started_at')

#trail_date = list_trial_started_at
#new_list = [user_names ,project_ids, com_user,trail_user,com_date,trail_date]
varc12 = open(filename,mode='a')
columnname = "Username , Project_ID , Community_type_user , Trial_type_user , Community_started_at , Trial_started_at"
varc12.write( columnname + "\n")
varc12.close()


i=0
user_names
while i<len(user_names):
	printdata =  user_names[i] + ' , ' +  project_ids[i] + ' , ' + com_user[i] + ' , ' +trail_user[i] + ' , ' + com_date[i] + ' , ' + trail_date[i]
	varc11 = open(filename,mode='a')
	varc11.write(printdata  + "\n")
	varc11.close()
	i= i+1

print "please check users_data.csv at current dir."
print "###############################################################################################################"

"""
v1 = commands.getoutput("openstack usage list  -c Project  -f value")
v2= v1.split("\n")
i=0
while i<len(v2):
    v3 = v2[i].split(" ")
    v4 = v3[0]
    print v4
    v5 =  commands.getoutput("openstack user show " + v4  +  " -f  shell")
    v6 = v5.replace("="," : ")
    v7= v6.split("\n")
    regex=re.compile(".*(description).*")
    v8 =  [m.group(0) for l in v7 for m in [regex.search(l)] if m]
    v9 = v8[0]
    v10 = v9[15:-1]
    print v10
    print "##############################"
    i= i+1


    v6= v5.split("\n")
    v7= v6[2]
    v8 = v7.split(" ")
    v9= v6[9]
    v10= "trial_started_at: " + v9
    if 'community' in v8:
        print "comunity user: True"
        v11= v8[1]
        print "community_started_at: " + v11 
    else:
        print "comunity user: False"
"""        

