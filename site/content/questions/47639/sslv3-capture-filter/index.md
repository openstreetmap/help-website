+++
type = "question"
title = "sslv3 capture filter"
description = '''What is a capture filter to capture SSLV3 traffic only? I know the display filter is ssl.record.version==0x0300.'''
date = "2015-11-16T08:26:00Z"
lastmod = "2015-11-17T05:25:00Z"
weight = 47639
keywords = [ "sslv3" ]
aliases = [ "/questions/47639" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [sslv3 capture filter](/questions/47639/sslv3-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47639-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47639-score" class="post-score" title="current number of votes">0</div><span id="post-47639-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is a capture filter to capture SSLV3 traffic only? I know the display filter is ssl.record.version==0x0300.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sslv3" rel="tag" title="see questions tagged &#39;sslv3&#39;">sslv3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '15, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/1ace388d473a7dc2c6ffb774562b02ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrickwill&#39;s gravatar image" /><p><span>patrickwill</span><br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrickwill has no accepted answers">0%</span></p></div></div><div id="comments-container-47639" class="comments-container"></div><div id="comment-tools-47639" class="comment-tools"></div><div class="clear"></div><div id="comment-47639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47642"></span>

<div id="answer-container-47642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47642-score" class="post-score" title="current number of votes">0</div><span id="post-47642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can you please try this:</p><blockquote><p>tcp[((tcp[12]&gt;&gt;4)*4)+9:2]=0x0300<br />
</p></blockquote><p><strong>HINT:</strong> As capture filters work in a frame level, this capture filter will only capture the frame with the SSLv3 handshake. No more, no less. If you want to capture the whole SSLv3 session, there is no simple capture filter for that. The only option would be to capture everything on port 443 and later filter for connections with SSLv3 handshake in tshark to get the TCP stream number and then you can filter for that TCP stream number in a second step (with scripting).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Nov '15, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-47642" class="comments-container"><span id="47664"></span><div id="comment-47664" class="comment"><div id="post-47664-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt it worked perfect.</p></div><div id="comment-47664-info" class="comment-info"><span class="comment-age">(17 Nov '15, 05:15)</span> <span class="comment-user userinfo">patrickwill</span></div></div><span id="47665"></span><div id="comment-47665" class="comment"><div id="post-47665-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-47665-info" class="comment-info"><span class="comment-age">(17 Nov '15, 05:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-47642" class="comment-tools"></div><div class="clear"></div><div id="comment-47642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

