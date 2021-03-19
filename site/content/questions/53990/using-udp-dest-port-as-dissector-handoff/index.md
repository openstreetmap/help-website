+++
type = "question"
title = "Using UDP dest port as dissector handoff"
description = '''Hi, I am working on a dissector but I&#x27;m having trouble performing the handoff correctly. The packet in question is tunneled so I need to perform the handoff after the external headers. Right now I was able to get it to work by using the UDP dest port as a trigger, but I am wondering if that is a saf...'''
date = "2016-07-11T11:58:00Z"
lastmod = "2016-07-11T14:28:00Z"
weight = 53990
keywords = [ "udp", "dissector", "handoff", "wireshark" ]
aliases = [ "/questions/53990" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Using UDP dest port as dissector handoff](/questions/53990/using-udp-dest-port-as-dissector-handoff)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53990-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am working on a dissector but I'm having trouble performing the handoff correctly. The packet in question is tunneled so I need to perform the handoff after the external headers. Right now I was able to get it to work by using the UDP dest port as a trigger, but I am wondering if that is a safe way to do it. Will any traffic going to the same UDP dest port be analyzed using this dissector then (including packets I may not want)?</p><pre><code>dissector_add_uint(&quot;udp.port&quot;, 8099, juniper_vn_handle);</code></pre></div><div id="question-tags" class="tags-container tags">udp dissector handoff wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '16, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/17990ea36534960267c25c248aa1eb8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asetia&#39;s gravatar image" /><p>asetia<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asetia has no accepted answers">0%</span></p></div></div><div id="comments-container-53990" class="comments-container"></div><div id="comment-tools-53990" class="comment-tools"></div><div class="clear"></div><div id="comment-53990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53995"></span>

<div id="answer-container-53995" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53995-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>Will any traffic going to the same UDP dest port be analyzed using this dissector then (including packets I may not want)?</code></pre><p>Yes, that would be the case. There is not concept of how much layering is applied then selecting the dissector (as you have noticed by the lack of any API parameter for this).</p><p>That stems from the fact the port numbers are/were intended to identify specific services at the various network hosts. Many still are present at their well known port numbers, but many more are present at the higher numbers. This is such a case. Therefor it's inevitable 'foreign protocol' may enter via this port number into your dissector.</p><p>There are two ways about it:</p><ol><li>Setting up a conversation (based on IP addresses, port numbers and transport layer protocol)</li><li>Make a heuristic dissector (which determines on the start of the packet if the packet is indeed the of the expected protocol)</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '16, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53995" class="comments-container"></div><div id="comment-tools-53995" class="comment-tools"></div><div class="clear"></div><div id="comment-53995-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

