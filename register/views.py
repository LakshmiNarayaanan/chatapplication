# -*- coding: utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import Users,Messages
from .forms import UForm,MsgForm,SearchForm1,SearchForm2
from django.contrib import messages
from django.db.models import Q
from time import gmtime,strftime

import pytz
import datetime

def register(request):
	form=UForm()
	print("GET Kulla")
	print(request.GET)
	if(request.method=='POST'):
		print("POST kulla")
		form=UForm(request.POST)
		print(request.POST)
		if form.is_valid():
			print("form validated")
			username=request.POST.get('username','')
			email=request.POST.get('email','')
			phoneno=request.POST.get('phoneno','')
			password=request.POST.get('password','')
			user=Users(username=username,email=email,phoneno=phoneno,password=password)
			user.save()
			return HttpResponseRedirect('/success')

	return render(request,'register/index.html',{'form':form})


def login(request):
	if(request.method=='POST'):
		print("INSIDE LOGIN POST!!")
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		checkuser=Users.objects.filter(username=username)
		if not checkuser.count() and username!="":
			messages.error(request, 'ACCOUNT NOT REGISTERED!!')
		else:
			check=Users.objects.filter(username=username,password=password)
			if check.count():
				request.session['user'] = username
				return HttpResponseRedirect('/home')
			else:
				messages.error(request, 'MENTION CORRECT DETAILS!!')


	return render(request,'register/login.html',{})

def success(request):
	return render(request,'register/success.html')

def home(request):
	users_chatted=[]
	dt_time=[]
	time=[]
	last_msg=[]
	user= request.session['user']
	total=Users.objects.filter()
	form=SearchForm1()
	sender=user
	print(sender)
	total_list=list(total)
	print(total_list)
	for receiver in total_list:
		if receiver.username==sender:
			continue

		print(receiver.username)
		msgs=Messages.objects.filter(Q(sender=sender,receiver=receiver.username) | Q(sender=receiver.username,receiver=sender))
		if msgs.count():
			Message=list(msgs)
			users_chatted.append(receiver.username)
			last_msg.append(Message[-1].message)
			time.append(Message[-1].time)
			dt_time.append(Message[-1].date_time)



	length=len(time)

	for i in range(0,length-1):
		for j in range(0,length-i-1):
			if dt_time[j]<dt_time[j+1]:
				dt_time[j],dt_time[j+1]=dt_time[j+1],dt_time[j]
				last_msg[j],last_msg[j+1]=last_msg[j+1],last_msg[j]
				users_chatted[j],users_chatted[j+1]=users_chatted[j+1],users_chatted[j]
				time[j],time[j+1]=time[j+1],time[j]



	full_details=zip(users_chatted,last_msg,time)
	if(request.method=='POST'):
		form1=SearchForm2(request.POST)
		if form1.is_valid():
			username=request.POST.get('user_','')
			if username in users_chatted:	
				return HttpResponseRedirect(username)


		form=SearchForm1(request.POST)
		if form.is_valid():
			username=request.POST.get('user','')
			check=Users.objects.filter(username=username)
			check1=list(check)
			if check.count() and check1[0].username!=user:
				return HttpResponseRedirect(username)
			else:
				messages.error(request, 'USERNAME NOT REGISTERED')
	return render(request,'register/home.html',{'user':user , 'total':total , 'details':full_details })



def chat(request,receiver):
	sender=request.session['user']
	request.session['receiver'] = receiver
	print(sender)
	print(receiver)
	check=Users.objects.filter(username=receiver)
	if not check.count():
		messages.error(request, 'NO USERNAME FOUND')
		return HttpResponseRedirect("")
	msgs=Messages.objects.filter(Q(sender=sender,receiver=receiver) | Q(sender=receiver,receiver=sender))
	form=MsgForm()
	print("GET Kulla")
	if(request.method=='POST'):
		form=MsgForm(request.POST)
		

		print("postkulla")
		print(request.POST)
		if form.is_valid():
			print("form validated")
			message=request.POST.get('message','')
			date_time=datetime.datetime.now()
			time=strftime("%H:%M", gmtime())
			arr_split=time.split(':')
			hour=int(arr_split[0])
			minute=int(arr_split[1])
			total=hour*3600+minute*60+19800
			if total>=86400:
				total=total-86400
			hour=int(total/3600)
			minute=int((total%3600)/60)
			check=hour*3600+minute*60
			if check>43140:
				check=check-43200
				hour=int(check/3600)
				minute=int((check%3600)/60)
				arr_split[0]=str(hour)
				if minute<10:
					arr_split[1]="0"+str(minute)
				else:
					arr_split[1]=str(minute)
				time=':'.join(arr_split)
				time=time+" PM"
				print(time)

			else:
				arr_split[0]=str(hour)
				if minute<10:
					arr_split[1]="0"+str(minute)
				else:
					arr_split[1]=str(minute)
				time=':'.join(arr_split)
				time=time+" AM"
				print(time)
			




			msg=Messages(sender=sender,receiver=receiver,message=message,date_time=date_time,time=time)
			msg.save()
			s=Users.objects.get(username=sender)
			s.date_time=date_time
			s.save()
			r=Users.objects.get(username=receiver)
			r.date_time=date_time
			r.save()
			
			

	return render(request,'register/chat.html',{'receiver':receiver,'sender':sender,'messages':msgs})



# def check(request):
# 	if(request.method=='POST'):
# 		form=MsgForm(request.POST)
# 		if form.is_valid():
# 			message=request.POST.get('message','')
# 			sender=request.session['user']
# 			receiver=request.session['receiver']
# 			date_time=datetime.datetime.now()
# 			time=strftime("%H:%M", gmtime())
# 			arr_split=time.split(':')
# 			hour=int(arr_split[0])
# 			minute=int(arr_split[1])
# 			total=hour*3600+minute*60+19800
# 			if total>=86400:
# 				total=total-86400
# 				hour=int(total/3600)
# 				minute=int((total%3600)/60)
# 				check=hour*3600+minute*60
# 				if check>43140:
# 					check=check-43200
# 					hour=int(check/3600)
# 					minute=int((check%3600)/60)
# 					arr_split[0]=str(hour)
# 					if minute<10:
# 						arr_split[1]="0"+str(minute)
# 					else:
# 						arr_split[1]=str(minute)
# 						time=':'.join(arr_split)
# 						time=time+" PM"
# 						print(time)

# 				else:
# 					arr_split[0]=str(hour)
# 					if minute<10:
# 						arr_split[1]="0"+str(minute)
# 					else:
# 						arr_split[1]=str(minute)
# 						time=':'.join(arr_split)
# 						time=time+" AM"

# 			msg=Messages(sender=sender,receiver=receiver,message=message,date_time=date_time,time=time)
# 			msg.save()
# 			return HttpResponse(json.dumps(response_data),content_type="application/json")
			



	

