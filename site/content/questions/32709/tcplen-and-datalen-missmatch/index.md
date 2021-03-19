+++
type = "question"
title = "Tcp.len and data.len missmatch"
description = '''What is the difference between tcp.len and data.len filters? I thought that both mean data size travelling in the segment (not including TCP header). I have a problem related to MTU issue and im trying to figure if data size from application layer is greater than the MSS announced by the server.  Th...'''
date = "2014-05-11T08:11:00Z"
lastmod = "2014-05-11T09:28:00Z"
weight = 32709
keywords = [ "mss", "tcp", "mtu" ]
aliases = [ "/questions/32709" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tcp.len and data.len missmatch](/questions/32709/tcplen-and-datalen-missmatch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32709-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the difference between <code>tcp.len</code> and <code>data.len</code> filters? I thought that both mean data size travelling in the segment (not including <code>TCP header</code>). I have a problem related to <code>MTU</code> issue and im trying to figure if data size from application layer is greater than the <code>MSS</code> announced by the server.</p><p>The capture shows some TCP packets encapsulating 1434 Bytes:</p><p><img src="http://i.stack.imgur.com/uWykw.png" alt="enter image description here" /></p><p>But the TCP layer analysis displays the same TCP packets with <code>len = 1448</code></p><p><img src="http://i.stack.imgur.com/jrnnx.png" alt="enter image description here" /><br />
</p><p>I think that this TCP segment is encapsulating 1448 Bytes. 1448B plus 32B of TCP header (some TCP options are enabled) plus 20B of IP Header = 1500 Bytes as it is displayed in the analysis of the IP layer.</p><p>So i have a question related to this one about <code>MSS clamping</code>. LAN clients are connected to router using <code>Ethernet</code> with MTU = 1500 Bytes and router is connected to Internet using <code>PPPoE</code> with MTU = 1492 Bytes. The router is manipulating <code>MSS</code> field in every TCP packet with <code>SYN flag</code> enabled in both directions, this is known as <code>MSS clamping</code>. This way LAN clients receive MSS = 1452 from servers in Internet and the servers receive MSS = 1452 from the LAN clients.</p><p>But what happens if server announces MSS &lt; 1452? LAN clients will receive MSS = 1452 from the server so only <code>PMTUD</code> can work here?<br />
</p></div><div id="question-tags" class="tags-container tags">mss tcp mtu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '14, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/21f0c1f83257b09700ed8c8592651e9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Miguelbc&#39;s gravatar image" /><p>Miguelbc<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Miguelbc has no accepted answers">0%</span> </br></br></p></img></div></div><div id="comments-container-32709" class="comments-container"></div><div id="comment-tools-32709" class="comment-tools"></div><div class="clear"></div><div id="comment-32709-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32710"></span>

<div id="answer-container-32710" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32710-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>MSS clamping should only modifiy the MSS option in SYN flagged packets if the advertized MSS in the SYN packet is greater than the MSS of the local segment. E.g. if an external server announces an MSS of 1300 then it should just pass through unchanged if you MSS is 1452. That way the client knows that the server can only deal with segments up to 1300 bytes and everything should be fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '14, 09:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-32710" class="comments-container"><span id="32711"></span><div id="comment-32711" class="comment"><div id="post-32711-score" class="comment-score"></div><div class="comment-text"><p>So i should check the iptables rule for MSS clamping in my router because its not working properly. By the way what is the difference between tcp.len and data.len filters?</p></div><div id="comment-32711-info" class="comment-info"><span class="comment-age">(11 May '14, 09:44)</span> Miguelbc</div></div><span id="32712"></span><div id="comment-32712" class="comment"><div id="post-32712-score" class="comment-score"></div><div class="comment-text"><p>not sure abou the tcp.len and data.len, as I have no trace that shows this. The ones I checked have the same tcp.len and data.len. I guess your example was created using frame slicing (meaning, you didn't capture the full packet), because it says in your screen shot "not all data available"). Maybe this is the reason why tcp.len and data.len differ.</p></div><div id="comment-32712-info" class="comment-info"><span class="comment-age">(11 May '14, 10:17)</span> Jasper ♦♦</div></div></div><div id="comment-tools-32710" class="comment-tools"></div><div class="clear"></div><div id="comment-32710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

