from django.urls import reverse
from django.shortcuts import redirect


class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
         
        #check user is authenticated
        if request.user.is_authenticated: #if request raised ,it checks the user is login are not
             #list of path to check
             paths_to_redirect = [reverse('blog:login'), reverse('blog:register')]
            
             if request.path in paths_to_redirect:
                 return redirect(reverse('blog:index')) #change to home page  
        response = self.get_response(request)
        return response

class RestrictUnauthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request): # This method is called every time a request is made.It checks if the user is authenticated before accessing restricted pages.
        restricted_paths = [reverse('blog:dashboard')] # List of restricted paths where only authenticated users are allowed

        if not request.user.is_authenticated and request.path in restricted_paths:
            return redirect(reverse('blog:login'))  # If the user is not authenticated and tries to access a restricted path, redirect to login
           # Process the request and get the response
        response = self.get_response(request)
        return response    # Return the response after processing