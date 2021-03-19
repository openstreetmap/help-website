+++
type = "question"
title = "Sending packets captured with Wireshark on Windows"
description = '''I captured some packets from server(like: ip.addr == 111.11.11.111 &amp;amp;&amp;amp; data), and want to send them again. How to do it? Googling didn&#x27;t yield any easy way not involving some complex stuff resulting in a script being able to send only this specific request, without any flexibility. I&#x27;am using...'''
date = "2017-01-11T14:22:00Z"
lastmod = "2017-01-11T14:24:00Z"
weight = 58675
keywords = [ "windows", "sending", "captured", "packet", "server" ]
aliases = [ "/questions/58675" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Sending packets captured with Wireshark on Windows](/questions/58675/sending-packets-captured-with-wireshark-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58675-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured some packets from server(like: ip.addr == 111.11.11.111 &amp;&amp; data), and want to send them again. How to do it? Googling didn't yield any easy way not involving some complex stuff resulting in a script being able to send only this specific request, without any flexibility.</p><p>I'am using only Windows 10 64Bit</p></div><div id="question-tags" class="tags-container tags">windows sending captured packet server</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '17, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/14579bac17258201c0cc89ee5d7a3e37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cascraft&#39;s gravatar image" /><p>cascraft<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cascraft has no accepted answers">0%</span></p></div></div><div id="comments-container-58675" class="comments-container"></div><div id="comment-tools-58675" class="comment-tools"></div><div class="clear"></div><div id="comment-58675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58678"></span>

<div id="answer-container-58678" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58678-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not a packet generator, it captures and decodes packets. Look at other tools like <a href="http://ostinato.org/">Ostinato</a> or <a href="http://www.secdev.org/projects/scapy/">scapy</a> to replay captured packets or generate new packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '17, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-58678" class="comments-container"><span id="58681"></span><div id="comment-58681" class="comment"><div id="post-58681-score" class="comment-score"></div><div class="comment-text"><p>thanks but that tools are crap. i get always error.</p><p>any good tools to sending captured packets?</p></div><div id="comment-58681-info" class="comment-info"><span class="comment-age">(11 Jan '17, 15:28)</span> cascraft</div></div><span id="58682"></span><div id="comment-58682" class="comment"><div id="post-58682-score" class="comment-score">1</div><div class="comment-text"><p>Check out this list:</p><p><a href="https://wiki.wireshark.org/Tools#Traffic_generators">https://wiki.wireshark.org/Tools#Traffic_generators</a></p></div><div id="comment-58682-info" class="comment-info"><span class="comment-age">(11 Jan '17, 15:31)</span> Jasper ♦♦</div></div></div><div id="comment-tools-58678" class="comment-tools"></div><div class="clear"></div><div id="comment-58678-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

