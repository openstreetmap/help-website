+++
type = "question"
title = "Strange Delay"
description = '''I am trying to get TCP and HTML working on &quot;Friendyarm&quot; board. The delays that I see in Wireshark are long. I get a &quot;syn&quot; packet and it shows that I sent the &quot;syn&quot; &quot;ack&quot; packet back 256 milliseconds later. There is no reason for this delay. It then gets worse. After getting the &quot;ack&quot; followed by the...'''
date = "2013-04-04T10:42:00Z"
lastmod = "2013-04-04T11:12:00Z"
weight = 20086
keywords = [ "delay", "problem" ]
aliases = [ "/questions/20086" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strange Delay](/questions/20086/strange-delay)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20086-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to get TCP and HTML working on "Friendyarm" board. The delays that I see in Wireshark are long. I get a "syn" packet and it shows that I sent the "syn" "ack" packet back 256 milliseconds later. There is no reason for this delay. It then gets worse. After getting the "ack" followed by the "psh" "ack" packet (with the HTML GET request) my response shows up about 3 seconds later - and meanwhile IE resets the connection. Is there a function in the router or PC that delays a packet with an error but still sends it through ? Any ideas on what might cause this ?</p></div><div id="question-tags" class="tags-container tags">delay problem</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '13, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/9a78648dd7bbea058b5e1adef678f8fe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vernon%20Lermond&#39;s gravatar image" /><p>Vernon Lermond<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vernon Lermond has no accepted answers">0%</span></p></div></div><div id="comments-container-20086" class="comments-container"></div><div id="comment-tools-20086" class="comment-tools"></div><div class="clear"></div><div id="comment-20086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20088"></span>

<div id="answer-container-20088" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20088-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like your "friendlyarm" board isn't really powerful enough to do what you want to do. I doubt that router or PC are causing any of this since your descriptions seems to say that packets coming back from that embedded device take a long time to arrive. You could verify this by using a tap just in front of the device, but that involves having a tap in the first place, and dedicated capture equipment to record the packets.</p><p>Can you monitor CPU load on the board? I guess it's probably 100% while processing your connection.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '13, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20088" class="comments-container"><span id="20090"></span><div id="comment-20090" class="comment"><div id="post-20090-score" class="comment-score">1</div><div class="comment-text"><p>Jasper's on the money here. General purpose computers with oodles of memory and processing power at hand can afford to lavish in the way they treat network connections. They can have buffers preallocated, and processes running "ready to take your call, right now". Embedded controller network stacks can't afford that, in that they have very tight limits on resources and have to be prudent. I'm pretty sure that's where your problem lies. Your stack is probably checking that it has a process running to connect to, allocates memory only when it needs, and so on. (That all said I know the Arduino (ATmega 328) and Wiznet 5100 combo I have responds to a SYN in about 20ms. Unfortunately though, at least with the standard library, it like sending flushing payload responses without delay , sending out tiny 60-70 byte packets, make the whole transaction quite slow)</p></div><div id="comment-20090-info" class="comment-info"><span class="comment-age">(04 Apr '13, 12:46)</span> martyvis</div></div></div><div id="comment-tools-20088" class="comment-tools"></div><div class="clear"></div><div id="comment-20088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

