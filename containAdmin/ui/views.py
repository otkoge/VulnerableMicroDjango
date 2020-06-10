from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

import subprocess
import os
# Create your views here.

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class RunningContainerView(LoginRequiredMixin, TemplateView):
    template_name = "containers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        process = subprocess.Popen(['docker', 'container', 'ls'], stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        context['containers'] = stdout.decode("utf-8")
        return context


class ImagesView(LoginRequiredMixin, TemplateView):
    template_name = "images.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        process = subprocess.Popen(['docker', 'image', 'ls'], stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        context['images'] = stdout.decode("utf-8")
        return context


class IfconfigView(LoginRequiredMixin, TemplateView):
    template_name = "nw_tool.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        process = subprocess.Popen(['ip', 'a'], stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        context['title'] = 'Ifconfig'
        context['result'] = stdout.decode("utf-8")
        return context


class RouteView(LoginRequiredMixin, TemplateView):
    template_name = "nw_tool.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        process = subprocess.Popen(['route', '-n'], stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        context['title'] = 'Route'
        context['result'] = stdout.decode("utf-8")
        return context

class PingView(LoginRequiredMixin, TemplateView):
    template_name = "nw_int_tool.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ip = self.request.GET.get('ip', '127.0.0.1')
        cmd = f'ping -c 2 {ip}'
        print(cmd)
        result = os.popen(cmd).read()
        context['title'] = 'Ping'
        context['result'] = result
        return context
