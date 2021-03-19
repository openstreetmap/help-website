+++
type = "question"
title = "x8033? What exactly is this?"
description = '''I have a program sending a raw ethernet packet of protocol &quot;0x8033&quot;. The info says Ethernet II, so I&#x27;m assuming it&#x27;s an ethernet packet, but I wanted confirmation. What is the 8033? Here&#x27;s the packet:  No. Time Source Destination Protocol Length Info 4 2.557326000 Dell_b9:54:a3 Broadcast 0x8033 80 E...'''
date = "2014-04-03T09:08:00Z"
lastmod = "2016-11-12T16:42:00Z"
weight = 31489
keywords = [ "ethernet", "8033" ]
aliases = [ "/questions/31489" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [x8033? What exactly is this?](/questions/31489/x8033-what-exactly-is-this)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31489-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a program sending a raw ethernet packet of protocol "0x8033". The info says Ethernet II, so I'm assuming it's an ethernet packet, but I wanted confirmation. What is the 8033?</p><p>Here's the packet: No. Time Source Destination Protocol Length Info 4 2.557326000 Dell_b9:54:a3 Broadcast 0x8033 80 Ethernet II</p><p>Frame 4: 80 bytes on wire (640 bits), 80 bytes captured (640 bits) on interface 0 Ethernet II, Src: Dell_b9:54:a3 (b8:ca:3a:b9:54:a3), Dst: Broadcast (ff:ff:ff:ff:ff:ff) Data (66 bytes)</p><p>0000 21 01 01 42 00 00 0d 6c 06 04 03 00 19 bc b8 ca !..B...l........</p><p>0010 3a b9 54 a3 c0 a8 02 63 ff ff ff ff ff ff 00 00 :.T....c........</p><p>0020 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................</p><p>0030 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................</p><p>0040 00 00<br />
</p></div><div id="question-tags" class="tags-container tags">ethernet 8033</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '14, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/17cd21ccb1cf25baa23f324d5afb09bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="katlucas&#39;s gravatar image" /><p>katlucas<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="katlucas has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-31489" class="comments-container"></div><div id="comment-tools-31489" class="comment-tools"></div><div class="clear"></div><div id="comment-31489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="31490"></span>

<div id="answer-container-31490" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31490-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to the <a href="http://standards.ieee.org/develop/regauth/ethertype/eth.txt">IEEE</a>, it is an ether type that VIA Systems registered. That, or a system on your network is sending strange ether types :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '14, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31490" class="comments-container"><span id="31495"></span><div id="comment-31495" class="comment"><div id="post-31495-score" class="comment-score"></div><div class="comment-text"><p>Thanks. hmm, yeah. I'm trying to recreate the packet in vb.net and hoping this would give me some insight on how to.</p></div><div id="comment-31495-info" class="comment-info"><span class="comment-age">(03 Apr '14, 09:38)</span> katlucas</div></div></div><div id="comment-tools-31490" class="comment-tools"></div><div class="clear"></div><div id="comment-31490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57342"></span>

<div id="answer-container-57342" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57342-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>HikVision SADP (discovery protocol) tool, for managing settings on Hikvision IP network cameras.</p><p>Cameras broadcast on this protocol. SADP tool (windows only), sends back configuration settings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '16, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/db72d47551e87515aff38772ad57e651?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davemc50&#39;s gravatar image" /><p>davemc50<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davemc50 has no accepted answers">0%</span></p></div></div><div id="comments-container-57342" class="comments-container"></div><div id="comment-tools-57342" class="comment-tools"></div><div class="clear"></div><div id="comment-57342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

