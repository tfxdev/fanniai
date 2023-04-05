import stripe
from itertools import chain
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from um.models import Package, Candidate, WorkExperience, Education
from django.conf import settings
from django.views.generic import ListView


class SearchView(ListView):
    template_name = "search/search.html"
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["query"] = self.request.GET.get("q")
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get("q", None)
        print("q:", query)

        if query is not None:
            candidate_results = Candidate.objects.search(query)
            works_experience_results = WorkExperience.objects.search(query)
            education_results = Education.objects.search(query)

            queryset_chain = chain(
                candidate_results, works_experience_results, education_results
            )
            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)
            return qs
        return Candidate.objects.none()  # just an empty queryset as default


stripe.api_key = settings.SECRET_KEY


@login_required(login_url="account_login")
@csrf_exempt
def package_type_subscription_view(request, pk):
    if request.method == "GET":
        return redirect("core:pricing")
    if request.method == "POST":
        package = get_object_or_404(Package, pk=pk)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": package.name,
                        },
                        "unit_amount": int(package.price * 100),
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url="http://127.0.0.1:8000/success",
            cancel_url="http://127.0.0.1:8000/",
        )
        return redirect(session.url, code=303)
