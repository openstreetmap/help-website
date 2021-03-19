+++
type = "question"
title = "Data dissection of 802.15.4 frames (lua-based)"
description = '''I am using a sniffer (Uracoli) for wireless frames IEEE 802.15.4. When I see them in Wireshark, the packet details show the following tree (example): + Frame 1550: 28 bytes on wire... + IEEE 802.15.4 Data, Dst: 0x0000, Src: 0x0002 + Data (17 Bytes)  Then, I have developed a custom protocol inside th...'''
date = "2015-03-09T06:06:00Z"
lastmod = "2015-03-09T14:04:00Z"
weight = 40381
keywords = [ "802.15.4", "lua", "dissector", "payload", "customprotocols" ]
aliases = [ "/questions/40381" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Data dissection of 802.15.4 frames (lua-based)](/questions/40381/data-dissection-of-802154-frames-lua-based)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40381-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using a sniffer (Uracoli) for wireless frames IEEE 802.15.4. When I see them in Wireshark, the packet details show the following tree (example):</p><pre><code>+ Frame 1550: 28 bytes on wire...
+ IEEE 802.15.4 Data, Dst: 0x0000, Src: 0x0002
+ Data (17 Bytes)</code></pre><p>Then, I have developed a custom protocol <strong>inside</strong> the "data" (=payload) field. I want to write a lua-based dissector to manage the new protocol. I.e. it should be like this (another example)</p><pre><code>+ Frame 1550: 28 bytes on wire...
+ IEEE 802.15.4 Data, Dst: 0x0000, Src: 0x0002
- My Custom Message type 0x0A
    + Custom field 1
    + Another field 2</code></pre><p>I have seen other posts, and I have the following in my .lua file:</p><pre><code> my_prot = Proto(&quot;my_prot&quot;,&quot;My Protocol&quot;)
 local IEEE802154_table = DissectorTable.get(&quot;wtap_encap&quot;)
 local IEEE802154_dissector = IEEE802154_table:get_dissector(104) -- 104 = &quot;IEEE802_15_4&quot; frames

 function my_prot.dissector(buffer, pinfo, tree)
      IEEE802154_dissector:call(buffer, pinfo, tree)

      -- How can I dissect ONLY the payload (data) of the 802.15.4 frame?

 end

 IEEE802154_table:add (104, my_prot);</code></pre><p>Some options I have tried:</p><ul><li><p>Using "buffer(offset,len)" to select the data I don't like because the data content may have different offsets from the start of frame.</p></li><li><p>Using "Field.new("data.data")" generates trouble like "A Field extractor must be defined before Taps of Dissectors get called".</p></li></ul><hr /><p><em>Thank you so much!<br />
Jose Antonio</em></p></div><div id="question-tags" class="tags-container tags">802.15.4 lua dissector payload customprotocols</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '15, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/85f73d6a38b53a7fba893c7e90d508ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JoseATG&#39;s gravatar image" /><p>JoseATG<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JoseATG has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-40381" class="comments-container"></div><div id="comment-tools-40381" class="comment-tools"></div><div class="clear"></div><div id="comment-40381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40404"></span>

<div id="answer-container-40404" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40404-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you (probably) need is a postdissector in Lua.</p><blockquote><p><a href="http://wiki.wireshark.org/Lua/Examples/PostDissector">http://wiki.wireshark.org/Lua/Examples/PostDissector</a></p></blockquote><p>You can also have a look at questions tagged with postdissector.</p><blockquote><p><a href="https://ask.wireshark.org/tags/postdissector/">https://ask.wireshark.org/tags/postdissector/</a></p></blockquote><p>You'll aslo find sample code in some of these questions.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '15, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '15, 14:07</p></div></div><div id="comments-container-40404" class="comments-container"></div><div id="comment-tools-40404" class="comment-tools"></div><div class="clear"></div><div id="comment-40404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

