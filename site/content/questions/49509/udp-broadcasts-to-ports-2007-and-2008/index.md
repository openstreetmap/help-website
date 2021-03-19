+++
type = "question"
title = "UDP Broadcasts to ports 2007 and 2008"
description = '''One client on my network is continually broadcasting to UDP ports 2007 and 2008 I have not seen the computer yet. I think its a Macbook. 1 2016-01-25 11:08:54.238890 10.23.10.108 255.255.255.255 UDP 71 54419 → 2008 Len=29 2 2016-01-25 11:08:54.240109 10.23.10.108 255.255.255.255 UDP 71 54419 → 2007 ...'''
date = "2016-01-25T11:34:00Z"
lastmod = "2016-01-26T07:57:00Z"
weight = 49509
keywords = [ "broadcast", "udp" ]
aliases = [ "/questions/49509" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [UDP Broadcasts to ports 2007 and 2008](/questions/49509/udp-broadcasts-to-ports-2007-and-2008)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49509-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>One client on my network is continually broadcasting to UDP ports 2007 and 2008 I have not seen the computer yet. I think its a Macbook.</p><pre><code>1   2016-01-25 11:08:54.238890  10.23.10.108    255.255.255.255 UDP 71  54419 → 2008  Len=29
2   2016-01-25 11:08:54.240109  10.23.10.108    255.255.255.255 UDP 71  54419 → 2007  Len=29</code></pre><p>any ideas what this might be?</p></div><div id="question-tags" class="tags-container tags">broadcast udp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '16, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/fb6681112e2c046a7fd078e3e341e4e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Choate&#39;s gravatar image" /><p>Choate<br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Choate has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jan '16, 12:06</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-49509" class="comments-container"></div><div id="comment-tools-49509" class="comment-tools"></div><div class="clear"></div><div id="comment-49509-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49517"></span>

<div id="answer-container-49517" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49517-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'll answer my own question. This behavior is caused by an Apple app called Remote Mouse (<a href="http://www.remotemouse.net/)">http://www.remotemouse.net/)</a> When installed on a MAC, it apparently is announcing itself dozens of times per second by sending UDP broadcasts with a destination port of 2007 and 2008. Not very nice! There is a companion app for the ipad or iphone that finds this "server" and allows you to use your iphone/ipad as a remote mouse for your computer. I didn't see any bad behavior from the iphone/ipad app, just the app that sits on the Macbook. I see there is a Windows version of this software too, but I didn't bother testing it. I would guess sit behaves the same way because it needs to announce itself to the mobil device.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '16, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/fb6681112e2c046a7fd078e3e341e4e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Choate&#39;s gravatar image" /><p>Choate<br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Choate has no accepted answers">0%</span></p></div></div><div id="comments-container-49517" class="comments-container"><span id="49521"></span><div id="comment-49521" class="comment"><div id="post-49521-score" class="comment-score">1</div><div class="comment-text"><p>Very well, now the last point is to press the checkmark icon next to the "thumbs up" and "thumbs down" for the answer, to mark the answer as the correct one for the other folks here. This makes the number of answers for the question appear on green background in the question list, highlighting the question as usefully answered.</p><p>Just for the case you have switched it off by mistake, you may switch on MAC address vendor resolution in <code>Edit -&gt; Preferences -&gt; Appearance -&gt; Name Resolution -&gt; Resolve MAC addresses</code>. With this setting, Wireshark shows you the beginning of vendor name for all MAC addresses (except locally administered ones marked as such), so you can see at once that the MAC address is an Apple one.</p></div><div id="comment-49521-info" class="comment-info"><span class="comment-age">(26 Jan '16, 11:11)</span> sindy</div></div><span id="60613"></span><div id="comment-60613" class="comment"><div id="post-60613-score" class="comment-score"></div><div class="comment-text"><p>According to <a href="http://www.remotemouse.net/faq">the FAQ</a> they (now?) use port 1978 (UDP and TCP). But I just ran into the very same situation as Choate: Saw about 10 packets per second for minutes on wifi with UDP destination port 2008 and the name of a MacBook in cleartext inside the payload. These packets clearly stuck out of all the other traffic even just by looking at the list of packets.</p></div><div id="comment-60613-info" class="comment-info"><span class="comment-age">(06 Apr '17, 05:38)</span> XTaran</div></div></div><div id="comment-tools-49517" class="comment-tools"></div><div class="clear"></div><div id="comment-49517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

