+++
type = "question"
title = "3gpp Compliance Chart"
description = '''Hi, Actually I want that how to detect wireshark compliance of 3gpp release. Currently I am checking the low-level dissectors code(e.g, packet-gtpv2.c) vs 3gpp release(e.g, integer number ie.) and assuming the compliance. But I am wondering from development perspective any docs are available so that...'''
date = "2017-02-09T00:24:00Z"
lastmod = "2017-02-09T01:29:00Z"
weight = 59269
keywords = [ "release", "version2.2.0", "3gpp", "releasenotes", "3gpp2" ]
aliases = [ "/questions/59269" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [3gpp Compliance Chart](/questions/59269/3gpp-compliance-chart)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59269-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Actually I want that how to detect wireshark compliance of 3gpp release. Currently I am checking the low-level dissectors code(e.g, packet-gtpv2.c) vs 3gpp release(e.g, integer number ie.) and assuming the compliance. But I am wondering from development perspective any docs are available so that one can understand the release-compliance. Is anywhere it's mentioned in wireshark release note!!!TIA.</p></div><div id="question-tags" class="tags-container tags">release version2.2.0 3gpp releasenotes 3gpp2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '17, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p>Abhisek<br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div></div><div id="comments-container-59269" class="comments-container"></div><div id="comment-tools-59269" class="comment-tools"></div><div class="clear"></div><div id="comment-59269-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59272"></span>

<div id="answer-container-59272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59272-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sorry there is no record of which 3GPP release a dissector is "compliant" with except for the ASN1 based ones where you can see which ASN1 document was used to generate it. The problem is that dissectors gets updated with the stuff the patch submitter chose to make code for which may just be a subset of new stuff in a particular release. If you do a check it would be helpful if you let us know the result.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '17, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-59272" class="comments-container"><span id="59273"></span><div id="comment-59273" class="comment"><div id="post-59273-score" class="comment-score"></div><div class="comment-text"><p>So you mean the version mentioned in the dissectors file are not correct always. (For example, in packet-gtpv2.c in wireshark2.2.2, * Ref: 3GPP TS 29.274 version 11.1.0 Release 11 ETSI TS 129 274 V8.1.1 (2009-04)) is not exactly correct.</p></div><div id="comment-59273-info" class="comment-info"><span class="comment-age">(09 Feb '17, 02:10)</span> Abhisek</div></div><span id="59274"></span><div id="comment-59274" class="comment"><div id="post-59274-score" class="comment-score">1</div><div class="comment-text"><p>Yes, I'd say GTPv2 dissection is pretty much up to date.</p><p>At the end you can see which IE's are not dissected <code> {GTPV2_IE_INTEGER_NUMBER, dissect_gtpv2_integer_number}, / 187, 8.118 Integer Number /      / 188, 8.119 Millisecond Time Stamp /      / 189, 8.120 Monitoring Event Information /      / 190, 8.121 ECGI List /      / 191, 8.122 Remote UE Context /      / 192, 8.123 Remote User ID /      / 193, 8.124 Remote UE IP Information / {GTPV2_IE_CIOT_OPT_SUPPORT_IND, dissect_gtpv2_ciot_opt_support_ind}, / 194, 8.125 CIoT Optimizations Support Indication /      / 195, 8.126 SCEF PDN Connection /      / 196, 8.127 Header Compression Configuration / {GTPV2_IE_EXTENDED_PCO, dissect_gtpv2_pco},  / 197, 8.128 Extended Protocol Configuration Options (ePCO) /      / 198, 8.129 Serving PLMN Rate Control /</code></code></p></div><div id="comment-59274-info" class="comment-info"><span class="comment-age">(09 Feb '17, 03:27)</span> Anders ♦</div></div><span id="59278"></span><div id="comment-59278" class="comment"><div id="post-59278-score" class="comment-score"></div><div class="comment-text"><p>got it. but still the IEs implementation is not open for development...:).</p></div><div id="comment-59278-info" class="comment-info"><span class="comment-age">(09 Feb '17, 04:47)</span> Abhisek</div></div><span id="59284"></span><div id="comment-59284" class="comment"><div id="post-59284-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but still the IEs implementation is not open for development...:).</p></blockquote><p>I'm not sure what you mean, if you want to add dissection of these IEs you are more than welcome. If you are asking if someone is working on it - not as far as I'm aware. This is opensource and people do work as they see fit and their spare time permits.</p></div><div id="comment-59284-info" class="comment-info"><span class="comment-age">(09 Feb '17, 05:32)</span> Anders ♦</div></div></div><div id="comment-tools-59272" class="comment-tools"></div><div class="clear"></div><div id="comment-59272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

