+++
type = "question"
title = "How to decode the RRC-Container in the s1ap Handover preparation message"
description = '''Hi, how do I decode the RRC-Container IE in the S1AP Handover preparation message  (inter RAT Handover) Paul'''
date = "2014-04-16T05:22:00Z"
lastmod = "2014-04-16T07:41:00Z"
weight = 31880
keywords = [ "rrc-container" ]
aliases = [ "/questions/31880" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode the RRC-Container in the s1ap Handover preparation message](/questions/31880/how-to-decode-the-rrc-container-in-the-s1ap-handover-preparation-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31880-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>how do I decode the RRC-Container IE in the S1AP Handover preparation message (inter RAT Handover)</p><p>Paul</p></div><div id="question-tags" class="tags-container tags">rrc-container</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '14, 05:22</strong></p><img src="https://secure.gravatar.com/avatar/4f2792912d6f7f8d3856f30ca73a7f4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulTee&#39;s gravatar image" /><p>PaulTee<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulTee has no accepted answers">0%</span></p></div></div><div id="comments-container-31880" class="comments-container"><span id="31890"></span><div id="comment-31890" class="comment"><div id="post-31890-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders,</p><p>thanks for your response, I have tried this and can see that the IE SourceRNC-ToTargetRNC-TransparentContainer is decoded with this setting.</p><p>But what I need next is actually the decode of the IE:<br />
rRC-Container</p><p>please see below for an extract (which I should have included in my original request)</p><p>Paul.</p><p>ProtocolIE-Field id: id-Source-ToTarget-TransparentContainer (104) criticality: reject (0) value Source-ToTarget-TransparentContainer: 00a069033a00009a86555aa0d4aad511490608900030002b... SourceRNC-ToTargetRNC-TransparentContainer rRC-Container: 033a00009a86555aa0d4aad511490608900030002b142128... numberOfIuInstances: 1 relocationType: ue-involved (1) targetCellId: 393335 iE-Extensions: 1 item Item 0 ProtocolExtensionField id: id-UE-History-Information (200) criticality: ignore (1) extensionValue UE-History-Information: 000032f549000050018003e6</p></div><div id="comment-31890-info" class="comment-info"><span class="comment-age">(16 Apr '14, 07:55)</span> PaulTee</div></div></div><div id="comment-tools-31880" class="comment-tools"></div><div class="clear"></div><div id="comment-31880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31887"></span>

<div id="answer-container-31887" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31887-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>At lest on trunk enable the (edit-&gt;preferences-&gt;protocols-&gt;s1ap) s1ap preference "Dissect transparent container"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '14, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span> </br></p></div></div><div id="comments-container-31887" class="comments-container"><span id="31891"></span><div id="comment-31891" class="comment"><div id="post-31891-score" class="comment-score"></div><div class="comment-text"><p>ProtocolIE-Field id: id-Source-ToTarget-TransparentContainer (104) criticality: reject (0) value</p><pre><code>      Source-ToTarget-TransparentContainer:</code></pre><p>00a069033a00009a86555aa0d4aad511490608900030002b...</p><pre><code>          SourceRNC-ToTargetRNC-TransparentContainer

              rRC-Container: &lt;&lt;-- this IE</code></pre><p>033a00009a86555aa0d4aad511490608900030002b142128...</p><pre><code>              numberOfIuInstances: 1

              relocationType: ue-involved (1)
              targetCellId:393335</code></pre></div><div id="comment-31891-info" class="comment-info"><span class="comment-age">(16 Apr '14, 08:00)</span> PaulTee</div></div><span id="31893"></span><div id="comment-31893" class="comment"><div id="post-31893-score" class="comment-score"></div><div class="comment-text"><p>I think I would need to see the complete message. In the code there is this</p><p><code>     switch(message_type){         case INITIATING_MESSAGE:         / 9.2.1.7 Source eNB to Target eNB Transparent Container /             dissect_lte_rrc_HandoverPreparationInformation_PDU(parameter_tvb, actx-&gt;pinfo, subtree, NULL);             break;         case SUCCESSFUL_OUTCOME:         / 9.2.1.7 Source eNB to Target eNB Transparent Container /             dissect_lte_rrc_HandoverCommand_PDU(parameter_tvb, actx-&gt;pinfo, subtree, NULL);             break;         default:             break;     }</code></p><p>So if it's not one of those message types it's not covered.</p></div><div id="comment-31893-info" class="comment-info"><span class="comment-age">(16 Apr '14, 08:40)</span> Anders ♦</div></div></div><div id="comment-tools-31887" class="comment-tools"></div><div class="clear"></div><div id="comment-31887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

