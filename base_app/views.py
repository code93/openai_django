from django.shortcuts import render
from django.http import JsonResponse
from .oai_queries import get_completion
from django.db import models
# from .forms import InputForm

answers = []

fprompt = """

Context: Act as HR Interviewer & Analyst

Prompt: I have received the questionnaire responses from a candidate applying for the position of Manager. 

Based on their responses, please help me evaluate their qualification for the role by classifying them as either QUALIFIED, SOMEWHAT QUALIFIED or NOT QUALIFIED. 

The evaluation should take into account their skills, communication abilities, experience & intelligence. Here are the candidate’s responses to the questionnaire: ..

Position Applied: Manager

Role: Manager

About Myself: 

Experience:

"""

questions = ["Can you describe your experience with diary management and scheduling appointments?",
             "How do you handle confidential information and sensitive situations?",
             "Can you provide an example of a complex problem you've solved in a similar role?",
             "How do you prioritize tasks and manage your time when dealing with a busy executive's schedule?",
             "How comfortable are you with liaising with high-level stakeholders and managing professional relationships?",
             "Can you describe a situation where you had to handle an unexpected issue or emergency?",
             "What experience do you have with travel planning and logistics?",
             "How do you ensure effective communication between the MD and other parties?",
             "Can you provide an example of an initiative you took to improve efficiency or effectiveness in your role?",
             "How do you handle stress and pressure in managing a busy executive's affairs?",
             ]

def query_view(request):
    quesans = ""
    if request.method == 'POST':
        for i in range(len(questions)):
            prompt = request.POST['prompt'+str(i)]
            answers.append(prompt)

        for i in range(len(questions)):
            quesans = quesans + "question: " +questions[i] + "\n" + "answer: " +answers[i] + "\n\n"
        finalprompt = fprompt + "\n"+ quesans
        
        response = get_completion(finalprompt)
        # return JsonResponse({'response': response})
        context = {
            'response': response
        }
        return render(request, 'result.html', context)
    # context ={} 
    # context['form']= InputForm() 
    # return render(request, "home.html", context)
    context = {
        'questions': questions
    }
    return render(request, 'query.html', context)
