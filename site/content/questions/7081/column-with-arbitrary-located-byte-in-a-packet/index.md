+++
type = "question"
title = "Column with arbitrary located byte in a packet"
description = '''How it is possible to create a &quot;Custom&quot; column which refers to an arbitrary offset in UDP payload. For example, in &quot;Filter definition&quot; it is possible to reffer to the 1st byte in UDP payload as udp[8]. Such simple approach seems to be blocked in Packet Display Plain. What am I missing?'''
date = "2011-10-26T07:18:00Z"
lastmod = "2011-11-09T18:06:00Z"
weight = 7081
keywords = [ "column", "offset" ]
aliases = [ "/questions/7081" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Column with arbitrary located byte in a packet](/questions/7081/column-with-arbitrary-located-byte-in-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7081-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>How it is possible to create a "Custom" column which refers to an arbitrary offset in UDP payload. For example, in "Filter definition" it is possible to reffer to the 1st byte in UDP payload as udp[8]. Such simple approach seems to be blocked in Packet Display Plain. What am I missing?</p></div><div id="question-tags" class="tags-container tags">column offset</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '11, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/b5a1393e4a31be8ec0a7e6d94d12282b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exbungee&#39;s gravatar image" /><p>exbungee<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exbungee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '11, 07:37</p></div></div><div id="comments-container-7081" class="comments-container"></div><div id="comment-tools-7081" class="comment-tools"></div><div class="clear"></div><div id="comment-7081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7273"></span>

<div id="answer-container-7273" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7273-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is (currently) not possible with Wireshark, although you might be able to do this with the <a href="http://wiki.wireshark.org/Lua">Lua</a> scripting engine that is part of Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 03:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Nov '11, 06:00</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-7273" class="comments-container"><span id="7333"></span><div id="comment-7333" class="comment"><div id="post-7333-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Is it possible to add an example. Please assume that the documented method to add LUA file is known.</p></div><div id="comment-7333-info" class="comment-info"><span class="comment-age">(09 Nov '11, 12:04)</span> exbungee</div></div><span id="29267"></span><div id="comment-29267" class="comment"><div id="post-29267-score" class="comment-score">1</div><div class="comment-text"><p>is it still not possible?</p></div><div id="comment-29267-info" class="comment-info"><span class="comment-age">(29 Jan '14, 03:35)</span> Daniil Kharkov</div></div></div><div id="comment-tools-7273" class="comment-tools"></div><div class="clear"></div><div id="comment-7273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7351"></span>

<div id="answer-container-7351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7351-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"use the Code, Luk"<br />
add the Custom "udp_dump.data" column in Preferences/Columns and tweak protocol port and byte offset in Preferences/Protocol/UDP_DUMP. Upvote! =)</p><pre><code>do
        local udp_dumper_proto = Proto(&quot;udp_dump&quot;, &quot;UDP dumper&quot;);

        udp_dumper_proto.prefs.ofs = Pref.uint( &quot;udp_dump_ofs&quot;, 1, &quot;UDP data byte offset&quot; )
        udp_dumper_proto.prefs.port   = Pref.uint( &quot;udp_dump_port&quot;, 53, &quot;UDP port&quot; )

        udp_dumper_proto.fields.dump   = ProtoField.uint8(&quot;udp_dump.data&quot;, &quot;a dump of byte&quot;, base.HEX)

        local prev_proto
        local f_udp    = Field.new(&quot;udp&quot;)

        function udp_dumper_proto.dissector(tvb, pinfo, tree)
            pcall(function()prev_proto:call(tvb, pinfo, tree)end)

            if not f_udp() then return end

            local ofs = udp_dumper_proto.prefs.ofs -- udp_dumper_proto.prefs.filter
            if (tvb:len() &lt; ofs) then return end

            -- this is just to add text to &quot;udp_dump.data&quot; field, 
            -- which you should display as column.
            -- as an alternate, you may remove set_hidden() and view selected data in the treeview
            tree:add(udp_dumper_proto.fields.dump, tvb(ofs,1)):set_hidden();
        end

        -- if we hook upon UDP port, then offset will mean the beginning of the UDP data
        udp_table = DissectorTable.get(&quot;udp.port&quot;)
        prev_proto = udp_table:get_dissector(udp_dumper_proto.prefs.port)
        udp_table:add(udp_dumper_proto.prefs.port, udp_dumper_proto)

        -- if we hook as post dissector, the offset will be from start of the frame. 
        -- don&#39;t forget to remove the prev_proto call if you&#39;ll use that kind of hook
--        register_postdissector(udp_dumper_proto)
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '11, 18:06</strong></p><img src="https://secure.gravatar.com/avatar/35d96b8e73e6deb4e332d076fd3269b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShomeaX&#39;s gravatar image" /><p>ShomeaX<br />
<span class="score" title="73 reputation points">73</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShomeaX has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Nov '11, 18:08</p></div></div><div id="comments-container-7351" class="comments-container"><span id="7362"></span><div id="comment-7362" class="comment"><div id="post-7362-score" class="comment-score"></div><div class="comment-text"><p>Short and cool! Really thanks! Just for clarity: on my WS (Rel 1.7.xx) it creates the following stack Protocols in frame: eth:vlan:ip:udp:udp_dump:dns I expected "udp_dump" to be the last item on the stack. Any way to get rid of "dns"?</p></div><div id="comment-7362-info" class="comment-info"><span class="comment-age">(10 Nov '11, 02:16)</span> exbungee</div></div></div><div id="comment-tools-7351" class="comment-tools"></div><div class="clear"></div><div id="comment-7351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

