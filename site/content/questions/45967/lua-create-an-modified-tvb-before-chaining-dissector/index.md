+++
type = "question"
title = "Lua: create an modified TVB before chaining dissector"
description = '''Hi,  I want to dissect an Wifi packet trace that seems to use the PTP/USB packet format instead of the PTP/IP one. Except two butter offsets and one changed field the packets are identical.  The easiest solution would be to create an modified copy of the tvb and pass it to the original ptp/ip dissec...'''
date = "2015-09-20T01:24:00Z"
lastmod = "2016-05-15T05:06:00Z"
weight = 45967
keywords = [ "lua", "dissector", "tvb" ]
aliases = [ "/questions/45967" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua: create an modified TVB before chaining dissector](/questions/45967/lua-create-an-modified-tvb-before-chaining-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45967-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to dissect an Wifi packet trace that seems to use the PTP/USB packet format instead of the PTP/IP one. Except two butter offsets and one changed field the packets are identical. The easiest solution would be to create an modified copy of the tvb and pass it to the original ptp/ip dissector. Is that possible? How?</p><p>Thanks, Thomas</p></div><div id="question-tags" class="tags-container tags">lua dissector tvb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '15, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/4875dbde2eebdc54b43edef7b9c29473?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Thomas%20E&#39;s gravatar image" /><p>Thomas E<br />
<span class="score" title="36 reputation points">36</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Thomas E has no accepted answers">0%</span></p></div></div><div id="comments-container-45967" class="comments-container"></div><div id="comment-tools-45967" class="comment-tools"></div><div class="clear"></div><div id="comment-45967-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52590"></span>

<div id="answer-container-52590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52590-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If this one is still interesting... I'm afraid there will be some collateral damages because you cannot augment (or replace) the packet data with forged ones just like that. In another words, the tvb type exists on a purpose, e.g. when you <code>treeitem:add</code> a protocol field as a <code>tvb:range[:typedef]</code>, clicking on that field in the packet dissection pane causes its corresponding bytes to be highlighted in the packet bytes pane, and vice versa. In fact, what you actually do in this case is that you add to the tree a reference to that tvb range and tell Wireshark how to translate its contents into human-readable form.</p><p>So you can extract the part of the message which is identical for both formats from the buffer into a byte array, concatenate it with a byte array representing the forged header, and use <a href="https://wiki.wireshark.org/LuaAPI/ByteArray#ByteArray.tvb.28bytearray.2C_name.29">bytearray:tvb</a> function to create a new tvb from it and call the existing dissector, giving it your new tvb as a target. While I'm sure the packet bytes pane highlight functionality will not work in this case (because no mapping between the position of a given byte in the "real" and "forged" tvb will survive such double-conversion), I have no idea what else may go wrong.</p><p>Another chance could be to do that operation offline, outside Wireshark, by using other software to patch the capture file that way.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '16, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52590" class="comments-container"></div><div id="comment-tools-52590" class="comment-tools"></div><div class="clear"></div><div id="comment-52590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

