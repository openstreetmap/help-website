+++
type = "question"
title = "VERY Novis User - Question"
description = '''My Q: On my first overall use I chose to view tcp vs http. Wondering what this might mean: It says: Who has (xyz IP address)? tell (my IP address) Source: dellpcba_f5:75:85 - destination: broadcast - protocol: ARP second: Source: Cisco_eb:db:dd - DellPcba_f5:75:85 - Protocol: ARP Then it says: xyz I...'''
date = "2010-11-24T09:47:00Z"
lastmod = "2010-11-24T11:07:00Z"
weight = 1110
keywords = [ "question", "http-tcp" ]
aliases = [ "/questions/1110" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VERY Novis User - Question](/questions/1110/very-novis-user-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1110-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My Q:</p><p>On my first overall use I chose to view tcp vs http. Wondering what this might mean:</p><p>It says: Who has (xyz IP address)? tell (my IP address)</p><p>Source: dellpcba_f5:75:85 - destination: broadcast - protocol: ARP second: Source: Cisco_eb:db:dd - DellPcba_f5:75:85 - Protocol: ARP</p><p>Then it says: xyz IP address is @ 00:14:f1:eb:db:dd</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">question http-tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '10, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/e31bc9cf0d0edcaa63403e79a9aee2f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valioop&#39;s gravatar image" /><p>valioop<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valioop has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Nov '10, 10:00</p></div></div><div id="comments-container-1110" class="comments-container"><span id="1137"></span><div id="comment-1137" class="comment"><div id="post-1137-score" class="comment-score"></div><div class="comment-text"><p>Check out some of the free Wireshark training courses we offer over at chappellseminars.com. There are also some practice trace files and videos over at wiresharkbook.com.</p></div><div id="comment-1137-info" class="comment-info"><span class="comment-age">(27 Nov '10, 14:34)</span> lchappell ♦</div></div></div><div id="comment-tools-1110" class="comment-tools"></div><div class="clear"></div><div id="comment-1110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1112"></span>

<div id="answer-container-1112" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1112-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is an ARP Request and an ARP response, which basically means that the Dell PC is looking for the Ethernet MAC address of a Cisco Router, which probably is the default gateway. Even though the Dell PC is communicating from it's own IP to the target IP (on OSI layer 3) the actual frame needs to be transported by Layer 2 (Ethernet in this case), and for that the Dell PC asks for the Ethernet MAC to be able to send the packet. It is sort of a "name resolution" between layer 2 and 3.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '10, 11:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1112" class="comments-container"><span id="1113"></span><div id="comment-1113" class="comment"><div id="post-1113-score" class="comment-score"></div><div class="comment-text"><p>Gotcha! :)</p></div><div id="comment-1113-info" class="comment-info"><span class="comment-age">(24 Nov '10, 11:54)</span> valioop</div></div></div><div id="comment-tools-1112" class="comment-tools"></div><div class="clear"></div><div id="comment-1112-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

