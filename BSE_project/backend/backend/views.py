from django.shortcuts import render
from django.http import JsonResponse
import redis
import json

redis_connection = redis.Redis(host='localhost', port=6379, db=0)

# Search the data by name


def search_by_name(request):
    invalid_request = JsonResponse({"error": "Invalid request"}, status=400)
    if request.method == 'GET':
        body = json.loads(request.body.decode('utf-8'))
        try:
            search_string = body["search_string"]
            keys = redis_connection.keys(search_string + "*")
            search_result = []
            for key in keys:
                value = json.loads(redis_connection.get(key))
                search_result.append(value)
            response = {"search_result": search_result}

            return JsonResponse(response)
        except:
            print("yikes")
            return invalid_request

    return invalid_request
