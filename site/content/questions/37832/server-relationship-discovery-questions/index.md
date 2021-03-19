+++
type = "question"
title = "Server Relationship/ Discovery Questions"
description = '''We are looking for information on your software tool “name”   This is what we are looking to do: We are looking to capture the relationships of servers within a network. We need to know how the servers are related. Relationship means that the servers had communications(Db call, backup,…) between the...'''
date = "2014-11-13T11:26:00Z"
lastmod = "2014-11-15T15:12:00Z"
weight = 37832
keywords = [ "relationships", "server" ]
aliases = [ "/questions/37832" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Server Relationship/ Discovery Questions](/questions/37832/server-relationship-discovery-questions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37832-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are looking for information on your software tool “name”<br />
</p><p>This is what we are looking to do:</p><p>We are looking to capture the relationships of servers within a network. We need to know how the servers are related. Relationship means that the servers had communications(Db call, backup,…) between them. Any kind of communication would need to be captured.</p><p>We were thinking of the following and wanted to know if your SW can do what we need: • Monitor/scan the network over a period of time (1 week … 1 week +) based on a range of IP addresses. • We are looking to do this without an agent. • We are looking to capture and track the server relationships. By track, we mean keep a count of the number of times an interaction took place • We want the relationship to be captured as follows:</p><p>Primary Server Machine Name Primary Server IP Address Related Server Machine Name Related Server IP address Count Server 1 IP1 Server 2 IP2 8700 Server 7 IP7 500 Server 12 IP12 300000 Server 2 IP2 Server 1 IP1 8700 Server 9 IP9 6722 Server 3 IP3 998866 Server 12 IP12 2220 Server 11 IP11 7 Server 3 IP3 . . . . . . . . . . . . . . . . . . . . . . .</p><p>Can your sw provide us this information? If so, how? If not, do you know of any sw that can provide it? Bonus – Nice to have if it could also capture the type of communication and the application that made the call.</p></div><div id="question-tags" class="tags-container tags">relationships server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '14, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/ca4c7739f4cd9c77d6b78936d4d637f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Browndog801&#39;s gravatar image" /><p>Browndog801<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Browndog801 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-37832" class="comments-container"></div><div id="comment-tools-37832" class="comment-tools"></div><div class="clear"></div><div id="comment-37832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37881"></span>

<div id="answer-container-37881" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37881-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's possible to do this with Wireshark (or more correctly tshark) but you have to use something to summarise the output - we've used SAS to do this in the past. However, you have to deploy capture units all over your network. It's easier to use a flow-based tool; one that collects and processes netflow, jflow, etc.</p><p>Riverbed Steelcentral AppMapper could do it for you.</p><p>You could probably also write a Powershell script that executes netstat -aob remotely on each Windows server say every minute and saves the results for later summarising. The -aob will give you conversation and executable information.</p><p>Best rdgards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '14, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-37881" class="comments-container"></div><div id="comment-tools-37881" class="comment-tools"></div><div class="clear"></div><div id="comment-37881-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

