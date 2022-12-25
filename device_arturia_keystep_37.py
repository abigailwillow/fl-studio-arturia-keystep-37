# name=Arturia Keystep 37
# url=https://forum.image-line.com/viewtopic.php?f=1994&t=295188
# supportedDevices=Arturia Keystep 37
# version=1.0.0

import transport, general, mixer, midi

BUTTON_RECORD = 0x32
BUTTON_STOP = 0x33
BUTTON_PLAY = 0x36

def OnControlChange(event):
    event.handled = False
    if event.data1 == BUTTON_RECORD:
        print(f'{"Disabled" if transport.isRecording() else "Enabled"} recording')
        transport.record()
    elif event.data1 == BUTTON_STOP and event.data2 > 0:
        print('Stopped playback')
        transport.stop()
    elif event.data1 == BUTTON_PLAY and event.data2 > 0:
        print(f'{"Paused" if transport.isPlaying() else "Started"} playback')
        transport.start()
    event.handled = True