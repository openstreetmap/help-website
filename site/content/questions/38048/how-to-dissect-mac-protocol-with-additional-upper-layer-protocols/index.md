+++
type = "question"
title = "How to dissect MAC protocol with additional upper layer protocols"
description = '''I have a simple MAC layer protocol that wraps IPv6. I have captured some frames (text) and converted them using text2pcap.exe and the user defined link layer option DLT_USER0.  Next, I followed directions here and added my &#x27;SimpleMAC&#x27; protocol as follows:      Opening the pcap file in Wireshark, I c...'''
date = "2014-11-21T10:42:00Z"
lastmod = "2014-12-23T23:32:00Z"
weight = 38048
keywords = [ "lua", "mac", "dissector", "wireshark", "encapsulation" ]
aliases = [ "/questions/38048" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to dissect MAC protocol with additional upper layer protocols](/questions/38048/how-to-dissect-mac-protocol-with-additional-upper-layer-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38048-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a simple MAC layer protocol that wraps IPv6. I have captured some frames (text) and converted them using text2pcap.exe and the user defined link layer option DLT_USER0.<br />
</p><p>Next, I followed directions <a href="http://wiki.wireshark.org/HowToDissectAnything">here</a> and added my 'SimpleMAC' protocol as follows: <img src="https://osqa-ask.wireshark.org/upfiles/WireshakSimpleMAC.PNG" alt="edit_preferences" /><br />
<br />
Opening the pcap file in Wireshark, I can see that it recognizes my MAC protocol and successfully dissects the IPv6 packet: <img src="https://osqa-ask.wireshark.org/upfiles/WireshakSimpleMAC2.PNG" alt="ipv6_dissected" /></p><p>However, I want to add a Lua dissector to view the MAC details. Setting my Lua dissector to the correct wtap_encap dissector table entry, I can now see my 'SimpleMAC' protocol dissected, but I can no longer see the details for the IPv6 packet:<br />
<img src="https://osqa-ask.wireshark.org/upfiles/WireshakSimpleMAC3.PNG" alt="simplemac_dissected" /></p><p>How can I do this so I can see both?</p><p>Here is the code for my Lua dissector:</p><pre><code>oProtoSimpleMac = Proto(&quot;simplemac&quot;, &quot;Simple MAC&quot;)
function oProtoSimpleMac.dissector(oTvbData, oPinfo, oTreeItemRoot)
    if oTvbData:len() &lt; 33 then
        return
    end

    --Get SimpleMAC details
    local dStartByte  = oTvbData(0, 1)
    local uiVersion    = oTvbData(1, 1):uint()
    local uiLnkQuality = oTvbData(2, 1):uint()
    local uiSeqNum     = oTvbData(3, 2):uint()
    local dFlags       = oTvbData(5, 4)
    local uiTimeSecs   = oTvbData(9, 4):uint()
    local uiTimeMSecs  = oTvbData(13,4):uint()
    local dSrcMacAddr  = oTvbData(17,8)
    local dDestMacAddr = oTvbData(25,8)

    --Update Protocol and Info columns
    oPinfo.cols.protocol = &#39;SimpleMAC&#39;
    oPinfo.cols.info = &#39;Simple MAC&#39;

    --Add tree and sub-tree data for expanding the packet info
    local oSubtree = oTreeItemRoot:add(oProtoSimpleMac, oTvbData(), &#39;Simple MAC Protocol Data&#39;)
    oSubtree:add(oTvbData(0,1), &#39;StartByte : 0x&#39; .. dStartByte)
    oSubtree:add(oTvbData(1,1), string.format(&#39;Version   : %d&#39;, uiVersion))
    oSubtree:add(oTvbData(2,1), string.format(&#39;Link Quality: %d&#39;, uiLnkQuality))
    oSubtree:add(oTvbData(3,2), string.format(&#39;Sequence Number: %d&#39;, uiSeqNum))
    oSubtree:add(oTvbData(5,4), &#39;Flags: 0x&#39; .. dFlags)
    oSubtree:add(oTvbData(9,8), &#39;Time:&#39;)
    oSubtree:add(oTvbData(25,8), &#39;Source MAC Addr      : &#39; .. dSrcMacAddr)
    oSubtree:add(oTvbData(17,8), &#39;Destination MAC Addr : &#39; .. dDestMacAddr)
end

local wtap_encap_table = DissectorTable.get(&quot;wtap_encap&quot;)
wtap_encap_table:add(45, oProtoSimpleMac)</code></pre></div><div id="question-tags" class="tags-container tags">lua mac dissector wireshark encapsulation</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '14, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/1def9e13e259013e40816a43899308fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="littleman&#39;s gravatar image" /><p>littleman<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="littleman has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 21 Nov '14, 10:43</p></div></div><div id="comments-container-38048" class="comments-container"><span id="38110"></span><div id="comment-38110" class="comment"><div id="post-38110-score" class="comment-score"></div><div class="comment-text"><p>Interestingly, I've found that when I modify the Lua dissector to add the Simple MAC protocol back to the wrong value ( <strong>wtap_encap_table:add(46,oProtoSimpleMac)</strong> ), Wireshark dissects both the Simple MAC and the IPv6 packet.</p><p>The problem now is, if the frame contains only MAC information (no, payload with IPv6), I get a Malformed packet error and 'IPv6' appears in the Protocol Column: <img src="https://osqa-ask.wireshark.org/upfiles/WireshakSimpleMAC4.PNG" alt="malformed_pkt" /></p><p>How do I make it stop at the Simple MAC layer if there is no additional data?</p></div><div id="comment-38110-info" class="comment-info"><span class="comment-age">(24 Nov '14, 10:09)</span> littleman</div></div></div><div id="comment-tools-38048" class="comment-tools"></div><div class="clear"></div><div id="comment-38048-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38692"></span>

<div id="answer-container-38692" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38692-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>When you use a Lua script to create a new protocol and dissect a packet as it, Wireshark has no idea what other protocol(s) might be after your new protocol in the packet. So when you did this:</p><pre><code>wtap_encap_table:add(45, oProtoSimpleMac)</code></pre><p>You told Wireshark to use your Lua-based <code>oProtoSimpleMac</code> dissector for any packets of link-layer encapsulation number 45 (i.e., <code>USER0</code>). So wireshark calls your <code>oProtoSimpleMac.dissector()</code> function when it sees a packet of encapsulation 45.</p><p>When you <em>instead</em> add a user DLT entry to the DLT table in the preferences, as you did at the beginning, you told wireshark not only what your encapsulation info is for USER0, but also that the payload's protocol after it is IPv6. So when wireshark does it that way, it worked.</p><p>So to do the same thing in Lua, at the end of your <code>oProtoSimpleMac.dissector()</code> function you need to call the appropriate dissector, namely the IPv6 one - or not call it if there is no IPv6 payload.</p><p>To call a built-in dissector, first you need to get it using <code>Dissector.get("ipv6")</code>, and then you need to <code>call()</code> the retrieved dissector.</p><p>So like this:</p><hr /><pre><code>local oProtoSimpleMac = Proto(&quot;simplemac&quot;, &quot;Simple MAC&quot;)
local oIPv6Dissector = Dissector.get(&quot;ipv6&quot;)

function oProtoSimpleMac.dissector(oTvbData, oPinfo, oTreeItemRoot)
    -- do stuff here

    if my_packet_has_ipv6 then
        -- invoke the ipv6 dissector, giving it a Tvb starting at offset 33 to the end
        oIPv6Dissector:call(oTvbData(33):tvb(), oPinfo, oTreeItemRoot)
    end
end

local wtap_encap_table = DissectorTable.get(&quot;wtap_encap&quot;)
wtap_encap_table:add(45, oProtoSimpleMac)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '14, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span> </br></br></p></img></div></div><div id="comments-container-38692" class="comments-container"><span id="38769"></span><div id="comment-38769" class="comment"><div id="post-38769-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that worked like a charm!</p></div><div id="comment-38769-info" class="comment-info"><span class="comment-age">(29 Dec '14, 08:33)</span> littleman</div></div></div><div id="comment-tools-38692" class="comment-tools"></div><div class="clear"></div><div id="comment-38692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

