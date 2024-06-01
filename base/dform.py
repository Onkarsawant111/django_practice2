# from django import forms

# class userform(forms.Form):
#     Num1 = forms.CharField()
#     Num2 = forms.CharField()

#  <!-- django form -->
#     <form  method="post">
#         {% csrf_token %}   
#         {{form}} 
#         <button type="submit">submit</button>
#         <br>
#         Value : <input type="number" value='{{content}}'>
#     </form>
# </body>
# </html>

# # django-form:
# def form(request):
#     final_value = 0
#     dform = userform
#     data = {"form":dform}
#     try:
#         if request.method == "POST":
#             value1 = int(request.POST.get('Num1'))
#             value2 = int(request.POST.get('Num2'))
#         final_value = value1 + value2
#         data = {'form':dform, 'content':final_value}
#     except:
#         pass
#     data = {'form':dform, 'content':final_value}
#     return render(request,"form.html",data)