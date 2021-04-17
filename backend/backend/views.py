from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import redis
import json
import pandas as pd
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.template import loader

redis_connection = redis.Redis(host='localhost', port=6379, db=0)
internal_error = JsonResponse({"error": "Internal server error"}, status=500)

# return vue static files


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


# Search By name
@require_http_methods(["GET"])
def search_by_name(request):
    try:
        search_string = request.GET["search_string"].upper()
        keys = []
        for key in redis_connection.scan_iter(match=search_string + '*'):
            keys.append(key)
        search_result = []
        for key in keys:
            value = json.loads(redis_connection.get(key))
            search_result.append(value)
        response = {"search_result": search_result}

        return JsonResponse(response)
    except:
        return internal_error


# Download results as CSV
@require_http_methods(["POST"])
@csrf_exempt
def download_results_csv(request):
    try:
        results_list = json.loads(request.body)["search_result"]
        results = pd.DataFrame(results_list)
        response = HttpResponse()
        response["Content-Disposition"] = "attachment; filename=BSE_data.csv"
        results.to_csv(path_or_buf=response, sep=';',
                       float_format='%.2f', index=False, decimal=",")
    except:
        return internal_error
    return response
