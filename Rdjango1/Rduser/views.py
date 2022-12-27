from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework.decorators import api_view
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import jwt,datetime
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse
import json
# Create your views here.
class TodoView(viewsets.ModelViewSet):  
    serializer_class = UserSerializer 
    queryset = customer.objects.all()

class jwtCheck(APIView):
    permission_classes=[IsAuthenticated]   



class pos(APIView):

    def get(self,request):
        ft=customer.objects.all()
        ftt=UserSerializer(ft,many=True)
        return Response(ftt.data)

    def post(self,request):
        username=request.data["username"]
        password=request.data["password"]
        user=customer.objects.filter(username=username).exists()

        if user is None:
            mess="user already exist"
            return Response(mess)



         
         
        else:
            serializer=UserSerializer(data=request.data)

            if serializer.is_valid():
              serializer.save()
            # refresh = RefreshToken.for_user(serializer.data)

              return Response(serializer.data)
        return Response({serializer.errors}) 

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        print("mi",token)

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = customer.objects.filter(username=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


   

    







@api_view(['POST','GET'])
def hello_world(request):
    username=request.data['username']
    password=request.data['pass']
    # check=customer.objects.filter(username=username,password=password)
 

    user = customer.objects.filter(username=username).first()
    
 

    if user is None:
        api_res="invalid credentials"
        
    elif user:
        payload = {
            'id': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        

        response = Response()

        response.set_cookie(key='jwt',value= token,httponly=True)
        response.data = {
                'jwt': token
            }
     
    else:
        api_res="false"         

 
    
       


    return response   
 


class DeleteUser(APIView):

    def get(self,request,name):
            
            try:
                inst=customer.objects.get(username=name)
            except:
                return Response("not found")
        
            inst.delete()
            return Response("successs") 
      
        


class UserEdit(APIView):

   
    def patch(self,request,namee):
        try:
            detail=customer.objects.get(username=namee)
        except:
            return Response("not found")  

  
        print("initial",request.data)  
        print(type(request.data))
             
        my_dict={key:val for key,val in request.data.items() if val is not None}
        if len(my_dict) < len(request.data):
            edit_json=json.dumps(my_dict)
            edit_value=my_dict
        else:
            edit_value=request.data    
        print("after",my_dict)
        print(type(edit_value))

        serializer=UserSerializer(detail,data=edit_value,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("success")
        return Response(serializer.errors)  
           


@api_view(['POST','GET'])
def admin_api(request):
    username=request.data['username']
    password=request.data['pass']
    check=authenticate(username=username,password=password)
    if check:
        api_res="true"
    else:
        api_res="false"    


    return Response(api_res) 

@api_view(['GET'])
def searchh(request,name):
    try:
        inst=customer.objects.filter(username=name) 
    except:
        return Response("not found in database") 

    serializer=UserSerializer(inst,many=True)    

    return Response(serializer.data)        

