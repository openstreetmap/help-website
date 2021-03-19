+++
type = "question"
title = "Define a custom RTP header Extensions"
description = '''Hello, I hope you can help me a little bit I have a RTP Protocol with a RTP Header Extensions. I have some UDP streams recorded and now I would like to decode as RTP with my RTP Header Extensions. Wireshark decode the main RTP Header correct. But he doesn’t know my Header Extensions. What is now the...'''
date = "2014-03-11T09:50:00Z"
lastmod = "2014-03-11T10:30:00Z"
weight = 30686
keywords = [ "lua", "rtp" ]
aliases = [ "/questions/30686" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Define a custom RTP header Extensions](/questions/30686/define-a-custom-rtp-header-extensions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30686-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I hope you can help me a little bit I have a RTP Protocol with a RTP Header Extensions. I have some UDP streams recorded and now I would like to decode as RTP with my RTP Header Extensions. Wireshark decode the main RTP Header correct. But he doesn’t know my Header Extensions.</p><p>What is now the best way to add code to Wireshark so that Wireshark can read my RTP Header Extensions. I have read a lot about lua, but I have no Idea how I can build such a lua script.</p><p>Must I build my own Wireshark with the C code or is this with lua possible? I would like to have stable Version 1.10.6. I thing with lua I must build a protocol dissector. But know that ands a little bit.</p><p>I have tried it like this but I fail:</p><pre><code>local myfirstHeaderExtensionValue        = ProtoField. ?  -- i would like 2 bits that are calles MYSTUFF
dns.fields = {myfirstHeaderExtensionValue}
function dns.dissector(tvbuf,pktinfo,root){ ???}</code></pre><p>Have a nice Day</p></div><div id="question-tags" class="tags-container tags">lua rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '14, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/3378e4af34b02834b98e8a896efe303c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alias_alias&#39;s gravatar image" /><p>Alias_alias<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alias_alias has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Mar '14, 10:39</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-30686" class="comments-container"></div><div id="comment-tools-30686" class="comment-tools"></div><div class="clear"></div><div id="comment-30686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30688"></span>

<div id="answer-container-30688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30688-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to do this in Lua, I suggest you don't dissect all of RTP - it's a lot of work and you'd be missing out on the features RTP provides like media playback and such.</p><p>Instead, I believe you can create a dissector just for the RTP header extension, and register it into the DissectorTable for "rtp.hdr_ext". For example, instead of doing this:</p><pre><code>local udp_encap_table = DissectorTable.get(&quot;udp.port&quot;)
udp_encap_table:add(udp_port_number, my_rtp_proto)</code></pre><p>Do this:</p><pre><code>local rtp_hdrext_table = DissectorTable.get(&quot;rtp.hdr_ext&quot;)
rtp_hdrext_table:add(rtp_header_extension_number, my_rtp_proto)</code></pre><p>But the beginning part of creating your protocol dissector and fields and such (what you were trying to do in your example post I think) takes longer to explain. Did you read the comments in the <code>dissector.lua</code> file found through the <a href="http://wiki.wireshark.org/Lua/Examples">Lua examples wiki page</a>? If they're not clear enough, let me know and I'll try to update them. The purpose of all the comments was to try to explain why things were being done, because it is definitely confusing to new folks.</p><p>Do you have a sample capture file with your RTP packets that you can post on cloudshark or someplace?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '14, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30688" class="comments-container"></div><div id="comment-tools-30688" class="comment-tools"></div><div class="clear"></div><div id="comment-30688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

