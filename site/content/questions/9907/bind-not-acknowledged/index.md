+++
type = "question"
title = "Bind not acknowledged"
description = '''I was doing a capture from client&#x27;s end and there were 43 packets in warnings marked with &quot;Bind not acknowledged&quot;. Could somebody explain me what this is? Google didn&#x27;t give me any help. Thanks. -Rakki'''
date = "2012-04-02T23:31:00Z"
lastmod = "2012-04-04T08:29:00Z"
weight = 9907
keywords = [ "not", "bind", "acknowledged", "tcp" ]
aliases = [ "/questions/9907" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bind not acknowledged](/questions/9907/bind-not-acknowledged)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9907-score" class="post-score" title="current number of votes">0</div><span id="post-9907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was doing a capture from client's end and there were 43 packets in warnings marked with "Bind not acknowledged". Could somebody explain me what this is? Google didn't give me any help. Thanks.</p><p>-Rakki</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-bind" rel="tag" title="see questions tagged &#39;bind&#39;">bind</span> <span class="post-tag tag-link-acknowledged" rel="tag" title="see questions tagged &#39;acknowledged&#39;">acknowledged</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '12, 23:31</strong></p><img src="https://secure.gravatar.com/avatar/387f58c09269aee8709bb3d68f33ea93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakki&#39;s gravatar image" /><p><span>rakki</span><br />
<span class="score" title="0 reputation points">0</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakki has no accepted answers">0%</span></p></div></div><div id="comments-container-9907" class="comments-container"></div><div id="comment-tools-9907" class="comment-tools"></div><div class="clear"></div><div id="comment-9907-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9933"></span>

<div id="answer-container-9933" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9933-score" class="post-score" title="current number of votes">0</div><span id="post-9933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It means that (whether correctly or incorrectly) Wireshark thinks those packets are DCE RPC packets (at this point, Windows is probably the largest user of DCE RPC), and those are <a href="http://pubs.opengroup.org/onlinepubs/009629399/chap12.htm#tagcjh_17_06_04_05">"negative acknowledgment" replies</a> to a <a href="http://pubs.opengroup.org/onlinepubs/009629399/chap12.htm#tagcjh_17_06_04_03">"bind" request</a>.</p><p>As <a href="http://pubs.opengroup.org/onlinepubs/009629399/">the DCE RPC 1.1 specification</a> says, <a href="http://pubs.opengroup.org/onlinepubs/009629399/chap2.htm#tagcjh_05_01_01_03">"a remote procedure call requires a remote binding"</a>. The "bind" operation is <a href="http://pubs.opengroup.org/onlinepubs/009629399/chap2.htm#tagcjh_05_02_01">the second of the two forms of binding-related operations</a>.</p><p>We'd have to see the full dissection of those packets to see what they mean in your capture; a bind_nak could mean a number of things.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '12, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Apr '12, 08:30</strong> </span></p></div></div><div id="comments-container-9933" class="comments-container"></div><div id="comment-tools-9933" class="comment-tools"></div><div class="clear"></div><div id="comment-9933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

