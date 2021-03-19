+++
type = "question"
title = "Understanding DCERPC and &quot;TCP segment of a reassembled PDU&quot;"
description = '''I&#x27;m trying to understand how a PC application (which is unsupported and undocumented) talks to a device. The trace seems to consist mostly of DCERPC packets and TCP packets marked &quot;TCP segment of a reassembled PDU&quot;. What I expect to be happening here is either the download of a lot of records from a...'''
date = "2012-12-07T15:48:00Z"
lastmod = "2012-12-07T20:01:00Z"
weight = 16715
keywords = [ "dcerpc" ]
aliases = [ "/questions/16715" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding DCERPC and "TCP segment of a reassembled PDU"](/questions/16715/understanding-dcerpc-and-tcp-segment-of-a-reassembled-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16715-score" class="post-score" title="current number of votes">0</div><span id="post-16715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to understand how a PC application (which is unsupported and undocumented) talks to a device. The trace seems to consist mostly of DCERPC packets and TCP packets marked "TCP segment of a reassembled PDU". What I expect to be happening here is either the download of a lot of records from a database to the device, or some sort of synchronisation of a database in the device with the master database on the PC. The database is probably using Clarion/Topspeed.</p><p>Can someone give me an overview on what's going on here, and how I can set about analysing it? Eventually I have to write a new program that can communicate to the device in the same way.</p><p>Thanks - Rowan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dcerpc" rel="tag" title="see questions tagged &#39;dcerpc&#39;">dcerpc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '12, 15:48</strong></p><img src="https://secure.gravatar.com/avatar/fd3bc17dd17d9e0301f9329394be1539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rowan&#39;s gravatar image" /><p><span>Rowan</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rowan has no accepted answers">0%</span></p></div></div><div id="comments-container-16715" class="comments-container"></div><div id="comment-tools-16715" class="comment-tools"></div><div class="clear"></div><div id="comment-16715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16718"></span>

<div id="answer-container-16718" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16718-score" class="post-score" title="current number of votes">0</div><span id="post-16718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What's going on is probably either that the PC application is using <a href="https://en.wikipedia.org/wiki/DCE/RPC">DCE/RPC</a>, or <a href="https://en.wikipedia.org/wiki/MSRPC">Microsoft's extended version of DCE/RPC</a>, to communicate with the device, or some <em>other</em> programs are communicating using DCE/RPC or MSRPC and some of the traffic that's <em>not</em> DCE/RPC and <em>not</em> "TCP segment of a reassembled PDU" TCP segments that end up getting reassembled into DCE/RPC traffic is the traffic between the PC application and the device.</p><p>Apparently <a href="http://en.wikipedia.org/wiki/Clarion_(programming_language)">Topspeed's Clarion</a> "reads and writes several flat file desktop database formats including ASCII, CSV, DOS (Binary), FoxPro, Clipper, dBase, or all SQL RDBMS databases via ODBC, MS SQL Server, Sybase SQL Anywhere and Oracle through the use of accelerated native database drivers". Perhaps some of those access methods run over the networking using DCE/RPC (SQL Server/Sybase SQL Anywhere don't - they use TDS, which Wireshark also dissects - and Oracle doesn't - it uses some other protocol that Wireshark dissects).</p><p>Sadly, DCE/RPC isn't necessarily going to be easy to reverse-engineer - and you may then have to reverse-engineer the database schema as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '12, 20:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16718" class="comments-container"></div><div id="comment-tools-16718" class="comment-tools"></div><div class="clear"></div><div id="comment-16718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

