from bottle import route, run, post, request
import json
import uuid


@route('/upload', method='POST')
def upload():
    images = request.files.getall('img1')
    for image in images:
        filename = str(uuid.uuid1()) + '.png'
        path = './upload_images/' + filename
        image.save(path)
        break
    result = json.dumps([])
    return result


if __name__ == '__main__':
    run(host='0.0.0.0', port=8888, debug=True)
