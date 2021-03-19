+++
type = "question"
title = "[Lua] bytes consumed during dissection"
description = '''Hi, I&#x27;m new to Lua dissector and experimenting with Lua. I need some help understand how can a sub-protocol dissector return bytes consumed during its decoding to its caller dissector. Example: MYPROTO = Proto (&quot;myproto&quot;, &quot;My Simple Protocol&quot;) local myproto_dt = DissectorTable.new (&quot;myproto.msgid&quot;, ...'''
date = "2012-07-01T12:22:00Z"
lastmod = "2012-07-01T13:55:00Z"
weight = 12358
keywords = [ "lua", "dissector", "offset" ]
aliases = [ "/questions/12358" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[Lua\] bytes consumed during dissection](/questions/12358/lua-bytes-consumed-during-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12358-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm new to Lua dissector and experimenting with Lua. I need some help understand how can a sub-protocol dissector return bytes consumed during its decoding to its caller dissector.</p><p>Example:</p><pre><code>MYPROTO = Proto (&quot;myproto&quot;, &quot;My Simple Protocol&quot;)
local myproto_dt = DissectorTable.new (&quot;myproto.msgid&quot;, &quot;MYPROTO&quot;)

local f = MYPROTO.fields
f.var1 = ProtoField.uint16 (&quot;myproto.var1&quot;, &quot;var1&quot;)  
f.msgid = ProtoField.uint16 (&quot;myproto.msgid&quot;, &quot;Message Id&quot;)
f.var2 = ProtoField.uint16 (&quot;myproto.var1&quot;, &quot;var1&quot;)

function MYPROTO.dissector (buffer, pinfo, tree)
    subtree:add (f.var1, buffer(offset, 2))
    offset = offset + 2

    local msgid = buffer (offset, 2)
    local mi = subtree:add (f.msgid, msgid)
    offset = offset + 2

    --This is calling a nested/chain dissectors which has a variable length filed.
    --How can this function be made to return bytes it consumed while decoding the
    --variable length field?
    myproto_dt:try (msgid:uint(), buffer(offset):tvb(), pinfo, subtree)

    --This step is missing
    offset = offset + offset_consumed

    subtree:add (f.var2, buffer(offset, 2))
    offset = offset + 2
end</code></pre></div><div id="question-tags" class="tags-container tags">lua dissector offset</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '12, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/b3bc8479ca3cba80cde55777850572a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nrk1983&#39;s gravatar image" /><p>nrk1983<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nrk1983 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jul '12, 12:28</p></div></div><div id="comments-container-12358" class="comments-container"></div><div id="comment-tools-12358" class="comment-tools"></div><div class="clear"></div><div id="comment-12358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12359"></span>

<div id="answer-container-12359" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12359-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ideally, the sub-dissector would just return the number of consumed bytes, and you'd just check the return value, but <a href="http://wiki.wireshark.org/LuaAPI/Dissector#dissectortable:try.28pattern.2C_tvb.2C_pinfo.2C_tree.29"><code>DissectorTable.try()</code></a> does not return any values. Neither does <a href="http://wiki.wireshark.org/LuaAPI/Dissector#dissector:call.28tvb.2C_pinfo.2C_tree.29"><code>Dissector.call()</code></a>. I suggest filing an enhancement request at <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a> to get those functions to return the <code>rval</code> of the called dissector.</p><p>A workaround is to declare a global variable, call <code>DissectorTable.try()</code> (whose sub-dissector would set the variable to the number of consumed bytes), and then check the value of the variable for the result. This is a bit ugly due to the usage of globals.</p><pre><code>foo.rval = -1
myproto_dt:try (...) -- subdissector sets foo.rval
print(&#39;number of consumed bytes&#39;, foo.rval)
foo.rval = nil -- cleanup</code></pre><p>You can avoid globals in this particular case by using <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Pinfo.html#lua_class_PrivateTable"><code>pinfo.private</code></a>, which contains a string hash table (of string keys and string values). This is only slightly less ugly than globals, but when life gives you lemons...</p><pre><code>pinfo.private.rval = -1
myproto_dt:try (...) -- subdissector sets pinfo.private.rval
print(&#39;number of consumed bytes&#39;, pinfo.private.rval) 
pinfo.private.rval = nil -- cleanup</code></pre><p>Note the value from a <code>pinfo.private</code> lookup is a string...use <a href="http://www.lua.org/manual/5.2/manual.html#pdf-tonumber"><code>tonumber()</code></a> to convert the string to a number if necessary.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '12, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-12359" class="comments-container"><span id="12376"></span><div id="comment-12376" class="comment"><div id="post-12376-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot.. pinfo.private.rval solution worked..</p></div><div id="comment-12376-info" class="comment-info"><span class="comment-age">(02 Jul '12, 10:29)</span> nrk1983</div></div></div><div id="comment-tools-12359" class="comment-tools"></div><div class="clear"></div><div id="comment-12359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

