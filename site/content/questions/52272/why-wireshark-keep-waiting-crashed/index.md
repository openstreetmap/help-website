+++
type = "question"
title = "why wireshark keep waiting, crashed?"
description = '''Problem description:  Wireshark(v2.0.1) crashed (a delay circle keep waiting there!) when communicating with 6 USB2Ether cards at the same time. why? Reception hardware/software devices description:  USB HUB: ORICO P10-U3(10 ports USB3.0 HUB), 1 pc  USB2Ether: UGREEN 20256(USB3.0 to RJ45 Ethernet ca...'''
date = "2016-05-05T23:41:00Z"
lastmod = "2016-05-05T23:41:00Z"
weight = 52272
keywords = [ "wireshark_crashed", "wireshark" ]
aliases = [ "/questions/52272" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [why wireshark keep waiting, crashed?](/questions/52272/why-wireshark-keep-waiting-crashed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52272-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Problem description: Wireshark(v2.0.1) crashed (a delay circle keep waiting there!) when communicating with 6 USB2Ether cards at the same time. why?</p><p>Reception hardware/software devices description:<br />
USB HUB: ORICO P10-U3(10 ports USB3.0 HUB), 1 pc<br />
USB2Ether: UGREEN 20256(USB3.0 to RJ45 Ethernet card), 6 pcs<br />
Wireshark: v2.0.1 (crashed!!!)</p><p>Transmission hardware devices description:<br />
USB HUB: ORICO P10-U3(10 ports USB3.0 HUB), 1 pc<br />
USB2Ether: UGREEN 20256(USB3.0 to RJ45 Ethernet card), 6 pcs<br />
Ostinato: version 0.7.1</p><p>Operation: Ostinato send 1 ether frame each for 6 channels, Wireshark monitor frame.</p></div><div id="question-tags" class="tags-container tags">wireshark_crashed wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '16, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/89cba64d94a054b319343cf4223f86ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="titron&#39;s gravatar image" /><p>titron<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="titron has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '16, 23:47</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></br></p></div></div><div id="comments-container-52272" class="comments-container"><span id="52274"></span><div id="comment-52274" class="comment"><div id="post-52274-score" class="comment-score"></div><div class="comment-text"><ul><li><p>does Wireshark freeze immediately after you start the capture or only when the first frame arrives?</p></li><li><p>what happens if you run <code>tshark -i interface1 -i interface2 -i interface3 ...</code> from command line, instead of Wireshark?</p></li><li><p>what happens if you run <code>dumpcap -i interface1 -i interface2 -i interface3 ... -w output_file.pcapng</code> from command line, instead of Wireshark?</p></li><li><p>as 2.0.1 seems to me too fresh to be part of some distribution, can you try the same with the most current one - 2.0.3?</p></li></ul></div><div id="comment-52274-info" class="comment-info"><span class="comment-age">(05 May '16, 23:57)</span> sindy</div></div></div><div id="comment-tools-52272" class="comment-tools"></div><div class="clear"></div><div id="comment-52272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

