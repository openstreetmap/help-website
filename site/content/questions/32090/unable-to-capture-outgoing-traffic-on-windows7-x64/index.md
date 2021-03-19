+++
type = "question"
title = "Unable to capture OUTGOING traffic on Windows7 x64"
description = '''I&#x27;ve tested wireshark latest versions (now 1.10.6), even developement one. When I try to capture packets I can&#x27;t see my own OUTGOING packets. There&#x27;s no filter issues. No filter. Laptoc works fine (connection to internet, so on...) BUT OUTgoing packets from my @IP are not shown. Any workaround? '''
date = "2014-04-23T01:54:00Z"
lastmod = "2014-04-24T04:02:00Z"
weight = 32090
keywords = [ "windows7", "outbound", "outgoing" ]
aliases = [ "/questions/32090" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to capture OUTGOING traffic on Windows7 x64](/questions/32090/unable-to-capture-outgoing-traffic-on-windows7-x64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32090-score" class="post-score" title="current number of votes">0</div><span id="post-32090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've tested wireshark latest versions (now 1.10.6), even developement one. When I try to capture packets I can't see my own OUTGOING packets. There's no filter issues. No filter. Laptoc works fine (connection to internet, so on...) BUT OUTgoing packets from my <span>@IP</span> are not shown.</p><p>Any workaround?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-outbound" rel="tag" title="see questions tagged &#39;outbound&#39;">outbound</span> <span class="post-tag tag-link-outgoing" rel="tag" title="see questions tagged &#39;outgoing&#39;">outgoing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/f318e43fc6efc020c770cc335a67626f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CarlosDD&#39;s gravatar image" /><p><span>CarlosDD</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CarlosDD has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Apr '14, 11:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-32090" class="comments-container"></div><div id="comment-tools-32090" class="comment-tools"></div><div class="clear"></div><div id="comment-32090-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32113"></span>

<div id="answer-container-32113" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32113-score" class="post-score" title="current number of votes">2</div><span id="post-32113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please read the questions with the following tags:</p><p><strong>outgoing</strong> or <strong>outbound</strong></p><blockquote><p><a href="http://ask.wireshark.org/tags/outgoing/">http://ask.wireshark.org/tags/outgoing/</a></p></blockquote><p>Usually the reason for this is some software on the capturing system (Enpoint Security, VPN, IPS, etc.) that prevents Wireshark from seeing outgoing/outbound packets. You'll find all the details in the other questions and answers.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32113" class="comments-container"><span id="32141"></span><div id="comment-32141" class="comment"><div id="post-32141-score" class="comment-score"></div><div class="comment-text"><p>CORRECT. In our case, unchecking "Stonegate IPSec VPN driver" on NIC properties, issue was solved. Thanks.</p></div><div id="comment-32141-info" class="comment-info"><span class="comment-age">(24 Apr '14, 04:00)</span> <span class="comment-user userinfo">CarlosDD</span></div></div><span id="32142"></span><div id="comment-32142" class="comment"><div id="post-32142-score" class="comment-score"></div><div class="comment-text"><p><span>@CarlosDD</span></p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-32142-info" class="comment-info"><span class="comment-age">(24 Apr '14, 04:02)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-32113" class="comment-tools"></div><div class="clear"></div><div id="comment-32113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

