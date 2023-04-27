from  django.http import HttpResponse
from django.shortcuts import render
from django.views import View

import pandas as pd
import io

# Create your views here.

def get_dataframe(filename, type_):
	if type_ == "XLS" or type_ == "XLSX":
		dataframe = pd.read_excel(filename)

	elif type_ == "CSV":
		dataframe = pd.read_csv(
			io.StringIO(filename.read().decode('utf-8')),
			delimiter=','
			)
	else:
		pass

	return dataframe

def index(request):
	return render(request, 'index.html')

class UploadFile(View):
	def get(self, request):
		return render(request, 'upload_file.html')

	def post(self, request):
		file_obj = request.FILES['filename']

		extension = file_obj.name.split('.')[-1].upper()

		dataframe = get_dataframe(file_obj, extension)

		data = dataframe.to_html(classes='data', header="true")
		return render(request, 'show_content.html', {'data': data})