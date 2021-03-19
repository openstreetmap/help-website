+++
type = "question"
title = "step by step explanation how to sniff data on serial channel on windows"
description = '''Hello, Can somebody publish a detailed step by step explanation how to sniff data on serial channel (rs 232 / rs 442 / rs 485) on windows? The PC already has internal rs232 ports and rs 442/rs485 card installed. If there is no need to have an external SW, it would be better. In addition, I have cust...'''
date = "2017-09-28T21:59:00Z"
lastmod = "2017-09-29T02:49:00Z"
weight = 63669
keywords = [ "sniffing", "serial" ]
aliases = [ "/questions/63669" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [step by step explanation how to sniff data on serial channel on windows](/questions/63669/step-by-step-explanation-how-to-sniff-data-on-serial-channel-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63669-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Can somebody publish a detailed step by step explanation how to sniff data on serial channel (rs 232 / rs 442 / rs 485) on windows?</p><p>The PC already has internal rs232 ports and rs 442/rs485 card installed.</p><p>If there is no need to have an external SW, it would be better.</p><p>In addition, I have custom dissector written in LUA that is attached to some UDP port. I'd like to use the same dissector over the captured RS data. How this could be done?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">sniffing serial</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '17, 21:59</strong></p><img src="https://secure.gravatar.com/avatar/b02c5dfff2049bed61dbced93bf455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMWE&#39;s gravatar image" /><p>BMWE<br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMWE has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '17, 22:12</p></div></div><div id="comments-container-63669" class="comments-container"></div><div id="comment-tools-63669" class="comment-tools"></div><div class="clear"></div><div id="comment-63669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63671"></span>

<div id="answer-container-63671" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63671-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at <a href="https://wiki.wireshark.org/CaptureSetup/NetworkMedia">the network media supported</a> the serial interface isn't one of them, so without some external means this may not be possible. USB can be captured, so serial data may be visible on that. Otherwise an extcap utility may be of help here.</p><p>So, without external support this won't be possible I'm afraid.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '17, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63671" class="comments-container"><span id="63676"></span><div id="comment-63676" class="comment"><div id="post-63676-score" class="comment-score"></div><div class="comment-text"><p>can you please elaborate on the full scenario and how to use extcap</p></div><div id="comment-63676-info" class="comment-info"><span class="comment-age">(29 Sep '17, 06:58)</span> BMWE</div></div><span id="63677"></span><div id="comment-63677" class="comment"><div id="post-63677-score" class="comment-score"></div><div class="comment-text"><p>Extcap is an interface specification that allows external applications to act as capture interfaces for Wireshark.</p><p>See the document <a href="https://github.com/wireshark/wireshark/blob/master/doc/README.extcap">here</a> for more info.</p></div><div id="comment-63677-info" class="comment-info"><span class="comment-age">(29 Sep '17, 07:13)</span> grahamb ♦</div></div></div><div id="comment-tools-63671" class="comment-tools"></div><div class="clear"></div><div id="comment-63671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63672"></span>

<div id="answer-container-63672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63672-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The way I've managed to capture serial data in the past has been to use an Ethernet to serial converter, e.g. A <a href="https://www.lantronix.com/products/uds1100-uds1100-poe/">Lantronix UDS1100</a> that presents a virtual serial port to the PC application but sends the traffic over Ethernet to the converter which is then connected to the serial device. Wireshark is then used to capture the Ethernet traffic and the serial protocol is seen running atop the transport protocol used by the converter, usually TCP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '17, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63672" class="comments-container"></div><div id="comment-tools-63672" class="comment-tools"></div><div class="clear"></div><div id="comment-63672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

