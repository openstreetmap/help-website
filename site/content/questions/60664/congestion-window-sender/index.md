+++
type = "question"
title = "Congestion Window - Sender"
description = '''Why do some TCP congestion algorithms stay in a congestion avoidance state all the time ?'''
date = "2017-04-08T02:26:00Z"
lastmod = "2017-04-08T03:07:00Z"
weight = 60664
keywords = [ "congestion-control", "congestion", "tcpwindowsize" ]
aliases = [ "/questions/60664" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Congestion Window - Sender](/questions/60664/congestion-window-sender)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60664-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why do some TCP congestion algorithms stay in a congestion avoidance state all the time ?</p></div><div id="question-tags" class="tags-container tags">congestion-control congestion tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '17, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p>armodes<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '17, 18:16</p></div></div><div id="comments-container-60664" class="comments-container"><span id="60666"></span><div id="comment-60666" class="comment"><div id="post-60666-score" class="comment-score"></div><div class="comment-text"><p>How did you get the values?</p></div><div id="comment-60666-info" class="comment-info"><span class="comment-age">(08 Apr '17, 03:08)</span> Christian_R</div></div></div><div id="comment-tools-60664" class="comment-tools"></div><div class="clear"></div><div id="comment-60664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60665"></span>

<div id="answer-container-60665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60665-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is the really bad thing about congestion avoidance algorithms like RENO. Once a session has entered congestion avoidance mode it will never escape.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '17, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-60665" class="comments-container"><span id="60669"></span><div id="comment-60669" class="comment"><div id="post-60669-score" class="comment-score"></div><div class="comment-text"><p>Don't know, have no good test setup for reproducing it. But I would give CTCP from Microsoft give a try. Because as I understand it right it doesn't grow linear after the congestion. I am curious about your findings.</p></div><div id="comment-60669-info" class="comment-info"><span class="comment-age">(08 Apr '17, 07:31)</span> Christian_R</div></div><span id="60672"></span><div id="comment-60672" class="comment"><div id="post-60672-score" class="comment-score">1</div><div class="comment-text"><p>I think the only one is probably BBR, which is pretty new:</p><p><a href="http://queue.acm.org/detail.cfm?id=3022184">http://queue.acm.org/detail.cfm?id=3022184</a></p></div><div id="comment-60672-info" class="comment-info"><span class="comment-age">(08 Apr '17, 10:11)</span> Jasper ♦♦</div></div><span id="60686"></span><div id="comment-60686" class="comment"><div id="post-60686-score" class="comment-score"></div><div class="comment-text"><p>@Jasper Very interesting link!</p></div><div id="comment-60686-info" class="comment-info"><span class="comment-age">(09 Apr '17, 14:44)</span> Christian_R</div></div></div><div id="comment-tools-60665" class="comment-tools"></div><div class="clear"></div><div id="comment-60665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

