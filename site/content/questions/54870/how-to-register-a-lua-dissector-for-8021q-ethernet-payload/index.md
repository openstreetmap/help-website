+++
type = "question"
title = "How to register a Lua dissector for 802.1Q Ethernet payload"
description = '''I am developing a custom dissector in Lua that decodes a proprietary protocol developed by my company. The dissector should process the payload of Ethernet II frames that have a VLAN tag (as defined by IEEE 802.1Q). How can I tell Wireshark that? I tried the following: original_vlan_dissector = Diss...'''
date = "2016-08-16T07:19:00Z"
lastmod = "2016-08-16T07:42:00Z"
weight = 54870
keywords = [ "lua", "dissector", "ethernet" ]
aliases = [ "/questions/54870" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to register a Lua dissector for 802.1Q Ethernet payload](/questions/54870/how-to-register-a-lua-dissector-for-8021q-ethernet-payload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54870-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am developing a custom dissector in Lua that decodes a proprietary protocol developed by my company. The dissector should process the payload of Ethernet II frames that have a VLAN tag (as defined by IEEE 802.1Q). How can I tell Wireshark that?</p><p>I tried the following:</p><pre><code>original_vlan_dissector = DissectorTable.get(&quot;ethertype&quot;):get_dissector(0x8100)
[...]
function my_protocol.dissector(buffer, packet_info, tree)
    original_vlan_dissector:call(buffer, packet_info, tree)
    [...]
end

local eth_table = DissectorTable.get(&quot;ethertype&quot;)
eth_table:add(0x8100, my_protocol)</code></pre><p>Is there a better place to register my dissector? There is no TCP or UDP involved here, so I have no idea which DissectorTable and port are suitable.</p></div><div id="question-tags" class="tags-container tags">lua dissector ethernet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '16, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/00a96bd28fd02417186122229a517000?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_oppermann&#39;s gravatar image" /><p>patrick_oppe...<br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_oppermann has no accepted answers">0%</span></p></div></div><div id="comments-container-54870" class="comments-container"></div><div id="comment-tools-54870" class="comment-tools"></div><div class="clear"></div><div id="comment-54870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54873"></span>

<div id="answer-container-54873" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54873-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is the right way to do it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Aug '16, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54873" class="comments-container"></div><div id="comment-tools-54873" class="comment-tools"></div><div class="clear"></div><div id="comment-54873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

