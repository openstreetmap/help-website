+++
type = "question"
title = "How to find each session in wireshark?"
description = '''hi, my question is how to find each session in wireshark? i cant find any session id in pcap file in wireshark... or i need try other filter conditions without session id?'''
date = "2015-03-11T21:56:00Z"
lastmod = "2015-03-12T20:43:00Z"
weight = 40502
keywords = [ "session-id", "traffic-analysis", "pcap", "packet", "wireshark" ]
aliases = [ "/questions/40502" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find each session in wireshark?](/questions/40502/how-to-find-each-session-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40502-score" class="post-score" title="current number of votes">0</div><span id="post-40502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>my question is how to find each session in wireshark?</p><p>i cant find any session id in pcap file in wireshark...</p><p>or i need try other filter conditions without session id?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-session-id" rel="tag" title="see questions tagged &#39;session-id&#39;">session-id</span> <span class="post-tag tag-link-traffic-analysis" rel="tag" title="see questions tagged &#39;traffic-analysis&#39;">traffic-analysis</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '15, 21:56</strong></p><img src="https://secure.gravatar.com/avatar/c99f54184fa51744dc6936afe55cec4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dong0129&#39;s gravatar image" /><p><span>dong0129</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dong0129 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Mar '15, 21:56</strong> </span></p></div></div><div id="comments-container-40502" class="comments-container"><span id="40505"></span><div id="comment-40505" class="comment"><div id="post-40505-score" class="comment-score"></div><div class="comment-text"><p>What kind of "session id" are you talking about?</p></div><div id="comment-40505-info" class="comment-info"><span class="comment-age">(12 Mar '15, 01:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-40502" class="comment-tools"></div><div class="clear"></div><div id="comment-40502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40530"></span>

<div id="answer-container-40530" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40530-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40530-score" class="post-score" title="current number of votes">0</div><span id="post-40530-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i cant find any session id in pcap file in wireshark</p></blockquote><p>Perhaps the protocols in the capture have no session ID fields.</p><p>For some protocols, there is no notion of a session; that's the case for NFS.</p><p>Some other protocols that use TCP have one session per TCP connection, so you would have to filter on, for example, the TCP connection number field (which is assigned by Wireshark; it's not part of the protocol - Wireshark determines TCP connections based on the source and destination addresses and ports and on connection initiation (3-way handshake) and termination (FIN handshake).</p><p>For what protocols are you trying to find sessions?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '15, 20:43</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40530" class="comments-container"></div><div id="comment-tools-40530" class="comment-tools"></div><div class="clear"></div><div id="comment-40530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

