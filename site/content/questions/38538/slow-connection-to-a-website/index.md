+++
type = "question"
title = "Slow connection to a website"
description = '''Hello, I&#x27;m looking for help about a problem that I have on my network. Some users complain about a very slow connection to a website, so I ran wireshark and did some tests. Sometime the website load very quickly and other times, it&#x27;s just impossible to reach the page. When the website is impossible ...'''
date = "2014-12-12T01:32:00Z"
lastmod = "2015-04-17T16:28:00Z"
weight = 38538
keywords = [ "slow" ]
aliases = [ "/questions/38538" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slow connection to a website](/questions/38538/slow-connection-to-a-website)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38538-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm looking for help about a problem that I have on my network. Some users complain about a very slow connection to a website, so I ran wireshark and did some tests. Sometime the website load very quickly and other times, it's just impossible to reach the page. When the website is impossible to reach, other website (like google) works perfectly.</p><p>I don't know much about wireshark and network so I would very much appreciate if you could take a look at my log, (I use tracewangler for anonymise the file but maybe I remove too many information, tell me if that's the case :) ). There's two files, one where the connection work fine, and the other where the connection took + 1min. <a href="https://docs.google.com/file/d/0B8elDt4XYQVoRk5mZlJybzlGeEU/edit?pli=1">https://docs.google.com/file/d/0B8elDt4XYQVoRk5mZlJybzlGeEU/edit?pli=1</a> <a href="https://docs.google.com/file/d/0B8elDt4XYQVoRDNaQ3ktTHliM2s/edit">https://docs.google.com/file/d/0B8elDt4XYQVoRDNaQ3ktTHliM2s/edit</a> (English is not my native language, sorry for the mistakes..)</p><p>Thanks</p><p>Valentin Chesné</p></div><div id="question-tags" class="tags-container tags">slow</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '14, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/86a478bb8af19bb47e432b000f773502?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vch&#39;s gravatar image" /><p>vch<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vch has no accepted answers">0%</span></p></div></div><div id="comments-container-38538" class="comments-container"></div><div id="comment-tools-38538" class="comment-tools"></div><div class="clear"></div><div id="comment-38538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41553"></span>

<div id="answer-container-41553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41553-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is a little bit sadly that we can´t see the session termination in the good example for baselining reasons.</p><p>But what do we see in the traces. We see that you have four parallel sessions to the server "x.y.218.39" And all are established at nearly the same time.</p><p>Then we see some data transmission and a some Retransmissions und Loast Packets. But at this moment we can´t see that they are causing some significant problems. But shortly after that period at Paket 125 we can see that the server starts closing the sockets by sending "FIN" Pakets. This is normally not normal, becaus ethe client is normally the session leader. The Client terminates the Session with an RST, maybe he think that this behaviour is not normal. In Paket 1130 we can see an ACK for the FIN seen in Paket 125. It took 77 seconds for this ACK. After that the Client send an RST. This Session uses Port 60636 on Client Side. So apoparently the Client needs to stop this before sending new SYN Packets.</p><p>I can´t tell you more about the need of the session and why the servers closes the ports, because I can´t see the application protocol layer. Maybe it is a ntework problem, because I see in this minute less traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Apr '15, 16:28</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-41553" class="comments-container"></div><div id="comment-tools-41553" class="comment-tools"></div><div class="clear"></div><div id="comment-41553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

