from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import html

from random import choice

from markdown2 import markdown

from . import util



class SubmitButton(forms.Input):
    input_type = "submit"
    def __init__(self, attrs={"type":"submit"}):
        self.attrs = attrs

class SearchForm(forms.Form):
    query = forms.CharField(label="Search Encyclopedia")
    button = forms.CharField(widget=SubmitButton(attrs={"type":"submit","value":"Search"}))

class NewEntryForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title of your entry"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":"5","placeholder":"The contents of your entry"}))
    button = forms.CharField(widget=SubmitButton(attrs={"type":"submit","value":"Create new entry"}))


def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            entry_name = form.cleaned_data["query"]

            if entry_name in util.list_entries():
                #I could't use reverse function here, because the website crashes if I use it
                return HttpResponseRedirect(f"/wiki/{entry_name}")
            else:
                if not util.search_results_for(entry_name):
                    return render(request, "encyclopedia/search_results.html",{
                        "messege":"Sorry, there is no entry matching your query"
                    })

                return render(request, "encyclopedia/search_results.html", {
                    "res" : util.search_results_for(entry_name)
                })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(),
                "sform": SearchForm()
            })
    else:
        rnd_page = choice(util.list_entries())

        return render(request, "encyclopedia/index.html", {
            "rnd_page":rnd_page,
            "entries": util.list_entries(),
            "sform": SearchForm()
        })


def entry(request, name):
    if md_content := util.get_entry(name):
        html_content = markdown(md_content)
    else:
        html_content = markdown("Sorry, no such entry was found")

    return render(request, "encyclopedia/entry.html",{
            "entry_content" : html_content,
            "entry_name" : name,
        })

def create_new_page(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if title in util.list_entries():
                return render(request, "encyclopedia/new_page.html", {
                    "neenform": NewEntryForm(),
                    "messege": "Entry with this title already exists"
                })
            else:
                util.save_entry(title, content)
                return HttpResponseRedirect(f"/wiki/{title}")
    else:
        return render(request, "encyclopedia/new_page.html",{
            "neenform": NewEntryForm()
        })


def edit_page(request, name):
    if request.method == "POST":
        contents = request.POST["contents"]

        if name not in util.list_entries():
            return render(request,"encyclopedia/edit_page.html",{
                 "messege": f"There is no such entry as {name}"
            })

        util.save_entry(name, contents)

        return HttpResponseRedirect(f"/wiki/{name}")

    else:
        if name not in util.list_entries():
            return render(request,"encyclopedia/edit_page.html",{
                 "messege": f"There is no such entry as {name}"
            })

        md_content = util.get_entry(name)

        return render(request,"encyclopedia/edit_page.html",{
            "entry_name": name,
            "edit_content": md_content
        })
