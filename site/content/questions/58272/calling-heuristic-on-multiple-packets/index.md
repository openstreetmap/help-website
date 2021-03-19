+++
type = "question"
title = "Calling heuristic on multiple packets"
description = '''Hello, I am writing dissectors for several udp protocols that use header only packets for heartbeating that lack exact identifying values for heuristic dissection. However, in the non heartbeat packets there are identifying fields. Is there a way to have a dissector look at multiple packets (like 10...'''
date = "2016-12-21T08:12:00Z"
lastmod = "2016-12-21T12:20:00Z"
weight = 58272
keywords = [ "heuristic", "lua" ]
aliases = [ "/questions/58272" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Calling heuristic on multiple packets](/questions/58272/calling-heuristic-on-multiple-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58272-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am writing dissectors for several udp protocols that use header only packets for heartbeating that lack exact identifying values for heuristic dissection. However, in the non heartbeat packets there are identifying fields. Is there a way to have a dissector look at multiple packets (like 10) in a heuristic method before determining which protocol to use?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">heuristic lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '16, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/d03ce1682e2a9e3bd9ed3be60088d031?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="william&#39;s gravatar image" /><p>william<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="william has no accepted answers">0%</span></p></div></div><div id="comments-container-58272" class="comments-container"></div><div id="comment-tools-58272" class="comment-tools"></div><div class="clear"></div><div id="comment-58272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58277"></span>

<div id="answer-container-58277" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58277-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A dissectors job is to look at (part of) the packet currently at hand, which is sequential when first read from the capture file, then at random when packet details are required for presentation in the GUI, or when running analysis, etc.</p><p>What you can do is use the other features of the dissection engine to support these needs. One that pops to mind is the use of conversations. There you define a flow of packets between two IP/port end points for UDP packets and associate a dissector to it then. That's how you have the dissector setup right dissector for these UDP packets. The same can be achieved manually through the use of the 'Decode as' feature, but automatic sounds better to me. See doc/README.dissector for some background on conversations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '16, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58277" class="comments-container"><span id="58279"></span><div id="comment-58279" class="comment"><div id="post-58279-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I will take a look. We are trying to avoid the 'Decode as' feature. Are there any examples where an existing dissector decodes some bytes then looks at a conversation before deciding decoding type?</p></div><div id="comment-58279-info" class="comment-info"><span class="comment-age">(21 Dec '16, 12:46)</span> william</div></div><span id="58281"></span><div id="comment-58281" class="comment"><div id="post-58281-score" class="comment-score"></div><div class="comment-text"><p>It's the other way around. The dissector heuristics decide if the current payload is his, then sets up a conversation based on the communication parameters so that any payload of packets matching these parameters are send there.</p></div><div id="comment-58281-info" class="comment-info"><span class="comment-age">(21 Dec '16, 14:51)</span> Jaap ♦</div></div></div><div id="comment-tools-58277" class="comment-tools"></div><div class="clear"></div><div id="comment-58277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

