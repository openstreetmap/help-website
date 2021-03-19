+++
type = "question"
title = "high ping times to server"
description = '''Hello, I have a microsoft based network, all clients are win 7 clients and there are about 14 windows 2008 servers. the ping times from all clients to just one particular server (ServerHQ) are intermittently high, between 100-600 ms. Then at other times they are &amp;lt;1ms.  Ran wireshark capture on th...'''
date = "2016-12-09T16:52:00Z"
lastmod = "2016-12-10T17:12:00Z"
weight = 57981
keywords = [ "ping" ]
aliases = [ "/questions/57981" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [high ping times to server](/questions/57981/high-ping-times-to-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57981-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a microsoft based network, all clients are win 7 clients and there are about 14 windows 2008 servers. the ping times from all clients to just one particular server (ServerHQ) are intermittently high, between 100-600 ms. Then at other times they are &lt;1ms.</p><p>Ran wireshark capture on the interface of the server that is producing the high ping times, but can't seem to find where the problem is coming from.</p><p>At nights, though, when all clients are off, the ping times from any server to ServerHQ is stable at &lt;1ms.</p><p>Any help will be appreciated millions.</p></div><div id="question-tags" class="tags-container tags">ping</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '16, 16:52</strong></p><img src="https://secure.gravatar.com/avatar/41701a0935cff594aee8e02d0537ce1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burtjaggs&#39;s gravatar image" /><p>burtjaggs<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burtjaggs has no accepted answers">0%</span></p></div></div><div id="comments-container-57981" class="comments-container"><span id="57994"></span><div id="comment-57994" class="comment"><div id="post-57994-score" class="comment-score"></div><div class="comment-text"><p>Did you try to do a tracert from the client to the server (ServerHQ) during the time when high ping times occur?</p></div><div id="comment-57994-info" class="comment-info"><span class="comment-age">(10 Dec '16, 12:13)</span> Amato_C</div></div></div><div id="comment-tools-57981" class="comment-tools"></div><div class="clear"></div><div id="comment-57981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57997"></span>

<div id="answer-container-57997" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57997-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>it's on the same lan, so there are no hops. On further investigation i found that the netwoork utilization is only high, when clients connect to an sql service, sqlservr.exe, that runs on the machine. If i kill the sql engine, the pings are stable again at &lt;1ms.</p><p>I may have to look at why the sqlservr.exe connections to the clients are high.DIRECTIIO</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '16, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/41701a0935cff594aee8e02d0537ce1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="burtjaggs&#39;s gravatar image" /><p>burtjaggs<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="burtjaggs has no accepted answers">0%</span></p></div></div><div id="comments-container-57997" class="comments-container"></div><div id="comment-tools-57997" class="comment-tools"></div><div class="clear"></div><div id="comment-57997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

