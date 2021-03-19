+++
type = "question"
title = "Tshark Packet Comments"
description = '''Hi, Is is possible to set the comment for an individual packet using tshark? I see in the man page this can be done for the capture comment with --capture-comment &amp;lt;comment&amp;gt; but is there a way to specify an individual packet by packet number? Many Thanks'''
date = "2015-06-21T10:37:00Z"
lastmod = "2015-06-21T10:51:00Z"
weight = 43408
keywords = [ "pkt_comment", "tshark", "comments" ]
aliases = [ "/questions/43408" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark Packet Comments](/questions/43408/tshark-packet-comments)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43408-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is is possible to set the comment for an individual packet using tshark? I see in the man page this can be done for the capture comment with --capture-comment &lt;comment&gt; but is there a way to specify an individual packet by packet number?</p><p>Many Thanks</p></div><div id="question-tags" class="tags-container tags">pkt_comment tshark comments</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '15, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/04f2459d8c2e3e8f9f9afc61a05fc8d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marv&#39;s gravatar image" /><p>Marv<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marv has no accepted answers">0%</span></p></div></div><div id="comments-container-43408" class="comments-container"></div><div id="comment-tools-43408" class="comment-tools"></div><div class="clear"></div><div id="comment-43408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43409"></span>

<div id="answer-container-43409" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43409-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, you can't do that with tshark (not implemented). However, you can add packet level comments in Wireshark (right click a frame and choose "Packet comment") and then save the file as a <strong>pcapng</strong> to preserve the comments.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '15, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jun '15, 10:53</p></div></div><div id="comments-container-43409" class="comments-container"><span id="43456"></span><div id="comment-43456" class="comment"><div id="post-43456-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt,</p><p>It would be great if tshark could do this, I wonder if this will be available in later versions?</p><p>Cheers</p></div><div id="comment-43456-info" class="comment-info"><span class="comment-age">(22 Jun '15, 11:42)</span> Marv</div></div><span id="43463"></span><div id="comment-43463" class="comment"><div id="post-43463-score" class="comment-score"></div><div class="comment-text"><p>I don't know. There is no feature "roadmap" for Wireshark. So, if you need this feature please file an enhancement but at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a> and hope that somebody has time to implement it. I think it should be a feature for editcap, instead of tshark.</p></div><div id="comment-43463-info" class="comment-info"><span class="comment-age">(22 Jun '15, 13:35)</span> Kurt Knochner ♦</div></div><span id="43750"></span><div id="comment-43750" class="comment"><div id="post-43750-score" class="comment-score"></div><div class="comment-text"><p>Had a chat with Martin about this at Sharkfest, he very kindly added this to editcap with the -a option:</p><p>-a &lt;framenum&gt;:&lt;comment&gt; Add or replace comment for given frame number</p><p><a href="https://github.com/wireshark/wireshark/commit/dd16c55e9f830e6febf5484a7a71ca0abd05bf16">https://github.com/wireshark/wireshark/commit/dd16c55e9f830e6febf5484a7a71ca0abd05bf16</a></p><p>Cheers</p></div><div id="comment-43750-info" class="comment-info"><span class="comment-age">(30 Jun '15, 15:11)</span> Marv</div></div></div><div id="comment-tools-43409" class="comment-tools"></div><div class="clear"></div><div id="comment-43409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

