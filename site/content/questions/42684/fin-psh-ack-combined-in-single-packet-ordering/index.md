+++
type = "question"
title = "FIN, PSH, ACK Combined in Single Packet (Ordering?)"
description = '''All, I&#x27;m having issues with 2 applications applications as follows:  The Client and Server establish a TCP  connection with SYN / ACK exchange no  problem The client sends a payload to the  server again without any issues as  follows: Client &amp;gt; Server [PSH,ACK] Includes  Payload The server gets th...'''
date = "2015-05-26T16:27:00Z"
lastmod = "2015-05-26T18:15:00Z"
weight = 42684
keywords = [ "ack", "psh", "fin" ]
aliases = [ "/questions/42684" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FIN, PSH, ACK Combined in Single Packet (Ordering?)](/questions/42684/fin-psh-ack-combined-in-single-packet-ordering)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42684-score" class="post-score" title="current number of votes">0</div><span id="post-42684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>All,</p><p>I'm having issues with 2 applications applications as follows:</p><ul><li>The Client and Server establish a TCP connection with SYN / ACK exchange no problem</li><li>The client sends a payload to the server again without any issues as follows:</li><li>Client &gt; Server [PSH,ACK] <strong><em>Includes Payload</em></strong></li><li>The server gets this message (I can see it in the app log)</li><li>Server &gt; Client [ACK]</li><li>Server &gt; Client [POS,ACK] <strong><em>Not really sure what this is but seems to just contain control data</em></strong></li><li>Server &gt; Client [FIN, PSH, ACK] <strong><em>Contains Response</em></strong></li><li>Client never gets this payload, or at least i don't see it in the logs</li><li>Client &gt; Server [ACK]</li><li>Client &gt; Server [FIN,ACK]</li><li>Server &gt; Client [ACK]</li></ul><p>What i would like to know is:</p><ol><li>Is it allowed to send FIN, PSH and ACK in a single packet?</li><li>Does the order of the tags matter; in my example FIN is sent before the PSH by the Server...so is the client closing the connection (the order of the tages is what i see in wireshark)</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-psh" rel="tag" title="see questions tagged &#39;psh&#39;">psh</span> <span class="post-tag tag-link-fin" rel="tag" title="see questions tagged &#39;fin&#39;">fin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '15, 16:27</strong></p><img src="https://secure.gravatar.com/avatar/44a83811a389feb467cce5ebe3ff7e5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris%20Thompson&#39;s gravatar image" /><p><span>Chris Thompson</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris Thompson has no accepted answers">0%</span></p></div></div><div id="comments-container-42684" class="comments-container"></div><div id="comment-tools-42684" class="comment-tools"></div><div class="clear"></div><div id="comment-42684-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42685"></span>

<div id="answer-container-42685" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42685-score" class="post-score" title="current number of votes">2</div><span id="post-42685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To the first question, yes this is allowed and normal. If it's the last data to be sent, the most efficient way to 1) acknowledge the previous data 2) indicate no new data is coming and 3) indicate that the data should be pushed to the application without any delay on upcoming data would be to set those three flags.</p><p>To the second question, the order of the flags in a single TCP packet are fixed, so there's no way to actually change the order as you say. You're just seeing the order that Wireshark analysis of set and unset flags displays, but there are nine flags in a fixed position in the "Flags" field of the TCP header, set or unset, always in the same order.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '15, 18:15</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-42685" class="comments-container"></div><div id="comment-tools-42685" class="comment-tools"></div><div class="clear"></div><div id="comment-42685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

