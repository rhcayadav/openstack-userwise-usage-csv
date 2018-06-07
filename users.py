import commands
import time
import datetime

print "###############################################################################################################"
print "please source your openstack cred. file , if not sourced just press Ctrl+c and source it 1st"
print "###############################################################################################################"
print "this script usages 'openstack endpoint group list' which is only in latest 'python-openstackclient' package"
print "###############################################################################################################"
print "this script only works good on version ===>>> '3.15.0' <<<==== ' python-openstackclient ' package"
print "###############################################################################################################"
var1 = commands.getstatusoutput("openstack endpoint group list --endpointgroup 28a6b4f533a245a88a86a0df5f8cb070  -f value")
#print var1
if var1[0] != 0:
        print "could not run command , conectivity issue !!!!!!!!!!!!! "
        quit()
v1 = var1[1]

print "percent completed :  5"
print "###############################################################################################################"
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


print "percent completed :  10"
print "###############################################################################################################"
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
#print project_id_list
#print list_user_id
#print list_user_name

print "percent completed :  20"
print "###############################################################################################################"
j=0
while j<len(list_user_id):
	user_id= list_user_id[j]
	user_name= list_user_name[j]
	if user_id in all_trial_users:
#		print(user_name + " trial_user")
		list_trial_type_user.append("True")
	else:
		list_trial_type_user.append("False")


	if user_id in all_community_users:
#		print(user_name + " community_user")
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


def days(date1):
	today = datetime.date.today()
	vardate1= date1.split('-')
	vardate2= int(vardate1[0])
	vardate3= int(vardate1[1])
	vardate4= int(vardate1[2])
	someday= datetime.date(vardate2,vardate3,vardate4)
	delta= today - someday
	daysno= delta.days
	return(daysno)

list_community_started_at_days= []
list_trial_started_at_days= []
s=0
while s<len(list_user_id):
	if list_community_started_at[s] == 'None':
		list_community_started_at_days.append("None")
	else:
		list_community_started_at_days.append(days(list_community_started_at[s]))

	if list_trial_started_at[s] == 'None':
                list_trial_started_at_days.append("None")
        else:
                list_trial_started_at_days.append(days(list_trial_started_at[s]))
	s=  s+1


list_community_started_at

user_names = list_user_name
project_ids = project_id_list
com_user = list_community_type_user
trail_user = list_trial_type_user
com_date = list_community_started_at
trail_date = list_trial_started_at

print "percent completed :  45"
print "###############################################################################################################"
#print list_community_type_user
#print list_trial_type_user
#print list_community_started_at
#print list_trial_started_at
#print "Now lenth \n"
#print len(list_community_type_user)
#print len(list_trial_type_user)
#print len(list_user_id)
#print len(project_id_list)
#print len(list_community_started_at)
#print len(list_trial_started_at)


if len(list_user_id) == len(project_id_list)  and len(list_community_type_user)  == len(list_user_id)  and len(list_trial_type_user) == len(list_user_id) and len(list_user_name) == len(list_trial_started_at) and len(list_community_started_at) == len(project_id_list):
    print "lenth of all lists containing information is equal ====>>> So creating csv from data."
    print "###############################################################################################################"
else:
    print "lenth of all lists containing information is equal ====>>> Please contact find out error , why lenth of list not equal. "
    print "###############################################################################################################"
    quit()
print "creating users_data<date>.csv file at current directory."
print "###############################################################################################################"
date1 = time.strftime("%d%m%Y")
filename = "users_data_"+date1+".csv"
csvfile = commands.getoutput("touch  "+  filename)
csvfile2 =  commands.getoutput(">"+filename)

#csvfile = "my.csv"

print "percent completed :  55"
print "###############################################################################################################"
totalSecurityGroupsUsed= {}
maxSecurityGroups= {}

totalInstancesUsed= {}
maxTotalInstances= {}

totalRAMUsed= {}
maxTotalRAMSize= {}

totalCoresUsed= {}
maxTotalCores= {}

totalFloatingIpsUsed= {}
maxTotalFloatingIps= {}

totalVolumesUsed= {}
maxTotalVolumes= {}

totalGigabytesUsed= {}
maxTotalVolumeGigabytes= {}

totalSnapshotsUsed= {}
maxTotalSnapshots= {}

