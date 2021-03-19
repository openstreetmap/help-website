+++
type = "question"
title = "check bidirectional traffic"
description = '''Hi, I have an application, that I would like to check if is using bidirectional traffic. Is possible to check these with wireshark? Thanks and sorry for my English!'''
date = "2016-06-16T09:30:00Z"
lastmod = "2016-06-16T14:30:00Z"
weight = 53497
keywords = [ "traffic" ]
aliases = [ "/questions/53497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [check bidirectional traffic](/questions/53497/check-bidirectional-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53497-score" class="post-score" title="current number of votes">0</div><span id="post-53497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have an application, that I would like to check if is using bidirectional traffic. Is possible to check these with wireshark? Thanks and sorry for my English!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '16, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/14f4b98ce1fbecd6533e668a69a130d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="absolut&#39;s gravatar image" /><p><span>absolut</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="absolut has no accepted answers">0%</span></p></div></div><div id="comments-container-53497" class="comments-container"></div><div id="comment-tools-53497" class="comment-tools"></div><div class="clear"></div><div id="comment-53497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53498"></span>

<div id="answer-container-53498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53498-score" class="post-score" title="current number of votes">0</div><span id="post-53498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you can see bidirectional traffic in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '16, 09:46</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-53498" class="comments-container"><span id="53499"></span><div id="comment-53499" class="comment"><div id="post-53499-score" class="comment-score"></div><div class="comment-text"><p>Thanks... but how could I can identificate?</p></div><div id="comment-53499-info" class="comment-info"><span class="comment-age">(16 Jun '16, 09:56)</span> <span class="comment-user userinfo">absolut</span></div></div><span id="53502"></span><div id="comment-53502" class="comment"><div id="post-53502-score" class="comment-score"></div><div class="comment-text"><p>Wireshark will show ingress/egress traffic to/from the capture point. Look at the Source address. Ingress traffic will have the Source address as the capture point. Egress traffic will have a different source address.</p></div><div id="comment-53502-info" class="comment-info"><span class="comment-age">(16 Jun '16, 12:45)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="53504"></span><div id="comment-53504" class="comment"><div id="post-53504-score" class="comment-score"></div><div class="comment-text"><p>Sorry I understand that the bi-directional communication always begin by source ip to destination ip, and communicates by the same port. So if I see like these:</p><pre><code>12335   1642.502395000  192.168.1.140   192.168.1.153   GIOP    165 GIOP 1.2 Request, s=99 id=84: op=CRB_ClientKeepAlive\000
12336   1642.502785000  192.168.1.153   192.168.1.140   GIOP    82  GIOP 1.2 Reply, s=16 id=84: No Exception
12337   1642.657680000  192.168.1.140   192.168.1.153   TCP 54  1093→38960 [ACK] Seq=5906 Ack=13916 Win=64557 Len=0</code></pre><p>It seems that is not bi-directional no? thanks!</p></div><div id="comment-53504-info" class="comment-info"><span class="comment-age">(16 Jun '16, 14:03)</span> <span class="comment-user userinfo">absolut</span></div></div><span id="53505"></span><div id="comment-53505" class="comment"><div id="post-53505-score" class="comment-score"></div><div class="comment-text"><p>It <strong>is</strong> bidirectional. The port numbers the participants use are independent of each other and tshark doesn't show them by default.</p><p>So one participant uses IP address <code>x.x.x.x</code> port <code>XXXX</code> and the other one uses IP address <code>y.y.y.y</code> port <code>YYYY</code>. One direction of the communication is then <code>x.x.x.x:XXXX -&gt; y.y.y.y:YYYY</code>, the other direction is <code>y.y.y.y:YYYY -&gt; x.x.x.x:XXXX</code>.</p><p>Besides, tshark shows the name of the highest-level protocol it could find in the frame. So if a transport protocol (TCP in your case) is used to convey PDUs of an application protocol (GIOP in your case), the frames which carry any GIOP as TCP's payload are marked as GIOP ones; the frames belonging to the same TCP session but carrying only TCP's overhead are marked as TCP ones (frame 12337 in your example).</p></div><div id="comment-53505-info" class="comment-info"><span class="comment-age">(16 Jun '16, 14:30)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-53498" class="comment-tools"></div><div class="clear"></div><div id="comment-53498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

