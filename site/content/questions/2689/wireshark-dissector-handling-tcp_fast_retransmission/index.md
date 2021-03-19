+++
type = "question"
title = "Wireshark dissector handling TCP_FAST_RETRANSMISSION"
description = '''I&#x27;m working on a Wireshark dissector plugin (C-based) to process some network data. The protocol that is being used over TCP is one where we can&#x27;t know the complete length of a response from a header field, so I need to use the desegment_offset/desegment_length pinfo fields (which I guess tcp_dissec...'''
date = "2011-03-07T00:54:00Z"
lastmod = "2011-03-07T04:28:00Z"
weight = 2689
keywords = [ "tcp-fast-retransmit", "dissector" ]
aliases = [ "/questions/2689" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark dissector handling TCP\_FAST\_RETRANSMISSION](/questions/2689/wireshark-dissector-handling-tcp_fast_retransmission)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2689-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on a Wireshark dissector plugin (C-based) to process some network data. The protocol that is being used over TCP is one where we can't know the complete length of a response from a header field, so I need to use the desegment_offset/desegment_length pinfo fields (which I guess tcp_dissect_pdus uses anyway).</p><p>Anyhow, this works fine until the network stream has some dup acks resulting in a TCP Fast Retransmission in the middle of the stream. At this point we get the retransmitted data in our dissector again, and lose any context of the previous desegmentation. In other words, after the retransmitted packet we get what should be the packet after the packet that came before the retransmit, but we don't get the data back from that previous packet, so the desegmentation is hosed. Not sure if that is clear or not, but I can't think of a better way to explain it off the top.</p><p>So, does anybody know of any elegant way to handle this situation?</p></div><div id="question-tags" class="tags-container tags">tcp-fast-retransmit dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '11, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/180eea9fb31f162096da95e7a8c744cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krippy2k&#39;s gravatar image" /><p>krippy2k<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krippy2k has no accepted answers">0%</span></p></div></div><div id="comments-container-2689" class="comments-container"></div><div id="comment-tools-2689" class="comment-tools"></div><div class="clear"></div><div id="comment-2689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2694"></span>

<div id="answer-container-2694" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2694-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There has been some improvements in the (very) <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=36131">recent Wireshark development code base</a>. Please have a look if this addresses your concerns.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '11, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2694" class="comments-container"><span id="2699"></span><div id="comment-2699" class="comment"><div id="post-2699-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response. I have checked out the latest source from SVN and added the dissector and stepped through it with a debugger, but at first glance I can't see any noticeable difference. I will keep digging.</p></div><div id="comment-2699-info" class="comment-info"><span class="comment-age">(07 Mar '11, 07:49)</span> krippy2k</div></div></div><div id="comment-tools-2694" class="comment-tools"></div><div class="clear"></div><div id="comment-2694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

