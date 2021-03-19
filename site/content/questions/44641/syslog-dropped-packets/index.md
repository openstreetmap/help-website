+++
type = "question"
title = "SysLog dropped packets"
description = '''Hello,  I am running an embedded controller with multiple threads and capturing events with SysLog and iprintf so in theory have identical messages generated over the net and the serial port. Ideally they should be the same. I placed a Wireshark readout alongside the serial readout, and saw that Wir...'''
date = "2015-07-30T09:26:00Z"
lastmod = "2015-08-03T02:37:00Z"
weight = 44641
keywords = [ "syslog", "udp", "packets", "dropped" ]
aliases = [ "/questions/44641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SysLog dropped packets](/questions/44641/syslog-dropped-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44641-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am running an embedded controller with multiple threads and capturing events with SysLog and iprintf so in theory have identical messages generated over the net and the serial port. Ideally they should be the same.</p><p>I placed a Wireshark readout alongside the serial readout, and saw that Wireshark had dropped a packet. Is there a limit to the rate at which SysLog messages are captured? I realize this is UDP so there may be dropped packets but its just a home network and have SNMP, SSDP,QUIC,SSDP going on. Is rate of SysLog generation or UDP corruption the most likely cause? Is there any way to make it more robust such as a mutex?</p><p>Thanks, Sam</p></div><div id="question-tags" class="tags-container tags">syslog udp packets dropped</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '15, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/683d81c0b9cff4fac2a396e04df5b51f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam%20Mallicoat&#39;s gravatar image" /><p>Sam Mallicoat<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam Mallicoat has no accepted answers">0%</span></p></div></div><div id="comments-container-44641" class="comments-container"></div><div id="comment-tools-44641" class="comment-tools"></div><div class="clear"></div><div id="comment-44641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44758"></span>

<div id="answer-container-44758" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44758-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a limit to the rate at which SysLog messages are captured?</p></blockquote><p>Yes, it depends on several parameters on your system (CPU speed, IO speed, etc.).</p><p><strong>HOWEVER</strong> you say, that you are sending the same syslog messages via a <strong>serial</strong> link. I doubt that the message rate via the serial link is high enough to cause any problems while capturing identical syslog messages sent via the network.</p><p>So, either there is real packet loss somewhere in your network OR you are not sending every syslog message via the network (bug in your code, bug in the local syslog implementation, etc.)</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-44758" class="comments-container"></div><div id="comment-tools-44758" class="comment-tools"></div><div class="clear"></div><div id="comment-44758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

