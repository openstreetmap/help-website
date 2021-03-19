+++
type = "question"
title = "Cannot create ProtoField with ftypes.NONE"
description = '''Hello, i&#x27;m trying to create a dissector in .lua for Wireshark (1.10.7 x64)  and i cannot add a field with ftypes.NONE, because Wireshark complains about &quot;invalid ftypes&quot;. So my question here is: Is this a bug, or is it supposed to be like that? Edit: Sorry i forgot the sample code. Im trying to conv...'''
date = "2014-05-30T15:52:00Z"
lastmod = "2014-06-22T11:01:00Z"
weight = 33225
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/33225" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot create ProtoField with ftypes.NONE](/questions/33225/cannot-create-protofield-with-ftypesnone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33225-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i'm trying to create a dissector in .lua for Wireshark (1.10.7 x64) and i cannot add a field with ftypes.NONE, because Wireshark complains about "invalid ftypes".</p><p>So my question here is: Is this a bug, or is it supposed to be like that?</p><p>Edit: Sorry i forgot the sample code. Im trying to convert this old dissector written in c to lua: C-Code:</p><pre><code>static hf_register hf[] = {
{ &amp;hf_myproto, { &quot;Data&quot;, &quot;myproto.data&quot;, FT_NONE, BASE_NONE, NULL, 0x0, &quot;myprotoPDU&quot;, HFILL}},
{ &amp;hf_myproto_header, { &quot;Header&quot;, &quot;myproto.header&quot;, FT_NONE, BASE_NONE, NULL, 0x0, &quot;myprotoHeader&quot;, HFILL}},
{ &amp;hf_myproto_packet, { &quot;Packet&quot;, &quot;myproto.packet&quot;, FT_NONE, BASE_NONE, NULL, 0x0, &quot;myprotoPacket&quot;, HFILL}}, 
...
}</code></pre><p>Lua-Code:</p><pre><code>local ncp = p_myproto.fields
ncp.hf_myproto = ProtoField.new(&quot;Data&quot;, &quot;myproto.data&quot;, ftypes.NONE, nil, base.NONE, 0x0, &quot;myprotoPDU&quot;)
ncp.hf_myproto_header = ProtoField.new(&quot;Header&quot;, &quot;myproto.header&quot;, ftypes.NONE, nil, base.NONE, 0x0, &quot;myprotoHeader&quot;)
ncp.hf_myproto_packet = ProtoField.new(&quot;Packet&quot;, &quot;myproto.packet&quot;, ftypes.NONE, nil, base.NONE, 0x0, &quot;myprotoPacket&quot;)
...</code></pre><p>There are some more fields with uint16 and such, but they are working just fine, so i removed them here.</p><p>-Namikon</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '14, 15:52</strong></p><img src="https://secure.gravatar.com/avatar/c4da026478cd759297facc4876c3e83f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Namikon&#39;s gravatar image" /><p>Namikon<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Namikon has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jun '14, 11:02</p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-33225" class="comments-container"><span id="33233"></span><div id="comment-33233" class="comment"><div id="post-33233-score" class="comment-score"></div><div class="comment-text"><p>can you please post some sample code?</p></div><div id="comment-33233-info" class="comment-info"><span class="comment-age">(31 May '14, 07:24)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33225" class="comment-tools"></div><div class="clear"></div><div id="comment-33225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34043"></span>

<div id="answer-container-34043" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34043-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>So my question here is: Is this a bug, or is it supposed to be like that?</p></blockquote><p>It's not a bug, per se. <code>ftypes.NONE</code> was explicitly excluded in the internal code; and it is not in the list of types allowed for that third argument of <code>ProtoField.new()</code>, as listed in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Proto.html#lua_class_ProtoField">API docs for ProtoField</a>.</p><p>I'm not sure <em>why</em> it was excluded though... maybe there was a sentiment at the time that <code>FT_NONE</code> would be removed someday?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '14, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-34043" class="comments-container"></div><div id="comment-tools-34043" class="comment-tools"></div><div class="clear"></div><div id="comment-34043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

