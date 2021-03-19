+++
type = "question"
title = "Tracking udp game latency"
description = '''Hello, complete wireshark rookie here. i experienced some issues with an online game i play and would like to use wireshark to plot my latency. i tried to track the udp filter on frame.time_delta_displayed but the data generated can&#x27;t be what im looking for. Can someone guide me in the right directi...'''
date = "2014-01-09T09:07:00Z"
lastmod = "2014-01-09T11:22:00Z"
weight = 28737
keywords = [ "latency", "udp" ]
aliases = [ "/questions/28737" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Tracking udp game latency](/questions/28737/tracking-udp-game-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28737-score" class="post-score" title="current number of votes">0</div><span id="post-28737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>complete wireshark rookie here.</p><p>i experienced some issues with an online game i play and would like to use wireshark to plot my latency. i tried to track the udp filter on frame.time_delta_displayed but the data generated can't be what im looking for.</p><p>Can someone guide me in the right direction?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '14, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/ada801512fdef81516c4d33d59bea623?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nick%20SB&#39;s gravatar image" /><p><span>Nick SB</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nick SB has no accepted answers">0%</span></p></div></div><div id="comments-container-28737" class="comments-container"></div><div id="comment-tools-28737" class="comment-tools"></div><div class="clear"></div><div id="comment-28737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28738"></span>

<div id="answer-container-28738" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28738-score" class="post-score" title="current number of votes">2</div><span id="post-28738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Nick SB has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>see my answer to a similar questions.</p><blockquote><p><a href="http://ask.wireshark.org/questions/26090/calculating-ping-time-for-a-game">http://ask.wireshark.org/questions/26090/calculating-ping-time-for-a-game</a></p></blockquote><p>Your problem is the same. You can't just plot the delta of two UDP frames, as you don't know if two consecutive frames are 'corresponding' request/response frames (see the comments in my answer).</p><p>So, without a deep understanding of the game protocol in use, there is no way to calculate the 'latency', 'ping time' or whatever that value is called in your game.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '14, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28738" class="comments-container"><span id="28744"></span><div id="comment-28744" class="comment"><div id="post-28744-score" class="comment-score"></div><div class="comment-text"><p>thank you very much for your fast answer, Kurt.</p></div><div id="comment-28744-info" class="comment-info"><span class="comment-age">(09 Jan '14, 11:22)</span> <span class="comment-user userinfo">Nick SB</span></div></div></div><div id="comment-tools-28738" class="comment-tools"></div><div class="clear"></div><div id="comment-28738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

