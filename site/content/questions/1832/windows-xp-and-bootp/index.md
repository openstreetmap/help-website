+++
type = "question"
title = "Windows XP and bootp?"
description = '''Is it normal for an XP computer to use bootp to request it&#x27;s IP? From the capture it appears the client only talks to the gateway and not direct to the DHCP server. The address in question is a manual DHCP that would be dished out for this client. So I see a DHCP request, 2 DHCP ACKs from the gatewa...'''
date = "2011-01-20T07:55:00Z"
lastmod = "2011-01-20T16:43:00Z"
weight = 1832
keywords = [ "windows", "dhcp", "bootp" ]
aliases = [ "/questions/1832" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Windows XP and bootp?](/questions/1832/windows-xp-and-bootp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1832-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it normal for an XP computer to use bootp to request it's IP? From the capture it appears the client only talks to the gateway and not direct to the DHCP server. The address in question is a manual DHCP that would be dished out for this client. So I see a DHCP request, 2 DHCP ACKs from the gateway and 3 G-ARPs from the client.</p></div><div id="question-tags" class="tags-container tags">windows dhcp bootp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '11, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/39cd80ed85e55962a47b03253968662c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="networkguy09&#39;s gravatar image" /><p>networkguy09<br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="networkguy09 has no accepted answers">0%</span></p></div></div><div id="comments-container-1832" class="comments-container"></div><div id="comment-tools-1832" class="comment-tools"></div><div class="clear"></div><div id="comment-1832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1837"></span>

<div id="answer-container-1837" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1837-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The gateway can also forward DHCP request to a remote dhcp server. This is sometimes known as a dhcp helper or dhcp relay. So basically, the gateway can convert packets/frames containing UDP sent to 255.255.255.255/FF:FF:FF:FF:FF:FF to a destination address assigned by the network administrator. In this case, there is a a "giaddr" field in the dhcp header that allows the router to record information so the dhcp server can respond with an appropriate address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '11, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p>Paul Stewart<br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1837" class="comments-container"></div><div id="comment-tools-1837" class="comment-tools"></div><div class="clear"></div><div id="comment-1837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1836"></span>

<div id="answer-container-1836" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1836-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that's normal. Very ofter the 'gateway' acts as DHCP server as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '11, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1836" class="comments-container"></div><div id="comment-tools-1836" class="comment-tools"></div><div class="clear"></div><div id="comment-1836-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