n=0
while n<len(project_id_list):
	v25 = commands.getoutput("openstack limits show --project   " + project_id_list[n] + "    --absolute  -f value")
	v26 = v25.split('\n')
	
        v27= v26[17].split(' ')
        totalSecurityGroupsUsed_value= v27[1]
        totalSecurityGroupsUsed.update({project_id_list[n]:totalSecurityGroupsUsed_value})
        v28= v26[16].split(' ')
        maxSecurityGroups_value= v28[1]
        maxSecurityGroups.update({project_id_list[n]:maxSecurityGroups_value})
#        print "totalSecurityGroupsUsed"
#        print totalSecurityGroupsUsed

        v29= v26[14].split(' ')
        totalInstancesUsed_value= v29[1]
        totalInstancesUsed.update({project_id_list[n]:totalInstancesUsed_value})
        v30= v26[1].split(' ')
        maxTotalInstances_value= v30[1]
        maxTotalInstances.update({project_id_list[n]:maxTotalInstances_value})
#        print  "totalInstancesUsed"
#        print  totalInstancesUsed

        v31= v26[11].split(' ')
        totalRAMUsed_value= v31[1]
        totalRAMUsed.update({project_id_list[n]:totalRAMUsed_value})
        v32= v26[6].split(' ')
        maxTotalRAMSize_value= v32[1]
        maxTotalRAMSize.update({project_id_list[n]:maxTotalRAMSize_value})
#        print "totalRAMUsed"
#        print totalRAMUsed

        v33= v26[10].split(' ')
        totalCoresUsed_value= v33[1]
        totalCoresUsed.update({project_id_list[n]:totalCoresUsed_value})
        v34= v26[18].split(' ')
        maxTotalCores_value= v34[1]
        maxTotalCores.update({project_id_list[n]:maxTotalCores_value})

#        print "totalCoresUsed"
#        print totalCoresUsed

        v35= v26[13].split(' ')
        totalFloatingIpsUsed_value= v35[1]
        totalFloatingIpsUsed.update({project_id_list[n]:totalFloatingIpsUsed_value})
        v36= v26[16].split(' ')
        maxTotalFloatingIps_value= v36[1]
        maxTotalFloatingIps.update({project_id_list[n]:maxTotalFloatingIps_value})

        v37= v26[26].split(' ')
        totalVolumesUsed_value= v37[1]
        totalVolumesUsed.update({project_id_list[n]:totalVolumesUsed_value})
        v38= v26[25].split(' ')
        maxTotalVolumes_value= v38[1]
        maxTotalVolumes.update({project_id_list[n]:maxTotalVolumes_value})

        v39= v26[28].split(' ')
        totalGigabytesUsed_value= v39[1]
        totalGigabytesUsed.update({project_id_list[n]:totalGigabytesUsed_value})
        v40= v26[21].split(' ')
        maxTotalVolumeGigabytes_value= v40[1]
        maxTotalVolumeGigabytes.update({project_id_list[n]:maxTotalVolumeGigabytes_value})

        v41= v26[19].split(' ')
        totalSnapshotsUsed_value= v41[1]
        totalSnapshotsUsed.update({project_id_list[n]:totalSnapshotsUsed_value})
        v42= v26[22].split(' ')
        maxTotalSnapshots_value= v42[1]
        maxTotalSnapshots.update({project_id_list[n]:maxTotalSnapshots_value})
	
#	print maxTotalSnapshots
	n= n+1

print "percent completed :  80"
print "###############################################################################################################"
totalSecurityGroupsUsed_list= []
maxSecurityGroups_list= []
totalInstancesUsed_list= []
maxTotalInstances_list= []
totalRAMUsed_list= []
maxTotalRAMSize_list= []
totalCoresUsed_list= []
maxTotalCores_list= []
totalFloatingIpsUsed_list= []
maxTotalFloatingIps_list= []
totalVolumesUsed_list= []
maxTotalVolumes_list= []
totalGigabytesUsed_list= []
maxTotalVolumeGigabytes_list= []
totalSnapshotsUsed_list= []
maxTotalSnapshots_list= []

