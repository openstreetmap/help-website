+++
type = "question"
title = "RADIUS Packet handling"
description = '''Hi, I am facing issue with radius accounting request Vs response which is affecting my radius proxy performance. I am seeing delay between radius proxy &amp;amp; radius server. So whenever I plot IO graph (filter name = radius.time) it shows me delay of 5 secs between Request Vs Response. But my radius ...'''
date = "2011-02-22T12:40:00Z"
lastmod = "2011-02-24T08:12:00Z"
weight = 2501
keywords = [ "graph" ]
aliases = [ "/questions/2501" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [RADIUS Packet handling](/questions/2501/radius-packet-handling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2501-score" class="post-score" title="current number of votes">0</div><span id="post-2501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am facing issue with radius accounting request Vs response which is affecting my radius proxy performance.</p><p>I am seeing delay between radius proxy &amp; radius server. So whenever I plot IO graph (filter name = radius.time) it shows me delay of 5 secs between Request Vs Response. But my radius server vendor is saying that "wireshark is incorrectly showing that information and actually there is no such delay"</p><p>Could someone please help me identifying what exactly is wrong in wireshark handling?</p><p>If required I can share radius packet trace.</p><p>Regards, Vijay</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '11, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p><span>Vijay Gharge</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-2501" class="comments-container"></div><div id="comment-tools-2501" class="comment-tools"></div><div class="clear"></div><div id="comment-2501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2505"></span>

<div id="answer-container-2505" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2505-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2505-score" class="post-score" title="current number of votes">1</div><span id="post-2505-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Vijay Gharge has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you checked the responses manualy? One thing I can imagine is that your RadiusID is being rotated within the time frame of the capture file. I'm not sure whether the radius dissector currently account for that situation. It might just link each response to the first request with the same RadiusID. If that's the case, please open a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>If not, please do share the radius trace-file so we can have a look at what is causing this behavior...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '11, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2505" class="comments-container"><span id="2551"></span><div id="comment-2551" class="comment"><div id="post-2551-score" class="comment-score"></div><div class="comment-text"><p>Hi Sake,</p><p>I have raised bug in wireshark bugzilla. I have also provided radius packet trace for more info. I hope that this will be fixed :-)</p></div><div id="comment-2551-info" class="comment-info"><span class="comment-age">(24 Feb '11, 08:12)</span> <span class="comment-user userinfo">Vijay Gharge</span></div></div></div><div id="comment-tools-2505" class="comment-tools"></div><div class="clear"></div><div id="comment-2505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

