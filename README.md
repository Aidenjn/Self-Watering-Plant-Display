# Self-Watering-Plant-Display
Code that's running on Aiden Nelson's personal plant watering sytem.
Water dispense script `water.py` run regularly thru cron jobs.

Hardware Used:
- 1 flow sensor
- 4 solenoid valves
- 1 Mac 2008 Pro case
- 1 grow light
- tubing
- power strip
- raspberry pi 2
- relay
- valves and pipes
- water reservoir

Watering script usage:
`python3 water.py [valve number]  [mL of water]`
EXAMPLE:
`python3 water.py 1 100`

Usage notes:
- The command above will dispense 100 ml of water from valve 1.
- [valve number] must be 1, 2, 3, or 4.
- [mL of water] must be greater than 0.

