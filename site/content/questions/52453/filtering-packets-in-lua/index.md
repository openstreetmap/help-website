+++
type = "question"
title = "Filtering packets in LUA"
description = '''I have read that in order to obtain information about packets in LUA you have to use taps, but there only a few supported types. I want to have filters for different protocols (ARP, goose, etc) and get their individual pinfo.number. I have tried using pinfo.curr_proto but it printed &amp;lt; Missing Pro...'''
date = "2016-05-11T15:05:00Z"
lastmod = "2016-07-19T10:42:00Z"
weight = 52453
keywords = [ "listener", "lua", "arp", "goose", "script" ]
aliases = [ "/questions/52453" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering packets in LUA](/questions/52453/filtering-packets-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52453-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have read that in order to obtain information about packets in LUA you have to use taps, but there only <a href="https://wiki.wireshark.org/LuaAPI/Listener">a few</a> supported types. I want to have filters for different protocols (ARP, <a href="https://en.wikipedia.org/wiki/Generic_Substation_Events">goose</a>, etc) and get their individual <code>pinfo.number</code>. I have tried using <code>pinfo.curr_proto</code> but it printed <code>&lt; Missing Protocol Name&gt;</code></p><p>Do I have to write a dissector for unsupported protocols?</p></div><div id="question-tags" class="tags-container tags">listener lua arp goose script</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '16, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/f9df4644e8c578c944b68144e0e7adce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="13utters&#39;s gravatar image" /><p>13utters<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="13utters has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jul '16, 10:44</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-52453" class="comments-container"><span id="52454"></span><div id="comment-52454" class="comment"><div id="post-52454-score" class="comment-score"></div><div class="comment-text"><p>pinfo.curr_proto returns &lt; Missing Protocol Name&gt; for HTTP packets too</p></div><div id="comment-52454-info" class="comment-info"><span class="comment-age">(11 May '16, 15:55)</span> 13utters</div></div></div><div id="comment-tools-52453" class="comment-tools"></div><div class="clear"></div><div id="comment-52453-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54167"></span>

<div id="answer-container-54167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54167-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the <a href="https://wiki.wireshark.org/Lua/Dissectors#postdissectors">Lua postdissectors</a>?</p><p>In the "Trivial" example provided, if you try to use <code>pinfo.curr_proto</code>, you will get "Trivial", which isn't what you want I don't think, but you should be able to use <code>frame.protocols</code> to determine which protocols are present in the frame. If you add/replace these lines to the postdissector example given, you can see what I mean:</p><pre><code> 7 frame_protocols_f = Field.new(&quot;frame.protocols&quot;)
13 protocols_F = ProtoField.string(&quot;trivial.protocols&quot;, &quot;Protocols&quot;)
14 trivial_proto.fields = {src_F, dst_F, conv_F, protocols_F}
22     local protocols = frame_protocols_f()
30         subtree:add(protocols_F,tostring(protocols))</code></pre><p>When I ran it, it displayed something like this:</p><pre><code>Source: 192.168.1.1:12345
Destination: 192.168.1.2:45678
Conversation: 192.168.1.1:12345-&gt;192.168.1.2:45678
Protocols: eth:ethertype:ip:tcp</code></pre><p>If you're only interested in the last protocol in the stack, <code>tcp</code> in this case, then you can write a function (or search for one) to trim all characters up to and including the ':' from the string.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '16, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54167" class="comments-container"></div><div id="comment-tools-54167" class="comment-tools"></div><div class="clear"></div><div id="comment-54167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

