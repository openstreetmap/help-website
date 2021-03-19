+++
type = "question"
title = "[closed] Help with a DDOS Attack"
description = '''Recently my server has been ddosed with an attack that sends a relatively huge data transfer (10k packets, 14M of data on one conversation) when the average conversation between server &amp;amp; client is more like 1-100 packets, 50-5000 bytes. I&#x27;m running a linux host and wondering if I can defend from...'''
date = "2017-01-04T17:31:00Z"
lastmod = "2017-01-04T22:22:00Z"
weight = 58519
keywords = [ "ddos" ]
aliases = [ "/questions/58519" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Help with a DDOS Attack](/questions/58519/help-with-a-ddos-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58519-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently my server has been ddosed with an attack that sends a relatively huge data transfer (10k packets, 14M of data on one conversation) when the average conversation between server &amp; client is more like 1-100 packets, 50-5000 bytes. I'm running a linux host and wondering if I can defend from this attack somehow throttling connections using iptables. I've already implemented the "low hanging fruit" of ddos defense. Any guidance appreciated!</p><p><img src="https://osqa-ask.wireshark.org/upfiles/14MConversation.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">ddos</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jan '17, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/30823bd0520b5d199710f4ad952d1ca1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PEMinecraft&#39;s gravatar image" /><p>PEMinecraft<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PEMinecraft has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>closed 04 Jan '17, 22:22</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-58519" class="comments-container"><span id="58536"></span><div id="comment-58536" class="comment"><div id="post-58536-score" class="comment-score"></div><div class="comment-text"><p>Anyway that's definitely not a DDOS. It could be a <strong>non-distributed</strong> DoS attack but it's certainly not a distributed one. More likely, though, it's just a long-lived connection (file transfer?) or something. I'd start by looking at the TCP ports involved.</p></div><div id="comment-58536-info" class="comment-info"><span class="comment-age">(05 Jan '17, 05:36)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-58519" class="comment-tools"></div><div class="clear"></div><div id="comment-58519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by Jaap 04 Jan '17, 22:22

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58525"></span>

<div id="answer-container-58525" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58525-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a question suitable for <a href="https://superuser.com">Super User at stackexchange</a>, not a Wireshark question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58525" class="comments-container"></div><div id="comment-tools-58525" class="comment-tools"></div><div class="clear"></div><div id="comment-58525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

