+++
type = "question"
title = "Ethernet Frame Check Sequence Incorrect"
description = '''Hi All, I am trying to connect to exchange server 2013 using IMAP in C# code and the code is failing to authenticate the user. So I am debugging using wireshark to check where exactly the problem occurs. From the wireshark trace I see &quot;Ethernet Frame Check Sequence Incorrect&quot; for all my IMAP request...'''
date = "2015-02-18T02:26:00Z"
lastmod = "2015-02-24T01:47:00Z"
weight = 39921
keywords = [ "eth.fcs_bad", "imap" ]
aliases = [ "/questions/39921" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ethernet Frame Check Sequence Incorrect](/questions/39921/ethernet-frame-check-sequence-incorrect)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39921-score" class="post-score" title="current number of votes">0</div><span id="post-39921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All, I am trying to connect to exchange server 2013 using IMAP in C# code and the code is failing to authenticate the user. So I am debugging using wireshark to check where exactly the problem occurs. From the wireshark trace I see "Ethernet Frame Check Sequence Incorrect" for all my IMAP request whereas this error is not seen when I connect to exchange server 2010. So I am not sure what could be the problem with exchange server 2013 machine. Please help to resolve this issue.</p><p>Thank you,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eth.fcs_bad" rel="tag" title="see questions tagged &#39;eth.fcs_bad&#39;">eth.fcs_bad</span> <span class="post-tag tag-link-imap" rel="tag" title="see questions tagged &#39;imap&#39;">imap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Feb '15, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/b772adc853118674aa8d8792c1b49282?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SSK&#39;s gravatar image" /><p><span>SSK</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SSK has no accepted answers">0%</span></p></div></div><div id="comments-container-39921" class="comments-container"><span id="39928"></span><div id="comment-39928" class="comment"><div id="post-39928-score" class="comment-score"></div><div class="comment-text"><p>Exactly where do you capture in each instance?</p></div><div id="comment-39928-info" class="comment-info"><span class="comment-age">(18 Feb '15, 06:13)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="39938"></span><div id="comment-39938" class="comment"><div id="post-39938-score" class="comment-score"></div><div class="comment-text"><p>I am capturing this on my exchange server machine</p></div><div id="comment-39938-info" class="comment-info"><span class="comment-age">(19 Feb '15, 00:54)</span> <span class="comment-user userinfo">SSK</span></div></div><span id="40032"></span><div id="comment-40032" class="comment"><div id="post-40032-score" class="comment-score"></div><div class="comment-text"><blockquote><p>and the code is failing to authenticate the user.</p></blockquote><p>Does that mean you are able to establish a TCP connection and then you get an error message while you are authenticating the user?</p></div><div id="comment-40032-info" class="comment-info"><span class="comment-age">(23 Feb '15, 09:54)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="40040"></span><div id="comment-40040" class="comment"><div id="post-40040-score" class="comment-score"></div><div class="comment-text"><p>Yes you are correct. And also this happens not all the time few times authentication is failed and then it is working for few more times then fails. I couldn't find any specific pattern in which authentication fails.</p></div><div id="comment-40040-info" class="comment-info"><span class="comment-age">(24 Feb '15, 00:57)</span> <span class="comment-user userinfo">SSK</span></div></div></div><div id="comment-tools-39921" class="comment-tools"></div><div class="clear"></div><div id="comment-39921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40041"></span>

<div id="answer-container-40041" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40041-score" class="post-score" title="current number of votes">0</div><span id="post-40041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As a follow-up to you comment: the FCS errors have no meaning if you are able to establish a TCP connection. They are probably just the result of your capture setup.</p><p>To figure out why the server does not accept the user credentials, you could also look at the IMAP error code, but I guess you've done that already.</p><p>A better approach would be to active some sort of debugging on the target server (Exchange).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '15, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-40041" class="comments-container"></div><div id="comment-tools-40041" class="comment-tools"></div><div class="clear"></div><div id="comment-40041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

