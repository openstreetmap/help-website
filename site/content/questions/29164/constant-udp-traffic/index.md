+++
type = "question"
title = "Constant UDP Traffic"
description = '''1/3 of my captured Packets are UDP packets from the same IP in my Network. Always 72 length and the info is always &quot;Source Port: 58869 Destination port: 8009&quot; The UDP stream consists of &quot;Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.1...'''
date = "2014-01-26T05:46:00Z"
lastmod = "2014-01-26T05:59:00Z"
weight = 29164
keywords = [ "traffic", "udp", "constant" ]
aliases = [ "/questions/29164" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Constant UDP Traffic](/questions/29164/constant-udp-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29164-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>1/3 of my captured Packets are UDP packets from the same IP in my Network. Always 72 length and the info is always "Source Port: 58869 Destination port: 8009" The UDP stream consists of</p><pre><code>&quot;Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154|2Big-D-PC|11112|172.16.12.154&quot; </code></pre>for the entire conversation. I cringe at the name yes, but what traffic is it? It doesn't seem to end.<p>I might add the source is a computer name I guess "AsusXxx_e8:3e ... " and it's IPv4. Thanks for your help :)</p></div><div id="question-tags" class="tags-container tags">traffic udp constant</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '14, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/7dea67f6fe673b24a1c7cd4789090c81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J4D0&#39;s gravatar image" /><p>J4D0<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J4D0 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jan '14, 05:59</p></div></div><div id="comments-container-29164" class="comments-container"></div><div id="comment-tools-29164" class="comment-tools"></div><div class="clear"></div><div id="comment-29164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29165"></span>

<div id="answer-container-29165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29165-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The normal way to determine what kind of traffic that is would be to go to that PC and check the process list to find the application using that source port (or destination port, depending on who is who), by using the "netstat" command line tool or a GUI tool like <a href="http://technet.microsoft.com/de-de/sysinternals/bb897437.aspx">TCPView</a>. If you can't access the PC (e.g. because it is not yours) you can only guess.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '14, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29165" class="comments-container"><span id="29166"></span><div id="comment-29166" class="comment"><div id="post-29166-score" class="comment-score"></div><div class="comment-text"><p>I can't easily access the Pc :s What would be a likely guess? I think it is suspicious, that the traffic is always and every day the same... I ran an nmap scan, too if it would help the cause...</p></div><div id="comment-29166-info" class="comment-info"><span class="comment-age">(26 Jan '14, 06:03)</span> J4D0</div></div><span id="29167"></span><div id="comment-29167" class="comment"><div id="post-29167-score" class="comment-score"></div><div class="comment-text"><p>What is the target IP of those packets? Can you find out anything about that? I doubt nmap is going to help here, unless that UDP application reacts to a UDP port scan with a banner.</p></div><div id="comment-29167-info" class="comment-info"><span class="comment-age">(26 Jan '14, 06:17)</span> Jasper ♦♦</div></div><span id="29168"></span><div id="comment-29168" class="comment"><div id="post-29168-score" class="comment-score"></div><div class="comment-text"><p>target is 255.255.255.255 :/ and no it doesn't.</p></div><div id="comment-29168-info" class="comment-info"><span class="comment-age">(26 Jan '14, 06:35)</span> J4D0</div></div><span id="29169"></span><div id="comment-29169" class="comment"><div id="post-29169-score" class="comment-score"></div><div class="comment-text"><p>So the target is the broadcast address. Which means that the source PC is just telling everyone on the network it's address and host name I guess. I wouldn't worry about it, it's probably some kind of name resolution protocol.</p></div><div id="comment-29169-info" class="comment-info"><span class="comment-age">(26 Jan '14, 06:45)</span> Jasper ♦♦</div></div></div><div id="comment-tools-29165" class="comment-tools"></div><div class="clear"></div><div id="comment-29165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

