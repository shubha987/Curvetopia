from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .image_processor import process_image
import numpy as np
import cv2
import base64
import io
import pandas as pd

import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def process_drawing(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            logger.debug(f"Received data: {data}")
            csv_data = data.get('csv')
            if not csv_data:
                logger.error("CSV data is required")
                return JsonResponse({'error': 'CSV data is required'}, status=400)
            
            # Convert CSV data to a NumPy array
            csv_io = io.StringIO(csv_data)
            try:
                df = pd.read_csv(csv_io)
            except pd.errors.EmptyDataError:
                logger.error("CSV data is empty or invalid")
                return JsonResponse({'error': 'CSV data is empty or invalid'}, status=400)
            except pd.errors.ParserError:
                logger.error("CSV data is malformed")
                return JsonResponse({'error': 'CSV data is malformed'}, status=400)
            
            # Check if the DataFrame is empty
            if df.empty:
                logger.error("CSV data is empty or invalid")
                return JsonResponse({'error': 'CSV data is empty or invalid'}, status=400)
            
            np_array = df.to_numpy()
            logger.debug(f"Converted CSV to NumPy array: {np_array}")
            
            # Process the NumPy array
            processed_data = process_image(np_array)
            logger.debug(f"Processed image data: {processed_data}")
            
            return JsonResponse({'csv': csv_data, 'image': processed_data}, status=200)
        except Exception as e:
            logger.error(f"Error processing request: {e}")
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)