+++
type = "question"
title = "Can&#x27;t get Lua dissector to add to tree with Protofields"
description = '''I&#x27;ve a simple Lua dissector, which uses what I think is the &#x27;old&#x27; format for adding to the tree. subtree:add(buffer(3,1),&quot;The 4th byte: &quot; .. buffer(3,1):uint())  I&#x27;ve tried using protofields instead, but nothing gets added to the tree. foo_proto.fields.u16 = ProtoField.uint16(&quot;foo.u16&quot;, &quot;Unsigned sh...'''
date = "2012-02-20T16:04:00Z"
lastmod = "2012-02-25T16:56:00Z"
weight = 9155
keywords = [ "lua", "dissector", "protofield" ]
aliases = [ "/questions/9155" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't get Lua dissector to add to tree with Protofields](/questions/9155/cant-get-lua-dissector-to-add-to-tree-with-protofields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9155-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I've a simple Lua dissector, which uses what I think is the 'old' format for adding to the tree.</p><pre><code>subtree:add(buffer(3,1),&quot;The 4th byte: &quot; .. buffer(3,1):uint())</code></pre><p>I've tried using protofields instead, but nothing gets added to the tree.</p><pre><code>foo_proto.fields.u16 = ProtoField.uint16(&quot;foo.u16&quot;, &quot;Unsigned short&quot;, base.HEX)
local t = tree:add(foo_proto,buf())
t:add(foo_proto.fields.u16, buf(0,2))</code></pre><p>Does anyone have any pointers to how to do this, or a <em>working</em> simple dummy TCP dissector?</p><p>This is Wireshark 1.6.5 on Windows, BTW.</p></div><div id="question-tags" class="tags-container tags">lua dissector protofield</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '12, 16:04</strong></p><img src="https://secure.gravatar.com/avatar/a8d5ac2a3567c1c6db891e5a6babcebe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roddyp&#39;s gravatar image" /><p>roddyp<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roddyp has no accepted answers">0%</span></p></div></div><div id="comments-container-9155" class="comments-container"><span id="10710"></span><div id="comment-10710" class="comment"><div id="post-10710-score" class="comment-score"></div><div class="comment-text"><p>I'd also like to know how to use the new "ProtoField" based TreeItem:add(), instead of having to manually construct labels etc. When I do it that way, my subtree shows up empty in the Wireshark GUI. Seems to be working OK in tshark though..</p><p>Code example:</p><pre><code>local f = CCMP.fields
f.start = ProtoField.uint8 (&quot;ccmp.start&quot;, &quot;Start&quot;, base.HEX)
subtree:add(f.start, buf(0, 1))</code></pre><p>I'm also on Windows, and have tried 1.6.6 stable and 1.7.1 development.</p></div><div id="comment-10710-info" class="comment-info"><span class="comment-age">(06 May '12, 20:48)</span> rfi</div></div><span id="10711"></span><div id="comment-10711" class="comment"><div id="post-10711-score" class="comment-score"></div><div class="comment-text"><p>I've updated my answer to include a <code>ProtoFields</code> example.</p></div><div id="comment-10711-info" class="comment-info"><span class="comment-age">(06 May '12, 21:42)</span> helloworld</div></div><span id="10712"></span><div id="comment-10712" class="comment"><div id="post-10712-score" class="comment-score"></div><div class="comment-text"><p>Thank you helloworld.</p><p>For anyone else that can't get this working, my problem was that I tested my script by evaluating it using Tools &gt; Evaluate in the GUI. When I ran it from the command line using</p><pre><code>wireshark -X lua_script:\proto.lua</code></pre><p>it worked fine.</p></div><div id="comment-10712-info" class="comment-info"><span class="comment-age">(06 May '12, 23:02)</span> rfi</div></div></div><div id="comment-tools-9155" class="comment-tools"></div><div class="clear"></div><div id="comment-9155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9210"></span>

<div id="answer-container-9210" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9210-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Lua you've shown is syntactically correct and functional. It's not exactly "old"; it's just another way of adding items to the tree.</p><p>I'm guessing you grabbed the snippet from the <a href="http://wiki.wireshark.org/Lua/Dissectors">Lua/Dissectors wiki page</a>, which I confirmed works in 1.7.0 on Windows 7. Here's the same code from the Lua wiki, modified for tcp:</p><pre><code>trivial_proto = Proto(&quot;trivial&quot;,&quot;Trivial Protocol&quot;)

function trivial_proto.dissector(buffer,pinfo,tree)
    pinfo.cols.protocol = &quot;TRIVIAL&quot;
    local subtree = tree:add(trivial_proto,buffer(),&quot;Trivial Protocol Data&quot;)
    subtree:add(buffer(0,2),&quot;The first two bytes: &quot; .. buffer(0,2):uint())
    subtree = subtree:add(buffer(2,2),&quot;The next two bytes&quot;)
    subtree:add(buffer(2,1),&quot;The 3rd byte: &quot; .. buffer(2,1):uint())
    subtree:add(buffer(3,1),&quot;The 4th byte: &quot; .. buffer(3,1):uint())
end

tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
-- register our protocol to handle tcp port 80 (HTTP)
tcp_table:add(80,trivial_proto)</code></pre><p>Copy that to a Lua file in your Wireshark plugins directory (e.g., <code>%APPDATA%\Wireshark\plugins\trivial.lua</code>). Start a Wireshark capture, open your browser to a web page (e.g., <a href="http://www.google.com">http://www.google.com</a>), and watch Wireshark's Protocol column fill up with "TRIVIAL". You'll also see the "Trivial" tree items.</p><p><strong>EDIT:</strong> Here's an equivalent dissector that uses <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_class_ProtoField"><code>ProtoFields</code></a>:</p><pre><code>local trivial_proto = Proto(&quot;trivial&quot;,&quot;Trivial Protocol&quot;)

local F = trivial_proto.fields

F.f_1 = ProtoField.uint16(&quot;trivial.first_two&quot;, &quot;The first two bytes&quot;)
F.f_2 = ProtoField.uint8(&quot;trivial.third&quot;, &quot;The 3rd byte&quot;)
F.f_3 = ProtoField.uint8(&quot;trivial.fourth&quot;, &quot;The 4th byte&quot;)

function trivial_proto.dissector(buffer,pinfo,tree)
    pinfo.cols.protocol = &quot;TRIVIAL&quot;
    local subtree = tree:add(trivial_proto,buffer(),&quot;Trivial Protocol Data&quot;)
    subtree:add(F.f_1, buffer(0,2))
    subtree = subtree:add(buffer(2,2),&quot;The next two bytes&quot;)
    subtree:add(F.f_2, buffer(2,1))
    subtree:add(F.f_3, buffer(3,1))
end

tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
-- register our protocol to handle tcp port 80 (HTTP)
tcp_table:add(80,trivial_proto)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '12, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 May '12, 21:48</p></div></div><div id="comments-container-9210" class="comments-container"></div><div id="comment-tools-9210" class="comment-tools"></div><div class="clear"></div><div id="comment-9210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

