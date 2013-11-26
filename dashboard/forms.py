import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from instance.models import Host


class HostAddTcpForm(forms.Form):
    name = forms.CharField(error_messages={'required': _('No hostname has been entered')},
                           max_length=20)
    hostname = forms.CharField(error_messages={'required': _('No IP / Domain name has been entered')},
                               max_length=100)
    login = forms.CharField(error_messages={'required': _('No login has been entered')},
                            max_length=20)
    password = forms.CharField(error_messages={'required': _('No password has been entered')},
                               max_length=20)

    def clean_name(self):
        name = self.cleaned_data['name']
        have_symbol = re.match('[^a-zA-Z0-9._-]+', name)
        if have_symbol:
            raise forms.ValidationError(_('The host name must not contain any special characters'))
        elif len(name) > 20:
            raise forms.ValidationError(_('The host name must not exceed 20 characters'))
        try:
            Host.objects.get(name=name)
        except Host.DoesNotExist:
            return name
        raise forms.ValidationError(_('This host is already connected'))

    def clean_hostname(self):
        hostname = self.cleaned_data['hostname']
        have_symbol = re.match('[^a-z0-9.-]+', hostname)
        wrong_ip = re.match('^0.|^255.', hostname)
        if have_symbol:
            raise forms.ValidationError(_('Hostname must contain only numbers, or the domain name separated by "."'))
        elif wrong_ip:
            raise forms.ValidationError(_('Wrong IP address'))
        try:
            Host.objects.get(hostname=hostname)
        except Host.DoesNotExist:
            return hostname
        raise forms.ValidationError(_('This host is already connected'))


class HostAddSshForm(forms.Form):
    name = forms.CharField(error_messages={'required': _('No hostname has been entered')},
                           max_length=20)
    hostname = forms.CharField(error_messages={'required': _('No IP / Domain name has been entered')},
                               max_length=100)
    login = forms.CharField(error_messages={'required': _('No login has been entered')},
                            max_length=20)

    def clean_name(self):
        name = self.cleaned_data['name']
        have_symbol = re.match('[^a-zA-Z0-9._-]+', name)
        if have_symbol:
            raise forms.ValidationError(_('The name of the host must not contain any special characters'))
        elif len(name) > 20:
            raise forms.ValidationError(_('The name of the host must not exceed 20 characters'))
        try:
            Host.objects.get(name=name)
        except Host.DoesNotExist:
            return name
        raise forms.ValidationError(_('This host is already connected'))

    def clean_hostname(self):
        hostname = self.cleaned_data['hostname']
        have_symbol = re.match('[^a-zA-Z0-9._-]+', hostname)
        wrong_ip = re.match('^0.|^255.', hostname)
        if have_symbol:
            raise forms.ValidationError(_('Hostname must contain only numbers, or the domain name separated by "."'))
        elif wrong_ip:
            raise forms.ValidationError(_('Wrong IP address'))
        try:
            Host.objects.get(hostname=hostname)
        except Host.DoesNotExist:
            return hostname
        raise forms.ValidationError(_('This host is already connected'))
