+++
type = "question"
title = "Display Filter: Data[X] and Data.Len"
description = '''I&#x27;d like to use filters to verify data in payload packets. The API in question uses the 5th byte as the length of the overall payload. I would like to create a filter so show me packets where this payload is malformed. Something like (Data[4] != Data.Len) appears like it would do the job, but I can&#x27;...'''
date = "2017-06-22T12:53:00Z"
lastmod = "2017-06-24T12:32:00Z"
weight = 62249
keywords = [ "filter" ]
aliases = [ "/questions/62249" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display Filter: Data\[X\] and Data.Len](/questions/62249/display-filter-datax-and-datalen)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62249-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to use filters to verify data in payload packets. The API in question uses the 5th byte as the length of the overall payload. I would like to create a filter so show me packets where this payload is malformed.</p><p>Something like (Data[4] != Data.Len) appears like it would do the job, but I can't get it to work due to type mismatching, etc. I can get (Data[4] == 0x12) &amp;&amp; (Data.Len != 0x12) to work, but that only helps me for that specific payload length and I would have to do search for every unique value.</p><p>It seems like this should be something easy enough to make work, but I think I'm just missing one little piece.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '17, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/8b1e5c476ea736f8ec6749237752bf98?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brimmstone&#39;s gravatar image" /><p>Brimmstone<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brimmstone has no accepted answers">0%</span></p></div></div><div id="comments-container-62249" class="comments-container"></div><div id="comment-tools-62249" class="comment-tools"></div><div class="clear"></div><div id="comment-62249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62283"></span>

<div id="answer-container-62283" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62283-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>While you could probably achieve this via <code>tshark</code> and some scripting, why not create a dissector for your <em>foo</em> protocol? That way, you could simply add an <em>"Expert Info"</em> warning for when <code>foo.len</code> is not equal to the actual payload length. You can write your dissector in C and compile it into Wireshark (Refer to the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developer's Guide</a> for how to do this), or you could more quickly just write a Lua dissector instead, which doesn't require that you recompile Wireshark. There are many resources available for helping to write a Lua dissector, among them:</p><ul><li><a href="https://wiki.wireshark.org/Lua">Wireshark Lua (wiki page)</a></li><li><a href="https://wiki.wireshark.org/Lua/Examples">Wireshark Lua Examples (wiki page)</a></li><li><a href="https://wiki.wireshark.org/Lua/Dissectors">Wireshark Lua Dissectors (wiki page)</a></li><li><a href="https://wiki.wireshark.org/Lua/Taps">Wireshark Lua Taps (wiki page)</a></li><li><a href="https://wiki.wireshark.org/Contrib">Wireshark Contributed scripts, macros, colouring rules and plugins (wiki page)</a></li><li><a href="https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm.html">Chapter 10. Lua Support in Wireshark (Wireshark Developer's Guide)</a></li><li><a href="https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm_modules.html">Chapter 11. Wireshark's Lua API Reference Manual (Wireshark Developer's Guide)</a></li><li><a href="https://wiki.wireshark.org/LuaAPI">Wireshark Lua API Reference Manual Addendum (wiki page)</a></li><li><a href="http://lua-users.org/wiki/LuaDirectory">Lua Directory</a></li></ul><p>In the event you just want to start with Lua, then to help get you started you can have a look at this simple example:</p><pre><code>-- Protocol
local p_foo = Proto(&quot;foo&quot;, &quot;FOO Protocol&quot;)
local FOO_PORT = 1234

-- Fields
local f_foo_field1 = ProtoField.uint32(&quot;foo.field1&quot;, &quot;Some Field&quot;, base.HEX)
local f_foo_field2 = ProtoField.uint8(&quot;foo.field2&quot;, &quot;Some Other Field&quot;, base.HEX)
local f_foo_len = ProtoField.uint8(&quot;foo.len&quot;, &quot;Length&quot;, base.DEC)
local f_foo_len_bad = ProtoField.bool(&quot;foo.len_bad&quot;, &quot;Length bad&quot;, base.NONE, {&quot;True&quot;, &quot;False&quot;}, 0x00)

p_foo.fields = { f_foo_field1, f_foo_field2, f_foo_len, f_foo_len_bad }

-- Initialize expert fields (See: https://wiki.wireshark.org/LuaAPI/TreeItem)
local ef_len_bad = ProtoExpert.new(&quot;foo.expert.length_bad&quot;, &quot;Bad length&quot;,
    expert.group.PROTOCOL, expert.severity.WARN)

-- Register expert fields
p_foo.experts = { ef_len_bad }

-- Dissection
function p_foo.dissector(tvbuf, pinfo, tree)
    local foo_tree = tree:add(p_foo, tvbuf(0,-1))
    local len_item

    pinfo.cols.protocol:set(&quot;FOO&quot;)
    foo_tree:add(f_foo_field1, tvbuf(0, 4))
    foo_tree:add(f_foo_field2, tvbuf(4, 1))
    len_item = foo_tree:add(f_foo_len, tvbuf(5, 1))

    local foolen = tvbuf(5, 1):uint()
    if foolen == tvbuf:len() then
        len_bad = foo_tree:add(f_foo_len_bad, tvbuf(5, 1), false)
        len_item:append_text(&quot; [correct]&quot;)
    else
        len_bad = foo_tree:add(f_foo_len_bad, tvbuf(5, 1), true)
        len_item:append_text(&quot; [invalid]&quot;)
        len_item:add_tvb_expert_info(ef_len_bad, tvbuf(5, 1))
    end
    len_bad:set_generated()
    -- len_bad:set_hidden()
end

-- Registration
local udp_table = DissectorTable.get(&quot;udp.port&quot;)
udp_table:add(FOO_PORT, p_foo)</code></pre><p>To see if any packets have a bad length field, you can just apply a display filter of <code>foo.len_bad</code> or choose *Analyze -&gt; Expert Information" to see if there are any.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '17, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-62283" class="comments-container"></div><div id="comment-tools-62283" class="comment-tools"></div><div class="clear"></div><div id="comment-62283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

