from scamp import Session, Clock
s = Session()

piano = s.new_part("piano")
# trombone = s.new_part("trombone")


# When a function is forked, it is run on a child clock of the process forking it.
# This child clock can be passed as the first argument and then manipulated.
def trumpet_part(clock: Clock):
    # play eighth notes for three beats
    while s.beat() < 3:
        piano.play_note(72, 1, 0.5)

    # tell the clock for this child process to slow down to 1/2 speed over six beats in the parent process
    # metric_phase_target of 0 ensures that we reach that we land perfectly on a beat
    clock.set_rate_target(0.5, 6, duration_units="time",
                          metric_phase_target=0)

    # keep playing eighth notes until 12 beats pass in the parent session
    while s.beat() < 12:
        piano.play_note(72, 1, 0.5)


# Have the session as a whole speed up to 100 BPM over the first nine beats
s.set_tempo_target(100, 9)
# Fork the trumpet part as a child process. It will be influenced both by its own tempo and that of the session
# s.fork(trumpet_part)
# s.start_transcribing()
# Play quarter notes for 12 beats
# while s.beat() < 12:
for x in range(5):
    for note in [60, 64, 67, 72]:
        piano.play_note(note, 1, 0.05)
    piano.play_note(64, 1, 0.3)

# Stop recording and show the result
# performance = s.stop_transcribing()
# performance.to_score(time_signature="3/4").show()
