import os
from trame.app.demo import Cone

print(os.environ.get("TRAME_JUPYTER_WWW"))

app = Cone()
await app.ui.ready

print(app.ui._jupyter_content())

app.ui