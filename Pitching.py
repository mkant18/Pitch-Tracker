import statistics
pitchers = {
}

pitchera = {
	"Height" : (input("Enter Height(ft,inches): ") + "'"),
	"Weight" : (input('Enter Weight(lbs): ') + " lbs")
}
pitchers["pitchera"] = pitchera
print(pitchers)
pitchnum = 0
input("Enter 'Go' to begin: ")
pitcherapitches = []
pa_pitch1 = [input("Enter velocity: "), input("Enter break: "), input("Enter location: ")]
pitch1_type = input("Enter Pitch Type (FB, CB, CH, SL: ")

pa_pitch1 = list(map(int, pa_pitch1))

if pitch1_type == 'FB':
	pa_pitch1.append(((pa_pitch1[0] * 4) * (pa_pitch1[1] * 2) * (pa_pitch1[2] * 0.5)) / 10)
elif pitch1_type == 'CB':
	pa_pitch1.append(((pa_pitch1[0] * 10) * (pa_pitch1[1] * 5) * (pa_pitch1[2] * 6)) / 10)
elif pitch1_type == 'CH':
	pa_pitch1.append(((pa_pitch1[0] * 0.2) * (pa_pitch1[1] * 6) * (pa_pitch1[2] * 5)) / 10)
elif pitch1_type == 'SL':
	pa_pitch1.append(((pa_pitch1[0] * 6) * (pa_pitch1[1] * 6) * (pa_pitch1[2] * 0.2)) / 10)
	
pa_pitch1.append(pitch1_type)
pitcherapitches.append(pa_pitch1)
print(pitcherapitches)

while (pitchnum < 0):
	pa_pitch = [input("Enter Velocity: "), input("Enter break: "), input("Enter location: ")]
	pa_pitch = list(map(int, pa_pitch))
	pitch_type = input("Enter Pitch Type (FB, CB, CH, SL): ")
	if pitch_type == 'FB':
		pa_pitch.append(((pa_pitch1[0] * 4) * 			(pa_pitch[1] * 2) * (pa_pitch[2] * 0.5)) / 10)
	elif pitch_type == 'CB':
		pa_pitch.append(((pa_pitch[0] * 10) * 			(pa_pitch[1] * 5) * (pa_pitch[2] * 6)) / 10)
	elif pitch_type == 'CH':
		pa_pitch.append(((pa_pitch[0] * 0.2) * (pa_pitch[1] * 6) * (pa_pitch[2] * 5)) / 10)
	elif pitch_type == 'SL':
		pa_pitch.append(((pa_pitch[0] * 6) * (pa_pitch[1] * 6) * (pa_pitch[2] * 0.2)) / 10)
	
	pa_pitch.append(pitch_type)
	pitcherapitches.append(pa_pitch)
	pitchnum = pitchnum+1
	print(pitcherapitches)

pitchera["bullpen"] = pitcherapitches
print(pitchera)