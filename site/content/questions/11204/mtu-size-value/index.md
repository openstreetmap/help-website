+++
type = "question"
title = "MTU Size value"
description = '''Hi, sorry for the &quot;beginners&quot; question :) I´ve a appliance that works as a transparent bridge. I wanted to know, if i can use wireshark in order to know which is the MTU value that is received by the bridge (i´ve been having issues in regards http latency, and i want to know if this could be network...'''
date = "2012-05-22T02:02:00Z"
lastmod = "2012-05-23T05:59:00Z"
weight = 11204
keywords = [ "mtu" ]
aliases = [ "/questions/11204" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [MTU Size value](/questions/11204/mtu-size-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11204-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, sorry for the "beginners" question :)</p><p>I´ve a appliance that works as a transparent bridge. I wanted to know, if i can use wireshark in order to know which is the MTU value that is received by the bridge (i´ve been having issues in regards http latency, and i want to know if this could be network related.</p><p>I´m using this filter: tcp.flags.syn== 1 and tcp.flags.ack==1 and tcp.port==80</p><p>Thanks in advance, RPLF</p></div><div id="question-tags" class="tags-container tags">mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/44d714f29caf2ae7862df8c690cd9061?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ruiplf&#39;s gravatar image" /><p>ruiplf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ruiplf has no accepted answers">0%</span></p></div></div><div id="comments-container-11204" class="comments-container"></div><div id="comment-tools-11204" class="comment-tools"></div><div class="clear"></div><div id="comment-11204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11205"></span>

<div id="answer-container-11205" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11205-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>a bridge should not modify the packet size (or do any fragmentation). If you want to know if the bridge is actually modifying the packets, you should sniff in front of the bridge and behind it, then compare the two captures files. Sniffing only at one "collection point" (client or server) makes it hard to detect any modification.</p><p>If you compare the capture files look at the packet size. You can do this, by adding a column in the packet list view.</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Columns -&gt; Add -&gt; Field type: Packet length (bytes).</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 03:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '12, 03:30</p></div></div><div id="comments-container-11205" class="comments-container"></div><div id="comment-tools-11205" class="comment-tools"></div><div class="clear"></div><div id="comment-11205-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11253"></span>

<div id="answer-container-11253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11253-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure sniffing traffic is the best way to test for MTU size... I'd use a tool like 'tracepath' to verify the path MTU. See: <a href="http://packetlife.net/blog/2008/aug/18/path-mtu-discovery/">http://packetlife.net/blog/2008/aug/18/path-mtu-discovery/</a></p><p>HTH, Will</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '12, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/e0423b823331f6b489f99b939d5c669d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willdennis&#39;s gravatar image" /><p>willdennis<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willdennis has no accepted answers">0%</span></p></div></div><div id="comments-container-11253" class="comments-container"><span id="11256"></span><div id="comment-11256" class="comment"><div id="post-11256-score" class="comment-score"></div><div class="comment-text"><p>a bridge/switch is a layer 2 device and would not answer to PMTU probes.</p></div><div id="comment-11256-info" class="comment-info"><span class="comment-age">(23 May '12, 06:38)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11253" class="comment-tools"></div><div class="clear"></div><div id="comment-11253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

