+++
type = "question"
title = "Http request method GET unavailable on PC Win"
description = '''Good evening, We are encountering a problem when sniffing network traffic on a PC Win 7 (64 bit). The problem is that we cannot see in the main area any packet when the filter is http.request.method==GET. Instead we are able to see packets, using a MAC device and sniffing the same network traffic. W...'''
date = "2016-04-28T08:48:00Z"
lastmod = "2016-04-29T03:07:00Z"
weight = 52056
keywords = [ "windows", "http", "unavailable", "get" ]
aliases = [ "/questions/52056" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Http request method GET unavailable on PC Win](/questions/52056/http-request-method-get-unavailable-on-pc-win)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52056-score" class="post-score" title="current number of votes">0</div><span id="post-52056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good evening,</p><p>We are encountering a problem when sniffing network traffic on a PC Win 7 (64 bit). The problem is that we cannot see in the main area any packet when the filter is http.request.method==GET.</p><p>Instead we are able to see packets, using a MAC device and sniffing the same network traffic.</p><p>We are encountering the problem both in wifi and ethernet.</p><p>Could you please help us?</p><p>Thank you,</p><p>Alberto</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-unavailable" rel="tag" title="see questions tagged &#39;unavailable&#39;">unavailable</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '16, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/e17a3a5005a366888535cd39087c64f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abusnelli&#39;s gravatar image" /><p><span>abusnelli</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abusnelli has no accepted answers">0%</span></p></div></div><div id="comments-container-52056" class="comments-container"><span id="52061"></span><div id="comment-52061" class="comment"><div id="post-52061-score" class="comment-score"></div><div class="comment-text"><p>Can you share the capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>, Google Drive, DropBox etc. and edit your question to add a link to the capture?</p></div><div id="comment-52061-info" class="comment-info"><span class="comment-age">(28 Apr '16, 13:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="52069"></span><div id="comment-52069" class="comment"><div id="post-52069-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>here you can find a capture taken from www.corriere.it:</p><p><a href="https://www.dropbox.com/s/aezx2u5tv6fz7wb/corriere.pcapng?dl=0">https://www.dropbox.com/s/aezx2u5tv6fz7wb/corriere.pcapng?dl=0</a></p><p>You can see that no packet is visible if you set the "http.request.method==GET" filter.</p></div><div id="comment-52069-info" class="comment-info"><span class="comment-age">(29 Apr '16, 00:39)</span> <span class="comment-user userinfo">abusnelli</span></div></div><span id="52071"></span><div id="comment-52071" class="comment"><div id="post-52071-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-52071-info" class="comment-info"><span class="comment-age">(29 Apr '16, 02:10)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-52056" class="comment-tools"></div><div class="clear"></div><div id="comment-52056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52073"></span>

<div id="answer-container-52073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52073-score" class="post-score" title="current number of votes">0</div><span id="post-52073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You appear to have only captured inbound traffic, i.e. the HTTP responses, so there are no HTTP requests that have the GET method.</p><p>Did you apply a capture filter when making the capture?</p><p>If not, you may have software installed on your PC that prevents capturing of outbound traffic, e.g. VPN software, Endpoint protection etc. This is a quite frequent on windows, there are many questions on this site about the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '16, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-52073" class="comments-container"></div><div id="comment-tools-52073" class="comment-tools"></div><div class="clear"></div><div id="comment-52073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

