+++
type = "question"
title = "Wireshark 2 missing option to &quot;Try to decode RTP outside of conversation&quot;?"
description = '''I use Wireshark mostly for reading SIP traffic and troubleshooting VoIP networks. In previous versions, the option (under Edit &amp;gt; Preferences &amp;gt; Protocols &amp;gt; RTP) &quot;Try to decode RTP outside of conversations&quot; was useful in cases in which sufficient SIP signaling is missing from the packet captu...'''
date = "2016-03-10T05:52:00Z"
lastmod = "2016-03-10T06:38:00Z"
weight = 50795
keywords = [ "udp", "sip", "rtp", "protocols", "preferences" ]
aliases = [ "/questions/50795" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2 missing option to "Try to decode RTP outside of conversation"?](/questions/50795/wireshark-2-missing-option-to-try-to-decode-rtp-outside-of-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50795-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use Wireshark mostly for reading SIP traffic and troubleshooting VoIP networks. In previous versions, the option (under Edit &gt; Preferences &gt; Protocols &gt; RTP) "Try to decode RTP outside of conversations" was useful in cases in which sufficient SIP signaling is missing from the packet capture. Without that option checked, RTP is represented as UDP packets with unknown data payload.</p><p>In version 2 of Wireshark this option is missing, at least under RTP protocol preferences. Is it somewhere else? Is there another way to replicate this behavior?</p><p>(I am using both versions 1.12.10 and 2.0.2.)</p></div><div id="question-tags" class="tags-container tags">udp sip rtp protocols preferences</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '16, 05:52</strong></p><img src="https://secure.gravatar.com/avatar/2b717cab9fa05d4810e050feb58962ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael_Lindsey&#39;s gravatar image" /><p>Michael_Lindsey<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael_Lindsey has no accepted answers">0%</span></p></div></div><div id="comments-container-50795" class="comments-container"></div><div id="comment-tools-50795" class="comment-tools"></div><div class="clear"></div><div id="comment-50795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50796"></span>

<div id="answer-container-50796" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50796-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Starting from Wireshark 2.0, this option is replaced by the activation of RTP heuristic dissectors. Go to Analyze -&gt; Enabled Protocols -&gt; RTP and activate rtp_udp checkbox</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '16, 06:38</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Mar '16, 06:38</p></div></div><div id="comments-container-50796" class="comments-container"><span id="50797"></span><div id="comment-50797" class="comment"><div id="post-50797-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I have enabled it and will try that out.</p></div><div id="comment-50797-info" class="comment-info"><span class="comment-age">(10 Mar '16, 07:36)</span> Michael_Lindsey</div></div></div><div id="comment-tools-50796" class="comment-tools"></div><div class="clear"></div><div id="comment-50796-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

