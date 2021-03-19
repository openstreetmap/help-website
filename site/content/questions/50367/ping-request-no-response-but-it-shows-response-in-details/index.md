+++
type = "question"
title = "Ping request no response? But it shows response in details"
description = '''Good day, I try to investigate a annoying problem on my netgear R7000 router. I probably make a new topic for it. I installed and checked wireshark before but never really had the need to use it, until now.  First I setup ping tests to different pc&#x27;s in / outside my network.  Then when I check the p...'''
date = "2016-02-20T07:33:00Z"
lastmod = "2016-02-20T10:23:00Z"
weight = 50367
keywords = [ "ping", "response", "wireshark" ]
aliases = [ "/questions/50367" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Ping request no response? But it shows response in details](/questions/50367/ping-request-no-response-but-it-shows-response-in-details)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50367-score" class="post-score" title="current number of votes">0</div><span id="post-50367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good day,</p><p>I try to investigate a annoying problem on my netgear R7000 router. I probably make a new topic for it. I installed and checked wireshark before but never really had the need to use it, until now.</p><p>First I setup ping tests to different pc's in / outside my network.<br />
</p><p>Then when I check the ping requests I already see something weird. Wireshark says "No response found!" but in the details it just says "response frame 1847". So why does it say "no response found" while in the details it links the response to the request??</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_bKyovAS.PNG" alt="Wireshark_ping" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '16, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/e2d562659800c666fa24d7b946c9a079?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RFMuser&#39;s gravatar image" /><p><span>RFMuser</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RFMuser has no accepted answers">0%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Feb '16, 07:35</strong> </span></p></div></div><div id="comments-container-50367" class="comments-container"></div><div id="comment-tools-50367" class="comment-tools"></div><div class="clear"></div><div id="comment-50367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50368"></span>

<div id="answer-container-50368" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50368-score" class="post-score" title="current number of votes">2</div><span id="post-50368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RFMuser has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a known Wireshark bug. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11414">bug 11414</a> for details and to add your e-mail address to the bug CC list so you can be informed of any future updates/fixes for the bug if you so choose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '16, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-50368" class="comments-container"><span id="50370"></span><div id="comment-50370" class="comment"><div id="post-50370-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the fast response. I didn't expect a bug like that. Good to know. As I just started with WS I questioned my judgement first.</p></div><div id="comment-50370-info" class="comment-info"><span class="comment-age">(20 Feb '16, 10:23)</span> <span class="comment-user userinfo">RFMuser</span></div></div></div><div id="comment-tools-50368" class="comment-tools"></div><div class="clear"></div><div id="comment-50368-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

