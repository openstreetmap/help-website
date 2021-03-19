+++
type = "question"
title = "ssl continuation data?"
description = '''hello, can someone please help me understand what &#x27;continuation data&#x27; in &#x27;Info&#x27; column means? protocol was SSL. thank you'''
date = "2017-06-14T17:22:00Z"
lastmod = "2017-06-15T08:35:00Z"
weight = 62035
keywords = [ "ssl", "data", "continuation" ]
aliases = [ "/questions/62035" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [ssl continuation data?](/questions/62035/ssl-continuation-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62035-score" class="post-score" title="current number of votes">1</div><span id="post-62035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello,</p><p>can someone please help me understand what 'continuation data' in 'Info' column means? protocol was SSL.</p><p>thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-continuation" rel="tag" title="see questions tagged &#39;continuation&#39;">continuation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '17, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/caeeac1c6da5e015e73afca647add18b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rapidusync&#39;s gravatar image" /><p><span>rapidusync</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rapidusync has no accepted answers">0%</span></p></div></div><div id="comments-container-62035" class="comments-container"></div><div id="comment-tools-62035" class="comment-tools"></div><div class="clear"></div><div id="comment-62035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62044"></span>

<div id="answer-container-62044" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62044-score" class="post-score" title="current number of votes">0</div><span id="post-62044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rapidusync has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Frames are marked as "Continuation Data" when the contents are not fully understood. It happens when TLS records are split over multiple TCP segments and one of these cases happen:</p><ul><li>Capture begins in the middle of an existing SSL/TLS connection, not capturing the begin of a record.</li><li>Out-of-order packets where the begin and end of a record are swapped (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9461">Bug 9461</a>).</li><li>TCP reassembly is disabled (so while the begin of a record is partially dissected, the second half will not be recognized).</li></ul><p>Finally, it could be truly the case that the protocol under analysis is not really TLS. For example, some users could try to bypass firewalls by running their VPN software over port 443 which is registered for HTTPS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '17, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-62044" class="comments-container"></div><div id="comment-tools-62044" class="comment-tools"></div><div class="clear"></div><div id="comment-62044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

