+++
type = "question"
title = "Wireshark and openflow"
description = '''I need to scan openflow packets. I successfully compiled and installed the openflow plugin from sources, anyway on most of packets I get a DISSECTOR_ASSERT_NOT_REACHED on the file proto.c. Those are tcp, icmp and the 90% of packets I scan, just the hellos messages are dissected with no problem. So I...'''
date = "2014-03-01T02:39:00Z"
lastmod = "2014-03-01T12:21:00Z"
weight = 30305
keywords = [ "openflow", "wireshark" ]
aliases = [ "/questions/30305" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark and openflow](/questions/30305/wireshark-and-openflow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30305-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to scan openflow packets. I successfully compiled and installed the openflow plugin from sources, anyway on most of packets I get a DISSECTOR_ASSERT_NOT_REACHED on the file proto.c. Those are tcp, icmp and the 90% of packets I scan, just the hellos messages are dissected with no problem.</p><p>So I'd like an help..I even heard somewhere that some more recent versions of wireshark already include an openflow dissector. Does it work fine? And what version should I use? Currently I have an 1.8.2 which comes from the default repositories of ubuntu 12.04.</p></div><div id="question-tags" class="tags-container tags">openflow wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '14, 02:39</strong></p><img src="https://secure.gravatar.com/avatar/e90dd5fab923255e04b76822e2112776?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phate867&#39;s gravatar image" /><p>phate867<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phate867 has no accepted answers">0%</span></p></div></div><div id="comments-container-30305" class="comments-container"></div><div id="comment-tools-30305" class="comment-tools"></div><div class="clear"></div><div id="comment-30305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30307"></span>

<div id="answer-container-30307" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30307-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The openflow dissector only exists in the development version.You need to download and build it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '14, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-30307" class="comments-container"></div><div id="comment-tools-30307" class="comment-tools"></div><div class="clear"></div><div id="comment-30307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30308"></span>

<div id="answer-container-30308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30308-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Or get the latest <a href="http://www.wireshark.org/download/automated/">nightly build</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '14, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30308" class="comments-container"><span id="30312"></span><div id="comment-30312" class="comment"><div id="post-30312-score" class="comment-score"></div><div class="comment-text"><p>Not available for the OP's OS, Ubuntu 12.04</p></div><div id="comment-30312-info" class="comment-info"><span class="comment-age">(01 Mar '14, 13:33)</span> grahamb ♦</div></div></div><div id="comment-tools-30308" class="comment-tools"></div><div class="clear"></div><div id="comment-30308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

