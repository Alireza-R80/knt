# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate,login,logout,get_user
# from rest_framework import status
# from .form import CreateCustomerForm
#
# @csrf_exempt
# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#
#         if user:
#             login(request,username)
#             a=get_user(request)
#             print(a,"=================")
#             print("loggin success")
#             return redirect('/')
#         else:
#             print("loggin error")
#             return HttpResponse('login page', status=status.HTTP_400_BAD_REQUEST)
#     return HttpResponse('login page')
#
#
# @csrf_exempt
# def registerPage(request):
#     if request.method == 'POST':
#         form = CreateCustomerForm(request.POST)
#         print(form.data['username'])
#         form.save()
#         if form.is_valid():
#             form.save()
#             print("register success")
#             return redirect('../login')
#         else:
#             #print(form)
#             print("register error")
#     return HttpResponse('register page')
#
#
# @csrf_exempt
# def logoutPage(request):
#     logout(request)
#     redirect('login')
#     return HttpResponse('logout page')
