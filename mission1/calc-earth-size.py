#!/usr/bin/env python3

import argparse
import json
import math
import os.path as op

def get_parser():
    parser = argparse.ArgumentParser(
        description="Estimate Earth's size from two shadow readings at different latitudes."
    )
    parser.add_argument(
        'results',
        nargs='?',
        help="Path to a JSON file containing reading results",
    )
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    results_path = args.results
    if not results_path:
        print("No results file path specified. Reading simulation.json")
        results_path = op.join(op.dirname(__file__), 'simulation.json')
    results = json.load(open(results_path, 'rt'))
    stick_length = results['stick_length_m']
    reading1 = results['reading1_m']
    reading2 = results['reading2_m']
    distance = results['distance_km']
    # tan(a) = opposite / adjacent
    angle1 = math.atan(reading1 / stick_length)
    angle2 = math.atan(reading2 / stick_length)
    diff = abs(angle2 - angle1)
    WHOLE_CIRCLE = math.pi * 2
    proportion = diff / WHOLE_CIRCLE
    estimate = distance / proportion
    output_lines = [
        "Stick length: {:1.6f} m".format(stick_length),
        "Distance between readings: {:1.2f} km".format(distance),
        "Reading 1: {:1.6f} m".format(reading1),
        "Reading 2: {:1.6f} m".format(reading2),
        "Angle 1: {:1.6f} rad".format(angle1),
        "Angle 2: {:1.6f} rad".format(angle2),
        "Earth's estimated circumference: {:1.2f} km".format(estimate),
    ]
    print('\n'.join(output_lines))

if __name__ == '__main__':
    main()

