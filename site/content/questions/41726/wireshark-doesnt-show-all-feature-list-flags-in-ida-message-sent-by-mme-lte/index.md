+++
type = "question"
title = "Wireshark doesn&#x27;t show all feature list flags in IDA message sent by MME (LTE)"
description = '''In LTE environment there is the IDA (Insert Subscriber Data answer) message (Diameter protocol) that is sent by MME to HSS as reply to IDR message. The version 1.12.1 of Wireshark doesn&#x27;t display the &#x27;PCSCF restoration&#x27; feature list flag in IDA message in pcap file although MME is sending it (MME ge...'''
date = "2015-04-23T05:44:00Z"
lastmod = "2015-04-23T06:48:00Z"
weight = 41726
keywords = [ "wireshark" ]
aliases = [ "/questions/41726" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't show all feature list flags in IDA message sent by MME (LTE)](/questions/41726/wireshark-doesnt-show-all-feature-list-flags-in-ida-message-sent-by-mme-lte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41726-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In LTE environment there is the IDA (Insert Subscriber Data answer) message (Diameter protocol) that is sent by MME to HSS as reply to IDR message. The version 1.12.1 of Wireshark doesn't display the 'PCSCF restoration' feature list flag in IDA message in pcap file although MME is sending it (MME gets this request flag properly in IDR message and replies correctly as feature is enabled in MME). I see also that IDR message doesn't contain all feature flag list bits (feature list 1 &amp; 2). Can anyone help on this one ? Thx</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '15, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/a32939e6d64be21c252d9e87c4f18e8a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="costas&#39;s gravatar image" /><p>costas<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="costas has no accepted answers">0%</span></p></div></div><div id="comments-container-41726" class="comments-container"><span id="41727"></span><div id="comment-41727" class="comment"><div id="post-41727-score" class="comment-score"></div><div class="comment-text"><p>Can you try the current version, 1.12.4, or a development build, 1.99.5?</p></div><div id="comment-41727-info" class="comment-info"><span class="comment-age">(23 Apr '15, 06:02)</span> grahamb ♦</div></div><span id="41729"></span><div id="comment-41729" class="comment"><div id="post-41729-score" class="comment-score"></div><div class="comment-text"><p>That's currently not implemented for feature list 2 only bit 0 and 1 is implemented.(packet-diameter_3gpp.c AVP 630 ref TS 29.272 11.7.0)</p></div><div id="comment-41729-info" class="comment-info"><span class="comment-age">(23 Apr '15, 07:26)</span> Anders ♦</div></div><span id="41732"></span><div id="comment-41732" class="comment"><div id="post-41732-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders, Yes, this is what I also see. Only two bits (0 and 1) are set for FeatureList2 , for SMS in SGSN and MME. Do you know if there are plans for implementing the rest bits according to latest 3GPP doc? Thank you. Kostas</p></div><div id="comment-41732-info" class="comment-info"><span class="comment-age">(23 Apr '15, 08:09)</span> costas</div></div></div><div id="comment-tools-41726" class="comment-tools"></div><div class="clear"></div><div id="comment-41726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41728"></span>

<div id="answer-container-41728" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>We do not support the dissection of those flags yet. Could you fill an enhancement request on <a href="https://bugs.wireshark.org/bugzilla/">Bugzilla</a> witha pcap file attached so that we can verify the implementation?</p><p>Edit: when looking at 3GPP 29.272 release 13.1.0, I can only see bit 0 being used in IDA Flags IE (chapter 7.3.47). Could you indicate which specification describes this P-CSCF Restoration flag? I can only find it in IDR Flags IE.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '15, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '15, 07:16</p></div></div><div id="comments-container-41728" class="comments-container"><span id="41731"></span><div id="comment-41731" class="comment"><div id="post-41731-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal, Thank you for your answer. First of all the P-CSCF restoration procedure is described in 3GPP TS 23.380 subcaluse 5.4. In chapter 7.3.10 regarding the IDR flag bits you can see that bit 8 refers to PCSCF restoration. Furthermore in IDA message the AVP supported features may contain two feature lists, one with list ID 1 and one with ID 2. The feature bit 16 of the feature list 2 is regarding the PCSCF restoration as you can see also in table 7.3.10/2 of the 29272 3GPP doc v13.10. Yes, I could open an ER on Bugzilla attaching also the requested pcap file. Thank you very much once more. Kostas</p></div><div id="comment-41731-info" class="comment-info"><span class="comment-age">(23 Apr '15, 08:06)</span> costas</div></div></div><div id="comment-tools-41728" class="comment-tools"></div><div class="clear"></div><div id="comment-41728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

