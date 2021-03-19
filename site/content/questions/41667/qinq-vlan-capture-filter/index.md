+++
type = "question"
title = "QinQ VLAN capture filter"
description = '''I&#x27;m trying to set up a capture filter for the following double tagged packets: Wireshark v 1.12.4 running on Windows 8.1 with Intel PRO 1000 MT NIC Ethernet II  Type: 0x9100 802.1Q Virtual LAN:  Type: 0x8100 802.1Q Virtual LAN:  Type: 0x0800 I have tried &#x27;vlan&#x27; and also &#x27;vlan and vlan&#x27; but no packet...'''
date = "2015-04-22T03:21:00Z"
lastmod = "2015-04-22T04:02:00Z"
weight = 41667
keywords = [ "filter", "double", "tagged", "vlan", "capture" ]
aliases = [ "/questions/41667" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [QinQ VLAN capture filter](/questions/41667/qinq-vlan-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41667-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to set up a capture filter for the following double tagged packets:</p><p>Wireshark v 1.12.4 running on Windows 8.1 with Intel PRO 1000 MT NIC</p><p>Ethernet II<br />
Type: 0x9100<br />
802.1Q Virtual LAN:<br />
Type: 0x8100<br />
802.1Q Virtual LAN:<br />
Type: 0x0800</p><p>I have tried 'vlan' and also 'vlan and vlan' but no packets are captured. If I capture without a capture filter I can see all packets and both inner and outer VLAN tags.</p><p>Any help would be greatly appreciated.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Q-in-Q_2_83Q0ARO.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">filter double tagged vlan capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '15, 03:21</strong></p><img src="https://secure.gravatar.com/avatar/7addf8865ef7a9819162afe977458460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NickR&#39;s gravatar image" /><p>NickR<br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NickR has one accepted answer">50%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '15, 03:29</p></div></div><div id="comments-container-41667" class="comments-container"></div><div id="comment-tools-41667" class="comment-tools"></div><div class="clear"></div><div id="comment-41667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41671"></span>

<div id="answer-container-41671" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41671-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>See my answer to a very similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/31953/unusual-behavior-with-stacked-vlan-tags-and-capture-filter/32006">https://ask.wireshark.org/questions/31953/unusual-behavior-with-stacked-vlan-tags-and-capture-filter/32006</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 04:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '15, 04:07</p></div></div><div id="comments-container-41671" class="comments-container"><span id="41677"></span><div id="comment-41677" class="comment"><div id="post-41677-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, that does shed some light on the issue.</p><p>I can capture the packets from a specific inner vlan using:</p><p>vlan <strong>or</strong> vlan 618<br />
vlan 202 <strong>or</strong> vlan 618<br />
vlan xxx <strong>or</strong> vlan 618</p><p>All of the above allow packets with an inner vlan tag of 618 to be captured.</p><p>Using 'vlan 618' alone doesn't capture any packets as expected.</p><p>Using and combination of 'vlan <strong>and</strong> vlan' or 'vlan xxx <strong>and</strong> vlan xxx' doesn't capture any packets.</p><p>I'm going to mark this as answered as I can now capture on inner vlan tag.</p><p>Thanks for the assistance.</p></div><div id="comment-41677-info" class="comment-info"><span class="comment-age">(22 Apr '15, 05:43)</span> NickR</div></div><span id="41678"></span><div id="comment-41678" class="comment"><div id="post-41678-score" class="comment-score"></div><div class="comment-text"><p>I converted you answer to a comment, as that's how this site works. Please see the FAQ: <a href="https://ask.wireshark.org/faq/">https://ask.wireshark.org/faq/</a></p></div><div id="comment-41678-info" class="comment-info"><span class="comment-age">(22 Apr '15, 05:45)</span> Kurt Knochner ♦</div></div><span id="41680"></span><div id="comment-41680" class="comment"><div id="post-41680-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I'm going to mark this as answered as I can now capture on inner vlan tag.<br />
Thanks for the assistance.</p></blockquote><p>O.K. You're welcome.</p></div><div id="comment-41680-info" class="comment-info"><span class="comment-age">(22 Apr '15, 05:47)</span> Kurt Knochner ♦</div></div><span id="41681"></span><div id="comment-41681" class="comment"><div id="post-41681-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41681-info" class="comment-info"><span class="comment-age">(22 Apr '15, 06:06)</span> grahamb ♦</div></div></div><div id="comment-tools-41671" class="comment-tools"></div><div class="clear"></div><div id="comment-41671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

