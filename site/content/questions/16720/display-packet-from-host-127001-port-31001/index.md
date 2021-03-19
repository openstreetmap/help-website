+++
type = "question"
title = "display packet from host 127.0.0.1 port 31001"
description = '''I have a receiver on usb that sends packets to host 127.0.0.1, port 31001. How can I get wireshark to display these packets? I am not interested in capturing, just displaying to insure the receiver is sending packets ok.'''
date = "2012-12-07T22:25:00Z"
lastmod = "2012-12-08T02:32:00Z"
weight = 16720
keywords = [ "recvraddress" ]
aliases = [ "/questions/16720" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [display packet from host 127.0.0.1 port 31001](/questions/16720/display-packet-from-host-127001-port-31001)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16720-score" class="post-score" title="current number of votes">0</div><span id="post-16720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a receiver on usb that sends packets to host 127.0.0.1, port 31001. How can I get wireshark to display these packets? I am not interested in capturing, just displaying to insure the receiver is sending packets ok.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-recvraddress" rel="tag" title="see questions tagged &#39;recvraddress&#39;">recvraddress</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '12, 22:25</strong></p><img src="https://secure.gravatar.com/avatar/ebcf41b9b16792a0c9b571b1179eb80e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krychak4a&#39;s gravatar image" /><p><span>krychak4a</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krychak4a has no accepted answers">0%</span></p></div></div><div id="comments-container-16720" class="comments-container"></div><div id="comment-tools-16720" class="comment-tools"></div><div class="clear"></div><div id="comment-16720-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16721"></span>

<div id="answer-container-16721" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16721-score" class="post-score" title="current number of votes">2</div><span id="post-16721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="krychak4a has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't display packets unless <em>something</em> has captured them. If the packets are being sent to 127.0.0.1, that's a loopback address, so you might only see it if you can <a href="http://wiki.wireshark.org/CaptureSetup/Loopback">capture on a loopback address</a>, which you can't do on all operating systems.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '12, 00:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16721" class="comments-container"><span id="16723"></span><div id="comment-16723" class="comment"><div id="post-16723-score" class="comment-score"></div><div class="comment-text"><p>Thank you, Guy. That was what I was afraid of after reading the help files and faq's. I thought I might have to develope a small program to read the port involved. I do have a program that does, and decodes the packets, it is not my program, so I cannot modify it. Again, thanks for your fast reply. John</p></div><div id="comment-16723-info" class="comment-info"><span class="comment-age">(08 Dec '12, 02:32)</span> <span class="comment-user userinfo">krychak4a</span></div></div></div><div id="comment-tools-16721" class="comment-tools"></div><div class="clear"></div><div id="comment-16721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

