+++
type = "question"
title = "Dropped packet stats in CLI during capture"
description = '''For tcmdump or dumpcap, is it possible to have the dropped packets counter statistics during the capture? Currently only available at the end of the capture... How can I know if my capture is missing packets in real-time? Update: I&#x27;ve discovered that pressing CTRL+T (sending SIGINFO according to man...'''
date = "2016-10-26T13:56:00Z"
lastmod = "2016-10-31T14:50:00Z"
weight = 56715
keywords = [ "capture", "tcpdump", "dumpcap" ]
aliases = [ "/questions/56715" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dropped packet stats in CLI during capture](/questions/56715/dropped-packet-stats-in-cli-during-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56715-score" class="post-score" title="current number of votes">0</div><span id="post-56715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For tcmdump or dumpcap, is it possible to have the dropped packets counter statistics during the capture? Currently only available at the end of the capture...</p><p>How can I know if my capture is missing packets in real-time?</p><p>Update: I've discovered that pressing CTRL+T (sending SIGINFO according to manpage) during a dumpcap -q capture, displays some info on demand, maybe could add afix to display dropped packets if the info is available:</p><pre><code>load: 1.32  cmd: dumpcap 4451 running 0.04u 0.03s
Packets captured: 8</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '16, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/822be38630e1b9b5a1505f259322c63b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomLaBaude&#39;s gravatar image" /><p><span>TomLaBaude</span><br />
<span class="score" title="66 reputation points">66</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomLaBaude has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Oct '16, 14:53</strong> </span></p></div></div><div id="comments-container-56715" class="comments-container"></div><div id="comment-tools-56715" class="comment-tools"></div><div class="clear"></div><div id="comment-56715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56880"></span>

<div id="answer-container-56880" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56880-score" class="post-score" title="current number of votes">-1</div><span id="post-56880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As an example:</p><p>tshark -i 1 -qz icmp,srt</p><p>This will show # of packets lost and also a % of packet loss.</p><p>hope this is helpful, John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '16, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-56880" class="comments-container"><span id="56884"></span><div id="comment-56884" class="comment"><div id="post-56884-score" class="comment-score"></div><div class="comment-text"><p>All of this is available at the end of the capture, I was asking for packet drop info during the capture</p></div><div id="comment-56884-info" class="comment-info"><span class="comment-age">(31 Oct '16, 14:50)</span> <span class="comment-user userinfo">TomLaBaude</span></div></div></div><div id="comment-tools-56880" class="comment-tools"></div><div class="clear"></div><div id="comment-56880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

