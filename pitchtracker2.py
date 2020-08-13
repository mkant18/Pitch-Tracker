import statistics
pitchers = {
}

pitchera = {
	"Height" : (input("Enter Height(ft,inches): ") + "'"),
	"Weight" : (input('Enter Weight(lbs): ') + " lbs")
}

pitchnum = 0
input("Enter 'Go' to begin: ")
pitcherapitches = []
pitcheraq =[]

while (pitchnum < 3):
	pa_pitch = [input("Enter Velocity: "), input("Enter break: "), input("Enter location: ")]
	pa_pitch = list(map(int, pa_pitch))
	pitch_type = input("Enter Pitch Type (FB, CB, CH, SL): ")
	if pitch_type == 'FB':
		pitchq = (((pa_pitch[0] * 4) * 			(pa_pitch[1] * 2) * (pa_pitch[2] * 0.5)) / 10)
	elif pitch_type == 'CB':
		pitchq = (((pa_pitch[0] * 10) * 			(pa_pitch[1] * 5) * (pa_pitch[2] * 6)) / 10)
	elif pitch_type == 'CH':
		pitchq = (((pa_pitch[0] * 0.2) * (pa_pitch[1] * 6) * (pa_pitch[2] * 5)) / 10)
	elif pitch_type == 'SL':
		pitchq = (((pa_pitch[0] * 6) * (pa_pitch[1] * 6) * (pa_pitch[2] * 0.2)) / 10)
	
	pitcheraq.append(pitchq)
	pa_pitch.append(pitchq)
	pa_pitch.append(pitch_type)
	pitcherapitches.append(pa_pitch)
	pitchnum = pitchnum+1
	print(pitcherapitches)

gen_scorea = statistics.mean(pitcheraq)

bullpen = pitcherapitches
pitchera["bullpenq"] = pitcheraq
pitchers["Average Score"] = int(gen_scorea)
pitchers[input("Enter last name: ")] = pitchera
print(pitchers)