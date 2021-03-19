+++
type = "question"
title = "Why are Ethernet pseudo-wire packets over MPLS incorrectly identified as 802.3?"
description = '''I am sending Ethernet II frames with Destination MAC address of 02:29:99:99:00:21 wireshark is decoding those as 802.3 while two-octet field after Source MAC address is 0x8902. It seems The most significant bits of destination MAC address have special functions according to the IEEE 802 specificatio...'''
date = "2014-06-17T19:59:00Z"
lastmod = "2014-06-18T14:18:00Z"
weight = 33913
keywords = [ "mpls" ]
aliases = [ "/questions/33913" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why are Ethernet pseudo-wire packets over MPLS incorrectly identified as 802.3?](/questions/33913/why-are-ethernet-pseudo-wire-packets-over-mpls-incorrectly-identified-as-8023)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33913-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am sending Ethernet II frames with Destination MAC address of 02:29:99:99:00:21</p><p>wireshark is decoding those as 802.3 while two-octet field after Source MAC address is 0x8902. It seems The most significant bits of destination MAC address have special functions according to the IEEE 802 specification. Hence I changed the MAC address to 00:29:99:99:00:21 but couldn't solve the issue. I changed it again to one of the previously working MAC of 00:80:99:99:99:00:21 and workrd fine. I am trying to find out the reason and appreciate your help.</p></div><div id="question-tags" class="tags-container tags">mpls</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '14, 19:59</strong></p><img src="https://secure.gravatar.com/avatar/58c70d03384125664fa8cae7ff531791?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parisa&#39;s gravatar image" /><p>parisa<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parisa has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jun '14, 16:16</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-33913" class="comments-container"><span id="33914"></span><div id="comment-33914" class="comment"><div id="post-33914-score" class="comment-score"></div><div class="comment-text"><p>Could you please file a bug about this at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and, if possible, attach a capture file (pcap, pcap-ng, etc.) that shows this problem? We probably can't figure out the problem unless we see the capture.</p></div><div id="comment-33914-info" class="comment-info"><span class="comment-age">(17 Jun '14, 20:51)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-33913" class="comment-tools"></div><div class="clear"></div><div id="comment-33913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33940"></span>

<div id="answer-container-33940" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33940-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Because they're carried over MPLS, and the default payload type for MPLS, when the MPLS dissector can't determine the payload type, is "Ethernet pseudo-wire with a control word", but, in your traffic, the MPLS traffic is "Ethernet pseudo-wire <em>without</em> a control word". See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10195">the bug you filed</a> for details on how to change the default.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '14, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jun '14, 14:19</p></div></div><div id="comments-container-33940" class="comments-container"></div><div id="comment-tools-33940" class="comment-tools"></div><div class="clear"></div><div id="comment-33940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

