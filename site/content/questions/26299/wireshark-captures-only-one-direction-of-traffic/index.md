+++
type = "question"
title = "Wireshark captures only one direction of traffic"
description = '''hi , I am using wireshark 1.10.2 with the latest winPcap 4.1.3 all 64 bit with windows 7 64 bit however , the only stream the wireshark capture is the incoming direction but all the outgong are not , no capture filter applied . I uninstalled the whole program with it&#x27;s dependencies and reinstall it ...'''
date = "2013-10-22T16:10:00Z"
lastmod = "2016-09-08T05:57:00Z"
weight = 26299
keywords = [ "capture-problem" ]
aliases = [ "/questions/26299" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark captures only one direction of traffic](/questions/26299/wireshark-captures-only-one-direction-of-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26299-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26299-score" class="post-score" title="current number of votes">0</div><span id="post-26299-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi , I am using wireshark 1.10.2 with the latest winPcap 4.1.3 all 64 bit with windows 7 64 bit however , the only stream the wireshark capture is the incoming direction but all the outgong are not , no capture filter applied . I uninstalled the whole program with it's dependencies and reinstall it back again with no diffrence . other tools like network monitor tool for microsoft can capture both direction on the same Laptop . note: i have symantic end point protection installed on my device.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-problem" rel="tag" title="see questions tagged &#39;capture-problem&#39;">capture-problem</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '13, 16:10</strong></p><img src="https://secure.gravatar.com/avatar/30a36a13a6e6c3859cb4b68912b9e763?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msecurity&#39;s gravatar image" /><p><span>Msecurity</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msecurity has no accepted answers">0%</span></p></div></div><div id="comments-container-26299" class="comments-container"><span id="26306"></span><div id="comment-26306" class="comment"><div id="post-26306-score" class="comment-score"></div><div class="comment-text"><p>Have you looked <a href="http://ask.wireshark.org/questions/11714/only-inbound-traffic">here</a>?</p></div><div id="comment-26306-info" class="comment-info"><span class="comment-age">(22 Oct '13, 19:49)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-26299" class="comment-tools"></div><div class="clear"></div><div id="comment-26299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26324"></span>

<div id="answer-container-26324" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26324-score" class="post-score" title="current number of votes">0</div><span id="post-26324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have seen this happen on a Ciena core switch (5305) when using a mirror; explanation from Ciena was that they only mirror ingress traffic on that particular model, not egress traffic. They tell me they are "working on a solution". Don't know what device you are spanned on, but might be something to check.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '13, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/3d1f94fd059d26805abac57ed6299bc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="randyp&#39;s gravatar image" /><p><span>randyp</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="randyp has no accepted answers">0%</span></p></div></div><div id="comments-container-26324" class="comments-container"></div><div id="comment-tools-26324" class="comment-tools"></div><div class="clear"></div><div id="comment-26324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55392"></span>

<div id="answer-container-55392" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55392-score" class="post-score" title="current number of votes">0</div><span id="post-55392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See also: <a href="https://wiki.wireshark.org/CaptureSetup/InterferingSoftware">InterferingSoftware</a></p><p>In my case, installed VPN software prevented seeing outbound traffic and had to be uninstalled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '16, 05:57</strong></p><img src="https://secure.gravatar.com/avatar/01aa855068a6805deac3f3371c5b00d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kbulgrien&#39;s gravatar image" /><p><span>kbulgrien</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kbulgrien has no accepted answers">0%</span></p></div></div><div id="comments-container-55392" class="comments-container"></div><div id="comment-tools-55392" class="comment-tools"></div><div class="clear"></div><div id="comment-55392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

