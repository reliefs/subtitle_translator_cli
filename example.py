from subprocess import call

wc = call("wc subtitle/w.srt | awk '{print $1}'", shell=True)
print("There are so many lines", wc)
call('python run.py /folder/to/your/subtitle_translator/subtitle ' + str(wc) + ' yandex en da', shell=True)
