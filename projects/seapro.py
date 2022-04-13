from flask import Flask, render_template

app = Flask(__name__)
from flask_restful import Resource, Api, reqparse
import werkzeug

class UploadImage(Resource):
   def post(self):
     parse = reqparse.RequestParser()
     parse.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
     args = parse.parse_args()
     image_file = args['file']
     image_file.save("your_file_name.jpg")
@app.route("/")
def hello_world():
    return render_template("HOME.html")


@app.route("/about/")
def hello_worl():
    return "<h1><p>!!!!!!this fucking world is nasty!!!!!!!!!!!!!</p></h1>"


@app.route("/bubble/")
def bubble_sort():
    return "<h1><p>Bubble Sort</p></h1>"


@app.route("/upload")
def upload():
    return render_template("upload.html")

 # sorting algorithms
def bubble_sort(arr):
    for i in range(len(arr)):
     for j in range(len(arr) - i - 1):
         if arr[j] > arr[j + 1]:
             arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
     min_index = i
     for j in range(i + 1, len(arr)):
         if arr[min_index] > arr[j]:
             min_index = j
     arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
     j = i
     while j > 0 and arr[j - 1] > arr[j]:
         arr[j], arr[j - 1] = arr[j - 1], arr[j]
         j -= 1
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
     return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
     if left[0] <= right[0]:
         result.append(left.pop(0))
     else:
         result.append(right.pop(0))
    if len(left) > 0:
     result += left
    if len(right) > 0:
     result += right
    return result

def quick_sort(arr):
    if len(arr) <= 1:
     return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def heap_sort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
     heapify(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
     arr[0], arr[i] = arr[i], arr[0]
     heapify(arr, 0, i)
    return arr

def heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, heap_size)   # recursion
