+++
type = "question"
title = "writing dissector using lua scripts"
description = '''Hello, I&#x27;m trying to write wireshark dissector using lua script. I look at the web pages for examples and explanations : https://wiki.wireshark.org/Lua https://wiki.wireshark.org/Lua/Examples However, i still have something that i do not understand. I receive data in EtherNet/IP (Industrial Protocol...'''
date = "2017-10-24T08:47:00Z"
lastmod = "2017-10-27T09:39:00Z"
weight = 64158
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/64158" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [writing dissector using lua scripts](/questions/64158/writing-dissector-using-lua-scripts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64158-score" class="post-score" title="current number of votes">0</div><span id="post-64158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm trying to write wireshark dissector using lua script. I look at the web pages for examples and explanations : <a href="https://wiki.wireshark.org/Lua">https://wiki.wireshark.org/Lua</a> <a href="https://wiki.wireshark.org/Lua/Examples">https://wiki.wireshark.org/Lua/Examples</a> However, i still have something that i do not understand. I receive data in EtherNet/IP (Industrial Protocol) using UDP. So i have something like that IP-&gt;UDP-&gt;EtherNet/IP --&gt; My dissector Until now, i can use my dissector but it always start at the UDP data level. I want it to start and EtherNet/IP data level. Where should i do that ? And How can I do that ?</p><p>I have a doubt about three lines that should contains the modification : Maybe i should set root with something but i cannot find which one ? Where can i find information about that ?</p><pre><code>local tree = root:add(cip, tvbuf:range(0,pktlen))
cip.dissector(tvbuf,pktinfo,root)</code></pre><p>Maybe i need to set something different from "udp" here, but where can i find the string for EtherNet/IP protocol ?</p><pre><code>cip:register_heuristic(&quot;udp&quot;,heur_dissect_dns)</code></pre><p>Can anyone help me with that ? Thank you very much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '17, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/4d7366f0ba4d9f9e9c6a11f40ae1ab66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicolas2333&#39;s gravatar image" /><p><span>Nicolas2333</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicolas2333 has no accepted answers">0%</span></p></div></div><div id="comments-container-64158" class="comments-container"><span id="64196"></span><div id="comment-64196" class="comment"><div id="post-64196-score" class="comment-score"></div><div class="comment-text"><p>Can you provide a sample capture file (a single packet should be enough)? As I don't know CIP, I cannot be more specific than below without seeing the packet.</p><p>CIP dissector is embedded to Wireshark so the first question is whether either the UDP dissector finds out using heuristic that the UDP payload is a CIP one or whether there is an IANA registered UDP port for CIP, which means that the dissector table <code>udp.port</code> would contain a line saying that for this port numberm CIP dissector should be invoked on the payload. If neither is true, you have to add such line to <code>udp.port</code> dissector table for the port number your equipment is using.</p><p>The second point is that you have to tell the CIP dissector itself that it should use your Lua dissector for particular types of its payload. The embedded CIP dissector uses two dissector tables: <code>cip.class.iface</code> and <code>cip.data_segment.iface</code>, and if your private payload can be identified using one of the fields used as indice to these tables, you have to register your dissector to one of these tables.</p></div><div id="comment-64196-info" class="comment-info"><span class="comment-age">(25 Oct '17, 11:03)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="64249"></span><div id="comment-64249" class="comment"><div id="post-64249-score" class="comment-score"></div><div class="comment-text"><p>I know you probably wrote this as an answer because of the size.</p><p>Can you convert it to a comment, I've tried (after fixing the images for display in a comment) but some OSQA brokeness won't let me?</p></div><div id="comment-64249-info" class="comment-info"><span class="comment-age">(26 Oct '17, 12:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="64250"></span><div id="comment-64250" class="comment"><div id="post-64250-score" class="comment-score"></div><div class="comment-text"><p>If you register your dissector with the UDP port then you will override the CIP dissector, hence the output you see.</p><p>You will need to hook your dissector into the CIP one via a dissector table, but I'm not sure if there is a suitable table to do so for a connected data item.</p></div><div id="comment-64250-info" class="comment-info"><span class="comment-age">(26 Oct '17, 12:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="64254"></span><div id="comment-64254" class="comment"><div id="post-64254-score" class="comment-score"></div><div class="comment-text"><p>Placing my comment here as it would otherwise disappear once you would convert your "Answer" into a comment as <a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> has asked you to.</p><p>I am a bit confused by seeing UDP port 2222 on your pictures and 65533 in your Lua code. As you've guessed yourself and as <a href="https://ask.wireshark.org/users/1225/grahamb"></a><a href="https://ask.wireshark.org/users/1225/grahamb">@grahamb</a> wrote, the Lua line below replaces the original CIP dissector (which handles ENIP as well as the two are close twins) by your <code>cip_ddu</code> one (the <code>add</code> method is actually a <code>replace</code> if there already is a record for that index) in UDP dissector's only dissector table (<code>udp.port</code>) for port 65533, but it should <strong>not</strong> do so for port 2222.</p><p>If you are lucky, replacing the line<br />
<code>DissectorTable.get("udp.port"):add(65533, cip_ddu)</code><br />
by<br />
<code>DissectorTable.get("cip.data_segment.iface"):add(0xb1, cip_ddu)</code><br />
(or, possibly, by <code>DissectorTable.get("cip.data_segment.iface"):add(0x31, cip_ddu)</code>)<br />
could hook your <code>cip_ddu</code> dissector to the right place.</p><p>If you are not lucky, you'll have to extend your Lua dissector with a part duplicating the functionality of the embedded CIP/ENIP dissector as it would mean that none of the existing one's hook points (dissection tables) is the right one you need, and you would hook that extended one to the <code>udp.port</code> table.</p></div><div id="comment-64254-info" class="comment-info"><span class="comment-age">(26 Oct '17, 13:14)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="64296"></span><div id="comment-64296" class="comment"><div id="post-64296-score" class="comment-score"></div><div class="comment-text"><p>Hello, Thank you for your help. I will try that. I will also try to change the answer i made yesterday to comment. It's not working just now. Thank you</p></div><div id="comment-64296-info" class="comment-info"><span class="comment-age">(27 Oct '17, 09:39)</span> <span class="comment-user userinfo">Nicolas2333</span></div></div></div><div id="comment-tools-64158" class="comment-tools"></div><div class="clear"></div><div id="comment-64158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64241"></span>

<div id="answer-container-64241" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-64241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-64241-score" class="post-score" title="current number of votes">0</div><span id="post-64241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, Thank you for your answer. In fact, actually, using wireshark without the dissector I wrote, i get the Capture_CIP.jpg image. The ENIP protocol is used with UDP protocol. I want to add a dissector to parse the data part at the end of the ENIP packet. "Data : 7905010000..."</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_CIP.JPG" width="640" /></p><p>To do that i wrote the following lua script: -- creates a Proto object, but doesn't register it yet local cip_ttt = Proto("myCIP","CIP Sub Protocol")</p><pre><code>-- multiple ways to do the same thing: create a protocol field (but not register it yet)
local pf_header             = ProtoField.new    (&quot;Header&quot;, &quot;myCIP.header&quot;, ftypes.UINT32)
local pf_div1               = ProtoField.new    (&quot;Div1&quot;, &quot;myCIP.Divers_1&quot;, ftypes.UINT32)
local pf_div2               = ProtoField.new    (&quot;Div2&quot;, &quot;myCIP.Divers_2&quot;, ftypes.UINT32)
local pf_div3               = ProtoField.new    (&quot;Div3&quot;, &quot;myCIP.Divers_3&quot;, ftypes.UINT16)
local pf_IO_Byte1           = ProtoField.new    (&quot;IO Table Byte 1&quot;, &quot;myCIP.IOByte1&quot;, ftypes.UINT8, nil, base.HEX)

local pf_IO_24_2                    = ProtoField.new    (&quot;Bit8&quot;, &quot;myCIP.pf_IO_Byte1.bit8&quot;, ftypes.BOOLEAN, nil, 8, 0x80)
local pf_IO_24_1                    = ProtoField.new    (&quot;Bit7&quot;, &quot;myCIP.pf_IO_Byte1.bit7&quot;, ftypes.BOOLEAN, nil, 8, 0x40)
local pf_IO_14_5                    = ProtoField.new    (&quot;Bit6&quot;, &quot;myCIP.pf_IO_Byte1.bit6&quot;, ftypes.BOOLEAN, nil, 8, 0x20)
local pf_IO_14_4                    = ProtoField.new    (&quot;Bit5&quot;, &quot;myCIP.pf_IO_Byte1.bit5&quot;, ftypes.BOOLEAN, nil, 8, 0x10)
local pf_IO_14_3                    = ProtoField.new    (&quot;Bit4&quot;, &quot;myCIP.pf_IO_Byte1.bit4&quot;, ftypes.BOOLEAN, nil, 8, 0x08)
local pf_IO_14_2                    = ProtoField.new    (&quot;Bit3&quot;, &quot;myCIP.pf_IO_Byte1.bit3&quot;, ftypes.BOOLEAN, nil, 8, 0x04)
local pf_IO_14_1                    = ProtoField.new    (&quot;Bit2&quot;, &quot;myCIP.pf_IO_Byte1.bit2&quot;, ftypes.BOOLEAN, nil, 8, 0x02)
local pf_IO_13_1                    = ProtoField.new    (&quot;Bit1&quot;, &quot;myCIP.pf_IO_Byte1.bit1&quot;, ftypes.BOOLEAN, nil, 8, 0x01)

cip_ddu.fields = {pf_header, pf_div1, pf_div2, pf_div3, pf_IO_Byte1, pf_IO_24_2, pf_IO_24_1, pf_IO_14_5, pf_IO_14_4, 
    pf_IO_14_3, pf_IO_14_2, pf_IO_14_1, pf_IO_13_1 }

function cip_ddu.dissector(tvbuf,pktinfo,root)
    -- set the protocol column to show our protocol name
    pktinfo.cols.protocol:set(&quot;CIP_perso&quot;)

    local pktlen = tvbuf:reported_length_remaining()
    local tree = root:add(cip_ddu, tvbuf:range(0,pktlen))

    --tree:add(pf_trasaction_id, tvbuf:range(0,2))
    tree:add(pf_header, tvbuf:range(0,4))

    -- add other fields divx
    tree:add(pf_div1, tvbuf:range(4,4))
    tree:add(pf_div2, tvbuf:range(8,4))
    tree:add(pf_div3, tvbuf:range(12,2))

    -- add subtree for IO
    local IO_byte1 = tvbuf:range(14,1):uint()
    local IO_byte1_tree = tree:add(pf_IO_Byte1, IO_byte1)

    IO_byte1_tree:add(pf_IO_24_2, IO_byte1)
    IO_byte1_tree:add(pf_IO_24_1, IO_byte1)
    IO_byte1_tree:add(pf_IO_14_5, IO_byte1) 
    IO_byte1_tree:add(pf_IO_14_4, IO_byte1)     
    IO_byte1_tree:add(pf_IO_14_3, IO_byte1)     
    IO_byte1_tree:add(pf_IO_14_2, IO_byte1)
    IO_byte1_tree:add(pf_IO_14_1, IO_byte1)
    IO_byte1_tree:add(pf_IO_13_1, IO_byte1)

end

DissectorTable.get(&quot;udp.port&quot;):add(65533, cip_ddu)
--DissectorTable.get(&quot;etherip&quot;):add(65533, cip_ddu)
--local enip_dissector_table = DissectorTable.get(&quot;etherip&quot;)
--enip_dissector_table:add(65533,cip_ddu)</code></pre><p>With this script, i got the Capture_Actual_Dissector.jpg image. <img src="https://osqa-ask.wireshark.org/upfiles/Capture_Actual_Dissector_44dytok.JPG" width="640" /></p><p>The problem i meet, is that my dissector starts from the UDP Data packet, and not the data from the ENIP packet. I think it is due to this line:</p><pre><code>DissectorTable.get(&quot;udp.port&quot;):add(65533, cip_ddu)</code></pre><p>But i do not know how to change it and with which code in order to to what i want. Can you help me understand what's wrong in my script and what's the best solution ? Thank you very much.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '17, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/4d7366f0ba4d9f9e9c6a11f40ae1ab66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nicolas2333&#39;s gravatar image" /><p><span>Nicolas2333</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nicolas2333 has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '17, 12:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></br></p></img></div></div><div id="comments-container-64241" class="comments-container"></div><div id="comment-tools-64241" class="comment-tools"></div><div class="clear"></div><div id="comment-64241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

