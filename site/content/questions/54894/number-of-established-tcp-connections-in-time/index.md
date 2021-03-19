+++
type = "question"
title = "Number of established TCP connections in time"
description = '''Hi, is it possible to graph number of established tcp connections in to the endpoint using IO graph in wireshark?  We can graph number of TCP.SYN or TCP.FIN/RST packets but don&#x27;t know how to create graph with establised sessions.'''
date = "2016-08-17T01:16:00Z"
lastmod = "2016-08-18T13:13:00Z"
weight = 54894
keywords = [ "established", "tcp", "io_graph" ]
aliases = [ "/questions/54894" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Number of established TCP connections in time](/questions/54894/number-of-established-tcp-connections-in-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54894-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>is it possible to graph number of established tcp connections in to the endpoint using IO graph in wireshark? We can graph number of TCP.SYN or TCP.FIN/RST packets but don't know how to create graph with establised sessions.</p></div><div id="question-tags" class="tags-container tags">established tcp io_graph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '16, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/da43c87efbf68f893c0a388117e43055?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="razor85&#39;s gravatar image" /><p>razor85<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="razor85 has no accepted answers">0%</span></p></div></div><div id="comments-container-54894" class="comments-container"></div><div id="comment-tools-54894" class="comment-tools"></div><div class="clear"></div><div id="comment-54894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54962"></span>

<div id="answer-container-54962" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54962-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. With the IO Graph you can plot only value of fields or count fields. You can´t graph session states, if there is no field in Wireshark.</p><p>So from my Point of view you have different options to do that kind of Graph:</p><ol><li><p>You can Export the SYN and FFIN/RST Packets to Excel (CSV Export) and use the Functions or macros to count the number of concurrent sseions.</p></li><li><p>You can write your own field in Wireshark and graph that.</p></li><li><p>You can achieve that goal with a LUA script.</p></li><li><p>You can use tshark to print the SYN/FIN/RST packets to console or file and script something around that new file.</p></li></ol><p>I have done this once with Excel.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '16, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Aug '16, 13:16</p></div></div><div id="comments-container-54962" class="comments-container"></div><div id="comment-tools-54962" class="comment-tools"></div><div class="clear"></div><div id="comment-54962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

