from bottle import route, post, get, run, request, static_file
import requests
import json

config_file = "config.json"
ss_endpoint = "http://localhost:8080"

config = None

default_servo = {
    "id":0,
    "min":200,
    "max":600,
    "scale":1.0,
    "offset":0.0
}

def set_servo(name,value) :
    pass

def transform(conf,value) :
    return int(conf["scale"]*value + conf["offset"])

def batch_servo(data) :
    rdat = []
    for x in data :
        if x in config :
            conf = config[x]
            rdat.append({
                "id":conf['id'],
                "value":transform(conf,data[x])
            })
    requests.post(ss_endpoint,data=json.dumps(rdat))

def merge_config(main,prev) :
    out = {}
    vals = {"id":int,"scale":float,"offset":float,"min":float,"max":float}
    for x in vals :
        if x in main :
            out[x] = vals[x](main[x])
        elif x in prev :
            out[x] = vals[x](prev[x])
    return out

with open(config_file) as fil :
    config = json.load(fil)
    for x in config :
        config[x] = merge_config(config[x],default_servo)

@get("/config")
def get_all() :
    return config

@post("/config/<name>")
def post_config(name) :
    data = request.json
    if name in config :
        config[name] = merge_config(data,config[name])
    else :
        config[name] = merge_config(data,default_servo)
    return get_config(name)

@get("/config/<name>")
def get_config(name) :
    if name not in config :
        return "{}"
    else :
        return config[name]

@post("/batch")
def post_batch() :
    dat = request.json
    batch_servo(dat)
    return "OK\n"

@post("/raw/<num>")
def post_raw(num) :
    dat = request.json
    requests.post(ss_endpoint,data=json.dumps([{"id":int(num),"value":int(dat)}]))
    return "OK\n"

@route("/hello")
def page():
    return "hello"

@get("/static/<path:path>")
def get_static(path):
    return static_file(path,root="static")

run(host="localhost",port=8080)
json.dump(config,open(config_file,"w"),indent=2)
print("DONE")
