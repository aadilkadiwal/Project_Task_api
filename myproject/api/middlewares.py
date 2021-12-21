# Function based middleware

'''
def MyFunctionMiddleware(get_response):

    print("One Time Initialization")

    def my_function(request):
        print("This is before View")
        response = get_response(request)
        print("This is after View")

     return response

return my_function   
'''

# Class based middleware

'''
class MyClassMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Initialization")

    def __call__(self, request):
        print("This is before View")
        response = self.get_response(request)
        # response = HttpResponse("Hi")  <-- To response a request 
        print("This is after View")
        return response  
'''