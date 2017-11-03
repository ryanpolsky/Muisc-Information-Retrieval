# Created by Ryan Polsky on 10/31/17
# Code snippets taken from http://musicinformationretrieval.com/beat_tracking.html


import numpy, scipy
import librosa, librosa.display
#from ADTLib.models import ADTBDRNN
#from ipywidgets import interact

def getBeatInfo(song_name):
    x, sr = librosa.load('audio/' + song_name)
    tempo, beat_times = librosa.beat.beat_track(x, sr=sr, start_bpm=60, units='time')
    return (tempo, beat_times)

def getOnsetTimes(song_name,levels):
    x, sr = librosa.load('audio/' + song_name)
    hop_length = 256
    onset_envelope = librosa.onset.onset_strength(x, sr=sr, hop_length=hop_length)
    N = len(x)
    T = N / float(sr)
    t = numpy.linspace(0, T, len(onset_envelope))
    peaks = []
    for i in range (1,levels):
        samps = 20 * i*i
        onset_frames = librosa.util.peak_pick(onset_envelope, samps, samps, samps, samps, 0.5, samps)
        onset_times = []
        for index in onset_frames:
            onset_times.append(t[index])
        peaks.append(onset_times)


    return peaks


# def getDrumTracking(song_name):
#     x, fs = librosa.load('audio/' + song_name)
#     onset_times, onset_types = ADTBDRNN(['audio/' + song_name])

if __name__ == '__main__':
    # x, sr = librosa.load('audio/stretchedBreak2.wav')

    # tempo, beat_times = getBeatInfo('stretchedBreak2.wav')
    # print (tempo)
    # print(beat_times)

    peaks = getOnsetTimes('background-music-aac.wav', 8)
    for peakList in peaks:
        print(len(peakList))
        print(peakList)
