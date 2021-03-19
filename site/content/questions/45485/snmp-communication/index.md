+++
type = "question"
title = "SNMP Communication"
description = '''Hi, I have a client who I think is filtering SNMP communication to some print devices. I have a software on their server that relays on SNMP communication. All of the issues point to this communication. Can you please tell me how I can configure the filter in wireshark on there server to collect SNM...'''
date = "2015-08-28T12:03:00Z"
lastmod = "2015-08-29T02:34:00Z"
weight = 45485
keywords = [ "communication", "snmp" ]
aliases = [ "/questions/45485" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SNMP Communication](/questions/45485/snmp-communication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45485-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a client who I think is filtering SNMP communication to some print devices. I have a software on their server that relays on SNMP communication. All of the issues point to this communication. Can you please tell me how I can configure the filter in wireshark on there server to collect SNMP communications to all my print devices and nothing else. I need to collect as much information possible.</p></div><div id="question-tags" class="tags-container tags">communication snmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '15, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/f62206a07a7af6164e9a476c313a22e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pprasad&#39;s gravatar image" /><p>pprasad<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pprasad has no accepted answers">0%</span></p></div></div><div id="comments-container-45485" class="comments-container"></div><div id="comment-tools-45485" class="comment-tools"></div><div class="clear"></div><div id="comment-45485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45501"></span>

<div id="answer-container-45501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45501-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To see only SNMP traffic, please use the capture filter</p><blockquote><p>udp and (port 161 or port 162)</p></blockquote><p>Don't filter on the print devices in the first place. You can do that much better with display filters later and maybe there are some interesting details in SNMP queries going to other devices than the printers!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '15, 02:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Aug '15, 02:36</p></div></div><div id="comments-container-45501" class="comments-container"></div><div id="comment-tools-45501" class="comment-tools"></div><div class="clear"></div><div id="comment-45501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

