+++
type = "question"
title = "Is it syn Dos attack?"
description = '''Guys, I have packet, but not sure is it syn dos attack? If it&#x27;s not, please can you explain why? I see only syn packets and thought syn flood should look like that.'''
date = "2014-11-21T17:41:00Z"
lastmod = "2014-11-22T03:52:00Z"
weight = 38063
keywords = [ "flooding", "syn", "wireshark" ]
aliases = [ "/questions/38063" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it syn Dos attack?](/questions/38063/is-it-syn-dos-attack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38063-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Guys, I have <a href="http://postimg.org/image/ai01fmr0n/">packet</a>, but not sure is it syn dos attack? If it's not, please can you explain why? I see only syn packets and thought syn flood should look like that.</p></div><div id="question-tags" class="tags-container tags">flooding syn wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '14, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/f6cd72fe54f3eed9c68aaa327c1e44ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Madina%20Mika%20Igibayeva&#39;s gravatar image" /><p>Madina Mika ...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Madina Mika Igibayeva has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Nov '14, 02:47</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-38063" class="comments-container"></div><div id="comment-tools-38063" class="comment-tools"></div><div class="clear"></div><div id="comment-38063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38066"></span>

<div id="answer-container-38066" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38066-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe it is, but I don't think so - the frequency is too slow. SYN dos attacks require hundreds and thousands of SYN packets per second, and you have huge jumps in the time column. So I doubt this is a SYN flood attack, or it is a pretty sloppy one.</p><p>By the way, for determining that type of attack it is not good enough to post an image with some SYN packets, especially when the time column format is not clear. Does it display delta times or relative times? If those are delta times, you have pauses of 17 seconds and more between SYNs, which is way too much for any kind of attack. If those are relative times, your column sorting is bad, because they should increase, not go up and down.</p><p>Also, to determine a SYN flood attack you'd need to check for SYN/ACKs and if they're answered with a third handshake packet. Plus, your "flood" is comming from a private IP, which is highly unusal for an attack, because it means it is coming from your local network, and you can easily identify the source .</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '14, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38066" class="comments-container"></div><div id="comment-tools-38066" class="comment-tools"></div><div class="clear"></div><div id="comment-38066-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

