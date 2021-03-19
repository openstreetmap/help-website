+++
type = "question"
title = "Unknown DTAP message types in trace (MM type 3, RR type 1 and CC type 0)"
description = '''Greetings! Hoping someone can help me. In a trace from a customer, I have three DTAP messages that are giving Wireshark grief in trying to dissect them. I&#x27;ve put in bold the protocol discriminator octet and the message type octet: GSM A-I/F DTAP - Unknown DTAP Message Type (0x03)  Protocol Discrimin...'''
date = "2015-08-14T09:22:00Z"
lastmod = "2015-08-14T09:22:00Z"
weight = 45115
keywords = [ "2g", "gsm", "ranap", "dtap" ]
aliases = [ "/questions/45115" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unknown DTAP message types in trace (MM type 3, RR type 1 and CC type 0)](/questions/45115/unknown-dtap-message-types-in-trace-mm-type-3-rr-type-1-and-cc-type-0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45115-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings! Hoping someone can help me. In a trace from a customer, I have three DTAP messages that are giving Wireshark grief in trying to dissect them. I've put in bold the protocol discriminator octet and the message type octet:</p><pre><code>GSM A-I/F DTAP - Unknown DTAP Message Type (0x03)
    Protocol Discriminator: Mobility Management messages (5)
        .... 0101 = Protocol discriminator: Mobility Management messages (0x05)
        0000 .... = Skip Indicator: No indication of selected PLMN (0)
    00.. .... = Sequence number: 0
    ..00 0011 = DTAP Mobility Management Message Type: Unknown (0x03)

0000  00 50 56 be 6e 10 00 13 5f e1 d4 00 08 00 45 00   .PV.n..._.....E.
0010  00 50 00 00 40 00 36 11 b6 f9 0a 4a 00 d7 ac 1c   [email protected]
0020  d6 66 ca ce 12 79 00 3c f5 3e 02 04 01 00 82 00   .f...y.&lt;.&gt;......
0030  00 00 00 15 52 7b 07 00 00 00 03 00 fd **05 03** 15   ....R{..........
0040  10 36 00 b0 28 43 80 17 c0 87 ff f2 b8 41 4a 02   .6..(C.......AJ.
0050  04 18 38 02 80 a1 98 1a ba c5 32 00 00 00         ..8.......2...

GSM A-I/F DTAP - Unknown DTAP Message Type (0x01)
    Protocol Discriminator: Radio Resources Management messages (6)
        .... 0110 = Protocol discriminator: Radio Resources Management messages (0x06)
        0000 .... = Skip Indicator: No indication of selected PLMN (0)
    DTAP Radio Resources Management Message Type: Unknown (0x01)

0000  00 50 56 be 6e 10 00 13 5f e1 d4 00 08 00 45 00   .PV.n..._.....E.
0010  00 38 00 00 40 00 36 11 b7 11 0a 4a 00 d7 ac 1c   [email protected]
0020  d6 66 ca ce 12 79 00 24 e1 73 02 04 01 00 82 00   .f...y.$.s......
0030  00 00 00 15 52 7b 07 00 00 00 03 00 fd **06 01** a2   ....R{..........
0040  e7 fc 23 0b c8 00                                 ..#...

GSM A-I/F DTAP - Unknown DTAP Message Type (0x00)
    Protocol Discriminator: Call Control; call related SS messages (3)
        .... 0011 = Protocol discriminator: Call Control; call related SS messages (0x03)
        0... .... = TI flag: allocated by sender
        .000 .... = TIO: 0
    00.. .... = Sequence number: 0
    ..00 0000 = DTAP Call Control Message Type: Unknown (0x00)

0000  00 50 56 be 6e 10 00 13 5f e1 d4 00 08 00 45 00   .PV.n..._.....E.
0010  00 3d 00 00 40 00 36 11 b7 0c 0a 4a 00 d7 ac 1c   [email protected]
0020  d6 66 ca ce 12 79 00 29 7b 55 02 04 01 00 82 00   .f...y.){U......
0030  00 00 00 15 52 7b 07 00 00 00 03 00 fd **03 00** 31   ....R{.........1
0040  4a 00 99 ff 20 80 0b 10 13 01 18                  J... ......</code></pre><p>I'm not inclined to think this is interference, because these three messages come up regularly and I don't think a mangled message would make it that far up the protocol stack.</p><p>Any help is appreciated!</p></div><div id="question-tags" class="tags-container tags">2g gsm ranap dtap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '15, 09:22</strong></p><img src="https://secure.gravatar.com/avatar/d6872b1cae1da5fcd92837a89d05942c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tiger762&#39;s gravatar image" /><p>tiger762<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tiger762 has no accepted answers">0%</span></p></div></div><div id="comments-container-45115" class="comments-container"></div><div id="comment-tools-45115" class="comment-tools"></div><div class="clear"></div><div id="comment-45115-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

