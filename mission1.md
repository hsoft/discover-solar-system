# Misson 1: Earth's circumference

The goal is to estimate Earth's circumference.

## Method

The plan is to use the shadow of sticks pointing at Earth's center. By measuring the shadow that
such a stick produces when the Sun is at its zenith, and this, at two different latitudes, we can
calculate the angle difference that a given latitude change produced, and thus, calculate Earth's
circumference.

Our first reading will be somewhere in the northern hemisphere, and our second reading, `X`km
north. The length of the shadow will give us the angle at which the light from the Sun hits th
ground. Let's call that angle A. Because we know that angle B is `X`km north, our circumference
will simply be `2πX/(B-A)`.

Seasons will affect our angles, but not our calculation because all we care about is relative
angles.

## Simulation

To ensure that our plan is sound, let's try to detail our calculations with an hypothetical
Earth with a 1000km diameter. If the null angle is where the sun hits with no shadow, let's
imagine our first reading being `π/4` (45 degrees) northward.

If our stick is 1m long, it should have a 1m shadow when the sun is at its zenith.

Now, if we go 100km north for our second reading, our angle will be `π/4 + (100/1000π)⋅2π`, or,
`π/4 + 0.2`. Using the tangeant function, we'll see that our shadow should have a length of
`tan(π/4 + 0.2) / 1m` (`tan(angle) = opposite / adjacent`), that is, `1.508m`. That measure
would be enough for us to work our way up to a `1000πkm` circumference.

*TODO: diagram*

## Sources of innaccuracies

* Earth is probably not exactly round. We know that, as a general rule, centrifugal force of a
  planet spinning on itself will make it not round.
* The stick will not point precisely at the center.
* If the terrain is not perfectly flat, shadow's length will not be the same.
* The time at which the measurement will occur won't be precisely the time of the zenith.
* Distance measurement between the two readings will be inexact.
* Because our two readings are not taken exactly at the same time, Earth will have tilted
  compared to the sun. This will affect our shadow length.
* Clouds could affect the sharpness of the shadow.

## Innaccuracies mitigation

Because the length of the stick is going to be much smaller than Earth, any source of innaccuracy
listed above is going to have a significant impact on the end result, so it's important to mitigate
these issues as much as possible.

* Rather than planting the stick in the ground, we'll suspend it to something, letting gravity
  make the stick point directly to Earth's center.
* We'll want to choose a terrain that is as flat as possible and with the lowest inclination
  possible, but I don't think that it's a very big source of innaccuracy, so I'm not planning
  on doing anything special here.
* To ensure that we measure our shadow at the right time, we'll make multiple measurements
  around the time when zenith should be reached. The shadow will shrink and reach its minimum
  at zenith, so we can simply measure the shadow until it starts growing.
* The second reading will be taken one day after the first to minimize Earth tilting impact.
* For this mission, we'll estimate the circumference of a round Earth and forget about this
  centrifugal force thing. We'll try to make our estimates more exact in a future mission.

## Experiment planning

*TODO*

## Experiment execution log

*TODO*

## Results

*TODO*

