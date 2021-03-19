+++
type = "question"
title = "How to write dissector for http request body with special header?"
description = '''Hi, I want to write a dissector for http request body when a certain header present in the request (for example protocol: my protocol). Can somebody give me direction of how to do that? Thanks'''
date = "2013-02-14T14:24:00Z"
lastmod = "2013-02-15T07:01:00Z"
weight = 18642
keywords = [ "dissector" ]
aliases = [ "/questions/18642" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to write dissector for http request body with special header?](/questions/18642/how-to-write-dissector-for-http-request-body-with-special-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18642-score" class="post-score" title="current number of votes">1</div><span id="post-18642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to write a dissector for http request body when a certain header present in the request (for example protocol: my protocol). Can somebody give me direction of how to do that?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '13, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/7656adad2ef7c5ac31f6a55fcdb1734d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="seannguyen&#39;s gravatar image" /><p><span>seannguyen</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="seannguyen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Feb '13, 08:47</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-18642" class="comments-container"></div><div id="comment-tools-18642" class="comment-tools"></div><div class="clear"></div><div id="comment-18642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18643"></span>

<div id="answer-container-18643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18643-score" class="post-score" title="current number of votes">1</div><span id="post-18643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can only do that if you register for a specific media-type, as defined through http.content-type. There's no other way to influence the HTTP dissector for body dissection than altering the HTTP dissector code itself.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '13, 14:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-18643" class="comments-container"><span id="18655"></span><div id="comment-18655" class="comment"><div id="post-18655-score" class="comment-score"></div><div class="comment-text"><p>Can you show me how to do it with a specific media-type header? I am very new to wireshark dissector. Thanks</p></div><div id="comment-18655-info" class="comment-info"><span class="comment-age">(15 Feb '13, 07:01)</span> <span class="comment-user userinfo">seannguyen</span></div></div></div><div id="comment-tools-18643" class="comment-tools"></div><div class="clear"></div><div id="comment-18643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

