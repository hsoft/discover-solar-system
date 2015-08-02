# Mission 2: Sun's position at dusk and dawn

From past observation, we know that the sun generally rises east and falls west. However, depending
on seasons, it does not precisely show up at the same place every day.

The goal is to be able to accurately predict the sun's position at dusk and dawn on any given day.

## Method

Because watching the sun directly is hazardous for one's eyes, we'll use the sun's shadow instead.

We'll make ourselves a kind of sun dial with a small stick glued to a piece of wood. Then, a piece
of paper can be placed on that piece of wood so that we can record the angle of the sun's shadow
relative to the north (which we'll indicate on the paper using a compass).

By taking such readings regularly and consistently, we should be able to garner enough data to
extract a equation from it.

Conveniently, each reading could serve as a confirmation of our previous tentative equation.

### Gear

* [Homemade sundial](gear.md#homemade-sundial)
* [Compass](gear.md#compass)

## Experiment planning

I live in downtown Quebec City and I have to walk a little bit to get access to sunrise and sunset
sights, but not that much, so frequent readings are not much of a hassle.

I'll initially try for daily readings (if the weather permits) and see what's the angle variation
like. I expect it will not be significant, so I'll probably go for weekly readings afterwards.

I should try to take my readings at consistent hours to have consistent angle progression.

Readings will be recorded in a CSV file.

Readings steps are:

1. Get a new piece of paper.
2. Write down basic info: mission, location, date of the reading (time will be writting during the
   reading).
3. Make a hole in the middle for the stick and put the piece of paper on the sundial.
4. Go somewhere with access to sunset/sunrise direct sight.
5. Place the sundial so that it stick tilting (see gear page) points towards the sun.
6. Mark the shadow.
7. By carefully keeping the sundial in place, remove the stick and place the compass on it.
8. Mark the north on the piece of paper.
9. Draw a straight line from the shadow mark, through the stick hole. Mark the end of that line as
   the sun's position.
10. Using the compass, read the angle between the sun's position and the north. This is the
    reading we were looking for.

*WARNING*: The compass gives the *magnetic* north. Adjustments will have to be made to derive the
geographical north from that, but I don't know how yet.

Angle measurement with the compass is not very precise. I'll go buy myself a protractor. It will
feel like primary school again!

## Experiment log

The first reading was made on 2015-08-01 20:15, but it was a little too late, the shadow was very
faint. I took the reading anyway, but following ones will take place earlier. I need a protractor
to calculate the angle and thus record it.

