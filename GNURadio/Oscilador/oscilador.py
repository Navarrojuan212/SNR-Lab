#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: captain
# GNU Radio version: 3.10.4.0

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
from gnuradio import analog
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, GrRangeWidget
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
        self.samp_rate = samp_rate = 48e3
        self.gol = gol = 40
        self.fol = fol = 142e6
        self.f_factor = f_factor = 40

        ##################################################
        # Blocks
        ##################################################
        self._gol_range = Range(0, 80, 1, 40, 200)
        self._gol_win = GrRangeWidget(self._gol_range, self.set_gol, "Ganancia oscilador local", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._gol_win)
        self._fol_range = Range(80e6, 480e6, 0.1e6, 142e6, 200)
        self._fol_win = GrRangeWidget(self._fol_range, self.set_fol, "Frecuencia de oscilador local", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._fol_win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("serial=30B5874", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_sink_0.set_center_freq(fol, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(gol, 0)
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
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.uhd_usrp_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TxRx_FM")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_gol(self):
        return self.gol

    def set_gol(self, gol):
        self.gol = gol
        self.uhd_usrp_sink_0.set_gain(self.gol, 0)

    def get_fol(self):
        return self.fol

    def set_fol(self, fol):
        self.fol = fol
        self.uhd_usrp_sink_0.set_center_freq(self.fol, 0)

    def get_f_factor(self):
        return self.f_factor

    def set_f_factor(self, f_factor):
        self.f_factor = f_factor




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
