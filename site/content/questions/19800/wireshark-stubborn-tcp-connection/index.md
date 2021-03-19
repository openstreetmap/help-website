+++
type = "question"
title = "Wireshark stubborn TCP connection"
description = '''Hi Everyone! I am firwer123 and i just joined Wireshark Q&amp;amp;A! Firstly,  I hope some one could help me one this, --Source--------Destination---Protocol----------------Length &amp;amp; Information-------------- 192.XXX.1.XX----70.39.98.126-------TCP------54 54589 &amp;gt; dhanalakshmi [ACK] Seq=1 Ack=1 Win...'''
date = "2013-03-25T04:28:00Z"
lastmod = "2013-03-25T04:52:00Z"
weight = 19800
keywords = [ "phoning", "wireshark", "exploit", "emergency", "help" ]
aliases = [ "/questions/19800" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark stubborn TCP connection](/questions/19800/wireshark-stubborn-tcp-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19800-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone! I am firwer123 and i just joined Wireshark Q&amp;A!</p><p>Firstly, I hope some one could help me one this,</p><p><strong><em>--Source--------Destination---Protocol----------------Length &amp; Information--------------</em></strong></p><p>192.XXX.1.XX----70.39.98.126-------TCP------54 54589 &gt; dhanalakshmi [ACK] Seq=1 Ack=1 Win=17520 Len=0<br />
70.39.98.126----192.XXX.1.XX-------TCP------67 dhanalakshmi &gt; 54589 [PSH, ACK] Seq=1 Ack=74 Win=65462 Len=13<br />
and a few more similar ones..</p><p>192.XXX.1.XX is my local machine</p><p>70.39.98.126 is that remote server</p><p>Above, is a TCP connection that I've filtered out of my network traffic and besides that this network activity log came from a program that would contact its server(70.39.98.126) whenever i open it..</p><p>But now, I wished to stop this program from contacting their server again.. Is there anyway i can stop it using Wireshark...or lets don't say stop it, is there anyway to exploit it?</p><p>Additional Information about that remote server (70.39.98.126)</p><ul><li>Server IP: 70.39.98.126</li><li>Protocol: TCP</li><li>Source Port: Dhanalakshmi (34567)</li><li>Destination Port: 50949</li></ul><p>Peoples please help me! I need your help!!</p><p>Your Sincerely, firwer123</p></div><div id="question-tags" class="tags-container tags">phoning wireshark exploit emergency help</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '13, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/d91ef6576eebf8cb84bc89b705626d1d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="firwer123&#39;s gravatar image" /><p>firwer123<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="firwer123 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Mar '13, 05:04</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-19800" class="comments-container"></div><div id="comment-tools-19800" class="comment-tools"></div><div class="clear"></div><div id="comment-19800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19801"></span>

<div id="answer-container-19801" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19801-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is not a firewall, so no there's no way it can stop it for you. Wireshark is a (rather passive) network sniffer, so cannot 'exploit' (whatever that means) this or any other TCP connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19801" class="comments-container"></div><div id="comment-tools-19801" class="comment-tools"></div><div class="clear"></div><div id="comment-19801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

