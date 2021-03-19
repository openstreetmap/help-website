+++
type = "question"
title = "lua dissector &#92; running for TCP AND UDP"
description = '''Hello, i am currently writing a dissector with lua which use data from UDP AND TCP. So i register the dissector like this udp_table = DissectorTable.get(&quot;udp.port&quot;) udp_table:add(1024, SEL) tcp_table = DissectorTable.get(&quot;tcp.port&quot;) tcp_table:add(1024, SEL)  but in the function SEL.dissector(_tvbuf,...'''
date = "2017-04-26T12:28:00Z"
lastmod = "2017-04-26T23:48:00Z"
weight = 61061
keywords = [ "lua" ]
aliases = [ "/questions/61061" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lua dissector \\ running for TCP AND UDP](/questions/61061/lua-dissector-running-for-tcp-and-udp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61061-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>i am currently writing a dissector with lua which use data from UDP AND TCP. So i register the dissector like this</p><pre><code>udp_table = DissectorTable.get(&quot;udp.port&quot;)
udp_table:add(1024, SEL)
tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
tcp_table:add(1024, SEL)</code></pre><p>but in the function SEL.dissector(_tvbuf, _pktinfo, _root), i need to know if this if data is coming from UDP or TCP.</p><p>Is there a way to detect UDP ou TCP data ?</p><p>Thank</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '17, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/52c3825749489f8e41ff11f522d9bdbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SebastienRolle&#39;s gravatar image" /><p>SebastienRolle<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SebastienRolle has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Apr '17, 17:07</p></div></div><div id="comments-container-61061" class="comments-container"></div><div id="comment-tools-61061" class="comment-tools"></div><div class="clear"></div><div id="comment-61061-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61064"></span>

<div id="answer-container-61064" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61064-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, there is. Create the <code>SEL_udp</code> and <code>SEL_tcp</code> functions to register with the respective protocols and have them call <code>SEL</code> with an extra flag indicating the protocol it came from. This is how it's done in other dissectors as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '17, 23:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-61064" class="comments-container"><span id="61070"></span><div id="comment-61070" class="comment"><div id="post-61070-score" class="comment-score"></div><div class="comment-text"><p>Thank a lot. Can you point me to an existing dissector in order for me to understand.</p><p>Thank, Sebastien</p></div><div id="comment-61070-info" class="comment-info"><span class="comment-age">(27 Apr '17, 05:36)</span> SebastienRolle</div></div><span id="61081"></span><div id="comment-61081" class="comment"><div id="post-61081-score" class="comment-score"></div><div class="comment-text"><p>i have done this but unfortunately, it doesn't work. Can you give me a little more details about the proposed solution.</p><pre><code>local SEL = Proto(&quot;sel&quot;, &quot;sel&quot;);

function aa(_tvbuf, _pktinfo, _root)
end
function bb(_tvbuf, _pktinfo, _root)
end
function SEL.dissector(_tvbuf, _pktinfo, _root)
end

DissectorTable.get(&quot;udp.port&quot;):add_for_decode_as(aa)
DissectorTable.get(&quot;tcp.port&quot;):add_for_decode_as(bb)</code></pre></div><div id="comment-61081-info" class="comment-info"><span class="comment-age">(27 Apr '17, 10:59)</span> SebastienRolle</div></div><span id="61088"></span><div id="comment-61088" class="comment"><div id="post-61088-score" class="comment-score"></div><div class="comment-text"><p>I don't do LUA myself, but recon it would be something like this:</p><pre><code>local SEL_udp = Proto(&quot;sel_udp&quot;, &quot;sel_udp&quot;)
udp_table = DissectorTable.get(&quot;udp.port&quot;)
udp_table:add(1024, SEL_udp)
local SEL_tcp = Proto(&quot;sel_tcp&quot;, &quot;sel_tcp&quot;)
tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
tcp_table:add(1024, SEL_tcp)

function SEL_udp(_tvb, _pktinfo, _root)
    SEL(_tvbuf, _pktinfo, _root, FALSE)
end
function SEL_tcp(_tvb, _pktinfo, _root)
    SEL(_tvbuf, _pktinfo, _root, TRUE)
end
function SEL(_tvb, _pktinfo, _root, is_tcp)
    ...
end</code></pre><p>If you don't want to have the separate dissector registrations (one for UDP, one for TCP) you might also be able to look at pktinfo. In that structure you should have a ptype field, which indicates the (transport) protocol as well.</p></div><div id="comment-61088-info" class="comment-info"><span class="comment-age">(28 Apr '17, 01:39)</span> Jaap ♦</div></div></div><div id="comment-tools-61064" class="comment-tools"></div><div class="clear"></div><div id="comment-61064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

