from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    """
    Main view for serving the React frontend application.
    All routing will be handled by React Router on the client side.
    """
    template_name = 'user_frontend/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any initial data needed by React
        context['initial_data'] = {
            'api_url': '/api/',
            'is_authenticated': self.request.user.is_authenticated
        }
        return context