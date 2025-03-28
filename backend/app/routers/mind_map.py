from fastapi import APIRouter
from typing import Dict
import random

router = APIRouter(
    prefix="/mind_map",
    tags=["Mind Map"]
)

@router.get("/generate/")
def generate_mind_map(topic: str):
    # Placeholder: generate a simple random mind map structure
    nodes = [f"{topic} Node {i}" for i in range(1, 6)]
    links = {nodes[i]: [random.choice(nodes) for _ in range(2)] for i in range(len(nodes))}
    return {"topic": topic, "nodes": nodes, "links": links}
