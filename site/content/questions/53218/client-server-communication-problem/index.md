+++
type = "question"
title = "Client Server Communication Problem"
description = '''Hello, I am facing one issue when Server initiate FIN first. Having FIN, Client sending ACK and then in another packet Client is sending PSH+ACK. This PSH (data) server unable to read or capture.  Here is the MSG flow in our case. 4343: ------------FIN---------&amp;gt; (from SAP, Server) 4345&amp;lt;-------...'''
date = "2016-06-06T01:51:00Z"
lastmod = "2016-06-06T04:03:00Z"
weight = 53218
keywords = [ "azam" ]
aliases = [ "/questions/53218" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Client Server Communication Problem](/questions/53218/client-server-communication-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53218-score" class="post-score" title="current number of votes">0</div><span id="post-53218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am facing one issue when Server initiate FIN first. Having FIN, Client sending ACK and then in another packet Client is sending PSH+ACK. This PSH (data) server unable to read or capture.</p><p>Here is the MSG flow in our case.</p><p>4343: ------------FIN---------&gt; (from SAP, Server)</p><p>4345&lt;-------------ACK--------- (from EMA, Client)</p><p>4347&lt;----------PSH,ACK------- (From EMA, Client)</p><p>4349&lt;---------FIN,ACK--------(From EMA, Client)</p><p>4351-------------RST---------&gt;(From SAP, Server)</p><p>4352------------RST---------&gt;(From SAP,Server)</p><p>I would like to know sending PSH+ACK after (FIN) and acknowledging the same is standard or not. Why Server is not able to read this PSH data?<img src="https://osqa-ask.wireshark.org/upfiles/Server_Client_Communication_Issue_XlvtMVj.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-azam" rel="tag" title="see questions tagged &#39;azam&#39;">azam</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '16, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/c026768a5b03d1cbcce483af23f6af1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Isme%20Azam&#39;s gravatar image" /><p><span>Isme Azam</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Isme Azam has no accepted answers">0%</span></p></img></div></div><div id="comments-container-53218" class="comments-container"><span id="53219"></span><div id="comment-53219" class="comment"><div id="post-53219-score" class="comment-score"></div><div class="comment-text"><p>Please review and share any kind of feedback. This issue is burning my life.</p></div><div id="comment-53219-info" class="comment-info"><span class="comment-age">(06 Jun '16, 01:52)</span> <span class="comment-user userinfo">Isme Azam</span></div></div></div><div id="comment-tools-53218" class="comment-tools"></div><div class="clear"></div><div id="comment-53218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53222"></span>

<div id="answer-container-53222" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53222-score" class="post-score" title="current number of votes">0</div><span id="post-53222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Posting screenshots is discouraged since it makes investigating a problem really hard. If possible can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p><p>From the description it seems that the server doesn't handle closing the TCP connection gracefully. Since the TCP connection is bi-directional both ends have to <a href="http://www.tcpipguide.com/free/t_TCPConnectionTermination.htm">finish the connection</a> once all data has been exchanged (both ways). When that is is decided by each end individually, hence the FIN flag going both ways.</p><p>In this case the server terminates the TCP connection, without letting the client close the connection on it's own. The last data from the client, before it closes its end of the connection, can no longer be received by the server, as it terminated the connection instead of just closing its end.</p><p>I would say the relevant socket in the server application is shutdown() instead of close()ed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '16, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53222" class="comments-container"><span id="53223"></span><div id="comment-53223" class="comment"><div id="post-53223-score" class="comment-score"></div><div class="comment-text"><p>Please find the TCPDUMP from below location.</p><p><a href="https://www.cloudshark.org/captures/e5cc26206a6b">https://www.cloudshark.org/captures/e5cc26206a6b</a></p><p>How to improve this situation? please suggest. Is it good idea if we use timeout value (in server side which would be greater than client end)? or is there any mechanism where only Client shall initiate close the connection?</p></div><div id="comment-53223-info" class="comment-info"><span class="comment-age">(06 Jun '16, 02:39)</span> <span class="comment-user userinfo">Isme Azam</span></div></div><span id="53228"></span><div id="comment-53228" class="comment"><div id="post-53228-score" class="comment-score"></div><div class="comment-text"><p>After de-duplication the TCP flow is obvious, the server shuts down the connection leaving the client out to dry.</p><p>As for the reason why the server does this, and what the client has to report at the end, and what to do with that is up to the application developers.</p></div><div id="comment-53228-info" class="comment-info"><span class="comment-age">(06 Jun '16, 04:03)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-53222" class="comment-tools"></div><div class="clear"></div><div id="comment-53222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

