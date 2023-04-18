"""server !!"""
from sanic import Sanic
from sanic.response import text, json
# import sync_test


app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    """GET Request"""
    return text("Hello, world.")


@app.post("/test")
async def handle_post(request):
    """POST Request"""
    data = request.json
    # return text("success!")
    return json({"status": "success"})
# test_basic_test_client(app)


@app.put("/test")
async def handle_put(request):
    """PUT Request"""
    data = request.json
    return json({"status": "success"})


@app.patch("/test")
async def handle_patch(request):
    """PATCH Request"""
    data = request.json
    return json({"status": "success"})

@app.delete("/test")
async def handle_del(request):

    """DELETE Request"""
    data = request.json
    return json({"status": "success"})
