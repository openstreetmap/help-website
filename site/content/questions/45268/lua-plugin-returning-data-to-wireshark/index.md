+++
type = "question"
title = "Lua plugin returning data to Wireshark"
description = '''Hello, I&#x27;m pretty new to Lua, so sorry if this question is too easy. However, I have searched a great part of internet looking for the answear, hope you will be able to help. I am running on Wireshark v1.99.9rc0-197-g7833b93 I am writing a plugin for Wireshark in Lua, in order to enable it to read I...'''
date = "2015-08-20T07:45:00Z"
lastmod = "2015-08-20T10:00:00Z"
weight = 45268
keywords = [ "wireshark1.99", "lua", "sml", "ipt" ]
aliases = [ "/questions/45268" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Lua plugin returning data to Wireshark](/questions/45268/lua-plugin-returning-data-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45268-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm pretty new to Lua, so sorry if this question is too easy. However, I have searched a great part of internet looking for the answear, hope you will be able to help. I am running on Wireshark v1.99.9rc0-197-g7833b93</p><p>I am writing a plugin for Wireshark in Lua, in order to enable it to read IPT protocol. The problem is, that inside the IPT message, there is another message, written in SML. This is why I would like to "give" the data (a part of the frame that is in fact SML frame) back to Wireshark, so that I could decode it as the SML frame.</p><p>Another problem with SML is that I can not invoke it from my protocole - function:</p><pre><code>Dissector.get(&quot;sml&quot;):call(tvb, pktinfo, tree)</code></pre><p>gives the following error:</p><p>Lua Error: [string "C:\Development\wireshark\wireshark-gtk2\plugi..."]:214: bad argument #1 to 'get' (Dissector_get: No such dissector)</p><p>So I can not even do it in this more "simple" way. Is it even possible to call SML from Lua script?</p></div><div id="question-tags" class="tags-container tags">wireshark1.99 lua sml ipt</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '15, 07:45</strong></p><img src="https://secure.gravatar.com/avatar/f691af113096bf9b41038440dc2950c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Macko125&#39;s gravatar image" /><p>Macko125<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Macko125 has no accepted answers">0%</span></p></div></div><div id="comments-container-45268" class="comments-container"></div><div id="comment-tools-45268" class="comment-tools"></div><div class="clear"></div><div id="comment-45268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45274"></span>

<div id="answer-container-45274" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45274-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is possible, I think, but fairly tricky. The problem is SML does not register its dissector by name, so you can't get it by name. Instead, I think you can get it from the "tcp.port" or "udp.port" table it adds its dissector into, by using the <code>get_dissector()</code> method. For example:</p><pre><code>-- assuming the SML dissector is registered for TCP port 7259
local sml_dissector = DissectorTable.get(&quot;tcp.port&quot;):get_dissector(7259)</code></pre><p>Unfortunately, the SML dissector is not added to the TCP or UDP port table unless/until its preference settings tell it to be (it's disabled by default). So... you'll have to:</p><ol><li><p>Set the preference for SML to use the TCP or UDP port for some number you choose, in Edit-&gt;Preferences-&gt;Protocols-&gt;SML. Save that preference, and restart wireshark.</p></li><li><p>You can't get the SML dissector until it's read its preference settings, which won't happen until after your Lua file loads. That means you'll need to not get the dissector until later - for example within your dissector function or in a <code>myproto.init()</code> function. You don't need to get it every time, just save it to a local variable that was declared outside of your function. For example:</p><pre><code>-- this will hold the SML dissector
local sml_dissector

function myhproto.dissector(tvbuf, pinfo, tree)
    if not sml_dissector then
        -- assuming your SML dissector registers on TCP port 7259
        sml_dissector = DissectorTable.get(&quot;tcp.port&quot;):get_dissector(7259)
    end

    -- use the dissector
    sml_dissector:call(tvb, pktinfo, tree)
end</code></pre></li></ol><p>Note: I haven't tried the above, but it should work. (hopefully)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '15, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-45274" class="comments-container"><span id="45289"></span><div id="comment-45289" class="comment"><div id="post-45289-score" class="comment-score"></div><div class="comment-text"><p>That helped. Thanks a lot!</p></div><div id="comment-45289-info" class="comment-info"><span class="comment-age">(21 Aug '15, 01:42)</span> Macko125</div></div></div><div id="comment-tools-45274" class="comment-tools"></div><div class="clear"></div><div id="comment-45274-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

