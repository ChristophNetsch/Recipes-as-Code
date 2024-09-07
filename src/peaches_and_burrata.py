import asyncio


INGREDIENTS = {
    'peaches': 4, # pcs
    'burrata_balls': 2, # pcs
    'honey': 10, # mL
    'olive_oil': 1, # tbsp
    'vineagar': 1, # tbsp
    'chili_flakes': 1, # tsp
    'salt': 1, # tsp
    'pepper': 1, # tsp
    'cashew': 30, # g 
    'sugar': 10, # g
    'cherry_tomatoes': 10, # pcs
}


async def make_peaches_and_burrata():
    peach_slices = _cut(INGREDIENTS['peaches'], slices_per_peach=8)
    sauteed_peach_slices = await _sautee(peach_slices, INGREDIENTS['honey'], INGREDIENTS['chili_flakes'], INGREDIENTS['salt'])
    caramelized_cashews = _caramelize(INGREDIENTS['cashew'], INGREDIENTS['sugar'])
    diced_tomatoes = _dice(INGREDIENTS['cherry_tomatoes'], style='brunoise')
    return _serve(sauteed_peach_slices, INGREDIENTS['burrata_balls'], INGREDIENTS['olive_oil'], INGREDIENTS['vineagar'], 
                        caramelized_cashews, diced_tomatoes, INGREDIENTS['pepper'], INGREDIENTS['salt'])

def _cut(peaches, slices_per_peach=8):
    return peaches

async def _sautee(peach_slices, honey, chili_flakes, salt):
    SAUTEE_TIME_MIN = 10
    await asyncio.sleep(SAUTEE_TIME_MIN * 60)
    return peach_slices + honey + chili_flakes + salt

def _caramelize(cashews, sugar):
    return cashews + sugar

def _dice(cherry_tomatoes, style='brunoise'):
    return cherry_tomatoes

def _serve(sauteed_peach_slices, burrata, olive_oil, vineagar, caramelized_cashews, diced_tomatoes, pepper, salt):
    """Spread burrata on a plate, top with caramelized peaches, cashews, and cherry tomatoes. Drizzle with olive oil and sprinkle with pepper."""
    PLATE = []
    PLATE.append(burrata)
    PLATE.append(olive_oil + vineagar + pepper + salt)
    PLATE.append(sauteed_peach_slices)
    PLATE.append(caramelized_cashews)
    PLATE.append(diced_tomatoes)
    
    return PLATE

if __name__ == '__main__':
    asyncio.run(make_peaches_and_burrata())
    
    
    