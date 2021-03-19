+++
type = "question"
title = "Malformed Packet GSM-SIM 11.11"
description = '''I am seeing a &quot;Malformed Packet&quot; or an incorrect GSMTAP packet,  while i am sending a GSM-SIM 11.11 packet over SIMtrace. I am generating the packet and I think it is valid. I am thinking that the problem is is caused because SIMtrace is using the gsmtap port 4729 and wireshark is waiting to see a G...'''
date = "2014-06-30T05:06:00Z"
lastmod = "2014-06-30T07:53:00Z"
weight = 34286
keywords = [ "simtrace", "gsm", "packet", "malformed", "sim" ]
aliases = [ "/questions/34286" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed Packet GSM-SIM 11.11](/questions/34286/malformed-packet-gsm-sim-1111)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34286-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am seeing a "Malformed Packet" or an incorrect GSMTAP packet, while i am sending a GSM-SIM 11.11 packet over SIMtrace. I am generating the packet and I think it is valid. I am thinking that the problem is is caused because SIMtrace is using the gsmtap port 4729 and wireshark is waiting to see a GSMTAP packet, so maybe it is expecting a different lenght. I would like to learn what is wrong with the packets</p><p>I have an example on the pcap here: <a href="https://www.cloudshark.org/captures/437b9d6bf107">https://www.cloudshark.org/captures/437b9d6bf107</a></p><p>Thanks for any ideas!</p></div><div id="question-tags" class="tags-container tags">simtrace gsm packet malformed sim</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '14, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/4d77eb980b48d40beb2a675ecad4a904?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mozbery&#39;s gravatar image" /><p>mozbery<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mozbery has no accepted answers">0%</span></p></div></div><div id="comments-container-34286" class="comments-container"></div><div id="comment-tools-34286" class="comment-tools"></div><div class="clear"></div><div id="comment-34286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34289"></span>

<div id="answer-container-34289" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34289-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It seems like your tool is sending the decoding of the SIM command as plain text, which is definitely not what Wireshark (and the GSMTAP dissector) is expecting (we can see the decoding of the APDU in the ASCII part of the byte panel, while it should be an hex dump of the GSMTAP protocol). I guess you must be using the wrong command line when launching SIMtrace, and should ask for help on the osmocom mailing list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '14, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-34289" class="comments-container"></div><div id="comment-tools-34289" class="comment-tools"></div><div class="clear"></div><div id="comment-34289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

