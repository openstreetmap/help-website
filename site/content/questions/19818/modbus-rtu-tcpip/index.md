+++
type = "question"
title = "Modbus RTU TCP/IP"
description = '''I am a field service technician and I am wanting to capture Modbus RTU TCP/IP polls and responses on a SCADA network. I have downloaded the wireshark program and I am testing it on our in house network. I have another machine polling across the network using mod bus rtu tcp/ip polls and a end device...'''
date = "2013-03-25T10:32:00Z"
lastmod = "2013-03-25T11:17:00Z"
weight = 19818
keywords = [ "modbus", "rtu", "tcp_ip" ]
aliases = [ "/questions/19818" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Modbus RTU TCP/IP](/questions/19818/modbus-rtu-tcpip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19818-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am a field service technician and I am wanting to capture Modbus RTU TCP/IP polls and responses on a SCADA network. I have downloaded the wireshark program and I am testing it on our in house network. I have another machine polling across the network using mod bus rtu tcp/ip polls and a end device is answering. I cannot see any of this communications going on.If I setup my machine to do the polling I can see the data request sent out and the data sent back from the end device.Am I missing something on the setup of winshark that is not allowing me to see the communications traffic of the other two devices?</p></div><div id="question-tags" class="tags-container tags">modbus rtu tcp_ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '13, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/271b71e9c89a71acb5693c62dc598ade?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gage%20Man&#39;s gravatar image" /><p>Gage Man<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gage Man has no accepted answers">0%</span></p></div></div><div id="comments-container-19818" class="comments-container"></div><div id="comment-tools-19818" class="comment-tools"></div><div class="clear"></div><div id="comment-19818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19819"></span>

<div id="answer-container-19819" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19819-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>First, make sure you are capturing in promiscuous mode, otherwise you will only see traffic to/from your PC. Promiscuous mode is set under Capture Options. It's enabled by default, so that is probably not the problem.</p><p>The cause of your problem is more likely that you are capturing on a switched network, so traffic between the two other systems is not transmitted out the switch port where your Wireshark PC is connected. See the Ethernet <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Capture Setup</a> page of the Wireshark wiki for information on how to capture on a switched Ethernet network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 11:17</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-19819" class="comments-container"></div><div id="comment-tools-19819" class="comment-tools"></div><div class="clear"></div><div id="comment-19819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

