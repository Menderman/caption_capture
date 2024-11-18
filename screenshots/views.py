from django.shortcuts import render
from django.http import JsonResponse
from .models import Subtitle, Show
from django.db.models import Q


# Create your views here.
def hello_view(request):
    return render(request, 'screenshots/hello_django.html', {
        'data': "Hello Django ",
    })

def search_index(request):
    # 主頁面，渲染基本模板
    return render(request, 'screenshots/search.html')

#API
def search_subtitles(request):
    query = request.GET.get('query', '')
    episode = request.GET.get('episode', '')
    results = []
    if query:
        subtitles = Subtitle.objects.filter(Q(text__icontains=query))

        if episode:
            subtitles = subtitles.filter(show__episode_number=episode)

        for subtitle in subtitles:
            results.append({
                "movie_title": subtitle.show.title,
                "movie_season": subtitle.show.season_number,
                "movie_episode": subtitle.show.episode_number,
                "subtitle_text": subtitle.text,
                "start_frame": subtitle.start_frame,
                "end_frame": subtitle.end_frame,
                "screenshot_path": subtitle.screenshot_path
            })
    #return JsonResponse({"results": results})
    return render(request, 'screenshots/items_partial.html', {
        'results': results
    })

