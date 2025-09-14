from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItineraryRequest(BaseModel):
    no_of_days: int
    budget: int
    user_tags: str

@app.post("/generate_itinerary")
def generate_itinerary(req: ItineraryRequest):
    # Backend logic to generate day-wise itinerary
    # Example static response
    itinerary = {
        "Day 1": ["Hundru Falls", "Jonha Falls"],
        "Day 2": ["Netarhat", "Patratu Valley"],
        "Day 3": ["Betla National Park", "Palamu Fort"]
    }
    return {"itinerary": itinerary}
