# grammarchecker/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .test import grammar

def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        user_input = request.POST.get('check')
        matches = grammar(user_input)
        offset = []
        length = []
        message = []
        suggestion = []
        for match in matches:
            offset.append(match.offset)
            length.append(match.errorLength)
            message.append(match.message)
            suggestion.append(', '.join(match.replacements))
        result = ''
        for i in range(len(offset)):
            if i == 0:
                result = user_input[:offset[i]]
            else:
                result += user_input[offset[i-1]+length[i-1]:offset[i]]
            result += f'<span class="highlight" data-toggle="tooltip" data-placement="bottom" title="{message[i]}  Suggestion: {suggestion[i]}">{user_input[offset[i]:offset[i]+length[i]]}</span>'
        return render(request, 'result.html', {'response': result})
    return HttpResponse("Invalid request method.")
