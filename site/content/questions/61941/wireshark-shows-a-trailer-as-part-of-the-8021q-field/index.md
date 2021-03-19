+++
type = "question"
title = "Wireshark shows a &quot;Trailer&quot; as part of the 802.1Q field"
description = '''Hello, I&#x27;m running Wireshark Version 2.0.2 (v2.0.2-0-ga16e22e from master-2.0). In some of the packets I&#x27;m analyzing, Wireshark is showing a Trailer as part of the VLAN tag. It shows up below the descriptions of the 3 VLAN sub-fields (Priority, CFI &amp;amp; ID) and the Type field (which, in this case, ...'''
date = "2017-06-11T19:26:00Z"
lastmod = "2017-06-19T14:00:00Z"
weight = 61941
keywords = [ "vlan", "trailer" ]
aliases = [ "/questions/61941" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark shows a "Trailer" as part of the 802.1Q field](/questions/61941/wireshark-shows-a-trailer-as-part-of-the-8021q-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61941-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm running Wireshark Version 2.0.2 (v2.0.2-0-ga16e22e from master-2.0). In some of the packets I'm analyzing, Wireshark is showing a Trailer as part of the VLAN tag. It shows up below the descriptions of the 3 VLAN sub-fields (Priority, CFI &amp; ID) and the Type field (which, in this case, is IPv4).</p><p>In one instance, this Trailer was 4 bytes long. In another it was much larger. In both cases, highlighting this Trailer field in the Packet Details pane showed that, in the Packet Bytes pane, the VLAN trailer was actually appended to the very end of the packet (not part of the VLAN field itself).</p><p>Googling around I saw mention of Wireshark Bug <strong>3587</strong>, that seemed to be relevant, but this bug report was dated in 2009, and it seemed unlikely that this bug was still present (unless... it reappeared?).</p><p>Any insight would be awesome.</p><p>Thx much...</p><p>feenyman99</p></div><div id="question-tags" class="tags-container tags">vlan trailer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '17, 19:26</strong></p><img src="https://secure.gravatar.com/avatar/ba0791e3a82c059268b46a45ae90989f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="feenyman99&#39;s gravatar image" /><p>feenyman99<br />
<span class="score" title="96 reputation points">96</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="feenyman99 has one accepted answer">25%</span></p></div></div><div id="comments-container-61941" class="comments-container"></div><div id="comment-tools-61941" class="comment-tools"></div><div class="clear"></div><div id="comment-61941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62141"></span>

<div id="answer-container-62141" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62141-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The dissection tree (the result of the dissection) is organized by relationship of the packet bytes to protocol layers, not by position of the bytes in the frame. Hence the trailer and/or checksum, although physically present at the end of the frame, are shown among the Ethernet/VLAN fields (and sorry, I cannot answer why it is shown in the VLAN portion rather than the Ethernet portion, I only remember that half of people thinks the VLAN should be treated as a separate layer and the other half thinks that it should be treated as part of Ethernet as IEEE wants it to be).</p><p>The occurrence of trailer octets is related to the minimum size of the Ethernet frame - if the useful contents is smaller than that, trailer octets are used to obtain the minimum size.</p><p>The bug you refer to deals with another issue - whether to handle the CRC in the end of the frame as CRC or as part of the payload, as the size of some types of payload is not expressed by any field of the frame.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '17, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-62141" class="comments-container"></div><div id="comment-tools-62141" class="comment-tools"></div><div class="clear"></div><div id="comment-62141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

