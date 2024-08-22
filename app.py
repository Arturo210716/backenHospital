
import os
from fastapi import FastAPI
import uvicorn
#from routes.persona import persona
#from routes.usuario import usuario
from routes.users import user
from routes.persons import person
from routes.roles import roles
from routes.usersrols import userrol

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app= FastAPI()
#app.include_router(persona)
#app.include_router(usuario)
app.include_router(user)
app.include_router(person)
app.include_router(roles)
app.include_router(userrol)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


print("Bienvenido a mi aplicacion")
