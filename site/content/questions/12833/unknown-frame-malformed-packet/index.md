+++
type = "question"
title = "Unknown frame [Malformed Packet]"
description = '''I am new at this, but my company has something serious going on. We are getting flooded with &quot;Unknown frame[Malformed Packet]&quot; that are 60 bits and lots of them. This is causing major issues with my VOIP system (ShoreTel) to the point that we are almost unable to use the phones. IP range: 10.0.x.x S...'''
date = "2012-07-18T10:42:00Z"
lastmod = "2012-07-19T05:02:00Z"
weight = 12833
keywords = [ "unknown", "frame", "malformed", "packet" ]
aliases = [ "/questions/12833" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unknown frame \[Malformed Packet\]](/questions/12833/unknown-frame-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12833-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new at this, but my company has something serious going on. We are getting flooded with "Unknown frame[Malformed Packet]" that are 60 bits and lots of them. This is causing major issues with my VOIP system (ShoreTel) to the point that we are almost unable to use the phones.</p><p>IP range: 10.0.x.x Subnet: 255.255.0.0 HP switching equipment</p><p>We have a flat network, but plan to change that soon.</p><p>How do I stop the Unknown frame[Malformed Packet]'s?</p><p>The packet has all 0's.</p><p>The bottom part of Wireshark has:</p><p>0000 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ........ ........</p><p>0010 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ........ ........</p><p>0020 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ........ ........</p><p>0030 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ........ ........</p></div><div id="question-tags" class="tags-container tags">unknown frame malformed packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '12, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/59e3b487632a971649edcb2bbbce43a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WEIglad&#39;s gravatar image" /><p>WEIglad<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WEIglad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jul '12, 13:10</p></div></div><div id="comments-container-12833" class="comments-container"><span id="12846"></span><div id="comment-12846" class="comment"><div id="post-12846-score" class="comment-score"></div><div class="comment-text"><p>interesting. Can you please post a sample capture file on <a href="http://cloudshark.org">cloudshark.org</a>?</p><p>HINT: As you cannot delete an anonymously uploaded file on <a href="http://cloudshark.org">cloudshark.org</a>, you better don't post any private data. Post just those packets in a capture file, that are required to analyze the problem.</p></div><div id="comment-12846-info" class="comment-info"><span class="comment-age">(19 Jul '12, 02:05)</span> Kurt Knochner ♦</div></div><span id="25336"></span><div id="comment-25336" class="comment"><div id="post-25336-score" class="comment-score"></div><div class="comment-text"><p>Mine does the same on every wifi network I attach my computer to. And I seem to allow everyone's connection to a mere crawl. I can't seem to locate the problem.</p></div><div id="comment-25336-info" class="comment-info"><span class="comment-age">(28 Sep '13, 19:45)</span> akosha</div></div></div><div id="comment-tools-12833" class="comment-tools"></div><div class="clear"></div><div id="comment-12833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12852"></span>

<div id="answer-container-12852" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12852-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That looks like a host interface gone cuckoo, sending out empty frames. It's hard to tell where it comes from because even the source address is empty. Now you're back at layer one, pulling cables.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '12, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-12852" class="comments-container"></div><div id="comment-tools-12852" class="comment-tools"></div><div class="clear"></div><div id="comment-12852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

