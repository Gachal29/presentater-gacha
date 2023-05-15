from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView
import re
import requests
import json
import random

class TopView(TemplateView):
    template_name = "gacha/index.html"

    def post(self, request):
        connpass_url = request.POST.get("connpass_url")

        if not re.search("https://connpass.com/event/[0-9]*/participation/#participants", connpass_url):
            raise ValueError("入力したURLを確認してください。")
        
        api_url = "https://asia-northeast1-notify-send.cloudfunctions.net/connpass-applicants/"
        response = json.loads(requests.get(api_url + connpass_url).text)

        participant = []

        keys = response.keys()
        for key in keys:
            for user in response.get(key, []):
                if user.get("label_status_tag") == "参加者":
                    participant.append(user.get("display_name"))

        random.shuffle(participant)

        for i, user in enumerate(participant, start=1):
            print(f"{i}番目： {user}")

        return redirect(reverse("top"))

