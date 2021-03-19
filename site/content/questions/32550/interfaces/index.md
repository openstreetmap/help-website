+++
type = "question"
title = "Interfaces"
description = '''Estoy trabajando con backtrack5 en un maquina virtual y quiero capturar todo el trafico de la red, pero solo me permite capturar el de el ordenador en el que está instalado wireshark, y no me aparece la interface wifi.  From Google Translate: Backtrack5 I&#x27;m working with a virtual machine and I want ...'''
date = "2014-05-06T08:57:00Z"
lastmod = "2014-05-06T09:10:00Z"
weight = 32550
keywords = [ "interface", "wifi" ]
aliases = [ "/questions/32550" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Interfaces](/questions/32550/interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32550-score" class="post-score" title="current number of votes">0</div><span id="post-32550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Estoy trabajando con backtrack5 en un maquina virtual y quiero capturar todo el trafico de la red, pero solo me permite capturar el de el ordenador en el que está instalado wireshark, y no me aparece la interface wifi.</p><p>From <a href="https://translate.google.com/">Google Translate</a>: Backtrack5 I'm working with a virtual machine and I want to capture all network traffic, but only allows me to capture the computer on which it is installed wireshark, and the wifi interface does not show me.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '14, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/a4361afacd7a3f3052ba3dc38fe704b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yadyz%20Qs&#39;s gravatar image" /><p><span>Yadyz Qs</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yadyz Qs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 May '14, 09:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-32550" class="comments-container"></div><div id="comment-tools-32550" class="comment-tools"></div><div class="clear"></div><div id="comment-32550-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32551"></span>

<div id="answer-container-32551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32551-score" class="post-score" title="current number of votes">1</div><span id="post-32551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll not have access to the physical network cards of the computer your VM is running on, so you can't see the WiFi adapter from the Backtrack VM. If you need to work with WiFi inside a Backtrack VM (or Kali, as it is called now) you could use an USB WiFi adapter (e.g. Alfa) and map that into the VM. Other than that, you'll have to run Backtrack/Kali directly on your hardware to be able to capture on the cards.</p><p>P.S: this Q&amp;A is using english, so please try to use it as well ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '14, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-32551" class="comments-container"></div><div id="comment-tools-32551" class="comment-tools"></div><div class="clear"></div><div id="comment-32551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

