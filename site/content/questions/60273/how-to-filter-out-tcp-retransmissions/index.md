+++
type = "question"
title = "How to filter out TCP retransmissions"
description = '''Hi,  I&#x27;m using tshark to analyze HTTPs traffic and I don&#x27;t want to capture TCP retransmissions. Is there a capture filter I can use for this? '''
date = "2017-03-23T05:04:00Z"
lastmod = "2017-03-23T05:17:00Z"
weight = 60273
keywords = [ "capture-filter", "tshark", "tcp", "tcp-retransmit" ]
aliases = [ "/questions/60273" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter out TCP retransmissions](/questions/60273/how-to-filter-out-tcp-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60273-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm using tshark to analyze HTTPs traffic and I don't want to capture TCP retransmissions. Is there a capture filter I can use for this?</p></div><div id="question-tags" class="tags-container tags">capture-filter tshark tcp tcp-retransmit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '17, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/eb5865c02f2d8398a2d02f7038b52da3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sarah&#39;s gravatar image" /><p>Sarah<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sarah has no accepted answers">0%</span></p></div></div><div id="comments-container-60273" class="comments-container"></div><div id="comment-tools-60273" class="comment-tools"></div><div class="clear"></div><div id="comment-60273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60274"></span>

<div id="answer-container-60274" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60274-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>IMHO it's not possible to have a capture filter to ignore retransmits. It's necessary to have the data to be able to detect a retransmit (analyse sequence numbers).</p><p>An option to ignore retransmits is using a display filter (e.g. <code>not tcp.analysis.retransmission and not tcp.analysis.fast_retransmission</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '17, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Mar '17, 05:18</p></div></div><div id="comments-container-60274" class="comments-container"><span id="60275"></span><div id="comment-60275" class="comment"><div id="post-60275-score" class="comment-score">1</div><div class="comment-text"><p>correct, retransmissions need to be diagnosed first, so you can't filter them away during capture.</p></div><div id="comment-60275-info" class="comment-info"><span class="comment-age">(23 Mar '17, 05:37)</span> Jasper ♦♦</div></div></div><div id="comment-tools-60274" class="comment-tools"></div><div class="clear"></div><div id="comment-60274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

