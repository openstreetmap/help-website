+++
type = "question"
title = "3GPP PCAP asn1"
description = '''Wireshark uses 3GPP TS 25.453 V11.0.0 specification for PCAP. I would like to use 3GPP TS 25.453 V9.1.0 for Wireshark decoding. Is it possible to rebuild Wireshark with a change of protocol Spec. How can I di this. Thank you in advance'''
date = "2017-10-24T04:44:00Z"
lastmod = "2017-10-24T07:27:00Z"
weight = 64148
keywords = [ "wireshark" ]
aliases = [ "/questions/64148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [3GPP PCAP asn1](/questions/64148/3gpp-pcap-asn1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark uses 3GPP TS 25.453 V11.0.0 specification for PCAP. I would like to use 3GPP TS 25.453 V9.1.0 for Wireshark decoding. Is it possible to rebuild Wireshark with a change of protocol Spec. How can I di this.</p><p>Thank you in advance</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '17, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/98c95d4003dec700239fba3670a70612?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oaa&#39;s gravatar image" /><p>oaa<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oaa has no accepted answers">0%</span></p></div></div><div id="comments-container-64148" class="comments-container"></div><div id="comment-tools-64148" class="comment-tools"></div><div class="clear"></div><div id="comment-64148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="64155"></span>

<div id="answer-container-64155" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64155-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure you need an earlier version? Most of the time it's backwards compatible. If you need to rebuild you could check the history to see if the dissector was built with the version you require. If not you need to replace the asn1 files under dissectors/asn1/pcap with the version you want and adjust the .cnf file to fit that version. Then rebuild the dissector and rebuild wireshark. The method depends a bit on the OS you want to build for.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '17, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-64155" class="comments-container"><span id="64177"></span><div id="comment-64177" class="comment"><div id="post-64177-score" class="comment-score"></div><div class="comment-text"><p>Anders, thank you for your help.</p><p>Unfortunately PCAP is encoded in Aligned Packed Encoding Rules (APER) ASN1.1 that is very sensitive to specification Version.</p><p>What is the "<strong>.cnf</strong>" file purpose?</p><p>Thank you in advance</p></div><div id="comment-64177-info" class="comment-info"><span class="comment-age">(25 Oct '17, 00:50)</span> oaa</div></div></div><div id="comment-tools-64155" class="comment-tools"></div><div class="clear"></div><div id="comment-64155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

