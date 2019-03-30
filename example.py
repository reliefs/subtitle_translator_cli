from subprocess import call
import time

print("Visit my github: http://github.com/reliefs/subtitle_translator_cli")
wc = call("wc subtitle/w.srt | awk '{print $1}'", shell=True)
print("^_^____ There are so many lines", wc)
time.sleep(5)
call('python run.py /folder/to/your/subtitle_translator/subtitle ' + str(wc) + ' yandex en da', shell=True)
