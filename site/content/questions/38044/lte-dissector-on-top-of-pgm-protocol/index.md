+++
type = "question"
title = "lte dissector on top of PGM protocol"
description = '''I am using wireshark 1.10.6 on Ubuntu 14.04. I am able to dissect lte packets which comes over UDP. Thus all lte packets details are visible in wireshark. But I want to use PGM protocol for LTE stack development. I want to put LTE packet details on top of PGM protocol. There is no settings available...'''
date = "2014-11-21T06:08:00Z"
lastmod = "2014-11-21T06:51:00Z"
weight = 38044
keywords = [ "pgm", "dissector", "lte" ]
aliases = [ "/questions/38044" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [lte dissector on top of PGM protocol](/questions/38044/lte-dissector-on-top-of-pgm-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38044-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark 1.10.6 on Ubuntu 14.04. I am able to dissect lte packets which comes over UDP. Thus all lte packets details are visible in wireshark. But I want to use PGM protocol for LTE stack development. I want to put LTE packet details on top of PGM protocol. There is no settings available for PGM protocol to dissect LTE packets. Like for UDP, setting avalable is "Try heuristic LTE-MAC over UDP framing". Is anyone have any idea? Is there any way so that I can use to build LTE frame on top of PGM protocol?</p></div><div id="question-tags" class="tags-container tags">pgm dissector lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '14, 06:08</strong></p><img src="https://secure.gravatar.com/avatar/c489374debe5c5996bfd794fb019a3af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="atul&#39;s gravatar image" /><p>atul<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="atul has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Nov '14, 06:10</p></div></div><div id="comments-container-38044" class="comments-container"></div><div id="comment-tools-38044" class="comment-tools"></div><div class="clear"></div><div id="comment-38044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38045"></span>

<div id="answer-container-38045" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38045-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to modify the source code so that LTE-MAC dissector registers itself in the PGM heuristic table (assuming that you use the same framing protocol than on UDP). Something like:</p><pre><code>--- a/epan/dissectors/packet-mac-lte.c
+++ b/epan/dissectors/packet-mac-lte.c
@@ -7282,6 +7282,7 @@ void proto_reg_handoff_mac_lte(void)
 {
     /* Add as a heuristic UDP dissector */
     heur_dissector_add(&quot;udp&quot;, dissect_mac_lte_heur, proto_mac_lte);
+    heur_dissector_add(&quot;pgm&quot;, dissect_mac_lte_heur, proto_mac_lte);

     /* Look up RLC dissector handle once and for all */
     rlc_lte_handle = find_dissector(&quot;rlc-lte&quot;);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '14, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-38045" class="comments-container"><span id="38088"></span><div id="comment-38088" class="comment"><div id="post-38088-score" class="comment-score"></div><div class="comment-text"><p>Hi pascal, Thank you for your suggestion. I have checked the source code, I think it will work.</p></div><div id="comment-38088-info" class="comment-info"><span class="comment-age">(23 Nov '14, 20:40)</span> atul</div></div><span id="38091"></span><div id="comment-38091" class="comment"><div id="post-38091-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-38091-info" class="comment-info"><span class="comment-age">(24 Nov '14, 00:37)</span> grahamb ♦</div></div></div><div id="comment-tools-38045" class="comment-tools"></div><div class="clear"></div><div id="comment-38045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

