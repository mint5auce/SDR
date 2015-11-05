#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Wav To Raw Iq
# Generated: Thu Nov  5 22:42:09 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class wav_to_raw_iq(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Wav To Raw Iq")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Blocks
        ##################################################
        self.test_wav = blocks.wavfile_source("original.wav", False)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=2000000,
                decimation=44100,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_streams_to_stream_0 = blocks.streams_to_stream(gr.sizeof_float*1, 2)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 127)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "sample.raw", False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.test_wav, 1), (self.blocks_streams_to_stream_0, 1))
        self.connect((self.blocks_streams_to_stream_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.test_wav, 0), (self.blocks_streams_to_stream_0, 0))



if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = wav_to_raw_iq()
    tb.Start(True)
    tb.Wait()
