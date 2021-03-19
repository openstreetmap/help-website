+++
type = "question"
title = "IPRange in Dumpcap"
description = '''Hi, I need to set a Range / Subnet (for example 10.244.0.0/24) in my trace. Hosts are no problem, but nobody knows what Adresses sre realy involved in my trace scenario... Sofar my trace looks like this:  &quot;C:&#92;Program Files&#92;Wireshark&#92;dumpcap.exe&quot; -i LAN1 -f &quot;port 1720 or portrange 5000-5060 or ip hos...'''
date = "2016-06-29T08:29:00Z"
lastmod = "2016-06-29T09:14:00Z"
weight = 53729
keywords = [ "dumpcap", "voip" ]
aliases = [ "/questions/53729" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IPRange in Dumpcap](/questions/53729/iprange-in-dumpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53729-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I need to set a Range / Subnet (for example 10.244.0.0/24) in my trace. Hosts are no problem, but nobody knows what Adresses sre realy involved in my trace scenario... Sofar my trace looks like this:</p><p>"C:\Program Files\Wireshark\dumpcap.exe" -i LAN1 -f "port 1720 or portrange 5000-5060 or ip host 10.244.1.3 or ip host 10.244.1.4 or ip host 10.244.1.55" -b files:100 -b filesize:5000 -w C:\Tools\traces\cap\Wireshark.pcapng</p></div><div id="question-tags" class="tags-container tags">dumpcap voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '16, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/e3b62c9f90b2854b213c3e8b6023605d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roy&#39;s gravatar image" /><p>Roy<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jun '16, 08:31</p></div></div><div id="comments-container-53729" class="comments-container"></div><div id="comment-tools-53729" class="comment-tools"></div><div class="clear"></div><div id="comment-53729-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53730"></span>

<div id="answer-container-53730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53730-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To set a network in a capture filter use the <code>net</code> primitive, e.g. <code>net 10.244.0.0/24</code>. See the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">tcpdump pcap filter syntax page</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '16, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53730" class="comments-container"></div><div id="comment-tools-53730" class="comment-tools"></div><div class="clear"></div><div id="comment-53730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

