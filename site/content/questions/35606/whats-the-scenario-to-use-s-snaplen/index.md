+++
type = "question"
title = "what&#x27;s the scenario to use -s snaplen?"
description = '''Hi, For large amounts of data transfer like video stream, FTP, I don&#x27;t really need data but I do want to get the full headers of each frame for analysis. The question is, would that cause any potential problem when doing analysis? For example, incorrect statistics, etc... If we do an IO graph, will ...'''
date = "2014-08-20T02:20:00Z"
lastmod = "2014-08-20T03:05:00Z"
weight = 35606
keywords = [ "snaplen" ]
aliases = [ "/questions/35606" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [what's the scenario to use -s snaplen?](/questions/35606/whats-the-scenario-to-use-s-snaplen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35606-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35606-score" class="post-score" title="current number of votes">0</div><span id="post-35606-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>For large amounts of data transfer like video stream, FTP, I don't really need data but I do want to get the full headers of each frame for analysis. The question is, would that cause any potential problem when doing analysis? For example, incorrect statistics, etc...</p><p>If we do an IO graph, will the result be the same if you captured a full trace as compared with a trace using -s &lt;snaplen&gt;?</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-snaplen" rel="tag" title="see questions tagged &#39;snaplen&#39;">snaplen</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '14, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Aug '14, 03:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-35606" class="comments-container"></div><div id="comment-tools-35606" class="comment-tools"></div><div class="clear"></div><div id="comment-35606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35607"></span>

<div id="answer-container-35607" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35607-score" class="post-score" title="current number of votes">1</div><span id="post-35607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, all statistics will be the same, because each frame will still know it's original length. The payload bytes just aren't there to decode, but that's all. So as long as you don't care about payload contents you can capture just the headers and do your analysis.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '14, 02:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35607" class="comments-container"><span id="35610"></span><div id="comment-35610" class="comment"><div id="post-35610-score" class="comment-score"></div><div class="comment-text"><p>many thanks for quick response!</p></div><div id="comment-35610-info" class="comment-info"><span class="comment-age">(20 Aug '14, 02:43)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="35611"></span><div id="comment-35611" class="comment"><div id="post-35611-score" class="comment-score"></div><div class="comment-text"><p>by the way, what the typical snaplen to specify to make sure all of the headers will be included? Is there a rule of thumb value?</p></div><div id="comment-35611-info" class="comment-info"><span class="comment-age">(20 Aug '14, 02:46)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="35613"></span><div id="comment-35613" class="comment"><div id="post-35613-score" class="comment-score"></div><div class="comment-text"><p>for normal TCP I go for 64 bytes, but if I need upper layer headers like NetBIOS/SMB as well I might choose 128 or 256, depending on how big they are.</p></div><div id="comment-35613-info" class="comment-info"><span class="comment-age">(20 Aug '14, 03:05)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-35607" class="comment-tools"></div><div class="clear"></div><div id="comment-35607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

