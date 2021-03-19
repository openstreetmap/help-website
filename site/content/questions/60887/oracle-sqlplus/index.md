+++
type = "question"
title = "Oracle SQL*Plus"
description = '''How can I capture Oracle SQLPlus traffic? I am running Wireshark with no capture filters and then starting SQLPlus and attempting to connect to a remote Oracle database (the connection doesn&#x27;t succeed). I cannot see any packets relating to the SQL*Plus traffic in the capture. Can someone talk me thr...'''
date = "2017-04-19T04:42:00Z"
lastmod = "2017-04-24T07:24:00Z"
weight = 60887
keywords = [ "oracle" ]
aliases = [ "/questions/60887" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Oracle SQL\*Plus](/questions/60887/oracle-sqlplus)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60887-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I capture Oracle SQLPlus traffic? I am running Wireshark with no capture filters and then starting SQLPlus and attempting to connect to a remote Oracle database (the connection doesn't succeed). I cannot see any packets relating to the SQL*Plus traffic in the capture.</p><p>Can someone talk me through exactly what's needed to capture traffic from SQLPlus connecting to a remote Oracle database?</p><p>Many thanks in advance.</p></div><div id="question-tags" class="tags-container tags">oracle</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '17, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/abfa09ae018770ddc052359c0a9772c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Corin&#39;s gravatar image" /><p>Corin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Corin has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '17, 04:44</p></div></div><div id="comments-container-60887" class="comments-container"><span id="60925"></span><div id="comment-60925" class="comment"><div id="post-60925-score" class="comment-score"></div><div class="comment-text"><p>Some questions to sort things out:</p><ul><li>Are you running Wireshark on the client where your SQLPlus client is also running?</li><li>Are you able to see any traffic (DNS, ARP...) in Wireshark?</li><li>Have you configured an IP address or a server name in your SQLPlus client resp. tnsnames.ora file?</li><li>When you've configured a server name: do you see name lookups (e.g. DNS requests or WINS) for this name in Wireshark?</li><li>SQLPlus normally connects to 1521/TCP: Is there any packet with this port? (display filter <code>tcp.port==1521</code>)</li></ul></div><div id="comment-60925-info" class="comment-info"><span class="comment-age">(20 Apr '17, 08:48)</span> Uli</div></div><span id="61007"></span><div id="comment-61007" class="comment"><div id="post-61007-score" class="comment-score"></div><div class="comment-text"><ul><li>Yes, running Wireshark on client machine where SQLPlus running</li><li>Yes, I can see ARP, DNS traffic, if I telnet to the address of my Oracle server I can see TCP traffic to that address</li><li>The IP address is configured in the tnsnames.ora. The service name is configured in the tnsnames.ora file.</li><li>I don't know the name of the Oracle database server, I only know its IP address. I know the Oracle service name, is that what you mean?</li><li>No, there is no packet with this port, the display filter tcp.port==1521 displays nothing</li></ul></div><div id="comment-61007-info" class="comment-info"><span class="comment-age">(24 Apr '17, 07:05)</span> Corin</div></div><span id="61008"></span><div id="comment-61008" class="comment"><div id="post-61008-score" class="comment-score"></div><div class="comment-text"><p>I've identified the problem, thank you for your help. I will post an answer below.</p></div><div id="comment-61008-info" class="comment-info"><span class="comment-age">(24 Apr '17, 07:18)</span> Corin</div></div></div><div id="comment-tools-60887" class="comment-tools"></div><div class="clear"></div><div id="comment-60887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61009"></span>

<div id="answer-container-61009" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61009-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem turned out to be a badly formatted tnsnames.ora file. The entries were originally formatted like this:</p><pre><code>{sid} =
(DESCRIPTION =
(ADDRESS = (PROTOCOL = TCP)(HOST = xxx.xxx.x.xx)(PORT = 1521))
(CONNECT_DATA =
(SERVER = DEDICATED)
(SERVICE_NAME = {servicename})
)
)</code></pre><p>The Oracle client tools reported this as ilegally formatted. I add spaces between the elements like so:</p><pre><code>{SID} =
 (DESCRIPTION =
  (ADDRESS = (PROTOCOL = TCP)(HOST = xxx.xxx.x.xx)(PORT = 1521))
  (CONNECT_DATA =
  (SERVER = DEDICATED)
  (SERVICE_NAME = {service_name})
 )
)</code></pre><p>Now I can see tcp.port==1521 traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '17, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/abfa09ae018770ddc052359c0a9772c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Corin&#39;s gravatar image" /><p>Corin<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Corin has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Apr '17, 07:27</p></div></div><div id="comments-container-61009" class="comments-container"></div><div id="comment-tools-61009" class="comment-tools"></div><div class="clear"></div><div id="comment-61009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

