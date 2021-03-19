+++
type = "question"
title = "Filter for [SYN] packages without [SYN,ACK] respons"
description = '''Our company is frequently involved in troubleshooting connection issues after a firewall implementation. Most of the times the firewall is blocking connections on ports which we were not aware of during investigation. Is it possible to have a filter which displays all TCP connection attempts , being...'''
date = "2013-05-24T11:24:00Z"
lastmod = "2013-05-24T12:41:00Z"
weight = 21453
keywords = [ "syn+ack" ]
aliases = [ "/questions/21453" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filter for \[SYN\] packages without \[SYN,ACK\] respons](/questions/21453/filter-for-syn-packages-without-synack-respons)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21453-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21453-score" class="post-score" title="current number of votes">0</div><span id="post-21453-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Our company is frequently involved in troubleshooting connection issues after a firewall implementation. Most of the times the firewall is blocking connections on ports which we were not aware of during investigation. Is it possible to have a filter which displays all TCP connection attempts , being [SYN] packages, which are NOT followed by a {SYN,ACK] acknowledgment from the destination host? This way we can quickly filter on connection attempts being blocked by the firewall.</p><p>Regards,</p><p>Fred van der Hoorn</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syn+ack" rel="tag" title="see questions tagged &#39;syn+ack&#39;">syn+ack</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '13, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/b7e76aa3051a46e38abb0817858e8f71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fred%20van%20der%20Hoorn&#39;s gravatar image" /><p><span>Fred van der...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fred van der Hoorn has no accepted answers">0%</span></p></div></div><div id="comments-container-21453" class="comments-container"></div><div id="comment-tools-21453" class="comment-tools"></div><div class="clear"></div><div id="comment-21453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21458"></span>

<div id="answer-container-21458" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21458-score" class="post-score" title="current number of votes">2</div><span id="post-21458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have not found a way (yet) to find a single SYN that does not get answered by a SYN/ACK. However, usually these are followed by a retransmission which can be found by using the filter:</p><pre><code>tcp.flags==2 &amp;&amp; tcp.time_relative&gt;0</code></pre><p>(You need to enable "Conversation Timestamps" in the TCP protocol preferences for this to work)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '13, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21458" class="comments-container"><span id="21459"></span><div id="comment-21459" class="comment"><div id="post-21459-score" class="comment-score"></div><div class="comment-text"><p>Superb!This is a classic example for rookie's answer vs seasoned person...</p></div><div id="comment-21459-info" class="comment-info"><span class="comment-age">(24 May '13, 12:02)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="21460"></span><div id="comment-21460" class="comment"><div id="post-21460-score" class="comment-score"></div><div class="comment-text"><p>This might be something where a expert message could be added in the future since they help a lot when searching for things that depend on packet relations. Something like "[lonely SYN]" :-)</p></div><div id="comment-21460-info" class="comment-info"><span class="comment-age">(24 May '13, 12:10)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="21461"></span><div id="comment-21461" class="comment"><div id="post-21461-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Your help is highly appreciated.</p><p>I will give it a try...where can I find the option enable "Conversation Timestamps" in the TCP protocol preferences ?</p><p>FYI Me question looks a lot like the question asked in "How to filter out streams that contain multiple SYN packets".</p><p>regards,</p><p>fred</p></div><div id="comment-21461-info" class="comment-info"><span class="comment-age">(24 May '13, 12:25)</span> <span class="comment-user userinfo">Fred van der...</span></div></div><span id="21462"></span><div id="comment-21462" class="comment"><div id="post-21462-score" class="comment-score"></div><div class="comment-text"><p>Edit&gt;Preferences&gt;Protocols&gt;TCP and you can check mark conversation timestamps box</p></div><div id="comment-21462-info" class="comment-info"><span class="comment-age">(24 May '13, 12:28)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="21464"></span><div id="comment-21464" class="comment"><div id="post-21464-score" class="comment-score"></div><div class="comment-text"><p>Solved...</p><p>The trick of enabling tcp timestamps AND the filter "tcp.flags==2 &amp;&amp; tcp.time_relative&gt;0" did the trick . Many thanks..this makes troubleshooting so much easier.</p><p>regards</p><p>fred</p></div><div id="comment-21464-info" class="comment-info"><span class="comment-age">(24 May '13, 12:41)</span> <span class="comment-user userinfo">Fred van der...</span></div></div></div><div id="comment-tools-21458" class="comment-tools"></div><div class="clear"></div><div id="comment-21458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21455"></span>

<div id="answer-container-21455" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21455-score" class="post-score" title="current number of votes">0</div><span id="post-21455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>tcp.flags==0x0002 in your display filter will display only "SINs" (or) tcp[13:1]==02</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '13, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 May '13, 11:38</strong> </span></p></div></div><div id="comments-container-21455" class="comments-container"><span id="21456"></span><div id="comment-21456" class="comment"><div id="post-21456-score" class="comment-score"></div><div class="comment-text"><p>True but it does not tell me whether the host the syn package has as destination responds with a syn,ack. I want to see all packages which are NOT followed by a syn,ack from the destination host. In that way I can quickly see to which hosts packages are send but for which NO response is received.</p></div><div id="comment-21456-info" class="comment-info"><span class="comment-age">(24 May '13, 11:37)</span> <span class="comment-user userinfo">Fred van der...</span></div></div><span id="21457"></span><div id="comment-21457" class="comment"><div id="post-21457-score" class="comment-score"></div><div class="comment-text"><p>Follow tcp stream option on syn packet will tell the whole story of that particular conversation. On syn packet right click and do a follow tcp stream to figure out on which conversation the syn-acks are missing.</p><p>(OR) Apply this display filter tcp.flags==0x0002 || tcp.flags==0x0012</p></div><div id="comment-21457-info" class="comment-info"><span class="comment-age">(24 May '13, 11:42)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div></div><div id="comment-tools-21455" class="comment-tools"></div><div class="clear"></div><div id="comment-21455-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

