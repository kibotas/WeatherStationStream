import cv2 as cv
class StreamReader:
    def __init__(self, source_url):
        self._source_stream = cv.VideoCapture(source_url)
        self._fps = int(self._source_stream.get(cv.CAP_PROP_FPS))
        self._width = int(self._source_stream.get(cv.CAP_PROP_FRAME_WIDTH))
        self._height = int(self._source_stream.get(cv.CAP_PROP_FRAME_HEIGHT))

    def isOpened(self):
        return self._source_stream.isOpened()

    def release(self):
        return self._source_stream.release()

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getFPS(self):
        return self._fps

    def read(self):
        return self._source_stream.read()
