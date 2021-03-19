+++
type = "question"
title = "Echo (ping) reply not generated, but can see Echo (ping) request is received on interface"
description = '''I have an odd situation 10.50.50.25 --- |Svr02| --- 10.50.50.26  10.50.50.16 --- |Srv01| --- 10.50.50.15 When I ping 10.50.50.25 and 10.50.50.26 from Srv01 I can see the echo requests and echo replies are received and the pings report as successful. When I ping 10.50.50.16 and 10.50.50.15 from Srv02...'''
date = "2015-11-09T10:47:00Z"
lastmod = "2015-11-10T00:33:00Z"
weight = 47435
keywords = [ "ping", "error" ]
aliases = [ "/questions/47435" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Echo (ping) reply not generated, but can see Echo (ping) request is received on interface](/questions/47435/echo-ping-reply-not-generated-but-can-see-echo-ping-request-is-received-on-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47435-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47435-score" class="post-score" title="current number of votes">0</div><span id="post-47435-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an odd situation</p><p>10.50.50.25 --- |Svr02| --- 10.50.50.26</p><p>10.50.50.16 --- |Srv01| --- 10.50.50.15</p><p>When I ping 10.50.50.25 and 10.50.50.26 from Srv01 I can see the echo requests and echo replies are received and the pings report as successful.</p><p>When I ping 10.50.50.16 and 10.50.50.15 from Srv02 only 10.50.50.16 sends the echo replies.</p><p>When doing a wireshark trace I can see the failing ping request from Srv02 goes like this</p><ul><li>echo request sent out of 10.50.50.26</li><li>interface echo request recieved on 10.50.50.15</li><li>Then however, I see no attempt on Srv01 to send an echo reply on any interface</li></ul><p>Why could this be?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '15, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/72d6bea28bbbf0536499ac3c76de8948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wshark_man_123&#39;s gravatar image" /><p><span>wshark_man_123</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wshark_man_123 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Nov '15, 12:29</strong> </span></p></div></div><div id="comments-container-47435" class="comments-container"></div><div id="comment-tools-47435" class="comment-tools"></div><div class="clear"></div><div id="comment-47435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47437"></span>

<div id="answer-container-47437" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47437-score" class="post-score" title="current number of votes">1</div><span id="post-47437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You haven't stated whether the icmp echo requests from Srv01 are sent from 10.50.50.15 or 10.50.50.16. I would suspect some firewall to block icmp on the 10.50.50.15 interface of srv01. What happens if you shut down 10.50.50.16 and try to ping 10.50.50.15 from Srv02?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 12:47</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-47437" class="comments-container"><span id="47450"></span><div id="comment-47450" class="comment"><div id="post-47450-score" class="comment-score"></div><div class="comment-text"><p>I can see Windows Firewall drops inbound for the failed pings which is why no echo reply is being generated.</p></div><div id="comment-47450-info" class="comment-info"><span class="comment-age">(09 Nov '15, 23:36)</span> <span class="comment-user userinfo">wshark_man_123</span></div></div><span id="47455"></span><div id="comment-47455" class="comment"><div id="post-47455-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-47455-info" class="comment-info"><span class="comment-age">(10 Nov '15, 00:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="47457"></span><div id="comment-47457" class="comment"><div id="post-47457-score" class="comment-score"></div><div class="comment-text"><p>So my assumption was correct and according to the principles of the site you should mark my answer as correct/helpful.</p><p>If the behaviour seems weird to you: libpcap (Wireshark) is hooked as close as possible to the hardware so it gets any incoming packet <em>before</em> the Windows firewall. So you can see <em>incoming</em> packets dropped by the firewall in the capture but they don't reach higher levels of the protocol stack because the firewall drops them. For <em>sent</em> packets, however, the same arrangement means that if an application sends a packet but the firewall drops it, the packet does not reach libpcap and so you won't see it in the capture. This would hardly happen in case of icmp but it does happen for application protocols.</p></div><div id="comment-47457-info" class="comment-info"><span class="comment-age">(10 Nov '15, 00:33)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-47437" class="comment-tools"></div><div class="clear"></div><div id="comment-47437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

