+++
type = "question"
title = "HTTP unknown codes"
description = '''Hi, I have codes that wire shark is not decoding, such as HTTP Response 422, HTTP Response 510. Are these unknown? in wikipedia I see those codes: http://en.wikipedia.org/wiki/List_of_HTTP_status_codes maybe I am using an older version (mine is 1.8.7) Thanks, Diana'''
date = "2014-12-09T02:58:00Z"
lastmod = "2014-12-09T06:19:00Z"
weight = 38469
keywords = [ "http.response" ]
aliases = [ "/questions/38469" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP unknown codes](/questions/38469/http-unknown-codes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38469-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38469-score" class="post-score" title="current number of votes">0</div><span id="post-38469-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have codes that wire shark is not decoding, such as HTTP Response 422, HTTP Response 510. Are these unknown? in wikipedia I see those codes: <a href="http://en.wikipedia.org/wiki/List_of_HTTP_status_codes">http://en.wikipedia.org/wiki/List_of_HTTP_status_codes</a></p><p>maybe I am using an older version (mine is 1.8.7)</p><p>Thanks, Diana</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http.response" rel="tag" title="see questions tagged &#39;http.response&#39;">http.response</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '14, 02:58</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p><span>Dianalab9</span><br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-38469" class="comments-container"></div><div id="comment-tools-38469" class="comment-tools"></div><div class="clear"></div><div id="comment-38469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38471"></span>

<div id="answer-container-38471" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38471-score" class="post-score" title="current number of votes">0</div><span id="post-38471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The current stable 1.12.2 (and development 1.99.x) versions decode 422, but not 510. Please submit an enhancement request at the <a href="https://bugs.wireshark.org">Wireshark Bugzilla</a> (mark the entry as an enhancement).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '14, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38471" class="comments-container"><span id="38475"></span><div id="comment-38475" class="comment"><div id="post-38475-score" class="comment-score"></div><div class="comment-text"><p>thanks you. do you know which HTTP rfc I can use in order to get ALL available codes?</p></div><div id="comment-38475-info" class="comment-info"><span class="comment-age">(09 Dec '14, 04:27)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="38477"></span><div id="comment-38477" class="comment"><div id="post-38477-score" class="comment-score">1</div><div class="comment-text"><p>The <a href="http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml">IANA HTTP Status Code</a> registry lists all the current status codes, along with their respective RFC.</p></div><div id="comment-38477-info" class="comment-info"><span class="comment-age">(09 Dec '14, 05:32)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="38480"></span><div id="comment-38480" class="comment"><div id="post-38480-score" class="comment-score"></div><div class="comment-text"><p>THANKS! this helps</p></div><div id="comment-38480-info" class="comment-info"><span class="comment-age">(09 Dec '14, 06:10)</span> <span class="comment-user userinfo">Dianalab9</span></div></div><span id="38481"></span><div id="comment-38481" class="comment"><div id="post-38481-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-38481-info" class="comment-info"><span class="comment-age">(09 Dec '14, 06:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-38471" class="comment-tools"></div><div class="clear"></div><div id="comment-38471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

