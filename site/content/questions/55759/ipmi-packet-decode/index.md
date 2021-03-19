+++
type = "question"
title = "IPMI packet decode"
description = '''I&#x27;m trying to decode an IPMI packet. I presently don&#x27;t have a means to get the packet into WireShark, because my computer does not yet have a working I2C port, so the packet below came from my logic analyzer. 20 10 D0 EE 00 02 04 F0 00 6F A0 80 C0 CD This packet was sent by the system processor to t...'''
date = "2016-09-22T13:08:00Z"
lastmod = "2016-09-22T13:23:00Z"
weight = 55759
keywords = [ "ipmi1547" ]
aliases = [ "/questions/55759" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IPMI packet decode](/questions/55759/ipmi-packet-decode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55759-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to decode an IPMI packet. I presently don't have a means to get the packet into WireShark, because my computer does not yet have a working I2C port, so the packet below came from my logic analyzer.</p><p>20 10 D0 EE 00 02 04 F0 00 6F A0 80 C0 CD</p><p>This packet was sent by the system processor to the backplane.</p><p>If someone could please help me by telling me what the message above means byte-by-byte, I would be very grateful.</p></div><div id="question-tags" class="tags-container tags">ipmi1547</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '16, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/a572cdae9835fe8d8a23fc95b95d4f3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CLinquist&#39;s gravatar image" /><p>CLinquist<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CLinquist has no accepted answers">0%</span></p></div></div><div id="comments-container-55759" class="comments-container"></div><div id="comment-tools-55759" class="comment-tools"></div><div class="clear"></div><div id="comment-55759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55761"></span>

<div id="answer-container-55761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55761-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark decodes your payload as follows:</p><pre><code>Intelligent Platform Management Bus
    Target Address: 0x20
    Target LUN: 0x00, NetFN: Sensor/Event Request (0x04)
        NetFn: Sensor/Event Request (0x04)
        .... ..00 = Target LUN: 0x0
    Header Checksum: 0xd0 (correct)
    Source Address: 0xee
    Source LUN: 0x00, SeqNo: 0x00
        .... ..00 = Source LUN: 0x0
        0000 00.. = Sequence Number: 0x00
    Command: Platform Event (0x02)
    Data
        Event Message Revision: IPMI 1.5+ (0x04)
        Sensor Type: Hot Swap (ATCA) (0xf0)
        Sensor #: 0
        Event Dir/Type: 0x6f
            0... .... = Event Direction: Assertion event
            .110 1111 = Event/Reading type: Sensor-specific (0x6f)
        Event Data 1: 0xa0
            10.. .... = Byte 2: OEM code (0x02)
            ..10 .... = Byte 3: OEM code (0x02)
            .... 0000 = Offset: M0 - FRU Not Installed (0x00)
        Previous state/Cause
            1000 .... = Cause: Invalid Hardware Address Detected (0x8)
            .... 0000 = Previous state: M0 - FRU Not Installed (0x00)
        FRU Id: 192
    Data checksum: 0xcd (correct)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '16, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-55761" class="comments-container"><span id="55767"></span><div id="comment-55767" class="comment"><div id="post-55767-score" class="comment-score"></div><div class="comment-text"><p>Amazing, fantastic, and THANKS!</p><p>BTW: Where can I get the decoder for IPMI? My version seems to only handle Ethernet.</p></div><div id="comment-55767-info" class="comment-info"><span class="comment-age">(22 Sep '16, 15:41)</span> CLinquist</div></div><span id="55771"></span><div id="comment-55771" class="comment"><div id="post-55771-score" class="comment-score"></div><div class="comment-text"><p>The decoder is part of the standard distribution of Wireshark, you just need to know how to feed Wireshark with your messages and tell it how to dissect them.</p><p>One way (there may be others I don't know about) is the following:</p><p>Prepend your data with a single <code>0</code> followed by a space, so you'll get <code>0 20 10 D0 EE 00 02 04 F0 00 6F A0 80 C0 CD</code> and save the result to a text file with a blank line after it.</p><p>Then, use <code>File -&gt; Import from Hex Dump</code> in Wireshark to import the file, choosing <code>Encapsulation Type</code> <code>User0</code> (or any other <code>UserX</code> one if you already use <code>User0</code> for any other purpose), and the <code>No Dummy Header</code> option.</p><p>Then, in the packet dissection pane, right-click the yellow line saying <code>User encapsulation not handled...</code>, choose <code>Protocol Preferences-&gt;Encapsulations Table</code>, and insert a new line into the table - choose <code>UserX</code> depending on which encapsulation you have indicated above for the <code>DLT</code> column, and write <code>ipmi</code> to the <code>Protocol</code> column.</p><p>This way you tell Wireshark to start dissecting the imported frame as IPMI data with no lower layer.</p><p>More details regarding import from hex dump are in <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChIOImportSection.html">the documentation</a>. The graphical layout of the import window is a bit outdated there but the principle is described properly.</p></div><div id="comment-55771-info" class="comment-info"><span class="comment-age">(23 Sep '16, 00:44)</span> sindy</div></div></div><div id="comment-tools-55761" class="comment-tools"></div><div class="clear"></div><div id="comment-55761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

