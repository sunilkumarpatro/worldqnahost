from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Qna, Comment, Related,Contact
from django.utils import timezone 
from django.views.static import serve
from django.conf import settings
def custom_404(request, exception=None):
    return render(request, '404.html', {}, status=404)

def custom_500_view(request):
    return render(request, '500.html', {}, status=500)
def robot(request):
    return serve(request, 'robots.txt', document_root=settings.STATIC_ROOT, show_indexes=False)

def sitemap(request):
    return serve(request, 'sitemap.xml', document_root=settings.STATIC_ROOT, show_indexes=False)
# English views
def index(request):
    return render(request, 'english/index.html')
def about(request):
    return render(request, 'english/about.html')
def contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('contact'))

    return render(request, 'english/contact.html', {'form_submitted': form_submitted})
def privacy(request):
    return render(request, 'english/privacy-policy.html')
def ask(request):
    form_submitted = False
    error_message = None

    if request.method == 'POST':
        english_title_question = request.POST.get('english_title_question')
        question_image = request.FILES.get('question_image')

        # Check if at least one of them (text or image) is provided
        if not english_title_question and not question_image:
            error_message = 'Please provide either text or an image.'

        # Check if english_title_question meets length requirements
        elif english_title_question and (len(english_title_question) < 10 or len(english_title_question) > 500):
            error_message = 'English title question should be between 10 and 500 characters.'

        # Check if question_image is not empty and under 2 MB
        elif question_image and question_image.size > 6 * 1024 * 1024:
            error_message = 'Question image should be under 2 MB.'

        if not error_message:
            # Save the form data to the Qna model
            qna_entry = Qna(english_title_question=english_title_question, question_image=question_image)
            qna_entry.save()

            # Set the flag to indicate successful submission
            form_submitted = True

    return render(request, 'english/ask-question.html', {'form_submitted': form_submitted, 'error_message': error_message})
def search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        allQnas = allQnaQuestion.union(allQnaAnswer)   
    
    params['allQnas'] = allQnas
    return render(request, 'english/search.html', params)
def redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('open', slug=slug)
def open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'english/qna.html', context)
def add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('qna_detail', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(english_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('open', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('home')

# Hindi views
def hi_index(request):
    return render(request, 'hindi/index.html')
def hi_about(request):
    return render(request, 'hindi/about.html')
def hi_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('hi_contact'))


    return render(request, 'hindi/contact.html', {'form_submitted': form_submitted})
def hi_privacy(request):
    return render(request, 'hindi/privacy-policy.html')
def hi_ask(request):
    return render(request, 'hindi/ask-question.html')
def hi_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_hindi = Qna.objects.filter(hindi_title_question__icontains=query, showhide="show")
        allQnaAnswer_hindi = Qna.objects.filter(hindi_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_hindi.union(allQnaAnswer_hindi, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'hindi/search.html', params)
def hi_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('hi_open_no_slash', slug=slug)
def hi_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'hindi/qna.html', context)
def hi_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('hi_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(hindi_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('hi_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('hi_home')

# Spanish views
def es_index(request):
    return render(request, 'spanish/index.html')
def es_about(request):
    return render(request, 'spanish/about.html')
def es_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('es_contact'))


    return render(request, 'spanish/contact.html', {'form_submitted': form_submitted})
def es_privacy(request):
    return render(request, 'spanish/privacy-policy.html')
def es_ask(request):
    return render(request, 'spanish/ask-question.html')
def es_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_spanish = Qna.objects.filter(spanish_title_question__icontains=query, showhide="show")
        allQnaAnswer_spanish = Qna.objects.filter(spanish_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_spanish.union(allQnaAnswer_spanish, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'spanish/search.html', params)
def es_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('es_open_no_slash', slug=slug)
def es_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'spanish/qna.html', context)
def es_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('es_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(spanish_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('es_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('es_home')
# Arabic views
def ar_index(request):
    return render(request, 'arabic/index.html')
def ar_about(request):
    return render(request, 'arabic/about.html')
def ar_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('ar_contact'))


    return render(request, 'arabic/contact.html', {'form_submitted': form_submitted})
def ar_privacy(request):
    return render(request, 'arabic/privacy-policy.html')
def ar_ask(request):
    return render(request, 'arabic/ask-question.html')
def ar_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_arabic = Qna.objects.filter(arabic_title_question__icontains=query, showhide="show")
        allQnaAnswer_arabic = Qna.objects.filter(arabic_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_arabic.union(allQnaAnswer_arabic, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'arabic/search.html', params)
def ar_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('ar_open_no_slash', slug=slug)
def ar_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'arabic/qna.html', context)
def ar_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('ar_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(arabic_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('ar_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('ar_home')
# Chinese views
def zh_index(request):
    return render(request, 'chinese/index.html')
def zh_about(request):
    return render(request, 'chinese/about.html')
def zh_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('zh_contact'))

    return render(request, 'chinese/contact.html', {'form_submitted': form_submitted})
def zh_privacy(request):
    return render(request, 'chinese/privacy-policy.html')
def zh_ask(request):
    return render(request, 'chinese/ask-question.html')
def zh_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_chinese = Qna.objects.filter(chinese_title_question__icontains=query, showhide="show")
        allQnaAnswer_chinese = Qna.objects.filter(chinese_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_chinese.union(allQnaAnswer_chinese, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'chinese/search.html', params)
def zh_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('zh_open_no_slash', slug=slug)
def zh_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'chinese/qna.html', context)
def zh_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('zh_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(chinese_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('zh_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('zh_home')
# Portuguese views
def pt_index(request):
    return render(request, 'portuguese/index.html')
def pt_about(request):
    return render(request, 'portuguese/about.html')
def pt_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('pt_contact'))


    return render(request, 'portuguese/contact.html', {'form_submitted': form_submitted})
def pt_privacy(request):
    return render(request, 'portuguese/privacy-policy.html')
def pt_ask(request):
    return render(request, 'portuguese/ask-question.html')
def pt_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_portuguese = Qna.objects.filter(portuguese_title_question__icontains=query, showhide="show")
        allQnaAnswer_portuguese = Qna.objects.filter(portuguese_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_portuguese.union(allQnaAnswer_portuguese, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'portuguese/search.html', params)
def pt_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('pt_open_no_slash', slug=slug)
def pt_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'portuguese/qna.html', context)
def pt_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('pt_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(portuguese_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('pt_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('pt_home')
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()
    context = {
        'qna': qna,
        'comment': comment,
        'related': related
    }
    return render(request, 'portuguese/qna.html', context)
# Russian views
def ru_index(request):
    return render(request, 'russian/index.html')
def ru_about(request):
    return render(request, 'russian/about.html')
def ru_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('ru_contact'))
        

    return render(request, 'russian/contact.html', {'form_submitted': form_submitted})
def ru_privacy(request):
    return render(request, 'russian/privacy-policy.html')
def ru_ask(request):
    return render(request, 'russian/ask-question.html')
def ru_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_russian = Qna.objects.filter(russian_title_question__icontains=query, showhide="show")
        allQnaAnswer_russian = Qna.objects.filter(russian_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_russian.union(allQnaAnswer_russian, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'russian/search.html', params)
def ru_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('ru_open_no_slash', slug=slug)
def ru_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'russian/qna.html', context)
def ru_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('ru_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(russian_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('ru_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('ru_home')
# French views
def fr_index(request):
    return render(request, 'french/index.html')
def fr_about(request):
    return render(request, 'french/about.html')
def fr_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('fr_contact'))
        

    return render(request, 'french/contact.html', {'form_submitted': form_submitted})
def fr_privacy(request):
    return render(request, 'french/privacy-policy.html')
def fr_ask(request):
    return render(request, 'french/ask-question.html')
def fr_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_french = Qna.objects.filter(french_title_question__icontains=query, showhide="show")
        allQnaAnswer_french = Qna.objects.filter(french_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_french.union(allQnaAnswer_french, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'french/search.html', params)
def fr_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('fr_open_no_slash', slug=slug)
def fr_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'french/qna.html', context)
def fr_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('fr_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(french_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('fr_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('fr_home')
# Japanese views
def ja_index(request):
    return render(request, 'japanese/index.html')
def ja_about(request):
    return render(request, 'japanese/about.html')
def ja_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('ja_contact'))


    return render(request, 'japanese/contact.html', {'form_submitted': form_submitted})
def ja_privacy(request):
    return render(request, 'japanese/privacy-policy.html')
def ja_ask(request):
    return render(request, 'japanese/ask-question.html')
def ja_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_japanese = Qna.objects.filter(japanese_title_question__icontains=query, showhide="show")
        allQnaAnswer_japanese = Qna.objects.filter(japanese_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_japanese.union(allQnaAnswer_japanese, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'japanese/search.html', params)
def ja_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('ja_open_no_slash', slug=slug)
def ja_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'japanese/qna.html', context)
def ja_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('ja_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(japanese_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('ja_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('ja_home')
# German views
def de_index(request):
    return render(request, 'german/index.html')
def de_about(request):
    return render(request, 'german/about.html')
def de_contact(request):
    form_submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the form data to the Contact model
        contact_entry = Contact(name=name, email=email, msg=message, time=timezone.now())
        contact_entry.save()

        # Set the flag to indicate successful submission
        return redirect(reverse('de_contact'))
        

    return render(request, 'german/contact.html', {'form_submitted': form_submitted})
def de_privacy(request):
    return render(request, 'german/privacy-policy.html')
def de_ask(request):
    return render(request, 'german/ask-question.html')
def de_search(request):
    query = request.GET.get('query', '')
    params = {'query': query}
    
    if len(query) > 78:
        allQnas = Qna.objects.none()
    else:
        allQnaQuestion_german = Qna.objects.filter(german_title_question__icontains=query, showhide="show")
        allQnaAnswer_german = Qna.objects.filter(german_answer__icontains=query, showhide="show")
        
        allQnaQuestion_english = Qna.objects.filter(english_title_question__icontains=query, showhide="show")
        allQnaAnswer_english = Qna.objects.filter(english_answer__icontains=query, showhide="show")
        
        allQnas = allQnaQuestion_german.union(allQnaAnswer_german, allQnaQuestion_english, allQnaAnswer_english)
    
    params['allQnas'] = allQnas
    return render(request, 'german/search.html', params)
def de_redirect_without_slash(request, slug):
    # Redirect to the URL without the trailing slash
    return redirect('de_open_no_slash', slug=slug)
def de_open(request, slug):
    # Your existing view logic
    qna = get_object_or_404(Qna, slug=slug)
    comment = Comment.objects.all()
    related = Related.objects.all()

    context = {
        'qna': qna,
        'comment': comment,
        'related': related,
    }

    return render(request, 'german/qna.html', context)
def de_add_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment', '')
        qna_catagary = request.POST.get('qna_catagary', '')

        qna = get_object_or_404(Qna, slug=qna_catagary)

        # Validate the comment input
        if len(comment_text) < 3 or len(comment_text) > 500:
            # Handle validation error, you may want to display an error message
            return redirect('de_open_no_slash', slug=qna_catagary)

        # Create a new Comment instance and save it to the database
        new_comment = Comment(german_comment=comment_text, qna_catagary=qna)
        new_comment.save()

        # Redirect back to the Qna detail page after adding the comment
        return redirect('de_open_no_slash', slug=qna_catagary)

    # Handle invalid request method, you may want to display an error message
    return redirect('de_home')

