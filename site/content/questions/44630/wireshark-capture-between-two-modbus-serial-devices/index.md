+++
type = "question"
title = "Wireshark capture between two Modbus Serial devices"
description = '''How to setup wireshark capture between two Serial Modbus Master/slave Devices? - Modbus RTU Protocol.'''
date = "2015-07-30T05:51:00Z"
lastmod = "2015-07-30T07:07:00Z"
weight = 44630
keywords = [ "rtu" ]
aliases = [ "/questions/44630" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark capture between two Modbus Serial devices](/questions/44630/wireshark-capture-between-two-modbus-serial-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44630-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to setup wireshark capture between two Serial Modbus Master/slave Devices? - Modbus RTU Protocol.</p></div><div id="question-tags" class="tags-container tags">rtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/e8b2515cc6a4f95cf533f3800fa6cb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Narasimhan%20Ragunathan&#39;s gravatar image" /><p>Narasimhan R...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Narasimhan Ragunathan has no accepted answers">0%</span></p></div></div><div id="comments-container-44630" class="comments-container"></div><div id="comment-tools-44630" class="comment-tools"></div><div class="clear"></div><div id="comment-44630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44636"></span>

<div id="answer-container-44636" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44636-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Out of the box it can't. The usual way to monitor such traffic is to convert the serial traffic to Ethernet using a device server such as these <a href="http://www.lantronix.com/device-networking/external-device-servers/eds1100_eds2100.html">Lantronix</a> devices (there are other similar, cheaper, devices available). You can then use one device at each end and use a tap or switch with port mirroring (or even a hub) in between each end and then capture the traffic.</p><p>If the Modbus master is on a PC, the application can often be configured to use TCP/IP instead of serial, in this case you only need one device server at the Modbus slave end.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jul '15, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-44636" class="comments-container"></div><div id="comment-tools-44636" class="comment-tools"></div><div class="clear"></div><div id="comment-44636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

