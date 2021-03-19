+++
type = "question"
title = "Does Wireshark ignore metamethod __index of table?"
description = '''I wrote a dissector in Lua as following. local values = {[2] = &quot;Two&quot;} setmetatable(values, {__index = function () return &quot;Not two&quot; end}) local proto = Proto(&quot;myproto&quot;, &quot;My Protocol&quot;) local field1 = ProtoField.uint8(proto.name..&quot;.field1&quot;, &quot;Field1&quot;, base.DEC, values) proto.fields = {field1} function p...'''
date = "2015-03-25T23:10:00Z"
lastmod = "2015-06-27T22:26:00Z"
weight = 40874
keywords = [ "lua", "metamethod", "dissector", "metatable", "index" ]
aliases = [ "/questions/40874" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark ignore metamethod \_\_index of table?](/questions/40874/does-wireshark-ignore-metamethod-__index-of-table)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40874-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a dissector in Lua as following.</p><pre><code>local values = {[2] = &quot;Two&quot;}
setmetatable(values, {__index = function () return &quot;Not two&quot; end})
local proto = Proto(&quot;myproto&quot;, &quot;My Protocol&quot;)
local field1 = ProtoField.uint8(proto.name..&quot;.field1&quot;, &quot;Field1&quot;, base.DEC, values)
proto.fields = {field1}
function proto.dissector (buf, pkt, root)
   local t = root:add(proto, buf())
   local r = buf(1, 1)
   t:add(field1, r)
   local i = r:uint()
   t:add(r, string.format(&quot;Field1: %s (%d)&quot;, values[i], i))
end
DissectorTable.get(&quot;tcp.port&quot;):add(10000, proto)</code></pre><p>When buf(1,1) is two, Wireshark dissected as following.</p><pre><code>My Protocol
  Field1: Two (2)
  Field1: Two (2)</code></pre><p>But, when buf(1,1) is not two, Wireshark dissected as following.</p><pre><code>My Protocol
  Field1: Unknown (130)
  Field1: Not two (130)</code></pre><p>It seems that Wireshark ignores metamethod "__index" of values table. Is this Wireshark behavior a bug or spec?</p><p>(I'm using Wireshark 1.10.2 and liblua 5.1.3)</p></div><div id="question-tags" class="tags-container tags">lua metamethod dissector metatable index</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '15, 23:10</strong></p><img src="https://secure.gravatar.com/avatar/9226a7d863f40da740476e5f59e04853?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cosmos&#39;s gravatar image" /><p>cosmos<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cosmos has no accepted answers">0%</span></p></div></div><div id="comments-container-40874" class="comments-container"></div><div id="comment-tools-40874" class="comment-tools"></div><div class="clear"></div><div id="comment-40874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43623"></span>

<div id="answer-container-43623" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43623-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This question is a bit old, but since no one has answered...</p><blockquote><p>Is this Wireshark behavior a bug or spec?</p></blockquote><p>It's not a bug, but more of a design issue - Wireshark does not use that "<code>values</code>" value-to-string Lua table as an actual Lua table during run-time processing/decoding of packets in its internal C-code field parsers... instead, it reads that Lua table when it processes the <code>ProtoField.uint8()</code> function to create the <code>ProtoField</code>, and converts the Lua table into an internal C-code "<code>value_string</code>" array (or really, an array of <code>value_string</code> C-structs). So that Lua table is only accessed when the Lua plugin script is first loaded, before any packet decoding. The C-code array is then used by the internal code to figure out things when packets are actually decoded.</p><p>In your code above, when you do "<code>t:add(field1, r)</code>", you're invoking the internal C-code to decode/parse the <code>ProtoField</code> from the buffer using the attributes you previously defined in the <code>ProtoField.uint8()</code> call, so no metamethod is invoked because it's not coming back into Lua during that C-code parsing; but when you later do "<code>t:add(r, string.format("Field1: %s (%d)", values[i], i))</code>" then you're doing the "parsing" yourself in Lua and thus the metamethod works for that case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '15, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43623" class="comments-container"></div><div id="comment-tools-43623" class="comment-tools"></div><div class="clear"></div><div id="comment-43623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

