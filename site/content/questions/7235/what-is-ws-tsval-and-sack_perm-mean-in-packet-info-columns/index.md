+++
type = "question"
title = "what is &#x27;WS&#x27; &#x27;TSval&#x27; and &#x27;SACK_PERM&#x27; mean in  packet info columns???"
description = '''Dear wireshark experts, I got stuck in with some really tough questions, just as mentioned in subject. What is that??? Help!!! 8 1.253204 172.30.87.216 119.167.194.133 TCP 74 50785 &amp;gt; http [SYN] Seq=0 Win=5840 Len=0 MSS=1460 ***SACK_PERM=1 TSval=1575384402 TSecr=0 WS=128***  So appreciated in adva...'''
date = "2011-11-04T03:56:00Z"
lastmod = "2011-11-04T04:10:00Z"
weight = 7235
keywords = [ "info", "capture", "packet" ]
aliases = [ "/questions/7235" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [what is 'WS' 'TSval' and 'SACK\_PERM' mean in packet info columns???](/questions/7235/what-is-ws-tsval-and-sack_perm-mean-in-packet-info-columns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Dear wireshark experts,</p><p>I got stuck in with some really tough questions, just as mentioned in subject. What is that???</p><p>Help!!!</p><pre><code>8   1.253204    172.30.87.216   119.167.194.133 TCP 74  50785 &gt; http [SYN] Seq=0 Win=5840 Len=0 MSS=1460 ***SACK_PERM=1 TSval=1575384402 TSecr=0 WS=128***</code></pre><p>So appreciated in advance!</p></div><div id="question-tags" class="tags-container tags">info capture packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '11, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/0fe75c000a4283113e487b9db901cb40?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wenchao_wang&#39;s gravatar image" /><p>wenchao_wang<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wenchao_wang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Nov '11, 03:57</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-7235" class="comments-container"></div><div id="comment-tools-7235" class="comment-tools"></div><div class="clear"></div><div id="comment-7235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7236"></span>

<div id="answer-container-7236" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7236-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, it is not really a tough question ;-)</p><p>What you have there is a SYN packet (which is used in the TCP handshake session setup), and in that packet optional TCP parameters are given - see <a href="http://tools.ietf.org/html/rfc1323">RFC 1323</a> for more details on what and why.</p><ul><li>SACK_PERM means that the node with IP 172.30.87.216 "knows" how to work with so called "<strong>S</strong>elective <strong>Ack</strong>nowledgements", as described in <a href="http://tools.ietf.org/html/rfc2018">RFC 2018</a>.</li><li>It also uses TCP Timestamps (TSval/TSecr), and uses a</li><li>"<strong>W</strong>indow <strong>S</strong>caling of 128, which is the result of it advertising a Scale Factor of 7 (not seen in the info column, but in the decode).</li></ul><p>All of these are so called high performance options that are now pretty common since all modern TCP stacks know about those and use them, especially in high latency high bandwidth environments (LFN).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Nov '11, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '12, 13:48</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7236" class="comments-container"></div><div id="comment-tools-7236" class="comment-tools"></div><div class="clear"></div><div id="comment-7236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

