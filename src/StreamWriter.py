import subprocess as sp
class StreamWriter:
    def __init__(self, target_url, video_codec, pix_fmt, width, height, fps):
        self._target_url = target_url
        self._command = ['ffmpeg',
                   '-re',
                   '-s', f"{width}x{height}",
                   '-r', str(fps),
                   '-i', '-',
                   '-pix_fmt', pix_fmt,
                   '-codec:v', video_codec,
                   '-f', 'rtsp',
                   '-rtsp_transport', 'tcp',
                   self._target_url]
        self._ffmpeg = sp.Popen(self._command, stdin=sp.PIPE)

    def writeToStream(self, bytes):
        self._ffmpeg.stdin.write(bytes)
