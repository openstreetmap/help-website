+++
type = "question"
title = "How to make wireshark thinking that 3GPP T-PDU is uplink?"
description = '''I try to decode the following 3GPP SMS-SUBMIT T-PDU, using gsm_sms dissector: 01000B811192979297F2000010ECF71B2E0E8FD7A076793E0F9FCB But wireshark thinks, that it is downlink tpdu, and decodes is as SMS-SUBMIT-REPORT. Of course, there is a way to encapsulate this T-PDU into some higher-level protoco...'''
date = "2016-12-23T07:09:00Z"
lastmod = "2016-12-23T07:16:00Z"
weight = 58321
keywords = [ "gsm_sms" ]
aliases = [ "/questions/58321" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to make wireshark thinking that 3GPP T-PDU is uplink?](/questions/58321/how-to-make-wireshark-thinking-that-3gpp-t-pdu-is-uplink)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58321-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I try to decode the following 3GPP SMS-SUBMIT T-PDU, using gsm_sms dissector: 01000B811192979297F2000010ECF71B2E0E8FD7A076793E0F9FCB But wireshark thinks, that it is downlink tpdu, and decodes is as SMS-SUBMIT-REPORT. Of course, there is a way to encapsulate this T-PDU into some higher-level protocol by adding fake header, and that protocol will call gsm_sms dissector with proper parameter. But for me is interesting, is there a way to put some parameter to text2pcap to make it thinking that this is uplink message? I use text2pcap in the following way: echo "000000 01 00 0B 81 11 92 97 92 97 F2 00 00 10 EC F7 1B 2E 0E 8F D7 A0 76 79 3E 0F 9F CB" &gt; tpdu.txt text2pcap -l 151 tpdu.txt tpdu.pcapng wireshark tpdu.pcapng And I see that it is decoded as SMS-SUBMIT REPORT, i.e. in wrong way. What I am asking is some parameter that can be used with text2pcap allowing to make it thinking that direction is uplink.</p></div><div id="question-tags" class="tags-container tags">gsm_sms</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '16, 07:09</strong></p><img src="https://secure.gravatar.com/avatar/db266be21c74d3df6288ca9ece91350e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sviat&#39;s gravatar image" /><p>Sviat<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sviat has no accepted answers">0%</span></p></div></div><div id="comments-container-58321" class="comments-container"></div><div id="comment-tools-58321" class="comment-tools"></div><div class="clear"></div><div id="comment-58321-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58322"></span>

<div id="answer-container-58322" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58322-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Sviat,</p><p>use the <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html">-D and -n text2pcap options</a> and before the packet dump use:</p><pre><code>I for an uplink packet (your case)
O for an downlink packet</code></pre><p>It will give the following decoding:</p><pre><code>GSM SMS TPDU (GSM 03.40) SMS-SUBMIT
0... .... = TP-RP: TP Reply Path parameter is not set in this SMS SUBMIT/DELIVER
.0.. .... = TP-UDHI: The TP UD field contains only the short message
..0. .... = TP-SRR: A status report is not requested
...0 0... = TP-VPF: TP-VP field not present (0)
.... .0.. = TP-RD: Instruct SC to accept duplicates
.... ..01 = TP-MTI: SMS-SUBMIT (1)
TP-MR: 0
TP-Destination-Address - (11297929792)
    Length: 11 address digits
    1... .... = Extension: No extension
    .000 .... = Type of number: Unknown (0)
    .... 0001 = Numbering plan: ISDN/telephone (E.164/E.163) (1)
    TP-DA Digits: 11297929792
TP-PID: 0
    00.. .... = Defines formatting for subsequent bits: 0x0
    ..0. .... = Telematic interworking: no telematic interworking, but SME-to-SME protocol
    ...0 0000 = The SM-AL protocol being used between the SME and the MS: 0
TP-DCS: 0
    00.. .... = Coding Group Bits: General Data Coding indication (0)
    Special case, GSM 7 bit default alphabet
TP-User-Data-Length: (16) depends on Data-Coding-Scheme
TP-User-Data
    SMS text: loopback message</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '16, 07:16</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-58322" class="comments-container"><span id="58334"></span><div id="comment-58334" class="comment"><div id="post-58334-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, it works perfectly!</p></div><div id="comment-58334-info" class="comment-info"><span class="comment-age">(26 Dec '16, 02:46)</span> Sviat</div></div><span id="58337"></span><div id="comment-58337" class="comment"><div id="post-58337-score" class="comment-score"></div><div class="comment-text"><p>If my answer solved your issue, do not forget to accept it: it will be helpful for anyone searching for an equivalent answer. See the FAQ for details.</p></div><div id="comment-58337-info" class="comment-info"><span class="comment-age">(26 Dec '16, 06:11)</span> Pascal Quantin</div></div></div><div id="comment-tools-58322" class="comment-tools"></div><div class="clear"></div><div id="comment-58322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

