+++
type = "question"
title = "How do I create multiple table entries for a single UDP packet?"
description = '''Hi, I hope this is the right place to ask my question... I wish to be able to receive a single UDP packet that contains several packets of my protocol and show each of those internal packet in the main GUI table as a standalone packet.  I know that Wireshark does not support this. So i thought to re...'''
date = "2013-04-22T01:55:00Z"
lastmod = "2013-05-05T11:47:00Z"
weight = 20694
keywords = [ "development" ]
aliases = [ "/questions/20694" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I create multiple table entries for a single UDP packet?](/questions/20694/how-do-i-create-multiple-table-entries-for-a-single-udp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20694-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I hope this is the right place to ask my question...</p><p>I wish to be able to receive a single UDP packet that contains several packets of my protocol and show each of those internal packet in the main GUI table as a standalone packet.</p><p>I know that Wireshark does not support this.</p><p>So i thought to resend it internally over socket in the machine after dissection so that the parsed packets are resent and captured by Wireshark and thus achieve my goal, but that does not work on Windows due to loopback limitations in that OS and I do need the application to be cross-platform.</p><p>That leaves me with the option to modify Wireshark code. I have been told this is a significant amount of work but I wonder if anyone knows about previous such attempts or can point me at how this may be implemented.</p><p>Many Thanks</p></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/fa7c952ff82c858b325ae0c691090dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amirix&#39;s gravatar image" /><p>amirix<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amirix has no accepted answers">0%</span></p></div></div><div id="comments-container-20694" class="comments-container"></div><div id="comment-tools-20694" class="comment-tools"></div><div class="clear"></div><div id="comment-20694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20964"></span>

<div id="answer-container-20964" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20964-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I found a way to do it that seems clean enough and will hopefully sustain the throughput needed and be easily ported to other OS: I altered the dumpcap code in a way that the fragmentation is made there, the original IP/UDP header is appended with needed changes and then forwarded to WS. I'll post this also in the development thread I opened.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '13, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/fa7c952ff82c858b325ae0c691090dc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amirix&#39;s gravatar image" /><p>amirix<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amirix has no accepted answers">0%</span></p></div></div><div id="comments-container-20964" class="comments-container"></div><div id="comment-tools-20964" class="comment-tools"></div><div class="clear"></div><div id="comment-20964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

