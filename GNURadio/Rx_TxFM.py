#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: captain
# GNU Radio version: 3.10.5.1

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore



from gnuradio import qtgui

class TxRx_FM(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "TxRx_FM")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.vol = vol = -2
        self.samp_rate = samp_rate = 48e3
        self.gol = gol = 45
        self.fol = fol = 142e6
        self.f_factor = f_factor = 40
        self.Gain_TxRx_A1 = Gain_TxRx_A1 = 45
        self.Gain_RF_Out = Gain_RF_Out = 23
        self.Gain = Gain = 78
        self.Frec_TxRx_A1 = Frec_TxRx_A1 = 140e6
        self.Frec_Tomada = Frec_Tomada = 103.5e6
        self.Frec_RF_Out = Frec_RF_Out = 26e6

        ##################################################
        # Blocks
        ##################################################

        self._vol_range = Range(-40, 10, 1, -2, 200)
        self._vol_win = RangeWidget(self._vol_range, self.set_vol, "Volumen", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._vol_win)
        self.nb = Qt.QTabWidget()
        self.nb_widget_0 = Qt.QWidget()
        self.nb_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.nb_widget_0)
        self.nb_grid_layout_0 = Qt.QGridLayout()
        self.nb_layout_0.addLayout(self.nb_grid_layout_0)
        self.nb.addTab(self.nb_widget_0, 'Spectrum RF Input')
        self.nb_widget_1 = Qt.QWidget()
        self.nb_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.nb_widget_1)
        self.nb_grid_layout_1 = Qt.QGridLayout()
        self.nb_layout_1.addLayout(self.nb_grid_layout_1)
        self.nb.addTab(self.nb_widget_1, 'Spectrum RF Output')
        self.top_layout.addWidget(self.nb)
        self._gol_range = Range(0, 50, 1, 45, 200)
        self._gol_win = RangeWidget(self._gol_range, self.set_gol, "Ganancia oscilador local", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._gol_win)
        self._fol_range = Range(80e6, 480e6, 0.1e6, 142e6, 200)
        self._fol_win = RangeWidget(self._fol_range, self.set_fol, "Frecuencia de oscilador local", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fol_win)
        self._Gain_TxRx_A1_range = Range(0, 80, 1, 45, 200)
        self._Gain_TxRx_A1_win = RangeWidget(self._Gain_TxRx_A1_range, self.set_Gain_TxRx_A1, "Ganancia Tx", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Gain_TxRx_A1_win)
        self._Gain_range = Range(0, 80, 1, 78, 200)
        self._Gain_win = RangeWidget(self._Gain_range, self.set_Gain, "Ganancia RF Radio", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Gain_win)
        self._Frec_TxRx_A1_range = Range(80e6, 480e6, 0.1e6, 140e6, 200)
        self._Frec_TxRx_A1_win = RangeWidget(self._Frec_TxRx_A1_range, self.set_Frec_TxRx_A1, "Frecuencia Tx", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Frec_TxRx_A1_win)
        self._Frec_Tomada_range = Range(80e6, 480e6, 0.1e6, 103.5e6, 200)
        self._Frec_Tomada_win = RangeWidget(self._Frec_Tomada_range, self.set_Frec_Tomada, "Frecuencia Rx Radio", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Frec_Tomada_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("serial=30C2C26", '')),
            uhd.stream_args(
                cpu_format="fc32",
                otw_format="sc12",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_clock_source('external', 0)
        self.uhd_usrp_source_0.set_samp_rate((samp_rate*f_factor))
        # No synchronization enforced.

        self.uhd_usrp_source_0.set_center_freq(Frec_Tomada+250000, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_gain(Gain, 0)
        self.uhd_usrp_sink_1_0_0 = uhd.usrp_sink(
            ",".join(("serial=30B584D", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_1_0_0.set_clock_source('internal', 0)
        self.uhd_usrp_sink_1_0_0.set_samp_rate((samp_rate*f_factor))
        self.uhd_usrp_sink_1_0_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_sink_1_0_0.set_center_freq(fol, 0)
        self.uhd_usrp_sink_1_0_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_1_0_0.set_gain(gol, 0)
        self.uhd_usrp_sink_1_0 = uhd.usrp_sink(
            ",".join(("serial=30C2C26", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_1_0.set_clock_source('internal', 0)
        self.uhd_usrp_sink_1_0.set_samp_rate((samp_rate*f_factor))
        self.uhd_usrp_sink_1_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_sink_1_0.set_center_freq(Frec_TxRx_A1, 0)
        self.uhd_usrp_sink_1_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_1_0.set_gain(Gain_TxRx_A1, 0)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            Frec_TxRx_A1, #fc
            (samp_rate*f_factor), #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(True)
        self.qtgui_freq_sink_x_0_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.qwidget(), Qt.QWidget)
        self.nb_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            Frec_Tomada, #fc
            (samp_rate*f_factor), #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.nb_layout_0.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            5,
            firdes.low_pass(
                1,
                (samp_rate*f_factor/8),
                15e3,
                3e3,
                window.WIN_HAMMING,
                6.76))
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(4, firdes.low_pass(1,samp_rate*f_factor,140e3,10e3), (-250e3), (samp_rate*f_factor))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, firdes.low_pass(1,samp_rate*f_factor,135e3,10e3), (-250e3), (samp_rate*f_factor))
        self.dc_blocker_xx_0_0 = filter.dc_blocker_cc(32, True)
        self.dc_blocker_xx_0 = filter.dc_blocker_cc(32, True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff((10**(vol/10)))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=(samp_rate*f_factor/4),
        	audio_decimation=2,
        )
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self._Gain_RF_Out_range = Range(0, 80, 1, 23, 200)
        self._Gain_RF_Out_win = RangeWidget(self._Gain_RF_Out_range, self.set_Gain_RF_Out, "Ganancia RF Out", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Gain_RF_Out_win)
        self._Frec_RF_Out_range = Range(25e6, 500e6, 0.1e6, 26e6, 200)
        self._Frec_RF_Out_win = RangeWidget(self._Frec_RF_Out_range, self.set_Frec_RF_Out, "Frecuencia RF Out", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Frec_RF_Out_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.uhd_usrp_sink_1_0_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.uhd_usrp_sink_1_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.dc_blocker_xx_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TxRx_FM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_vol(self):
        return self.vol

    def set_vol(self, vol):
        self.vol = vol
        self.blocks_multiply_const_vxx_0.set_k((10**(self.vol/10)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1,self.samp_rate*self.f_factor,135e3,10e3))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(firdes.low_pass(1,self.samp_rate*self.f_factor,140e3,10e3))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, (self.samp_rate*self.f_factor/8), 15e3, 3e3, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Frec_Tomada, (self.samp_rate*self.f_factor))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Frec_TxRx_A1, (self.samp_rate*self.f_factor))
        self.uhd_usrp_sink_1_0.set_samp_rate((self.samp_rate*self.f_factor))
        self.uhd_usrp_sink_1_0_0.set_samp_rate((self.samp_rate*self.f_factor))
        self.uhd_usrp_source_0.set_samp_rate((self.samp_rate*self.f_factor))

    def get_gol(self):
        return self.gol

    def set_gol(self, gol):
        self.gol = gol
        self.uhd_usrp_sink_1_0_0.set_gain(self.gol, 0)
        self.uhd_usrp_sink_1_0_0.set_gain(self.gol, 1)

    def get_fol(self):
        return self.fol

    def set_fol(self, fol):
        self.fol = fol
        self.uhd_usrp_sink_1_0_0.set_center_freq(self.fol, 0)
        self.uhd_usrp_sink_1_0_0.set_center_freq(self.fol, 1)

    def get_f_factor(self):
        return self.f_factor

    def set_f_factor(self, f_factor):
        self.f_factor = f_factor
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.low_pass(1,self.samp_rate*self.f_factor,135e3,10e3))
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(firdes.low_pass(1,self.samp_rate*self.f_factor,140e3,10e3))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, (self.samp_rate*self.f_factor/8), 15e3, 3e3, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Frec_Tomada, (self.samp_rate*self.f_factor))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Frec_TxRx_A1, (self.samp_rate*self.f_factor))
        self.uhd_usrp_sink_1_0.set_samp_rate((self.samp_rate*self.f_factor))
        self.uhd_usrp_sink_1_0_0.set_samp_rate((self.samp_rate*self.f_factor))
        self.uhd_usrp_source_0.set_samp_rate((self.samp_rate*self.f_factor))

    def get_Gain_TxRx_A1(self):
        return self.Gain_TxRx_A1

    def set_Gain_TxRx_A1(self, Gain_TxRx_A1):
        self.Gain_TxRx_A1 = Gain_TxRx_A1
        self.uhd_usrp_sink_1_0.set_gain(self.Gain_TxRx_A1, 0)
        self.uhd_usrp_source_0.set_gain(self.Gain_TxRx_A1, 1)

    def get_Gain_RF_Out(self):
        return self.Gain_RF_Out

    def set_Gain_RF_Out(self, Gain_RF_Out):
        self.Gain_RF_Out = Gain_RF_Out

    def get_Gain(self):
        return self.Gain

    def set_Gain(self, Gain):
        self.Gain = Gain
        self.uhd_usrp_source_0.set_gain(self.Gain, 0)

    def get_Frec_TxRx_A1(self):
        return self.Frec_TxRx_A1

    def set_Frec_TxRx_A1(self, Frec_TxRx_A1):
        self.Frec_TxRx_A1 = Frec_TxRx_A1
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.Frec_TxRx_A1, (self.samp_rate*self.f_factor))
        self.uhd_usrp_sink_1_0.set_center_freq(self.Frec_TxRx_A1, 0)
        self.uhd_usrp_source_0.set_center_freq(self.Frec_TxRx_A1, 1)

    def get_Frec_Tomada(self):
        return self.Frec_Tomada

    def set_Frec_Tomada(self, Frec_Tomada):
        self.Frec_Tomada = Frec_Tomada
        self.qtgui_freq_sink_x_0.set_frequency_range(self.Frec_Tomada, (self.samp_rate*self.f_factor))
        self.uhd_usrp_source_0.set_center_freq(self.Frec_Tomada+250000, 0)

    def get_Frec_RF_Out(self):
        return self.Frec_RF_Out

    def set_Frec_RF_Out(self, Frec_RF_Out):
        self.Frec_RF_Out = Frec_RF_Out




def main(top_block_cls=TxRx_FM, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
