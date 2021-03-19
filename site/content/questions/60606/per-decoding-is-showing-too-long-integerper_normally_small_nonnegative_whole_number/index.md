+++
type = "question"
title = "Per decoding is showing &quot;too long integer(per_normally_small_nonnegative_whole_number)&quot;"
description = '''Hi, at the time of decoding some sequence (the function &quot;dissect_per_sequence&quot; is called), we are getting  the error: &quot;too long integer(per_normally_small_nonnegative_whole_number)&quot;. The IEs with  &quot;ASN1_EXTENSION_ROOT,ASN1_OPTIONAL and ASN1_NOT_OPTIONAL&quot; are dissecting properly. after those dissecti...'''
date = "2017-04-06T03:05:00Z"
lastmod = "2017-04-06T03:05:00Z"
weight = 60606
keywords = [ "error", "dissector", "packet-per.c", "per", "developer" ]
aliases = [ "/questions/60606" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Per decoding is showing "too long integer(per\_normally\_small\_nonnegative\_whole\_number)"](/questions/60606/per-decoding-is-showing-too-long-integerper_normally_small_nonnegative_whole_number)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60606-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, at the time of decoding some sequence (the function "dissect_per_sequence" is called), we are getting the error: "too long integer(per_normally_small_nonnegative_whole_number)". The IEs with "ASN1_EXTENSION_ROOT,ASN1_OPTIONAL and ASN1_NOT_OPTIONAL" are dissecting properly. after those dissection the error is coming.</p><p>The sequence has extension marker (the ellipses or ...) in PROP_IEs.asn file. the dissection of IEs before (ellipses or ...) is fine. after that Malformed packet with "too long integer(per_normally_small_nonnegative_whole_number)" is shown.</p><p>snapshot of PROP_IEs.asn:</p><pre><code>pD-BearerDataList              PD-BearerDataList           OPTIONAL,
pD-FirstUeMeasurementDataItems PD-UeMeasurementDataListing OPTIONAL,
pD-LastUeMeasurementDataItems  PD-UeMeasurementDataListing OPTIONAL,
...,
measDataNotAvailable           MeasDataNotAvailable        OPTIONAL,
rrcEstablishmentReason         RrcEstablishmentCause       OPTIONAL,</code></pre><p>snapshot of packet-s1ap.c</p><pre><code>{ &amp;hf_s1ap_pD_BearerDataList, ASN1_EXTENSION_ROOT, ASN1_OPTIONAL, dissect_s1ap_PCMD_BearerDataList },
{ &amp;hf_s1ap_pD_FirstUeMeasurementDataItems, ASN1_EXTENSION_ROOT, ASN1_OPTIONAL, dissect_s1ap_UeMeasurementDataListing },
{ &amp;hf_s1ap_pD-LastUeMeasurementDataItems, ASN1_EXTENSION_ROOT, ASN1_OPTIONAL, dissect_s1ap_UeMeasurementDataListing },
{ &amp;hf_s1ap_measDataNotAvailable, ASN1_NOT_EXTENSION_ROOT, ASN1_OPTIONAL, dissect_s1ap_MeasDataNotPresent },
{ &amp;hf_s1ap_rrcEstablishmentReason, ASN1_NOT_EXTENSION_ROOT, ASN1_OPTIONAL, dissect_s1ap_RrcEstablishmentCause },</code></pre><p>So my question is regarding dissection of IEs/Components after extension marker (Ellipses or ...). How dissection happens? how to calculate number of extensions? why this error is coming? Any help specially from developer are welcome.</p></div><div id="question-tags" class="tags-container tags">error dissector packet-per.c per developer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '17, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p>Abhisek<br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Apr '17, 03:22</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-60606" class="comments-container"><span id="60645"></span><div id="comment-60645" class="comment"><div id="post-60645-score" class="comment-score"></div><div class="comment-text"><p>According to my understanding of packet-per.c, the dissect_per_sequence function dissected in two stage. Stage 1: components before extension marker.</p><ol><li>first calculate components with NOT(ASN1_NOT_EXTENSION_ROOT) and ASN1_OPTIONAL,</li><li>then check optional field flag for each components calculated earlier step and make an arrary of bits(0 or 1 depends on presence of optional field flag),</li><li>then call dissector function for components whose bit value is 1 in the array mentioned above.</li></ol><p>Upto this part is fine. the dissection is fine with respect to sequence. Stage 2:Components after extension marker.</p><ol><li>dissect_per_normally_small_nonnegative_whole_number is called. and here my dissection is getting failed with error of Malformed packet and error message "too long integer(per_normally_small_nonnegative_whole_number)".</li></ol><p>I don't know dissection part after that. Is any developer there, who can help me out.</p></div><div id="comment-60645-info" class="comment-info"><span class="comment-age">(07 Apr '17, 04:49)</span> Abhisek</div></div></div><div id="comment-tools-60606" class="comment-tools"></div><div class="clear"></div><div id="comment-60606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

