import os

def _CurrentDirectory():
    this_dir=os.path.dirname(os.path.abspath(__file__))
    return this_dir

class Config(object):
    #endpoint urls
    request_id='q4hzbmk'
    host='http://localhost/rcostedit/'
    jobhistory=host+'getjobs'
    qtrack=host+'Qtrack'
    status=host+'status/'+request_id
    results=host+'results/'+request_id
    log=host+'log/'+request_id
    download=host+'download/'+request_id
    edit_download=host+'editdownload'
    report=host+'report'