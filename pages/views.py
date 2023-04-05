from django.views.generic import TemplateView
from um.models import Package


class HomeView(TemplateView):
    template_name = "index.html"


class PricingPage(TemplateView):
    template_name = "pages/pricing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["packages"] = Package.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"


class PaymentSuccessView(TemplateView):
    template_name = "pages/success.html"
