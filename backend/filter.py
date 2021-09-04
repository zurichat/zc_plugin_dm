def filter_keywords(request):
    keyword = "Hi"
    print(keyword)
    #key
    filter_messages = [ 'Hi, dude',
                        'I\'m on my way home',
                        "Hi, buddy! what's up?",
                        'I\'m on my way home'
                        ]

    queryset = []

    for item in filter_messages:
        print(item)
        for k in item:
            print(k)
            if keyword == k:

                queryset.append(item)
            else:
                queryset = filter_messages

    return queryset

    #return JsonResponse(queryset)
