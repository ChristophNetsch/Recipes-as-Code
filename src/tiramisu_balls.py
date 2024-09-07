import asyncio
from utils.units import ml_to_g

# INGREDIENTS
INGREDIENTS = {
    "espresso": 50,  # mL
    "ladyfingers": 200,  # g,
    "mascarpone": 250,  # g
    "powdered_sugar": 40,  # g
    "vanilla_sugar": 10,  # g
    "amaretto": 20,  # mL, optional
    "cocoa_powder": 30  # g, for rolling
}

async def prepare_tiramisu_balls():
    espresso = _make_espresso(INGREDIENTS["espresso"])
    ladyfinger_crumbs = _grind_ladyfingers(INGREDIENTS["ladyfingers"])

    _soak_crumbs(ladyfinger_crumbs, espresso)

    filling = _mix_mascarpone(
        INGREDIENTS["mascarpone"],
        INGREDIENTS["powdered_sugar"],
        INGREDIENTS["vanilla_sugar"],
        INGREDIENTS.get("amaretto", 0) # Optional ingredient
    )

    dough = _combine_crumbs_and_filling(ladyfinger_crumbs, filling)

    balls = _shape_into_balls(dough, radius_cm=1)  # 1 teaspoon each
    _roll_in_cocoa(balls, INGREDIENTS["cocoa_powder"])

    return await _cool_balls(balls)

def _make_espresso(amount_ml):
    return amount_ml

def _grind_ladyfingers(ladyfingers_g):
    """Grind ladyfingers in a food processor."""
    ladyfingers_pulverized_g = ladyfingers_g
    return ladyfingers_pulverized_g

def _soak_crumbs(crumbs_g, espresso_mL):
    """Soak ladyfinger crumbs in espresso."""
    soaked_crumbs_g = crumbs_g + ml_to_g(espresso_mL, 1)
    return soaked_crumbs_g

def _mix_mascarpone(
    mascarpone_g,
    powdered_sugar_g,
    vanilla_sugar_g,
    amaretto_mL
):
    """Mix mascarpone, sugars, and amaretto (if used)."""
    return mascarpone_g + powdered_sugar_g + vanilla_sugar_g + ml_to_g(amaretto_mL , 1)

def _combine_crumbs_and_filling(crumbs_g, filling_g):
    dough = crumbs_g + filling_g
    return dough

def _shape_into_balls(dough_g, radius_cm = 1):
    balls_g = dough_g
    return balls_g

def _roll_in_cocoa(balls_g, cocoa_powder_g):
    return balls_g + cocoa_powder_g

async def _cool_balls(balls_g):
    CHILL_TIME_h = 2
    total_seconds = CHILL_TIME_h * 3600
    for second in range(total_seconds):
        if second % 5 == 0:
            print(f"{(second / total_seconds) * 100}%: {second // 3600} hour(s) passed, cooling...")
        await asyncio.sleep(1)
    return balls_g


if __name__ == "__main__":
    asyncio.run(prepare_tiramisu_balls())
