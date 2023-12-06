from collections import defaultdict
import sys

P1 = []
P2 = defaultdict(int)


with open(sys.argv[1], "r") as f:
  lines = [l.strip() for l in f.read().split("\n")]

  seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]

  for seed in seeds:
    val = seed
    changed = False

    for idx, line in enumerate(lines[1:]):
      if "seed-to-soil" in line:
        seed_to_soil = True
      elif "soil-to-fertilizer" in line:
        soil_to_fert = True
      elif "fertilizer-to-water" in line:
        fert_to_water = True
      elif "water-to-light" in line:
        water_to_light = True
      elif "light-to-temperature" in line:
        light_to_temp = True
      elif "temperature-to-humidity" in line:
        temp_to_humid = True
      elif "humidity-to-location" in line:
        humid_to_local = True

      if not line:
        changed = False
        seed_to_soil = False
        soil_to_fert = False
        fert_to_water = False
        water_to_light = False
        light_to_temp = False
        temp_to_humid = False
        humid_to_local = False

      if any(char.isdigit() for char in line):
        dest, source, range = [int(x) for x in line.split(" ")]

        if seed_to_soil:
          if source <= val <= source + range - 1:
            print(f"soil found: {val}, {val - source}, {dest + (val - source)}")
            val = dest + (val - source)
            seed_to_soil = False
        elif soil_to_fert:
          if source <= val <= source + range - 1:
            print(f"fert found: {val}, {val - source}, {dest + (val - source)}")
            val = dest + (val - source)
            soil_to_fert = False
        elif fert_to_water:
          if source <= val <= source + range - 1:
            print(f"water found: {val}, {val - source}, {dest + (val - source)}")
            val = dest + (val - source)
            fert_to_water = False
        elif water_to_light:
          if source <= val <= source + range - 1:
            print(f"light found: {val}, {val - source}, {dest + (val - source)}")
            val = dest + (val - source)
            water_to_light = False
        elif light_to_temp:
          if source <= val <= source + range - 1:
            print(f"temp found: {val}, {val - source}, {dest + (val - source)}")
            val = dest + (val - source)
            light_to_temp = False
        elif temp_to_humid:
          if source <= val <= source + range - 1:
            print(f"humid found: {val}, {val - source}, {dest + (val - source)}")
            val = dest + (val - source)
            temp_to_humid = False
        elif humid_to_local:
          if source <= val <= source + range - 1:
            print(f"location found: {val}, {val - source}, {dest + (val - source)}")
            val = dest + (val - source)
            humid_to_local = False

    P1.append(val)
    print("-----")

print(f"P1: {min(P1)}")
