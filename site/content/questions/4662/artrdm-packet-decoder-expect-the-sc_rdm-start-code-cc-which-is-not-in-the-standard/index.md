+++
type = "question"
title = "ArtRdm packet decoder expect the SC_RDM start code ($CC), which is not in the standard"
description = '''Hello everybody! I checked the FAQ before posting but I did not find anything about ArtRdm packets. These packet encapsulate RDM into ArtNet. Here you can find a document about the protocol: www.artisticlicence.com/WebSiteMaster/User%20Guides/art-net.pdf On page 30, you will see that the ArtRdm pack...'''
date = "2011-06-22T01:14:00Z"
lastmod = "2011-06-22T04:54:00Z"
weight = 4662
keywords = [ "artrdm", "rdm", "artnet" ]
aliases = [ "/questions/4662" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [ArtRdm packet decoder expect the SC\_RDM start code ($CC), which is not in the standard](/questions/4662/artrdm-packet-decoder-expect-the-sc_rdm-start-code-cc-which-is-not-in-the-standard)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4662-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody! I checked the FAQ before posting but I did not find anything about ArtRdm packets.</p><p>These packet encapsulate RDM into ArtNet. Here you can find a document about the protocol: www.artisticlicence.com/WebSiteMaster/User%20Guides/art-net.pdf</p><p>On page 30, you will see that the ArtRdm packet expect the RDM data WITHOUT start code (here erroneously referenced as "DMX start code").</p><p>In fact, if you download their DMX Workshop free program and capture any ArtRdm packet, you will see that wireshark fails to decode the rdm data just because everything is shifted by one byte. Works fine if you provide an ArtRdm packet WITH the $CC as the first rdm-data byte.</p><p>Here you can see a screenshot of such a packet: http://dl.dropbox.com/u/19254161/esta/Screenshot-eth0%20-%20Wireshark-chksum_ERRORE.png</p><p>the start code expected by wireshark (not present) is $CC; the message len ($18) is then wrong because fetched in the wrong place (the byte right after the real message len byte).</p><p>Of course, everything that follows in the packet decoding is wrong.</p><p>I'm using wireshark 1.2.11 under debian squeeze.</p><p>May you please help me?</p><p>Thanks a lot and Best Regards!</p></div><div id="question-tags" class="tags-container tags">artrdm rdm artnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '11, 01:14</strong></p><img src="https://secure.gravatar.com/avatar/66ca9f10c339533c013586e829bb33b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="proboscide99&#39;s gravatar image" /><p>proboscide99<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="proboscide99 has no accepted answers">0%</span></p></div></div><div id="comments-container-4662" class="comments-container"></div><div id="comment-tools-4662" class="comment-tools"></div><div class="clear"></div><div id="comment-4662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4665"></span>

<div id="answer-container-4665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4665-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That requires a code change. You should file this bug report at <a href="https://bugs.wireshark.org">bugs.wireshark.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '11, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-4665" class="comments-container"></div><div id="comment-tools-4665" class="comment-tools"></div><div class="clear"></div><div id="comment-4665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

