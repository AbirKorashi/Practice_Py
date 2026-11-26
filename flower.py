import math
import random

import numpy as np
import pygame

# ---------- settings ----------
W, H = 800, 600
BASE = (400, 570)        # where the stem is planted
DURATION = 29            # seconds for the whole life cycle
GRAVITY = 9.8
PX_PER_M = 20            # pixels that count as "one metre" for falling petals

PINK = (255, 105, 180)
GREY = (128, 128, 128)
GREEN = (60, 160, 70)
YELLOW = (255, 210, 60)
BG = (0, 0, 0)

life = 0.0   # 0 = seed, 1 = gone
t = 0.0      # running time, drives the stem sway


# ---------- helpers ----------
def ease(x):
    """Clamp to 0..1 and smooth the ends (smoothstep)."""
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def smooth(x, start, width=0.2):
    """0 before `start`, rises smoothly to 1 over `width` of life."""
    return ease((x - start) / width)


def mix(c1, c2, amount):
    """Blend two RGB colours. amount 0 -> c1, 1 -> c2."""
    return tuple(int(a + (b - a) * amount) for a, b in zip(c1, c2))


# ---------- petal data (random values made once, so they don't flicker) ----------
random.seed(7)
PETALS = []
for ring in range(4):
    count = ring * 6 + 5
    for i in range(count):
        PETALS.append({
            "ring": ring,
            "angle": 2 * math.pi * i / count + ring * 0.35,
            "delay": random.uniform(0, 4),       # seconds before it lets go
            "drift": random.uniform(-25, 25),    # sideways px per second
            "spin": random.uniform(-1.5, 1.5),   # radians per second
        })


def petal_polygon(cx, cy, length, angle):
    """Teardrop petal starting at (cx, cy) and pointing along `angle`."""
    top, bottom = [], []
    for k in range(11):
        u = k / 10
        w = math.sin(math.pi * u ** 0.8) * length * 0.3
        top.append((u * length, -w))
        bottom.append((u * length, w))
    local = top + bottom[::-1]
    ca, sa = math.cos(angle), math.sin(angle)
    return [(cx + x * ca - y * sa, cy + x * sa + y * ca) for x, y in local]


# ---------- the three stages ----------
def stem(life):
    h = ease(life / 0.4) * 470
    y = np.linspace(0, h, 900)
    anchor = np.minimum(1.0, y / 150)            # base stays still, top sways
    return 14 * np.sin(y / 80 + t) * anchor, y


def bloom(life):
    """Return how open each of the 4 rings is (0..1.3 scale)."""
    scales = []
    for ring in range(4):
        opened = smooth(life, 0.42 + ring * 0.04)
        scales.append(opened * 1.3)
    return scales


def wilt(life):
    """Return (colour, seconds since wilting began)."""
    droop = smooth(life, 0.75, 0.25)
    colour = mix(PINK, GREY, droop)
    fall_time = max(0.0, (life - 0.75) * DURATION)
    return colour, droop, fall_time


# ---------- drawing ----------
def draw(stem_data, ring_scales, wilt_data):
    x, y = stem_data
    colour, droop, fall_time = wilt_data

    # stem
    if len(y) > 1 and y[-1] > 1:
        pts = [(BASE[0] + float(a), BASE[1] - float(b)) for a, b in zip(x, y)]
        pygame.draw.lines(screen, mix(GREEN, GREY, droop), False, pts, 6)
        tip = pts[-1]
    else:
        tip = BASE

    # ground
    pygame.draw.line(screen, (70, 50, 30), (0, BASE[1] + 3), (W, BASE[1] + 3), 4)

    # petals (outer ring first so inner rings sit on top)
    if life >= 0.42:
        for p in sorted(PETALS, key=lambda q: -q["ring"]):
            length = (30 + p["ring"] * 9) * ring_scales[p["ring"]] * (1 - 0.3 * droop)
            if length < 1:
                continue
            cx, cy, angle = tip[0], tip[1], p["angle"]

            tf = max(0.0, fall_time - p["delay"])
            if tf > 0:
                cy += 0.5 * GRAVITY * PX_PER_M * tf ** 2
                cx += p["drift"] * tf
                angle += p["spin"] * tf
                cy = min(cy, BASE[1] - 3)        # stop at the ground

            pygame.draw.polygon(screen, colour, petal_polygon(cx, cy, length, angle))

        # flower centre
        r = int(9 * ring_scales[0] / 1.3 * (1 - 0.3 * droop))
        if r > 0:
            pygame.draw.circle(screen, mix(YELLOW, GREY, droop),
                               (int(tip[0]), int(tip[1])), r)


# ---------- main loop ----------
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flower life cycle")
clock = pygame.time.Clock()

running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    life += dt / DURATION
    t += dt
    if life >= 1:        # start over with a new seed
        life = 0.0

    screen.fill(BG)
    draw(stem(life), bloom(life), wilt(life))
    pygame.display.flip()

pygame.quit()
