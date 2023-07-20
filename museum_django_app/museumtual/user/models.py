# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django import forms
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from .models import UserProfile
# from .forms import UserProfileForm, UserForm
# from .models import Profile




    

#     def create_profile(sender, instance, created, **kwargs):
#         if created:
#             UserProfile.objects.create(user = instance) 

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['user', 'image']    

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email']

        
#     def register(request):
#        if request.method == 'POST':
#         user_form = UserCreationForm(request.POST)
#         user_profile_form = UserProfileForm(request.POST)
#         if user_form.is_valid() and user_profile_form.is_valid():
#             user = user_form.save()
#             user_profile = user_profile_form.save(commit=False)
#             user_profile.user = user
#             user_profile.save()
#             return redirect('home')
#         else:
#           user_form = UserCreationForm()
#         user_profile_form = UserProfileForm()
#         return render(request, 'registration/register.html', {'user_form': user_form, 'user_profile_form': user_profile_form})

# def edit_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         user_profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
#         if user_form.is_valid() and user_profile_form.is_valid():
#             user_form.save()
#             user_profile_form.save()
#             return redirect('home')
#     else:
#         user_form = UserForm(instance=request.user)
#         user_profile_form = UserProfileForm(instance=request.user.userprofile)
#     return render(request, 'registration/edit_profile.html', {'user_form': user_form, 'user_profile_form': user_profile_form})       