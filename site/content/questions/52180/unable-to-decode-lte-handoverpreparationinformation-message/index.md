+++
type = "question"
title = "Unable to decode LTE HandoverPreparationInformation message"
description = '''Hi, I have created a LUA dissector that dissects a custom protocol. This protocol, among other things, transports a LTE HandoverPreparationInformation message (see 3GPP TS 36.331 version 8.21.0 Release 8, section 10.2.2). The message is well formed, but I can&#x27;t decode it calling any of the Wireshark...'''
date = "2016-05-03T07:40:00Z"
lastmod = "2016-05-03T09:16:00Z"
weight = 52180
keywords = [ "dissector" ]
aliases = [ "/questions/52180" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to decode LTE HandoverPreparationInformation message](/questions/52180/unable-to-decode-lte-handoverpreparationinformation-message)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52180-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have created a LUA dissector that dissects a custom protocol. This protocol, among other things, transports a LTE HandoverPreparationInformation message (see 3GPP TS 36.331 version 8.21.0 Release 8, section 10.2.2).</p><p>The message is well formed, but I can't decode it calling any of the Wireshark dissectors. LTE-RRC and S1AP should be able to decode it (RRC has the lte-rrc.HandoverPreparationInformation_element filter, and S1AP has the s1ap.Source_ToTarget_TransparentContainer filter), but I haven't found the way to call them properly. If I do:</p><pre><code>function GetMessageRRC(buffer,pckinfo)
    local dissector = Dissector.get(&quot;lte-rrc&quot;)
    dissector:call(buffer:tvb(), pckinfo, subtree)
end</code></pre><p>I get an error because the dissector doesn't exist. I have to call lte-rrc.ul.ccch or s1ap, but they expect other messages and don't work.</p><p>Is there any way to call just the lte-rrc.HandoverPreparationInformation_element or s1ap.Source_ToTarget_TransparentContainer part of the dissector? What am I doing wrong?</p><p>Thanks and best regards,</p><p>Eduardo.</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '16, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/d4e531921a0a500817aa02ad570f2e21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EduardoTel&#39;s gravatar image" /><p>EduardoTel<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EduardoTel has no accepted answers">0%</span></p></div></div><div id="comments-container-52180" class="comments-container"></div><div id="comment-tools-52180" class="comment-tools"></div><div class="clear"></div><div id="comment-52180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52181"></span>

<div id="answer-container-52181" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52181-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>the registered name for this message (at least in Wireshark 2.0.x) is: "lte_rrc.handover_prep_info"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-52181" class="comments-container"><span id="52214"></span><div id="comment-52214" class="comment"><div id="post-52214-score" class="comment-score"></div><div class="comment-text"><p>Hi Pascal,</p><p>Thanks for your help, but what I was looking for is a way to call the lte-rrc dissector to dissect only that message. If I do:</p><p>function GetMessageRRC(buffer,pckinfo) local dissector = Dissector.get("lte_rrc.handover_prep_info") dissector:call(buffer:tvb(), pckinfo, subtree) end</p><p>I get a "no such dissector" error message.</p><p>Regards,</p><p>Eduardo.</p></div><div id="comment-52214-info" class="comment-info"><span class="comment-age">(03 May '16, 23:56)</span> EduardoTel</div></div><span id="52225"></span><div id="comment-52225" class="comment"><div id="post-52225-score" class="comment-score"></div><div class="comment-text"><p>Which Wireshark version are you using? The string I gave you is exactly what you are looking for (a dissector registered by name allowing to decode the Handover Preparation Information message)</p><pre><code>register_dissector(&quot;lte_rrc.handover_prep_info&quot;, dissect_lte_rrc_Handover_Preparation_Info, proto_lte_rrc);</code></pre></div><div id="comment-52225-info" class="comment-info"><span class="comment-age">(04 May '16, 06:16)</span> Pascal Quantin</div></div><span id="52230"></span><div id="comment-52230" class="comment"><div id="post-52230-score" class="comment-score"></div><div class="comment-text"><p>I was using Wireshark V1.12.1. With the latest Wireshark version it works without problems.</p><p>Thank you very much for your help and best regards.</p></div><div id="comment-52230-info" class="comment-info"><span class="comment-age">(04 May '16, 08:45)</span> EduardoTel</div></div></div><div id="comment-tools-52181" class="comment-tools"></div><div class="clear"></div><div id="comment-52181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

