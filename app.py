from aiohttp.web import Response, Application, run_app
import json

languages = [{'id': 1, 'language': 'Python'}]


async def handle_get_language(request):
    response = json.dumps(languages)
    return Response(body=response,
                    headers={'Content-Type': 'application/json'})


async def handle_post_language(request):
    payload = await request.json()
    if 'language' not in payload:
        response = {'results': 'language value is not present in POST body'}
        return Response(body=json.dumps(response), headers={'Content-Type': 'application/json'},
                        status=400)
    elif any(payload['language'] == row['language'] for row in languages):
        response = {'results': 'language value is already in the collection'}
        return Response(body=json.dumps(response), headers={'Content-Type': 'application/json'},
                        status=409)

    payload['id'] = len(languages) + 1
    languages.append(payload)
    response = {'results': 'language has been added'}
    return Response(body=json.dumps(response), headers={'Content-Type': 'application/json'},
                    status=201)

app = Application()
app.router.add_route('GET', '/language', handle_get_language)
app.router.add_route('POST', '/language', handle_post_language)


if __name__ == "__main__":
    run_app(app)
