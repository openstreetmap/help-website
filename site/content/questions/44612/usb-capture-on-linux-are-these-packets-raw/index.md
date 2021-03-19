+++
type = "question"
title = "USB capture on Linux: Are these packets raw?"
description = '''I have some packets like this one, captured from /dev/usbmon*: Frame 46199: 64 bytes on wire (512 bits), 64 bytes captured (512 bits) on interface 4  Interface id: 4 (usbmon5)  Encapsulation type: USB packets with Linux header and padding (115)  Arrival Time: Jul 27, 2015 22:29:15.245268000 EDT  [Ti...'''
date = "2015-07-29T17:44:00Z"
lastmod = "2015-07-29T17:44:00Z"
weight = 44612
keywords = [ "usb", "usbmon" ]
aliases = [ "/questions/44612" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [USB capture on Linux: Are these packets raw?](/questions/44612/usb-capture-on-linux-are-these-packets-raw)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44612-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have some packets like this one, captured from <code>/dev/usbmon*</code>:</p><pre><code>Frame 46199: 64 bytes on wire (512 bits), 64 bytes captured (512 bits) on interface 4
    Interface id: 4 (usbmon5)
    Encapsulation type: USB packets with Linux header and padding (115)
    Arrival Time: Jul 27, 2015 22:29:15.245268000 EDT
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1438050555.245268000 seconds
    [Time delta from previous captured frame: 0.001355000 seconds]
    [Time delta from previous displayed frame: 0.002407000 seconds]
    [Time since reference or first frame: 41.736743000 seconds]
    Frame Number: 46199
    Frame Length: 64 bytes (512 bits)
    Capture Length: 64 bytes (512 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: usb]
USB URB
    URB id: 0xffff8802bb061b40
    URB type: URB_SUBMIT (&#39;S&#39;)
    URB transfer type: URB_BULK (0x03)
    Endpoint: 0x85, Direction: IN
        1... .... = Direction: IN (1)
        .000 0101 = Endpoint value: 5
    Device: 50
    URB bus id: 5
    Device setup request: not relevant (&#39;-&#39;)
    Data: not present (&#39;&lt;&#39;)
    URB sec: 1438050555
    URB usec: 245268
    URB status: Operation now in progress (-EINPROGRESS) (-115)
    URB length [bytes]: 18944
    Data length [bytes]: 0
    [Response in: 55738]
    [bInterfaceClass: Vendor Specific (0xff)]
    Unused Setup Header
    Interval: 0
    Start frame: 0
    Copy of Transfer Flags: 0x00000200
    Number of ISO descriptors: 0
0000   40 1b 06 bb 02 88 ff ff 53 03 85 32 05 00 2d 3c  @.......S..2..-&lt;
0010   fb e8 b6 55 00 00 00 00 14 be 03 00 8d ff ff ff  ...U............
0020   00 4a 00 00 00 00 00 00 00 00 00 00 00 00 00 00  .J..............
0030   00 00 00 00 00 00 00 00 00 02 00 00 00 00 00 00  ................</code></pre><p>What I'm wondering is if this info/hex dump is the raw data that was sent over the wire, or if the kernel has added/processed some fields? In particular I notice many of the packets have an URB Length of 18944 (0x4A00) but a data length of 0 - is this normal?</p></div><div id="question-tags" class="tags-container tags">usb usbmon</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '15, 17:44</strong></p><img src="https://secure.gravatar.com/avatar/f2830d72f086d2cdc8ac5b4f1333c3cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RenaKunisaki&#39;s gravatar image" /><p>RenaKunisaki<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RenaKunisaki has no accepted answers">0%</span></p></div></div><div id="comments-container-44612" class="comments-container"></div><div id="comment-tools-44612" class="comment-tools"></div><div class="clear"></div><div id="comment-44612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

