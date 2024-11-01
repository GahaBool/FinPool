from django.shortcuts import render

def main(request):
    return render(request, 'main/index.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
