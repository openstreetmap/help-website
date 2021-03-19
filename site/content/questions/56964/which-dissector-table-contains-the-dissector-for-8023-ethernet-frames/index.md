+++
type = "question"
title = "Which dissector table contains the dissector for 802.3 Ethernet frames?"
description = '''I need to replace the dissector for IEEE 802.3 Ethernet frames with a custom one that I write in Lua, because I need to explicitly call a custom dissector for the payload. The payload is proprietary data that Wireshark can not recognize. Currently, my data is wrongly interpreted as LLC.  So I basica...'''
date = "2016-11-04T01:54:00Z"
lastmod = "2016-11-05T09:06:00Z"
weight = 56964
keywords = [ "lua", "dissector", "proprietary", "ethernet" ]
aliases = [ "/questions/56964" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Which dissector table contains the dissector for 802.3 Ethernet frames?](/questions/56964/which-dissector-table-contains-the-dissector-for-8023-ethernet-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56964-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to replace the dissector for IEEE 802.3 Ethernet frames with a custom one that I write in Lua, because I need to explicitly call a custom dissector for the payload. The payload is proprietary data that Wireshark can not recognize. Currently, my data is wrongly interpreted as LLC.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ethernet_payload.PNG" alt="alt text" /></p><p>So I basically want to do the same as described in my earlier question: <a href="https://ask.wireshark.org/questions/54870/how-to-register-a-lua-dissector-for-8021q-ethernet-payload">How to register a Lua dissector for 802.1Q Ethernet payload</a>. I just need to know how to replace the ethernet dissector for 802.3 frames with no VLAN tag. I guess (correct me if I'm wrong) this would be the dissectors <em>eth</em>, <em>eth_withfcs</em> and <em>eth_withoutfcs</em>.</p><pre><code>original_802_3_dissector = DissectorTable.get( ??? ):get_dissector( ??? )
[...]
function my_protocol.dissector(buffer, packet_info, tree)
    original_802_3_dissector:call(buffer, packet_info, tree)
    [...]
end
local eth_table = DissectorTable.get( ??? )
eth_table:add( ??? , my_protocol)</code></pre><p>As always, any help is appreciated. Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">lua dissector proprietary ethernet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '16, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/00a96bd28fd02417186122229a517000?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_oppermann&#39;s gravatar image" /><p>patrick_oppe...<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_oppermann has no accepted answers">0%</span></p></img></div></div><div id="comments-container-56964" class="comments-container"></div><div id="comment-tools-56964" class="comment-tools"></div><div class="clear"></div><div id="comment-56964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57015"></span>

<div id="answer-container-57015" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57015-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The dissector table you are looking for is <code>wtap_encap</code>, and the (integer) index value for Ethernet in that table is 1.</p><p>The standard Ethernet dissector assumes that your payload is LLC-encapsulated because the value of the two octets following the MAC addresses is lower than 1501, so it is interpreted as frame length, implying that the contents is LLC-encapsulated (unless the two octets following the length are 0xffff). Only values above 1535 (0x5ff) are interpreted as Ethertype.</p><p>So your Lua script can save the pointer to the default dissector for encapsulation type 1 and register your dissector instead of it. Your dissector can then call the default one whenever it finds out that the frame contents cannot be dissected as your proprietary protocol. Please note that if it would call the default dissector as the first thing to do, as the code snippet in your Question suggests, you'd step into the same rabbit hole like you do now as in that case, the default dissector would do its complete job, including creation of the LLC subtree.</p><p>Just bear in mind that Wireshark is not the only recipient to be confused by an Ethernet frame of such contents.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '16, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Nov '16, 11:03</p></div></div><div id="comments-container-57015" class="comments-container"></div><div id="comment-tools-57015" class="comment-tools"></div><div class="clear"></div><div id="comment-57015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

