from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, RedirectResponse
import random

app = FastAPI()

facts = [
	"Wood frogs can freeze up to 70% of their body water to survive cold temperatures. They just thaw out in the spring.",
	"Many fish can change their sexes, generally triggered by temperature changes or sex ratio in the local population",
	"Herping is the amphibian/reptile (herptile) equivalent to birding",
	"Crows can recognize human faces for years and pass down the knowledge through generations",
	"Male anglerfish get absorbed by the female angler fish after mating"
]

@app.get("/")
def go_to_snek():
    return RedirectResponse(url="https://bitememedusa.carrd.co/")

@app.get("/api/facts", response_class=PlainTextResponse)
def get_random_fact():
    return random.choice(facts)

