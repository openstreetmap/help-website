+++
type = "question"
title = "BER Error while dissecting CDR-DATA in gtp prime DRT packet"
description = '''We have added new dissector to dissect the CDR-DATA present in the data record transfer request (GTP Prime Protocol). We are facing the problem while aligning the information display for one parameter. The expected output is, Frame  |Internet Protocol  | UDP  |_GTP  |_EGSNPDPRecord  - Record type  -...'''
date = "2011-01-20T23:04:00Z"
lastmod = "2011-01-23T03:24:00Z"
weight = 1842
keywords = [ "dissector" ]
aliases = [ "/questions/1842" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [BER Error while dissecting CDR-DATA in gtp prime DRT packet](/questions/1842/ber-error-while-dissecting-cdr-data-in-gtp-prime-drt-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1842-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have added new dissector to dissect the CDR-DATA present in the data record transfer request (GTP Prime Protocol). We are facing the problem while aligning the information display for one parameter. The expected output is, Frame |<em>Internet Protocol |</em> UDP |_GTP |_EGSNPDPRecord - Record type - IMSI ... ... - list of service data |_Change of service condition |_qosInformationNeg - allocation_ret_priority information ( parameter 1) - delay_class_reliability_class information (parameter 2) ... ... - downlink_gbrate information (parameter 11) - uplink_gbrate information (parameter 12)</p><p>To achieve the expected result be have modified the code as below,</p><p>========= CODE Start ========================= static int hf_qoSInformationNeg_allocation_ret_priority = -1; static int hf_qoSInformationNeg_delay_class_reliability_class = -1; static int hf_qoSInformationNeg_peak_throughput_precedence_class = -1; static int hf_qoSInformationNeg_mean_throughput = -1; static int hf_qoSInformationNeg_traffic_class_delivery_order_err_sdu = -1; static int hf_qoSInformationNeg_max_sdu_size = -1; static int hf_qoSInformationNeg_max_uplink_bit_rate = -1; static int hf_qoSInformationNeg_max_downlink_bit_rate = -1; static int hf_qoSInformationNeg_residual_ber_sdu_err_ratio = -1; static int hf_qoSInformationNeg_trans_delay_traffic_handling_prio = -1; static int hf_qoSInformationNeg_downlink_gbrate = -1; static int hf_qoSInformationNeg_uplink_gbrate = -1;</p><p>.......... .....</p><p>static const ber_sequence_t QoSInformationNeg_set[] = { { &amp;hf_qoSInformationNeg_allocation_ret_priority, BER_CLASS_CON, 0, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_delay_class_reliability_class, BER_CLASS_CON, 1, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_peak_throughput_precedence_class, BER_CLASS_CON, 2, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_mean_throughput, BER_CLASS_CON, 3, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_traffic_class_delivery_order_err_sdu, BER_CLASS_CON, 4, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_max_sdu_size, BER_CLASS_CON, 5, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_max_uplink_bit_rate, BER_CLASS_CON, 6, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_max_downlink_bit_rate, BER_CLASS_CON, 7, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_residual_ber_sdu_err_ratio, BER_CLASS_CON, 8, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_trans_delay_traffic_handling_prio, BER_CLASS_CON, 9, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_downlink_gbrate, BER_CLASS_CON, 10, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { &amp;hf_qoSInformationNeg_uplink_gbrate, BER_CLASS_CON, 11, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_alloc_and_ret_priority}, { NULL, 0, 0, 0, NULL } };</p><p>static int dissect_gprschargingdatatypes_QoSInformation(gboolean implicit_tag <em>U_, tvbuff_t <em>tvb <em>U_, int offset _U</em>, asn1_ctx_t</em> actx _U</em>, proto_tree *tree <em>U_, int hf_index _U</em>) {</p><p>offset = dissect_ber_set(implicit_tag, actx, tree, tvb, offset, QoSInformationNeg_set, hf_index, ett_gprschargingdatatypes_qoSInformationNeg);</p><p>return offset; }</p><p>static const ber_sequence_t ChangeOfServiceCondition_sequence[] = { { &amp;hf_gprschargingdatatypes_ratingGroup, BER_CLASS_CON, 1, BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_RatingGroup }, { &amp;hf_gprschargingdatatypes_chargingRuleBaseName, BER_CLASS_CON, 2, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_ChargingRuleBaseName }, { &amp;hf_gprschargingdatatypes_resultCode, BER_CLASS_CON, 3, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_ResultCode }, { &amp;hf_gprschargingdatatypes_localSequenceNumber, BER_CLASS_CON, 4, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_LocalSequenceNumber }, { &amp;hf_gprschargingdatatypes_timeOfFirstUsage, BER_CLASS_CON, 5, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_TimeStamp }, { &amp;hf_gprschargingdatatypes_timeOfLastUsage, BER_CLASS_CON, 6, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_TimeStamp }, { &amp;hf_gprschargingdatatypes_timeUsage, BER_CLASS_CON, 7, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_CallDuration }, { &amp;hf_gprschargingdatatypes_serviceConditionChange, BER_CLASS_CON, 8, BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_ServiceConditionChange }, { &amp;hf_gprschargingdatatypes_qoSInformationNeg, BER_CLASS_CON, 9, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_QoSInformation }, { &amp;hf_gprschargingdatatypes_sgsn_Address, BER_CLASS_CON, 10, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG|BER_FLAGS_NOTCHKTAG, dissect_gprschargingdatatypes_GSNAddress }, { &amp;hf_gprschargingdatatypes_sGSNPLMNIdentifier, BER_CLASS_CON, 11, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_PLMN_Id/<em>dissect_gprschargingdatatypes_SGSNPLMNIdentifier</em>/ }, { &amp;hf_gprschargingdatatypes_datavolumeFBCUplink, BER_CLASS_CON, 12, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_DataVolumeGPRS }, { &amp;hf_gprschargingdatatypes_datavolumeFBCDownlink, BER_CLASS_CON, 13, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_DataVolumeGPRS }, { &amp;hf_gprschargingdatatypes_timeOfReport, BER_CLASS_CON, 14, BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_TimeStamp }, { &amp;hf_gprschargingdatatypes_rATType, BER_CLASS_CON, 15, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_RATType }, { &amp;hf_gprschargingdatatypes_failureHandlingContinue, BER_CLASS_CON, 16, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_FailureHandlingContinue }, { &amp;hf_gprschargingdatatypes_serviceIdentifier, BER_CLASS_CON, 17, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_ServiceIdentifier }, { &amp;hf_gprschargingdatatypes_pSFurnishChargingInformation, BER_CLASS_CON, 18, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_PSFurnishChargingInformation }, { &amp;hf_gprschargingdatatypes_userLocationInformation, BER_CLASS_CON, 20, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_OCTET_STRING }, { &amp;hf_gprschargingdatatypes_eventBasedChargingInformation, BER_CLASS_CON, 21, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_EventBasedChargingInformation }, { &amp;hf_gprschargingdatatypes_timeQuotaMechanism, BER_CLASS_CON, 22, BER_FLAGS_OPTIONAL|BER_FLAGS_IMPLTAG, dissect_gprschargingdatatypes_TimeQuotaMechanism }, { NULL, 0, 0, 0, NULL } };</p><p>static int dissect_gprschargingdatatypes_ChangeOfServiceCondition(gboolean implicit_tag <em>U_, tvbuff_t <em>tvb <em>U_, int offset _U</em>, asn1_ctx_t</em> actx _U</em>, proto_tree *tree <em>U_, int hf_index _U</em>) { offset = dissect_ber_sequence(implicit_tag, actx, tree, tvb, offset, ChangeOfServiceCondition_sequence, hf_index, ett_gprschargingdatatypes_ChangeOfServiceCondition);</p><p>return offset; }</p><pre><code>{ &amp;hf_gprschargingdatatypes_qoSInformationNeg,
  { &quot;qoSInformationNeg&quot;, &quot;gprschargingdatatypes.qoSInformationNeg&quot;,
    FT_NONE, BASE_NONE, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_allocation_ret_priority,
  { &quot;allocation_and_ret_prio&quot;, &quot;gprschargingdatatypes.allocation_and_ret_prio&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_delay_class_reliability_class,
  { &quot;delayAndReliabilityClass&quot;, &quot;gprschargingdatatypes.delayAndReliabilityClass&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_peak_throughput_precedence_class,
  { &quot;peakThroughputAndPrecedClass&quot;, &quot;gprschargingdatatypes.peakThroughputAndPrecedClass&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_mean_throughput,
  { &quot;meanThroughput&quot;, &quot;gprschargingdatatypes.meanThroughput&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_traffic_class_delivery_order_err_sdu,
  { &quot;trafficClassDeliveryOrderAndErrSdu&quot;, &quot;gprschargingdatatypes.trafficClassDeliveryOrderAndErrSdu&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_max_sdu_size,
  { &quot;maxSduSize&quot;, &quot;gprschargingdatatypes.maxSduSize&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_max_uplink_bit_rate,
  { &quot;maxUplinkBitRate&quot;, &quot;gprschargingdatatypes.maxUplinkBitRate&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_max_downlink_bit_rate,
  { &quot;maxDownlinkBitRate&quot;, &quot;gprschargingdatatypes.maxDownlinkBitRate&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_residual_ber_sdu_err_ratio,
  { &quot;residualBERSduErrRatio&quot;, &quot;gprschargingdatatypes.residualBERSduErrRatio&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_trans_delay_traffic_handling_prio,
  { &quot;transDelayAndTrafficHandlingPriority&quot;, &quot;gprschargingdatatypes.transDelayAndTrafficHandlingPriority&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_downlink_gbrate,
  { &quot;downlinkGBRate&quot;, &quot;gprschargingdatatypes.downlinkGBRate&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},
{ &amp;hf_qoSInformationNeg_uplink_gbrate,
  { &quot;uplinkGBRate&quot;, &quot;gprschargingdatatypes.uplinkGBRate&quot;,
    FT_UINT32, BASE_DEC, NULL, 0,
    NULL, HFILL }},</code></pre><p>========= CODE End =========================</p><p>With above changes it displays the label "qosInformationNeg" correctly but while dissecting the parameters it throws an error in dissect_ber_set as below,</p><p>BER Error: Unknown field in SET class:UNIVERSAL(0) tag:1 Expert Info (Warn/Malformed): BER Error: Unknown field in SET Message: BER Error: Unknown field in SET BER Error: length:11 longer than tvb_length_remaining:10 Expert Info (Warn/Malformed): BER Error length</p><p>Any idea what might be going wrong?</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '11, 23:04</strong></p><img src="https://secure.gravatar.com/avatar/1c367d93f2020c80c309ef1090c9af26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suresh%20panara&#39;s gravatar image" /><p>suresh panara<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suresh panara has no accepted answers">0%</span></p></div></div><div id="comments-container-1842" class="comments-container"></div><div id="comment-tools-1842" class="comment-tools"></div><div class="clear"></div><div id="comment-1842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1887"></span>

<div id="answer-container-1887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1887-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all if this is a dissector for standard CDR records transfered in GTP' it would be better to do this trough bugzilla and have the dissector in the released Wireshark in that way you would getr the support of the Wireshark developers. I would use as2wrs to generate the asn1 dissector and call that from packet-gtp.c. ": length:11 longer than tvb_length_remaining" it looks like all the data is not in the tvb. Regards Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '11, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-1887" class="comments-container"></div><div id="comment-tools-1887" class="comment-tools"></div><div class="clear"></div><div id="comment-1887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

