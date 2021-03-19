+++
type = "question"
title = "SIP Notify Message Body is gzip&#x27;ed"
description = '''Hi, I am looking to find out if Wireshark can decode the Body of a SIP Notify when the body is gzipped by the sender. I can see the SIP header, but just not the body. Thanks.'''
date = "2012-03-05T17:37:00Z"
lastmod = "2012-03-05T20:02:00Z"
weight = 9374
keywords = [ "body", "gzip", "sip" ]
aliases = [ "/questions/9374" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SIP Notify Message Body is gzip'ed](/questions/9374/sip-notify-message-body-is-gziped)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9374-score" class="post-score" title="current number of votes">0</div><span id="post-9374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am looking to find out if Wireshark can decode the Body of a SIP Notify when the body is gzipped by the sender. I can see the SIP header, but just not the body.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-body" rel="tag" title="see questions tagged &#39;body&#39;">body</span> <span class="post-tag tag-link-gzip" rel="tag" title="see questions tagged &#39;gzip&#39;">gzip</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '12, 17:37</strong></p><img src="https://secure.gravatar.com/avatar/f63fd202ed54195f69998fc01c57f3fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="decodeme&#39;s gravatar image" /><p><span>decodeme</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="decodeme has no accepted answers">0%</span></p></div></div><div id="comments-container-9374" class="comments-container"></div><div id="comment-tools-9374" class="comment-tools"></div><div class="clear"></div><div id="comment-9374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9380"></span>

<div id="answer-container-9380" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9380-score" class="post-score" title="current number of votes">0</div><span id="post-9380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The HTTP dissector includes code to handle gzipped content encodings of the body, but not gzipped transfer encodings.</p><p>The SIP dissector doesn't include code for either of those, so it can't decode gzipped SIP bodies.</p><p>If you want support for that in SIP, file an enhancement request at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '12, 20:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9380" class="comments-container"></div><div id="comment-tools-9380" class="comment-tools"></div><div class="clear"></div><div id="comment-9380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

