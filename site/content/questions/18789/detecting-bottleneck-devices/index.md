+++
type = "question"
title = "detecting bottleneck devices"
description = '''I have a client who wants to find out which devices on the network are the network traffic hogs. Does this software have feature that shows the network devices and the traffic each device is using in real-time over over a time period. I don&#x27;t need a very complicated software but just features to dis...'''
date = "2013-02-20T16:06:00Z"
lastmod = "2013-02-20T16:37:00Z"
weight = 18789
keywords = [ "device", "bandwidth", "network", "utilization" ]
aliases = [ "/questions/18789" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [detecting bottleneck devices](/questions/18789/detecting-bottleneck-devices)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18789-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a client who wants to find out which devices on the network are the network traffic hogs. Does this software have feature that shows the network devices and the traffic each device is using in real-time over over a time period.</p><p>I don't need a very complicated software but just features to display network devices and bandwidth usage for device.</p></div><div id="question-tags" class="tags-container tags">device bandwidth network utilization</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '13, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/0f6738196d7f9e60838be3dcb8fd1d88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zoinkman&#39;s gravatar image" /><p>zoinkman<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zoinkman has no accepted answers">0%</span></p></div></div><div id="comments-container-18789" class="comments-container"></div><div id="comment-tools-18789" class="comment-tools"></div><div class="clear"></div><div id="comment-18789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18791"></span>

<div id="answer-container-18791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18791-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is a primarily a network troubleshooting and packet capture tool. You can use it to analyze bandwidth usage (through the statistics functions), however it is not ideal to monitor a whole network for a longer period of time (hours, days), as you would have to record a lot of data (GByte or Tbyte).</p><p>If the network is really small and you are primarily interested in the traffic hogs regarding internet usage, then you may be able to use Wireshark for that, by capturing the whole traffic at the router interface for a limited time period (see <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet).">http://wiki.wireshark.org/CaptureSetup/Ethernet).</a></p><p>If you need to look at the whole intranet traffic of all systems, for a longer period (hours, days), then Wireshark is probably the wrong tool for you. I recommend to look at <a href="http://en.wikipedia.org/wiki/NetFlow">Netflow</a> and equivalents (listed in the Wikipedia article). Analyzing the traffic counters of your switch ports may also help (see <a href="http://www.cacti.net/">Cacti</a>, <a href="http://www.zenoss.com/solution/network">Zenoss</a>, <a href="http://www.zabbix.com/">Zabbix</a>, or similar).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '13, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '13, 16:59</p></div></div><div id="comments-container-18791" class="comments-container"></div><div id="comment-tools-18791" class="comment-tools"></div><div class="clear"></div><div id="comment-18791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

