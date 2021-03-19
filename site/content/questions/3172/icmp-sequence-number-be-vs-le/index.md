+++
type = "question"
title = "ICMP Sequence Number (BE) vs (LE)"
description = '''When applying a column for a capture looking at a trace route I noticed there are 2 sequence number choices - (BE) and (LE) in the packets detail screen. I did not see these in earlier version of WS. What&#x27;s the difference? Thanks Eric'''
date = "2011-03-28T05:19:00Z"
lastmod = "2011-03-28T06:41:00Z"
weight = 3172
keywords = [ "icmp" ]
aliases = [ "/questions/3172" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [ICMP Sequence Number (BE) vs (LE)](/questions/3172/icmp-sequence-number-be-vs-le)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3172-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When applying a column for a capture looking at a trace route I noticed there are 2 sequence number choices - (BE) and (LE) in the packets detail screen. I did not see these in earlier version of WS. What's the difference? Thanks Eric</p></div><div id="question-tags" class="tags-container tags">icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '11, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/f797bdc41d990dca073837114e048b1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EricKnaus&#39;s gravatar image" /><p>EricKnaus<br />
<span class="score" title="46 reputation points">46</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EricKnaus has no accepted answers">0%</span></p></div></div><div id="comments-container-3172" class="comments-container"></div><div id="comment-tools-3172" class="comment-tools"></div><div class="clear"></div><div id="comment-3172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3175"></span>

<div id="answer-container-3175" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3175-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The sequence number field is simply being displayed in both big endian (BE) and little endian (LE) formats to make it easier to follow when those sequence numbers are incrementing from one ICMP echo request/reply to the next. The reason both formats are shown is because sometimes those fields are populated in big endian format and sometimes they are populated in little endian format, and there is no definitive way to tell which format it's in from the contents of the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '11, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3175" class="comments-container"></div><div id="comment-tools-3175" class="comment-tools"></div><div class="clear"></div><div id="comment-3175-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

