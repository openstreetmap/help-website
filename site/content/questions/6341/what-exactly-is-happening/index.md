+++
type = "question"
title = "What exactly is happening?"
description = '''hi, first things first; i am a noob so i will be asking noobish questions i just captured a session for my LAN and was reading some intriguing traffic, apparently my ip address is sending check sums (i believe they are check sums due to the the pattern and byte-size,via UDP to a IP address in german...'''
date = "2011-09-14T00:42:00Z"
lastmod = "2011-09-14T04:22:00Z"
weight = 6341
keywords = [ "simple", "noob" ]
aliases = [ "/questions/6341" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What exactly is happening?](/questions/6341/what-exactly-is-happening)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6341-score" class="post-score" title="current number of votes">0</div><span id="post-6341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, first things first; i am a noob so i will be asking noobish questions</p><p>i just captured a session for my LAN and was reading some intriguing traffic,</p><p>apparently my ip address is sending check sums (i believe they are check sums due to the the pattern and byte-size,via UDP to a IP address in germany,</p><p>from the logs now i googled the MAC address and got that LiteOne Tech, apparently they manufacture routers and such, now i have a wireless netgear router and it appears the source is this LiteOne router and the destination is the netgear router, can someone explain or expound further on what exactly this traffic means?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-simple" rel="tag" title="see questions tagged &#39;simple&#39;">simple</span> <span class="post-tag tag-link-noob" rel="tag" title="see questions tagged &#39;noob&#39;">noob</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '11, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/54c32f3a73bb663b021217804178070c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slacker&#39;s gravatar image" /><p><span>slacker</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slacker has no accepted answers">0%</span></p></div></div><div id="comments-container-6341" class="comments-container"><span id="6347"></span><div id="comment-6347" class="comment"><div id="post-6347-score" class="comment-score"></div><div class="comment-text"><p>Given the nonexistent details you provide, there is nothing someone here can do to even guess what is happening - maybe you could provide some details or screenshots of your tracefile (anonymized of course)?</p></div><div id="comment-6347-info" class="comment-info"><span class="comment-age">(14 Sep '11, 01:39)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-6341" class="comment-tools"></div><div class="clear"></div><div id="comment-6341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6354"></span>

<div id="answer-container-6354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6354-score" class="post-score" title="current number of votes">1</div><span id="post-6354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The MAC addresses signify the local point-to-point link used to transport the packets. So here you'll see the MAC address of your computer (the LiteOne Tech) and the networking equipment connected to it (The NETGEAR).</p><p>On top of that rides IP, among other (network) protocols.</p><p>On top of that rides UDP, among other (transport) protocols.</p><p>On top of that are your 'checksums'.</p><p>So to gain further insight in your traffic, study IP and UDP as well. <a href="http://www.tcpipguide.com/">The TCP//IP guide</a> is a good starting point.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6354" class="comments-container"></div><div id="comment-tools-6354" class="comment-tools"></div><div class="clear"></div><div id="comment-6354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

