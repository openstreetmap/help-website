+++
type = "question"
title = "Ignore packets with TCP errors in custom dissector"
description = '''I&#x27;m developing a custom dissector for a version of Wireshark (1.0.15) that doesn&#x27;t have the tcp.no_subdissector_on_error option. How can my dissector determine that a TCP error (retransmit, out-of-order, etc) occurred so that it can choose not to dissect it?'''
date = "2015-07-01T08:57:00Z"
lastmod = "2015-07-01T11:19:00Z"
weight = 43790
keywords = [ "dissector", "tcp" ]
aliases = [ "/questions/43790" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Ignore packets with TCP errors in custom dissector](/questions/43790/ignore-packets-with-tcp-errors-in-custom-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43790-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm developing a custom dissector for a version of Wireshark (1.0.15) that doesn't have the tcp.no_subdissector_on_error option. How can my dissector determine that a TCP error (retransmit, out-of-order, etc) occurred so that it can choose not to dissect it?</p></div><div id="question-tags" class="tags-container tags">dissector tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '15, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/0a30b28d6b966c89c0989d781ac4963d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mjs9585&#39;s gravatar image" /><p>mjs9585<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mjs9585 has no accepted answers">0%</span></p></div></div><div id="comments-container-43790" class="comments-container"></div><div id="comment-tools-43790" class="comment-tools"></div><div class="clear"></div><div id="comment-43790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43796"></span>

<div id="answer-container-43796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43796-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Waouh, that is old!</p><p>Given what I see in wireshark-1.0.5 this does not seem possible as the TCP analysis is not available to sub dissectors. If you are building your own version of Wireshark, the easiest would probably to backport the check for tcp.no_subdissector_on_error check from master-1.12 branch to this version (it is only a few lines of code at the beginning of decode_tcp_ports() function).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '15, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43796" class="comments-container"></div><div id="comment-tools-43796" class="comment-tools"></div><div class="clear"></div><div id="comment-43796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

