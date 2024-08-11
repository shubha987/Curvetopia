from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .image_processor import process_image
import numpy as np
import io
import pandas as pd

@csrf_exempt
def process_drawing(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            csv_data = data.get('csv')
            if not csv_data:
                return JsonResponse({'error': 'CSV data is required'}, status=400)
            
            # Convert CSV data to a DataFrame
            csv_io = io.StringIO(csv_data)
            try:
                df = pd.read_csv(csv_io)
            except pd.errors.EmptyDataError:
                return JsonResponse({'error': 'CSV data is empty or invalid'}, status=400)
            except pd.errors.ParserError:
                return JsonResponse({'error': 'CSV data is malformed'}, status=400)
            
            if df.empty:
                return JsonResponse({'error': 'CSV data is empty or invalid'}, status=400)
            
            np_array = df.to_numpy()
            
            # Process the NumPy array
            processed_data = process_image(np_array)
            
            return JsonResponse({'csv': csv_data, 'image': processed_data}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)