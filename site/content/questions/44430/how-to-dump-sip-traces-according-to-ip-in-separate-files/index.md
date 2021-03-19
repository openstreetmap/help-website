+++
type = "question"
title = "How to dump sip traces according to ip in separate files?"
description = '''Hi, I have Opensips running on a static ip &quot;192.168.1.60&quot; to which multiple users are registered with different Ips. Like User A ip =&quot;192.168.1.43&quot; User B ip =&quot;192.168.1.33&quot; User C ip =&quot;192.168.1.23&quot; etc I want Sip dump traces, user wise(their ip based) into separate files. How can i do this? Any he...'''
date = "2015-07-24T06:52:00Z"
lastmod = "2015-07-24T10:51:00Z"
weight = 44430
keywords = [ "tshark", "voip", "wireshark" ]
aliases = [ "/questions/44430" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to dump sip traces according to ip in separate files?](/questions/44430/how-to-dump-sip-traces-according-to-ip-in-separate-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44430-score" class="post-score" title="current number of votes">0</div><span id="post-44430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have Opensips running on a static ip "192.168.1.60" to which multiple users are registered with different Ips. Like</p><p>User A ip ="192.168.1.43" User B ip ="192.168.1.33" User C ip ="192.168.1.23" etc</p><p>I want Sip dump traces, user wise(their ip based) into separate files. How can i do this?</p><p>Any help would be much appreciated.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '15, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/0fd6a9123c5686dec9ced8b314643a2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aqsyounas&#39;s gravatar image" /><p><span>aqsyounas</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aqsyounas has no accepted answers">0%</span></p></div></div><div id="comments-container-44430" class="comments-container"></div><div id="comment-tools-44430" class="comment-tools"></div><div class="clear"></div><div id="comment-44430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44438"></span>

<div id="answer-container-44438" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44438-score" class="post-score" title="current number of votes">0</div><span id="post-44438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>opensips provides a tool that does exactly what you need</p><p>Look for: <strong>pcapsipdump</strong><br />
</p><blockquote><p><a href="http://www.opensips.org/Documentation/Tools#toc7">http://www.opensips.org/Documentation/Tools#toc7</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '15, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jul '15, 10:51</strong> </span></p></div></div><div id="comments-container-44438" class="comments-container"></div><div id="comment-tools-44438" class="comment-tools"></div><div class="clear"></div><div id="comment-44438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

