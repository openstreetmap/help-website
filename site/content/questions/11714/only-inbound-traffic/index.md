+++
type = "question"
title = "Only inbound traffic"
description = '''Hi. I&#x27;m using Wireshark on the Windows 2008 Server PC with to interfaces and Firefront TMG installed on it. And when I start capturing packets with wireshark, it shows only inbound traffic. I tried it on both interfaces. Is this normal?'''
date = "2012-06-06T05:30:00Z"
lastmod = "2016-12-07T11:13:00Z"
weight = 11714
keywords = [ "wireshark" ]
aliases = [ "/questions/11714" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Only inbound traffic](/questions/11714/only-inbound-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11714-score" class="post-score" title="current number of votes">0</div><span id="post-11714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I'm using Wireshark on the Windows 2008 Server PC with to interfaces and Firefront TMG installed on it. And when I start capturing packets with wireshark, it shows only inbound traffic. I tried it on both interfaces.</p><p>Is this normal?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '12, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/9584eb70e2dcd6eecb4b96809e348a62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SKamil&#39;s gravatar image" /><p><span>SKamil</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SKamil has no accepted answers">0%</span></p></div></div><div id="comments-container-11714" class="comments-container"></div><div id="comment-tools-11714" class="comment-tools"></div><div class="clear"></div><div id="comment-11714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="11721"></span>

<div id="answer-container-11721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11721-score" class="post-score" title="current number of votes">0</div><span id="post-11721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>sounds like a similar problem as in this question</p><blockquote><p><code>http://ask.wireshark.org/questions/11560/unable-to-capture-or-display-incoming-tcpip-packets-with-port-8100</code></p></blockquote><p>Symantec Endpoint Protection prevented wireshark from seeing INCOMING packets. Maybe Firefront TMG does the same for OUTGOING packets in your environment.</p><p>See also: <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">http://wiki.wireshark.org/CaptureSetup/InterferingSoftware</a></p><p>Try to sniff on a different machine by using a mirror port on the switch or any other method described in the link below.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Ethernet</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '12, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11721" class="comments-container"></div><div id="comment-tools-11721" class="comment-tools"></div><div class="clear"></div><div id="comment-11721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21766"></span>

<div id="answer-container-21766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21766-score" class="post-score" title="current number of votes">0</div><span id="post-21766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>NetDMA and TCP Chimney Offload. Both technologies offload TCP processing to the NIC thereby bypassing the WinPCAP driver. Instructions for disabling: <a href="http://support.microsoft.com/kb/951037#LetMeFixItMyselfAlways">http://support.microsoft.com/kb/951037#LetMeFixItMyselfAlways</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '13, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/06a67351fbbe292f113a2a342f0641eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AbraCadaver&#39;s gravatar image" /><p><span>AbraCadaver</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AbraCadaver has no accepted answers">0%</span></p></div></div><div id="comments-container-21766" class="comments-container"></div><div id="comment-tools-21766" class="comment-tools"></div><div class="clear"></div><div id="comment-21766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55384"></span>

<div id="answer-container-55384" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55384-score" class="post-score" title="current number of votes">0</div><span id="post-55384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See: <a href="https://wiki.wireshark.org/CaptureSetup/InterferingSoftware">Interfering Software</a></p><p>On Windows 7 (64-bit), the SonicWall Global VPN Client (64-bit, version 4.9.9.1016) had to be uninstalled today to resolve a problem with only being able to monitor inbound traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '16, 15:35</strong></p><img src="https://secure.gravatar.com/avatar/01aa855068a6805deac3f3371c5b00d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kbulgrien&#39;s gravatar image" /><p><span>kbulgrien</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kbulgrien has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Sep '16, 05:55</strong> </span></p></div></div><div id="comments-container-55384" class="comments-container"><span id="57943"></span><div id="comment-57943" class="comment"><div id="post-57943-score" class="comment-score"></div><div class="comment-text"><p>Uninstalling the Global VPN fixed our issue too. Thanks.</p></div><div id="comment-57943-info" class="comment-info"><span class="comment-age">(07 Dec '16, 11:13)</span> <span class="comment-user userinfo">Werner G</span></div></div></div><div id="comment-tools-55384" class="comment-tools"></div><div class="clear"></div><div id="comment-55384-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

