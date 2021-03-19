+++
type = "question"
title = "specific tcp port bandwidth"
description = '''Hi, I would like to capture on real time the traffic that came from clients to a specific TCP port on my server. I am a newbie on wireshark and I would like some help to build a bash script that give the network bandwidth for each connection to my server. Thanks for any help. SP'''
date = "2015-12-15T15:16:00Z"
lastmod = "2015-12-16T04:12:00Z"
weight = 48551
keywords = [ "bandwidth", "port", "tcp" ]
aliases = [ "/questions/48551" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [specific tcp port bandwidth](/questions/48551/specific-tcp-port-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48551-score" class="post-score" title="current number of votes">0</div><span id="post-48551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to capture on real time the traffic that came from clients to a specific TCP port on my server. I am a newbie on wireshark and I would like some help to build a bash script that give the network bandwidth for each connection to my server.</p><p>Thanks for any help.</p><p>SP</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/0f3ff64bd97a7748cc4d63e6a7a8fc57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sperezz&#39;s gravatar image" /><p><span>sperezz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sperezz has no accepted answers">0%</span></p></div></div><div id="comments-container-48551" class="comments-container"></div><div id="comment-tools-48551" class="comment-tools"></div><div class="clear"></div><div id="comment-48551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48564"></span>

<div id="answer-container-48564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48564-score" class="post-score" title="current number of votes">0</div><span id="post-48564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Firstly note that neither Wireshark or tshark are great for long running captures as they will run out of memory due to state tracking between packets, see the Wiki <a href="https://wiki.wireshark.org/KnownBugs/OutOfMemory">page</a> on this issue for more information.</p><p>Given the above, when you have a capture file, Wireshark can show statistics by IP address which will relate to your client connections. This is in the Statistics -&gt; Conversations tables, then select the TCP tab.</p><p>For tshark, the corresponding option uses the -z conv,tcp arguments, see the man <a href="https://www.wireshark.org/docs/man-pages/tshark.html">page</a> for more info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48564" class="comments-container"></div><div id="comment-tools-48564" class="comment-tools"></div><div class="clear"></div><div id="comment-48564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

