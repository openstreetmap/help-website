+++
type = "question"
title = "Problem in displaying/printing a predefined string as per packet in the tree."
description = '''Hello, I am facing a problem in displaying the predefined string in the tree at a specific place. Below is the code using which I want to display the specific predefined string as per its packet info. The code below corresponds to the failure messages which I want to print at a specific place:  cons...'''
date = "2014-05-12T04:34:00Z"
lastmod = "2014-05-12T04:34:00Z"
weight = 32723
keywords = [ "dissector", "s1ap" ]
aliases = [ "/questions/32723" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem in displaying/printing a predefined string as per packet in the tree.](/questions/32723/problem-in-displayingprinting-a-predefined-string-as-per-packet-in-the-tree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32723-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am facing a problem in displaying the predefined string in the tree at a specific place. Below is the code using which I want to display the specific predefined string as per its packet info.</p><p>The code below corresponds to the failure messages which I want to print at a specific place:</p><pre><code>    const value_string s1ap_CauseRadioNetwork_vals[] = {
  {   0, &quot;unspecified&quot; },
  {   1, &quot;tx2relocoverall-expiry&quot; },
  {   2, &quot;successful-handover&quot; },
  {   3, &quot;release-due-to-eutran-generated-reason&quot; },
  {   4, &quot;handover-cancelled&quot; },
  {   5, &quot;partial-handover&quot; },
  {   6, &quot;ho-failure-in-target-EPC-eNB-or-target-system&quot; },
  {   7, &quot;ho-target-not-allowed&quot; },
  {   8, &quot;tS1relocoverall-expiry&quot; },
  {   9, &quot;tS1relocprep-expiry&quot; },
  {  10, &quot;cell-not-available&quot; },
  {  11, &quot;unknown-targetID&quot; },
  {  12, &quot;no-radio-resources-available-in-target-cell&quot; },
  {  13, &quot;unknown-mme-ue-s1ap-id&quot; },
  {  14, &quot;unknown-enb-ue-s1ap-id&quot; },
  {  15, &quot;unknown-pair-ue-s1ap-id&quot; },
  {  16, &quot;handover-desirable-for-radio-reason&quot; },
  {  17, &quot;time-critical-handover&quot; },
  {  18, &quot;resource-optimisation-handover&quot; },
  {  19, &quot;reduce-load-in-serving-cell&quot; },
  {  20, &quot;user-inactivity&quot; },
  {  21, &quot;radio-connection-with-ue-lost&quot; },
  {  22, &quot;load-balancing-tau-required&quot; },
  {  23, &quot;cs-fallback-triggered&quot; },
  {  24, &quot;ue-not-available-for-ps-service&quot; },
  {  25, &quot;radio-resources-not-available&quot; },
  {  26, &quot;failure-in-radio-interface-procedure&quot; },
  {  27, &quot;invalid-qos-combination&quot; },
  {  28, &quot;interrat-redirection&quot; },
  {  29, &quot;interaction-with-other-procedure&quot; },
  {  30, &quot;unknown-E-RAB-ID&quot; },
  {  31, &quot;multiple-E-RAB-ID-instances&quot; },
  {  32, &quot;encryption-and-or-integrity-protection-algorithms-not-supported&quot; },
  {  33, &quot;s1-intra-system-handover-triggered&quot; },
  {  34, &quot;s1-inter-system-handover-triggered&quot; },
  {  35, &quot;x2-handover-triggered&quot; },
  {  36, &quot;redirection-towards-1xRTT&quot; },
  {  37, &quot;not-supported-QCI-value&quot; },
  {  38, &quot;invalid-CSG-Id&quot; },
  { 0, NULL }
};
static value_string_ext s1ap_CauseRadioNetwork_vals_ext = VALUE_STRING_EXT_INIT(s1ap_CauseRadioNetwork_vals);

static int
dissect_s1ap_CauseRadioNetwork(tvbuff_t *tvb _U_, int offset _U_, asn1_ctx_t *actx _U_, proto_tree *tree _U_, int hf_index _U_) {
  offset = dissect_per_enumerated(tvb, offset, actx, tree, hf_index,
                                     36, NULL, TRUE, 3, &amp;CauseRadio);

  return offset;
}</code></pre><p>Below in proto_item_append_text() function, in its cause field I want to display it :</p><pre><code>    static void
dissect_s1ap(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    proto_item  *s1ap_item = NULL;
    proto_tree  *s1ap_tree = NULL;

    /* make entry in the Protocol column on summary display */
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;S1AP&quot;);

    /* create the s1ap protocol tree */
s1ap_item = proto_tree_add_item(tree, proto_s1ap, tvb, 0, -1, ENC_NA);
s1ap_tree = proto_item_add_subtree(s1ap_item, ett_s1ap);

dissect_S1AP_PDU_PDU(tvb, pinfo, s1ap_tree, NULL);
proto_item_append_text(s1ap_item, &quot;, Event-Message:%s ,Result:%s, Cause:%s &quot;,val_to_str_ext(ProcedureCode, &amp;s1ap_ProcedureCode_vals_ext,
                    &quot;unknown message&quot;),val_to_str(S1AP_PDU,s1ap_S1AP_PDU_vals, &quot;unknown&quot;),val_to_str(CauseRadio,s1ap_CauseRadioNetwork_vals, &quot;unknown&quot;));

}</code></pre><p>Need help urgently,</p><p>Thanks in advance,</p><p>Regards,</p><p>Ankur</p></div><div id="question-tags" class="tags-container tags">dissector s1ap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '14, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/5de132d51e4e183bf230804f938b987c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankur92&#39;s gravatar image" /><p>ankur92<br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankur92 has no accepted answers">0%</span></p></div></div><div id="comments-container-32723" class="comments-container"><span id="32724"></span><div id="comment-32724" class="comment"><div id="post-32724-score" class="comment-score"></div><div class="comment-text"><p>what exactly is "the problem you are facing" ?</p></div><div id="comment-32724-info" class="comment-info"><span class="comment-age">(12 May '14, 05:25)</span> Bill Meier ♦♦</div></div><span id="32727"></span><div id="comment-32727" class="comment"><div id="post-32727-score" class="comment-score"></div><div class="comment-text"><p>Hello Sir,</p><p>I need to sort out all the failure events and then I need to display its cause hence I want to display the s1ap_CauseRadioNetwork_vals strings in the cause as the failures here are due to them only. So, what is the procedure to print the corresponding cause to the failure.</p><p>I am not able to get any clue about how to print them also I have an issue regarding printing the failures due to NAS which is located in other file packet-nas_eps.c</p><p>It would be very helpful if you can help me out.</p><p>Regards, Ankur</p></div><div id="comment-32727-info" class="comment-info"><span class="comment-age">(12 May '14, 06:09)</span> ankur92</div></div><span id="32730"></span><div id="comment-32730" class="comment"><div id="post-32730-score" class="comment-score"></div><div class="comment-text"><p>What is going wrong with the code, it looks kind of ok if CauseRadio contains a valid cause.</p></div><div id="comment-32730-info" class="comment-info"><span class="comment-age">(12 May '14, 07:33)</span> Anders ♦</div></div><span id="32735"></span><div id="comment-32735" class="comment"><div id="post-32735-score" class="comment-score"></div><div class="comment-text"><p>Ankur,</p><p>The code in trunk shows the cause type and value in the Info column. There is a copy/paste error at the moment where RadioNetwork causes are incorrectly looking up s1ap_CauseRadioNetwork_vals, but I will try to check in my fix for this tonight.</p><p>Also, did you see the example code I pasted into your other query about the NAS reasons? We currently show (in the Info column) the codes for Detach, I can check in the change I described in your other question if it works for you.</p></div><div id="comment-32735-info" class="comment-info"><span class="comment-age">(12 May '14, 10:38)</span> MartinM</div></div><span id="32746"></span><div id="comment-32746" class="comment"><div id="post-32746-score" class="comment-score"></div><div class="comment-text"><p>Hey Martin,</p><p>Thanks for the help in NAS part of query. Also, I need your help to add a string to each and every cause like for Network Failure I need to display the following "Causes related to PLMN specific network failures and congestion / Authentication Failures) This cause is sent to the MS if the MSC cannot service an MS generated request because of PLMN failures, e.g. problems in MAP."</p><p>I need this to be printed as first text in the S1 Application Protocol.</p></div><div id="comment-32746-info" class="comment-info"><span class="comment-age">(12 May '14, 23:50)</span> ankur92</div></div></div><div id="comment-tools-32723" class="comment-tools"></div><div class="clear"></div><div id="comment-32723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

