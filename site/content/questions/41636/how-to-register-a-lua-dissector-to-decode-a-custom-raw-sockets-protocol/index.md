+++
type = "question"
title = "How to register a Lua dissector to decode a custom raw sockets protocol ?"
description = '''Hi. Since several days, I&#x27;ve tried (unsuccessfully) to create my own dissector written with the Lua langage in order to decode throw Wireshark the frames created with a custom raw sockets protocol. My frames have a classic Ethernet structure:  MAC destination address MAC source address MAC length pa...'''
date = "2015-04-21T07:35:00Z"
lastmod = "2015-04-21T07:35:00Z"
weight = 41636
keywords = [ "lua", "dissector", "proto_register" ]
aliases = [ "/questions/41636" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to register a Lua dissector to decode a custom raw sockets protocol ?](/questions/41636/how-to-register-a-lua-dissector-to-decode-a-custom-raw-sockets-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41636-score" class="post-score" title="current number of votes">0</div><span id="post-41636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>Since several days, I've tried (unsuccessfully) to create my own dissector written with the Lua langage in order to decode throw Wireshark the frames created with a custom raw sockets protocol.</p><p>My frames have a classic Ethernet structure:</p><ul><li>MAC destination address</li><li>MAC source address</li><li>MAC length payload (ethertype)</li><li>Payload</li><li>Eventual padding</li></ul><p>Without custom dissector, Wireshark uses LLC protocol to decode the frames.</p><p>Therefore, to have a specific decoding, I've tried to write a Lua dissector. I precise that I'm beginner with Lua langage working.</p><p>Anyway. After several tests, I can more or less decode my frame by registering my dissector as follows: <strong><em>local wtap_encap_table = DissectorTable.get("wtap_encap") wtap_encap_table:add(1, MyProto)</em></strong></p><p>However, Wireshark use my dissector to decode all the frames which pass over my Ethernet link and leaves Source column and Destination column empty.</p><p>So, I'd like to know how to make Wireshark decode only my frames with my custom dissector.</p><p>To complete my question, follows my Lua script:</p><pre><code>-- MyProto Dissector
local MyProto = Proto(&quot;MyProto&quot;, &quot;MyProto&quot;)

-- MyProto Dissector fields
--local f = MyProto.fields

--f.MAC_addr_dest = ProtoField.STRING(&quot;MyProto.MAC_addr_dest&quot;, &quot;MAC_addr_dest&quot;, base.NONE, MAC_addr_dest)
--f.MAC_addr_src = ProtoField.STRING(&quot;MyProto.MAC_addr_src&quot;, &quot;MAC_addr_src&quot;, base.NONE, MAC_addr_src)

function MyProto.dissector(buffer, pinfo, tree)
    if buffer:len() &lt; 18 then
        return
    end

    -- Parameters function
    local MAC_addr_dst0 = buffer(0, 1):uint()
    local MAC_addr_dst1 = buffer(1, 1):uint()
    local MAC_addr_dst2 = buffer(2, 1):uint()
    local MAC_addr_dst3 = buffer(3, 1):uint()
    local MAC_addr_dst4 = buffer(4, 1):uint()
    local MAC_addr_dst5 = buffer(5, 1):uint()
    local MAC_addr_src0 = buffer(6, 1):uint()
    local MAC_addr_src1 = buffer(7, 1):uint()
    local MAC_addr_src2 = buffer(8, 1):uint()
    local MAC_addr_src3 = buffer(9, 1):uint()
    local MAC_addr_src4 = buffer(10, 1):uint()
    local MAC_addr_src5 = buffer(11, 1):uint()
    local MAC_length = buffer(12, 2):uint()
    local Msg_LA = buffer(14, 2):uint()
    local Msg_length = buffer(16, 2):uint()

    -- Test for a specific message to see how it works !! 
    if (Msg_LA == 0x0000 and  Msg_length == 0x08) then
        -- Update &quot;Protocol&quot; and &quot;Info&quot; columns
        pinfo.cols.protocol = &#39;MyProto&#39;
        pinfo.cols.info = &quot;MSG : MON_HELLO_CNN&quot; .. &quot;, &quot; .. string.format(&#39;LA: %0.4x&#39;, Msg_LA) .. &quot;, &quot; .. string.format(&#39;Length: %0.2x&#39;, Msg_length)

        -- Add tree and sub-tree data for expanding the packet info
        local tree1 = tree:add(MyProto, buffer(), &#39;MyProto Protocol Data&#39;)
        tree1:add(buffer(0, 6), string.format(&#39;Destination MAC Addr: %0.2x:%0.2x:%0.2x:%0.2x:%0.2x:%0.2x&#39;, MAC_addr_dst0, MAC_addr_dst1, MAC_addr_dst2, MAC_addr_dst3, MAC_addr_dst4, MAC_addr_dst5))
        tree1:add(buffer(6, 6), string.format(&#39;Source MAC Addr: %0.2x:%0.2x:%0.2x:%0.2x:%0.2x:%0.2x&#39;, MAC_addr_src0, MAC_addr_src1, MAC_addr_src2, MAC_addr_src3, MAC_addr_src4, MAC_addr_src5))
        tree1:add(buffer(12, 2), string.format(&#39;MAC Length: 0x%0.4x&#39;, MAC_length))
        tree1:add(buffer(14, 2), string.format(&#39;MSG LA: %0.4x&#39;, Msg_LA))
        tree1:add(buffer(16, 2), string.format(&#39;MSG Length: 0x%0.4x&#39;, Msg_length))
    end
end

local wtap_encap_table = DissectorTable.get(&quot;wtap_encap&quot;)
wtap_encap_table:add(1, MyProto)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-proto_register" rel="tag" title="see questions tagged &#39;proto_register&#39;">proto_register</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/b241d4f9dd8837794694ef84d554e740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saj_B&#39;s gravatar image" /><p><span>Saj_B</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saj_B has no accepted answers">0%</span></p></div></div><div id="comments-container-41636" class="comments-container"></div><div id="comment-tools-41636" class="comment-tools"></div><div class="clear"></div><div id="comment-41636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

