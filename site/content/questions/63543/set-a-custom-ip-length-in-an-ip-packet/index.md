+++
type = "question"
title = "set a custom ip length in an ip packet"
description = '''hi, i have a custom dissector, after dissect this custom protocol, the remaining of the packet should be dissect as an ip packet. but the length of ip packet report in my custom dissector and ip length field set to zero in data.  ip packets are like this : 0x45000000.... 0100 .... = Version: 4 .... ...'''
date = "2017-08-31T12:31:00Z"
lastmod = "2017-08-31T14:35:00Z"
weight = 63543
keywords = [ "ip", "dissector", "custum" ]
aliases = [ "/questions/63543" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [set a custom ip length in an ip packet](/questions/63543/set-a-custom-ip-length-in-an-ip-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63543-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63543-score" class="post-score" title="current number of votes">0</div><span id="post-63543-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, i have a custom dissector, after dissect this custom protocol, the remaining of the packet should be dissect as an ip packet. but the length of ip packet report in my custom dissector and ip length field set to zero in data.</p><p>ip packets are like this : 0x45000000....</p><pre><code>0100 .... = Version: 4
.... 0101 = Header Length: 20 bytes (5)
Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
Total Length:0</code></pre><p>i want to read Total Length from my custom protocol not the 2-3th bytes of data.can any one help me?thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-custum" rel="tag" title="see questions tagged &#39;custum&#39;">custum</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '17, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p><span>ghader</span><br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Aug '17, 12:32</strong> </span></p></div></div><div id="comments-container-63543" class="comments-container"></div><div id="comment-tools-63543" class="comment-tools"></div><div class="clear"></div><div id="comment-63543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63544"></span>

<div id="answer-container-63544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63544-score" class="post-score" title="current number of votes">0</div><span id="post-63544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but the length of ip packet report in my custom dissector and ip length field set to zero in data.</p></blockquote><p>Then it's not a valid IP packet. Fix your custom protocol, or its implementation, to provide a valid length field in the IP header.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '17, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63544" class="comments-container"></div><div id="comment-tools-63544" class="comment-tools"></div><div class="clear"></div><div id="comment-63544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

