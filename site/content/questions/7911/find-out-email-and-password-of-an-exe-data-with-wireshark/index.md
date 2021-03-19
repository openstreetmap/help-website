+++
type = "question"
title = "Find out email and password of an .exe data with Wireshark."
description = '''A few days ago, I downloaded a simple program. The program sends data you can enter in message fields to a certain email. Somehow the email sends it to itself so the password must be the same as programmed in the program. I tried to change the password of the email address and the program didn&#x27;t wor...'''
date = "2011-12-12T05:47:00Z"
lastmod = "2011-12-16T05:28:00Z"
weight = 7911
keywords = [ "password", "email" ]
aliases = [ "/questions/7911" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Find out email and password of an .exe data with Wireshark.](/questions/7911/find-out-email-and-password-of-an-exe-data-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7911-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A few days ago, I downloaded a simple program. The program sends data you can enter in message fields to a certain email. Somehow the email sends it to itself so the password must be the same as programmed in the program. I tried to change the password of the email address and the program didn't work anymore. The program is an exe that you double click on and it starts itself.</p><p>My question is: Is there a way to find out the password and email address the program is connected to, and if so, what do I have to do? I'm asking out of curiosity as I'm trying it with my own program and I have email and password anyway.</p><p>I don't have any knowledge of programming. I'm German so sorry for my bad English. Peace.</p></div><div id="question-tags" class="tags-container tags">password email</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '11, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/ab4d54f3bc4b922c88a3e545a0e16b09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timmy%20Randall&#39;s gravatar image" /><p>Timmy Randall<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timmy Randall has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 21:17</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-7911" class="comments-container"><span id="7912"></span><div id="comment-7912" class="comment"><div id="post-7912-score" class="comment-score"></div><div class="comment-text"><p>which program ? Where did you download it?</p></div><div id="comment-7912-info" class="comment-info"><span class="comment-age">(12 Dec '11, 06:29)</span> Landi</div></div><span id="7913"></span><div id="comment-7913" class="comment"><div id="post-7913-score" class="comment-score"></div><div class="comment-text"><p>a friend of mine scripted it for my email and pass</p></div><div id="comment-7913-info" class="comment-info"><span class="comment-age">(12 Dec '11, 06:52)</span> Timmy Randall</div></div><span id="7918"></span><div id="comment-7918" class="comment"><div id="post-7918-score" class="comment-score"></div><div class="comment-text"><p>then i suggest u ask your friend about the way he scripted his program. I suppose your concern is whether s.o. could find out by sniffing the traffic - in that case it's dependent on the way your friend encrypts the data before being transmitted</p></div><div id="comment-7918-info" class="comment-info"><span class="comment-age">(12 Dec '11, 11:50)</span> Landi</div></div><span id="7945"></span><div id="comment-7945" class="comment"><div id="post-7945-score" class="comment-score"></div><div class="comment-text"><p>as far as i know its scripted in c++, no idea if thats the answer to your question my english is not perfect and im an amateur :)</p><p>thanks for your help so far</p></div><div id="comment-7945-info" class="comment-info"><span class="comment-age">(13 Dec '11, 05:37)</span> Timmy Randall</div></div><span id="7946"></span><div id="comment-7946" class="comment"><div id="post-7946-score" class="comment-score"></div><div class="comment-text"><p>(native on) Du solltest einfach deinen Kumpel mal fragen, wie er die Anwendung geschrieben hat. Normalerweise verschlüsselt man Benutzername / Email / Passwort vor dem senden, damit die Daten NICHT mit Wireshark o.ä. mitgelesen werden können. Wenn Dir das Sorgen macht, dass jemand deine Daten mitlesen könnte, frag deinen Bekannten wie die Daten übertragen werden.</p><p>(native off)</p></div><div id="comment-7946-info" class="comment-info"><span class="comment-age">(13 Dec '11, 06:06)</span> Landi</div></div></div><div id="comment-tools-7911" class="comment-tools"></div><div class="clear"></div><div id="comment-7911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8007"></span>

<div id="answer-container-8007" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8007-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>ich will doch nur wissen was übertragen wird mit dem programm und weiß nicht wie es geht &lt;.&lt; wenn ich das programm starte sehe ich da nur viele ips wenn ich da drauf klicke sehe ich bloß zeichensalat</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '11, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/ab4d54f3bc4b922c88a3e545a0e16b09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Timmy%20Randall&#39;s gravatar image" /><p>Timmy Randall<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Timmy Randall has no accepted answers">0%</span></p></div></div><div id="comments-container-8007" class="comments-container"><span id="8008"></span><div id="comment-8008" class="comment"><div id="post-8008-score" class="comment-score"></div><div class="comment-text"><p>Dann frag nicht hier im Expertenforum, sondern lies dir einfach mal die Tutorials und First-Step-Guides durch. Auf der Homepage findest du tonnenweise Material für den Einstieg.</p><p>Hint: Such dir die IP raus, an die das Programm die Daten sendet und filter danach (ip.addr==1.2.3.4). Wenn Du die Verbindungen hast, wird normalerwiese eins der ersten ausgehenden Pakete von Deiner IP nach dem Handshake (SYN, SYN/ACK, ACK) die Daten beinhalten. Wenns Zeichensalat ist, dann wirds wohl auch verschlüsselt sein</p></div><div id="comment-8008-info" class="comment-info"><span class="comment-age">(16 Dec '11, 05:34)</span> Landi</div></div></div><div id="comment-tools-8007" class="comment-tools"></div><div class="clear"></div><div id="comment-8007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

