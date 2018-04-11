from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .data_handler import *

class LoginView(FormView):
    """
    """
    template_name = 'login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        """
        """
        context = super(LoginView, self).get_context_data(**kwargs)
        context['query_string'] = self.request.META.get('QUERY_STRING')
        return context

    def get(self, request, *args, **kwargs):
        """
        """
        return super(LoginView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        """
        logout(request)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('admin-page'))
                return HttpResponseRedirect(reverse('home'))
            else:
                form = LoginForm()
                return render(request, 'login_error.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})


class HomeView(View):
    """
    """
    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated():
            return render(request, 'home.html', {'username': request.user.username})
        else:
            return HttpResponseRedirect(reverse('login'))

class ProductListView(ListView):
    """
    """
    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated():
            products = get_product_list(request.user)
            return render(request, 'show_product.html', {'products': products})
        else:
            return HttpResponseRedirect(reverse('login'))


class AddProductView(FormView):
    """
    """
    template_name = 'add_product.html'
    form_class = AddProductForm

    def get_form_kwargs(self):
        kwargs = super(AddProductView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated():
            return super(AddProductView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('login'))

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = AddProductForm(request.POST, request=request)
        if form.is_valid():
            if request.user.is_authenticated():
                name = request.POST['product_name']
                category = request.POST['product_category']
                database = request.POST['database']
                success = add_product_to_db(request.user, name, category, database)
                if success:
                    return HttpResponseRedirect(reverse('home'))
                else:
                    form = AddProductForm()
                    return render(request, 'add_product.html', {'form': form})
            else:
                return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'add_product.html', {'form': form})


class AdminPageView(View):
    """
    """
    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated() and request.user.is_superuser:
            all_products = get_all_user_products()
            return render(request, 'admin_page.html', {'all_products': all_products})
        else:
            HttpResponseRedirect(reverse('login'))
    pass


class AdminUserProductView(View):
    """
    """
    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        username = kwargs['username']
        if request.user.is_authenticated() and request.user.is_superuser:
            if (request.META['QUERY_STRING']) and (request.META['QUERY_STRING'] != ''):
                db = request.GET.get('db')
                product_name = request.GET.get('name')
                category = request.GET.get('category')
                product_id = request.GET.get('product_id')
                return render(request, 'admin_product_detail.html',
                              {'db': db, 'name': product_name,
                               'product_id': product_id, 'username': username,
                               'category': category})
            else:
                return HttpResponseRedirect(reverse('admin-page'))
        else:
            return HttpResponseRedirect(reverse('login'))

    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        username = kwargs['username']
        if request.user.is_authenticated() and request.user.is_superuser:
            if (request.META['QUERY_STRING']) and (request.META['QUERY_STRING'] != ''):
                db = request.GET.get('db')
                product_id = request.GET.get('product_id')
                success = delete_product(username, product_id, db)
                if success:
                    return HttpResponseRedirect(reverse('admin-page'))
            else:
                return HttpResponseRedirect(reverse('admin-page'))
        else:
            return HttpResponseRedirect(reverse('login'))


class AdminAddUserProductView(FormView):
    """
    """
    template_name = 'admin_add_product.html'
    form_class = AdminAddUserProductForm


    def get_context_data(self, **kwargs):
        """
        """
        context = super(AdminAddUserProductView, self).get_context_data(**kwargs)
        context['username'] = self.kwargs['username']
        return context

    def get_form_kwargs(self):
        kwargs = super(AdminAddUserProductView, self).get_form_kwargs()
        kwargs['request'] = self.request
        username = self.kwargs['username']
        kwargs['dbuser'] = get_dbuser(username)
        return kwargs

    def get(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated() and request.user.is_superuser:
            return super(AdminAddUserProductView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('login'))


    def post(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.user.is_authenticated() and request.user.is_superuser:
            username = kwargs['username']
            dbuser = get_dbuser(username)
            form = AdminAddUserProductForm(request.POST, request=request, dbuser=dbuser)
            if form.is_valid():
                name = request.POST['product_name']
                category = request.POST['product_category']
                database = request.POST['database']
                success = add_product_to_db(dbuser.user, name, category, database)
                if success:
                    return HttpResponseRedirect(reverse('admin-page'))
                else:
                    form = AdminAddUserProductForm()
                    return render(request, 'admin_add_product.html', {'form': form})

            else:
                return render(request, 'admin_add_product.html', {'form': form})
        else:
            return HttpResponseRedirect(reverse('login'))
        pass