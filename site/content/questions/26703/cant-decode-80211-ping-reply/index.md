+++
type = "question"
title = "Can&#x27;t decode 802.11 ping reply"
description = '''Hello,  Perhaps this question had been asked before but I&#x27;ve been searching and could not find answer.  I performed a ping from wifi client (laptop) and captured raw 802.11 packet via wireless nic interface. I used to WS to decode the packet and was able to see ping request clearly (802.11header, LL...'''
date = "2013-11-06T17:26:00Z"
lastmod = "2013-11-06T19:51:00Z"
weight = 26703
keywords = [ "qos", "802.11" ]
aliases = [ "/questions/26703" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't decode 802.11 ping reply](/questions/26703/cant-decode-80211-ping-reply)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26703-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Perhaps this question had been asked before but I've been searching and could not find answer. I performed a ping from wifi client (laptop) and captured raw 802.11 packet via wireless nic interface. I used to WS to decode the packet and was able to see ping request clearly (802.11header, LLC, IP, ICMP, etc):</p><p><img src="https://osqa-ask.wireshark.org/upfiles/802.11icmpreply.PNG" alt="alt text" /></p><p>However it seemed that WS cannot decoded a ping reply when it is an 802.11 QoS data packet. Here I noticed the different is that the ping reply does have an extra QoS header and LLC had been decoded as WEP (?). Subsequently WS could not decoded the rest as a ping packet. Please let me know how to resolve this issue... Thanks in advance (btw, I am using WS Version 1.10.3 (SVN Rev 53022 from /trunk-1.10) and please pardon my (clumsy) drawing :))</p><p><img src="https://osqa-ask.wireshark.org/upfiles/802.11ping.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">qos 802.11</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Nov '13, 17:26</strong></p><img src="https://secure.gravatar.com/avatar/81be229523eee98c8df436444218a42e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbdiep&#39;s gravatar image" /><p>dbdiep<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbdiep has no accepted answers">0%</span></p></img></div></div><div id="comments-container-26703" class="comments-container"></div><div id="comment-tools-26703" class="comment-tools"></div><div class="clear"></div><div id="comment-26703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26704"></span>

<div id="answer-container-26704" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26704-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>For the second packet, Wireshark apparently thinks the second packet has a QoS field when it appears not to. Please file a bug on <a href="http://bugs.wireshark.org/">the Wireshark bugzilla</a>, and attach the capture file if at all possible.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '13, 19:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div></div><div id="comments-container-26704" class="comments-container"></div><div id="comment-tools-26704" class="comment-tools"></div><div class="clear"></div><div id="comment-26704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