r=0
while r<len(project_ids):
	totalSecurityGroupsUsed_list.append(totalSecurityGroupsUsed[project_ids[r]])
	maxSecurityGroups_list.append(maxSecurityGroups[project_ids[r]])
	totalInstancesUsed_list.append(totalInstancesUsed[project_ids[r]])
	maxTotalInstances_list.append(maxTotalInstances[project_ids[r]])
	totalRAMUsed_list.append(totalRAMUsed[project_ids[r]])
	maxTotalRAMSize_list.append(maxTotalRAMSize[project_ids[r]])
	totalCoresUsed_list.append(totalCoresUsed[project_ids[r]])
	maxTotalCores_list.append(maxTotalCores[project_ids[r]])
	totalFloatingIpsUsed_list.append(totalFloatingIpsUsed[project_ids[r]])
	maxTotalFloatingIps_list.append(maxTotalFloatingIps[project_ids[r]])
	totalVolumesUsed_list.append(totalVolumesUsed[project_ids[r]])
	maxTotalVolumes_list.append(maxTotalVolumes[project_ids[r]])
	totalGigabytesUsed_list.append(totalGigabytesUsed[project_ids[r]])
	maxTotalVolumeGigabytes_list.append(maxTotalVolumeGigabytes[project_ids[r]])
	totalSnapshotsUsed_list.append(totalSnapshotsUsed[project_ids[r]])
	maxTotalSnapshots_list.append(maxTotalSnapshots[project_ids[r]])
	r= r+1



print "percent completed :  95"
print "###############################################################################################################"

#user_names1 = user_names.insert(0,'Username')
#project_ids1 = project_ids.insert(0,'Project_ID')
#com_user1 = list_community_type_user.insert(0,'Community_type_user')
#trail_user1 = list_trial_type_user.insert(0,'Trial_type_user')
#com_date1 = list_community_started_at.insert(0,'Community_started_at')
#trail_date1 = list_trial_started_at.insert(0,'Trial_started_at')

#trail_date = list_trial_started_at
#new_list = [user_names ,project_ids, com_user,trail_user,com_date,trail_date]
varc12 = open(filename,mode='a')
columnname = "Username , Project_ID , Community_type_user , Trial_type_user , Community_started_at , Trial_started_at , Community_started_days , Trial_started_days , maxTotalInstances , totalInstancesUsed , maxTotalCores , totalCoresUsed , maxTotalRAMSize , totalRAMUsed , maxTotalVolumes , totalVolumesUsed , maxTotalVolumeGigabytes , totalGigabytesUsed , maxTotalFloatingIps , totalFloatingIpsUsed , maxSecurityGroups , totalSecurityGroupsUsed , maxTotalSnapshots , totalSnapshotsUsed "
varc12.write( columnname + "\n")
varc12.close()



i=0
user_names
while i<len(user_names):
	printdata =  user_names[i] + ' , ' +  project_ids[i] + ' , ' + com_user[i] + ' , ' +trail_user[i] + ' , ' + com_date[i] + ' , ' + trail_date[i] + ' , '  + str(list_community_started_at_days[i]) + ' , ' +  str(list_trial_started_at_days[i]) + ' , ' +    maxTotalInstances_list[i] +   ' , ' +  totalInstancesUsed_list[i] +   ' , ' +  maxTotalCores_list[i] +   ' , ' +  totalCoresUsed_list[i] +   ' , ' +  maxTotalRAMSize_list[i] +   ' , ' +  totalRAMUsed_list[i] +   ' , ' +  maxTotalVolumes_list[i] +   ' , ' +  totalVolumesUsed_list[i] +   ' , ' +  maxTotalVolumeGigabytes_list[i] +   ' , ' +  totalGigabytesUsed_list[i] +   ' , ' +  maxTotalFloatingIps_list[i] +   ' , ' +  totalFloatingIpsUsed_list[i] +   ' , ' +  maxSecurityGroups_list[i] +   ' , ' +  totalSecurityGroupsUsed_list[i] +   ' , ' +  maxTotalSnapshots_list[i] +   ' , ' +  totalSnapshotsUsed_list[i]
	
	varc11 = open(filename,mode='a')
	varc11.write(printdata  + "\n")
	varc11.close()
	i= i+1

print "please check users_data.csv at current dir."
print "###############################################################################################################"

print "percent completed :  100 "

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

