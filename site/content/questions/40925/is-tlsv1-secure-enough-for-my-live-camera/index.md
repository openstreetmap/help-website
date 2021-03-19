+++
type = "question"
title = "is TLSV1 secure enough for my live camera"
description = '''I recently purchased a live camera which allows me to view the live video from the phone in real time. To make sure it can protect my privacy well, I used wireshark to analyse the network traffic. It uses TLSV1 to transfer the video data between the app and server. 1.I would like to know if TLSV1 is...'''
date = "2015-03-26T19:48:00Z"
lastmod = "2015-03-29T09:46:00Z"
weight = 40925
keywords = [ "tlsv1" ]
aliases = [ "/questions/40925" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [is TLSV1 secure enough for my live camera](/questions/40925/is-tlsv1-secure-enough-for-my-live-camera)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40925-score" class="post-score" title="current number of votes">0</div><span id="post-40925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently purchased a live camera which allows me to view the live video from the phone in real time. To make sure it can protect my privacy well, I used wireshark to analyse the network traffic.</p><p>It uses TLSV1 to transfer the video data between the app and server.</p><p>1.I would like to know if TLSV1 is secure enough as there is already TLSV1.1 and TLSV1.2 in place. And if the connection needs to last for 30 mins in order to decrypt it?</p><p>2.The live camera caches the live video in order to play the video smoothly, is it possible for the hacker to get the cached data by the hacker even the transportation is in SSL?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2015-03-27_at_3.22.44_AM.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tlsv1" rel="tag" title="see questions tagged &#39;tlsv1&#39;">tlsv1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '15, 19:48</strong></p><img src="https://secure.gravatar.com/avatar/c64b21faa48274323bb3d9e512b7339d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Alex&#39;s gravatar image" /><p><span>Yang Alex</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Alex has no accepted answers">0%</span></p></img></div></div><div id="comments-container-40925" class="comments-container"></div><div id="comment-tools-40925" class="comment-tools"></div><div class="clear"></div><div id="comment-40925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40982"></span>

<div id="answer-container-40982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40982-score" class="post-score" title="current number of votes">1</div><span id="post-40982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>While SSLv2 and SSLv3 are demonstratively broken, TLSv1.0 as protocol is still safe if configured correctly. One issue with TLSv1.0 (<a href="https://en.wikipedia.org/wiki/Transport_Layer_Security#BEAST_attack">BEAST</a>) was in combination with cipher suites using the CBC mode, but this is largely mitigated by clients.</li><li>TLS protects only the transport. Once the data reaches the end-user device, the security of the data depends on that device. That (cached) data could still be acquired by "the hacker" if he has access to your phone (for example, through a malicious application on the phone).</li></ol><p>I suggest you to run your client through <a href="https://www.ssllabs.com/ssltest/">https://www.ssllabs.com/ssltest/</a> for a configuration check. You need to configure a DNS name to point to the external IP address of the camera. Only port 443 is supported via the web interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '15, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-40982" class="comments-container"></div><div id="comment-tools-40982" class="comment-tools"></div><div class="clear"></div><div id="comment-40982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

