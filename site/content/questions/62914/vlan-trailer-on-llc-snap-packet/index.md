+++
type = "question"
title = "Vlan trailer on LLC-SNAP packet"
description = '''Hi, When import wireshark LLC-SNAP packet, it recognizes an eight bytes trailer as a part of the Vlan Tag. I haven&#x27;t read about this field and don&#x27;t know its meaning, can you tell me where is it come from? and does the &quot;length&quot; (a part of the LLC - SNAP packet) filed has influence on it? Thanks , Ay...'''
date = "2017-07-20T02:09:00Z"
lastmod = "2017-07-20T03:56:00Z"
weight = 62914
keywords = [ "snap", "llcsnap", "trailer" ]
aliases = [ "/questions/62914" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Vlan trailer on LLC-SNAP packet](/questions/62914/vlan-trailer-on-llc-snap-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62914-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, When import wireshark LLC-SNAP packet, it recognizes an eight bytes trailer as a part of the Vlan Tag. I haven't read about this field and don't know its meaning, can you tell me where is it come from? and does the "length" (a part of the LLC - SNAP packet) filed has influence on it?</p><p>Thanks , Aya</p></div><div id="question-tags" class="tags-container tags">snap llcsnap trailer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jul '17, 02:09</strong></p><img src="https://secure.gravatar.com/avatar/3cca087c83f55798a15e19db6111ce67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aya%20dagan&#39;s gravatar image" /><p>aya dagan<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aya dagan has no accepted answers">0%</span></p></div></div><div id="comments-container-62914" class="comments-container"></div><div id="comment-tools-62914" class="comment-tools"></div><div class="clear"></div><div id="comment-62914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62920"></span>

<div id="answer-container-62920" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62920-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is the common issue of octets belogning to the same logical layer being scattered at different physical places in the packet. There is the Ethernet header, the Vlan header, and the higher layers (either encapsulated using LLC or directly, identified by Ethertype in the Vlan header). If the headers + payload occupy less bytes than the minimum required length of an Ethernet frame, the payload is followed by stuffing octets, which the Wireshark dissector shows as part of the VLAN layer (or Ethernet layer if VLAN layer is not used in that frame), although physically they are not directly there. If you draw open the packet bytes pane from the bottom of the window and click the Trailer: line in the dissection tree, you'll see the last bytes of the frame to be highlighted in the packet bytes pane.</p><p>This behaviour does not depend on whether the payload is identified using LLC or Ethertype.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jul '17, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62920" class="comments-container"><span id="62926"></span><div id="comment-62926" class="comment"><div id="post-62926-score" class="comment-score"></div><div class="comment-text"><p>Hi , Thanks for you answer, but is the minimum packet size isn't 64 bytes? because my packet is 819 bytes, the user data is 731 bytes (payload) + 8 bytes TCP header + 20 bytes IPV4 header (=759 bytes) The Ethertype length filed is 789 , and I have 8 bytes trailer.</p><p>Am I missing something? because it looks my packet is larger than the minimum, packets size.</p><p>Thanks again Aya</p></div><div id="comment-62926-info" class="comment-info"><span class="comment-age">(20 Jul '17, 05:27)</span> aya dagan</div></div><span id="62929"></span><div id="comment-62929" class="comment"><div id="post-62929-score" class="comment-score"></div><div class="comment-text"><p>Well, it is hard to guess what's going on from incomplete information. If you can publish an export of that single packet into a pcap file at cloudhark or any file sharing service, login-free, and edit your question with a link to it, you shall get better information.</p></div><div id="comment-62929-info" class="comment-info"><span class="comment-age">(20 Jul '17, 07:56)</span> sindy</div></div></div><div id="comment-tools-62920" class="comment-tools"></div><div class="clear"></div><div id="comment-62920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

