+++
type = "question"
title = "Capturing gmail packets"
description = '''I was trying wireshark with different web pages when I log in to my gmail and then run wireshark and refresh gmail there is no http packet!why is it like this?'''
date = "2011-03-24T18:08:00Z"
lastmod = "2011-03-25T12:40:00Z"
weight = 3097
keywords = [ "http", "packet" ]
aliases = [ "/questions/3097" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing gmail packets](/questions/3097/capturing-gmail-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3097-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying wireshark with different web pages when I log in to my gmail and then run wireshark and refresh gmail there is no http packet!why is it like this?</p></div><div id="question-tags" class="tags-container tags">http packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '11, 18:08</strong></p><img src="https://secure.gravatar.com/avatar/0d1f835bfa8cc91838057ef65fc4d1c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A%20B&#39;s gravatar image" /><p>A B<br />
<span class="score" title="1 reputation points">1</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A B has no accepted answers">0%</span></p></div></div><div id="comments-container-3097" class="comments-container"><span id="3098"></span><div id="comment-3098" class="comment"><div id="post-3098-score" class="comment-score"></div><div class="comment-text"><p>Are you sure you're capturing on the right interface?</p></div><div id="comment-3098-info" class="comment-info"><span class="comment-age">(24 Mar '11, 19:44)</span> hansangb</div></div></div><div id="comment-tools-3097" class="comment-tools"></div><div class="clear"></div><div id="comment-3097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3102"></span>

<div id="answer-container-3102" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3102-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's for the same reason you don't want others to be able to capture and read your email. There is an <a href="http://en.wikipedia.org/wiki/Secure_Sockets_Layer">SSL</a> tunnel which carries the HTTP traffic, so it's hidden from you and the rest of the world, apart from the GMail server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 00:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3102" class="comments-container"></div><div id="comment-tools-3102" class="comment-tools"></div><div class="clear"></div><div id="comment-3102-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3129"></span>

<div id="answer-container-3129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3129-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>if you filter for SSL you will see packets, but will not be able to decode the data</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p>net_tech<br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div></div><div id="comments-container-3129" class="comments-container"></div><div id="comment-tools-3129" class="comment-tools"></div><div class="clear"></div><div id="comment-3129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

