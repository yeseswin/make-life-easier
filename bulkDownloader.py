import re
import requests
from multiprocessing.pool import ThreadPool
import time
import os 

start = time.perf_counter()
mit_ocw_linear_algebra_url = "http://ia802205.us.archive.org/18/items/MIT18.06S05_MP4/"

def download_file(url):
    print("DOWNLOADING FROM -> " +url)
    path = 'tmp/videos/' + re.search('[^\/]+$',url).group(0)

    if not os.path.exists(path):
        r=requests.get(url,stream = True)
        if r.status_code == 200:
            with open(path, 'wb') as f:  
                for chunk in r:
                    f.write(chunk)

    return path

urls=[]
for i in range(1,35):
    extension = ".mp4"
    fileNumber= "0"+str(i) if i<10  else str(i)
    filePath = mit_ocw_linear_algebra_url + fileNumber + extension
    urls.append(filePath)
    # download_file(filePath)


results = ThreadPool(4).imap_unordered(download_file,urls)
for path in results:
    print(path)

end = time.perf_counter()

print("Start: " + str(start), "End : "+ str(end), "Elapsed: " + str(end-start))