+++
type = "question"
title = "wireshark throughput graph empty?"
description = '''After capturing the packets using wireshark. If try to open TCP stream throughput grapth. It is coming empty. On Y-axis it is not taking any input. Can any one help me with this.'''
date = "2015-09-16T07:07:00Z"
lastmod = "2015-09-17T05:25:00Z"
weight = 45880
keywords = [ "throughput" ]
aliases = [ "/questions/45880" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark throughput graph empty?](/questions/45880/wireshark-throughput-graph-empty)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45880-score" class="post-score" title="current number of votes">0</div><span id="post-45880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After capturing the packets using wireshark. If try to open TCP stream throughput grapth. It is coming empty. On Y-axis it is not taking any input. Can any one help me with this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '15, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/cd9aa02fb912ab1758553dd0b2a2e617?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phaniK&#39;s gravatar image" /><p><span>phaniK</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phaniK has no accepted answers">0%</span></p></div></div><div id="comments-container-45880" class="comments-container"><span id="45900"></span><div id="comment-45900" class="comment"><div id="post-45900-score" class="comment-score"></div><div class="comment-text"><p>Hard to make any suggestions without seeing the capture file. Can you post it somewhere? One idea: Make sure you selected a packet that contained data - the graph might be empty if there was only unidirectional flow,</p></div><div id="comment-45900-info" class="comment-info"><span class="comment-age">(16 Sep '15, 22:41)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-45880" class="comment-tools"></div><div class="clear"></div><div id="comment-45880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45916"></span>

<div id="answer-container-45916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45916-score" class="post-score" title="current number of votes">0</div><span id="post-45916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Throughput graph only graphs one stream in one direction, based on the packet that is selected when you bring up the graph. It does not graph all packets in the trace. Look at the top of the graph and it will show you the source address and port, and the destination address and port, of the selected stream. The usual reason for the graph being blank is that data is flowing in only one direction, ACK packets are flowing back in the other direction, and you've selected a packet in the wrong direction. You need to select a packet in the direction of data flow, not the direction that the ACKs are flowing. The selected packet doesn't have to have data, but it has to be in the direction of data flow.</p><p>If data is being sent from A to B, and ACKs are going from B to A, make sure you've selected a packet from A to B. This is true of all the graphs under Statistics &gt; TCP Stream Graph.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '15, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-45916" class="comments-container"></div><div id="comment-tools-45916" class="comment-tools"></div><div class="clear"></div><div id="comment-45916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

