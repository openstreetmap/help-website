+++
type = "question"
title = "Extra ACK With SQL Server?"
description = '''I have an application that is communicating to a SQL server. Every once in a while, the queries the application calls are taking much longer. I&#x27;ve captured this with Wireshark. When everything is going fine, the log looks like this. These 5 entries take about 1ms. Client -&amp;gt; SQL Server : Remote Pr...'''
date = "2015-10-22T07:23:00Z"
lastmod = "2015-10-22T09:41:00Z"
weight = 46832
keywords = [ "ack", "sql" ]
aliases = [ "/questions/46832" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extra ACK With SQL Server?](/questions/46832/extra-ack-with-sql-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46832-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an application that is communicating to a SQL server. Every once in a while, the queries the application calls are taking much longer. I've captured this with Wireshark. When everything is going fine, the log looks like this. These 5 entries take about 1ms.</p><p>Client -&gt; SQL Server : Remote Procedure Call</p><p>SQL Server -&gt; Client: Response</p><p>Client -&gt; SQL Server : SQL Batch</p><p>SQL Server -&gt; Client : [ACK] Seq=3218061 Ack=4449533 Win=131328 Len = 0</p><p>SQL Server -&gt; Client: Response</p><p>When things start to get slow, the SQL Server/Client communication looks like this. The entire transaction takes about 500ms</p><p>Client -&gt; SQL Server : Remote Procedure Call</p><p>SQL Server -&gt; Client: Response</p><p>Client -&gt; SQL Server : SQL Batch</p><p>SQL Server -&gt; Client : [ACK] Seq=3222735 Ack=4458045 Win=131328 Len = 0 (Packet length = 60)</p><p>Client -&gt; SQL Server: [ACK] Seq=596422 Ack=560033 Win=65280 Len = 0 (Packet length = 54)</p><p>SQL Server -&gt; Client: Response</p><p>Notice the extra ACK from the client to the server. There is also a mixture of ARP requests in there, SSDP Notify's, STP, NBNS. I'm not sure why there are a bunch of other calls in there suddenly when there weren't before, but from everything I've found it should be pretty harmless. What I don't understand is why would the client be sending an ACK back to the SQL server? Any thoughts? Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">ack sql</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '15, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/1420665c60bdf8bb1cabce08d13a97f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kw2107&#39;s gravatar image" /><p>kw2107<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kw2107 has no accepted answers">0%</span></p></div></div><div id="comments-container-46832" class="comments-container"></div><div id="comment-tools-46832" class="comment-tools"></div><div class="clear"></div><div id="comment-46832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46845"></span>

<div id="answer-container-46845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46845-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>ACK is a TCP feature (Layer 4) to assure that the segments are transmitted correctly. For example to show the sender that all transmitted segments have reached its destination.</p><p>A response is an application things and is different from application to application. The TCP behaviour is equal to all applications the at use the TCP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '15, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Oct '15, 09:42</p></div></div><div id="comments-container-46845" class="comments-container"><span id="46846"></span><div id="comment-46846" class="comment"><div id="post-46846-score" class="comment-score"></div><div class="comment-text"><p>Sure, I understand that. I guess my question is why does the client sometimes send back an ACK and sometimes it doesn't? And when it does send back the ACK, there is a 500ms delay in the SQL server response?</p></div><div id="comment-46846-info" class="comment-info"><span class="comment-age">(22 Oct '15, 10:03)</span> kw2107</div></div><span id="46847"></span><div id="comment-46847" class="comment"><div id="post-46847-score" class="comment-score"></div><div class="comment-text"><p>Depends on the moment. Without a trace I can't say much more. But in fact every packet is an ACK, too.</p></div><div id="comment-46847-info" class="comment-info"><span class="comment-age">(22 Oct '15, 10:13)</span> Christian_R</div></div></div><div id="comment-tools-46845" class="comment-tools"></div><div class="clear"></div><div id="comment-46845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

