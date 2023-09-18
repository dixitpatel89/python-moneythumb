# from django.shortcuts import render
from django.shortcuts import render
import boto3
from django.templatetags.static import static
from django.http import HttpResponse, FileResponse, Http404


def init_fuc(request):
    return render(request, 'index.html')


def text_ract_fuc(request):
    try:
        # return FileResponse(open('static/ART.pdf', 'rb'), content_type='application/pdf')
        client = boto3.client('textract')
        with open('static/ART.pdf', 'rb') as pdf:
            img_test = pdf.read()
            bytes_test = bytearray(img_test)

        response = client.analyze_document(
            Document={'Bytes': bytes_test}, FeatureTypes=['PAGE'])
        return HttpResponse(response)
    except FileNotFoundError:
        raise Http404()


def text_ract_doc_fuc(request):
    try:
        client = boto3.client('textract')
        with open('static/ART.pdf', 'rb') as pdf:
            img_test = pdf.read()
            bytes_test = bytearray(img_test)

        response = client.detect_document_text(
            Document={'Bytes': bytes_test}, FeatureTypes=['QUERIES'])
        return HttpResponse(response)
    except FileNotFoundError:
        raise Http404()


def text_ract_doc_s3_fuc(request):
    try:
        textractmodule = boto3.client('textract')
        response = textractmodule.detect_document_text(
            Document={
                'S3Object': {
                    'Bucket': "testmoneythumb",
                    'Name': "plain.png"
                }
            })
        return HttpResponse(response)

        # with open('static/ART.pdf', 'rb') as pdf:
        #     img_test = pdf.read()
        #     bytes_test = bytearray(img_test)

        # response = client.detect_document_text(
        #     Document={'Bytes': bytes_test}, FeatureTypes=['QUERIES'])
    except FileNotFoundError:
        raise Http404()
