from aiohttp import web
import json

languages = [{'id': 1, 'language': 'Python'}]


async def handle_get_language(request):
    payload = json.dumps(languages)
    return web.Response(
        body=payload,
        content_type='application/json')


async def handle_post_language(request):
    payload = await request.json()

    if 'language' not in payload:
        payload = json.dumps(
            {'results': 'language value is not present in POST body'})

        return web.Response(
            body=payload,
            content_type='application/json',
            status=400)

    elif any(payload['language'] == row['language'] for row in languages):
        payload = json.dumps(
            {'results': 'language value is already in the collection'})

        return web.Response(
            body=payload,
            content_type='application/json',
            status=409)

    payload['id'] = len(languages) + 1
    languages.append(payload)
    payload = json.dumps({'results': 'language has been added'})

    return web.Response(
        body=payload,
        content_type='application/json',
        status=201)
