+++
type = "question"
title = "PING reply not recognized - No response found"
description = '''Anybody has an idea why wireshark doesn&#x27;t recognize the PING reply as the response to the request when SEQ and ID are the same ? Here&#x27;s the tracefile ping_noreply.pcapng  Regards Matthias '''
date = "2016-07-06T12:57:00Z"
lastmod = "2016-07-06T21:22:00Z"
weight = 53861
keywords = [ "not", "found", "ping", "response" ]
aliases = [ "/questions/53861" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [PING reply not recognized - No response found](/questions/53861/ping-reply-not-recognized-no-response-found)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53861-score" class="post-score" title="current number of votes">0</div><span id="post-53861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anybody has an idea why wireshark doesn't recognize the PING reply as the response to the request when SEQ and ID are the same ?<br />
Here's the tracefile <a href="https://ibm.box.com/s/lc8peq6nx744ezwrakc1sy2uvoecphzh">ping_noreply.pcapng</a> <img src="https://osqa-ask.wireshark.org/upfiles/Selection_003.png" alt="alt text" /></p><p>Regards Matthias</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-found" rel="tag" title="see questions tagged &#39;found&#39;">found</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '16, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jul '16, 13:40</strong> </span></p></div></div><div id="comments-container-53861" class="comments-container"><span id="53862"></span><div id="comment-53862" class="comment"><div id="post-53862-score" class="comment-score"></div><div class="comment-text"><p>Matthias, your link asks for a login...</p></div><div id="comment-53862-info" class="comment-info"><span class="comment-age">(06 Jul '16, 13:08)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="53865"></span><div id="comment-53865" class="comment"><div id="post-53865-score" class="comment-score"></div><div class="comment-text"><p>Thanks for letting me know, I moved it to another location...</p></div><div id="comment-53865-info" class="comment-info"><span class="comment-age">(06 Jul '16, 13:41)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-53861" class="comment-tools"></div><div class="clear"></div><div id="comment-53861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53867"></span>

<div id="answer-container-53867" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53867-score" class="post-score" title="current number of votes">0</div><span id="post-53867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mrEEde has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The code field doesn't match.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '16, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53867" class="comments-container"><span id="53874"></span><div id="comment-53874" class="comment"><div id="post-53874-score" class="comment-score"></div><div class="comment-text"><p>Easy enough :-) Thanks</p></div><div id="comment-53874-info" class="comment-info"><span class="comment-age">(06 Jul '16, 21:22)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-53867" class="comment-tools"></div><div class="clear"></div><div id="comment-53867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

