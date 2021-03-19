+++
type = "question"
title = "IEEE 802.11 Vendor-specific Action"
description = '''I want to make dissector for custom protocol, that applies IEEE802.11 Action Vendor frame technology. I made capture and it turns out the packets of this protocol are marked malformed. The packet contains radiotap header, followed by radio header and then comes IEEE 802.11, the type is management fr...'''
date = "2016-10-29T08:19:00Z"
lastmod = "2016-10-29T15:50:00Z"
weight = 56816
keywords = [ "specific", "customprotocols", "dissector", "ieee802_11", "wireshark" ]
aliases = [ "/questions/56816" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [IEEE 802.11 Vendor-specific Action](/questions/56816/ieee-80211-vendor-specific-action)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56816-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to make dissector for custom protocol, that applies IEEE802.11 Action Vendor frame technology. I made capture and it turns out the packets of this protocol are marked malformed. The packet contains radiotap header, followed by radio header and then comes IEEE 802.11, the type is management frame and the subtype is action. The problem comes with IEEE 802.11 wireless LAN management frame, the category code is Vendor Specific(127), followed by OUI(Organization Unique Identifier). The remaining bytes (without 4 bytes for frame check sum) must be Vendor Specific content, but for some reason wireshark is looking for tag number and tag length, this two fields are marked red. I am wondering if I can make dissector that works between IEEE 802.11 Action and IEEE 802.11 wireless LAN management frame. I will add the capture, and you can use this filter (wlan_mgt.fixed.category_code == 127 &amp;&amp; wlan_mgt.tag.oui == 1637940).</p><p>capture - <a href="https://drive.google.com/file/d/0BzvRjmQgxbzUNWdMTWFSQkphQmM/view?usp=sharing">https://drive.google.com/file/d/0BzvRjmQgxbzUNWdMTWFSQkphQmM/view?usp=sharing</a></p></div><div id="question-tags" class="tags-container tags">specific customprotocols dissector ieee802_11 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '16, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/d9456ad3fef8a9368ca3fabce70056ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ivan1&#39;s gravatar image" /><p>ivan1<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ivan1 has no accepted answers">0%</span></p></div></div><div id="comments-container-56816" class="comments-container"></div><div id="comment-tools-56816" class="comment-tools"></div><div class="clear"></div><div id="comment-56816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56822"></span>

<div id="answer-container-56822" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56822-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at epan/dissectors/packet-ieee8011.c:add_ff_action_vendor_specific() there seems to be no code handling OUI's other than OUI_MARVELL and OUI_WFA, and there's no subdissector table to register to. So other than modifying this code and recompiling Wireshark I see no option getting this in and the moment.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '16, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56822" class="comments-container"></div><div id="comment-tools-56822" class="comment-tools"></div><div class="clear"></div><div id="comment-56822-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

