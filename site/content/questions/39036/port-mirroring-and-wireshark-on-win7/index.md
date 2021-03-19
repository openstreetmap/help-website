+++
type = "question"
title = "port mirroring and wireshark on Win7"
description = '''Hi i have some problems. i use port mirroring and wireshark.  I want to do it on my main computer and monitor my second. But when i use wireshark i dont get much. I unchecked everything in my ethernet properties so that i only receive data from the secod computer. Is there anything else which i need...'''
date = "2015-01-11T02:37:00Z"
lastmod = "2015-01-11T05:53:00Z"
weight = 39036
keywords = [ "windows7", "port", "mirroring", "win7" ]
aliases = [ "/questions/39036" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [port mirroring and wireshark on Win7](/questions/39036/port-mirroring-and-wireshark-on-win7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39036-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i have some problems. i use port mirroring and wireshark. I want to do it on my main computer and monitor my second. But when i use wireshark i dont get much. I unchecked everything in my ethernet properties so that i only receive data from the secod computer. Is there anything else which i need to do with my first pc so that it will receive the data? I use WIn 7. When i try wireshark to monitor the data on the first pc it works fine. It just lookes that i dont "see" the data from the the second or at least only a small part of it. Btw the port mirroring is correctly checked it mantimes.</p><p>Thank You!</p></div><div id="question-tags" class="tags-container tags">windows7 port mirroring win7</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '15, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/f167851bdd929de87bcef0d7b8c2728c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaxMoritz&#39;s gravatar image" /><p>MaxMoritz<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaxMoritz has no accepted answers">0%</span></p></div></div><div id="comments-container-39036" class="comments-container"></div><div id="comment-tools-39036" class="comment-tools"></div><div class="clear"></div><div id="comment-39036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39041"></span>

<div id="answer-container-39041" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39041-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This looks like a typical SPAN port misconfiguration. Have you configured source port and destination ports correctly (they are often swapped by mistake)? It's usually not enough just to enable mirroring on the switch, but you also need to tell the switch which ports you want to have copied where.</p><p>Other than that, make sure that when you capture your checkmark for "Use Promiscuous mode" is active in the capture options dialog, because otherwise your first PC will not accept packets that are not meant for it's network card.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '15, 05:53</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39041" class="comments-container"></div><div id="comment-tools-39041" class="comment-tools"></div><div class="clear"></div><div id="comment-39041-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

