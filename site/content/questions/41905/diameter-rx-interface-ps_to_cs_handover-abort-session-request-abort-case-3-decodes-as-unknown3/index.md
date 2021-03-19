+++
type = "question"
title = "Diameter Rx Interface - PS_TO_CS_Handover - Abort Session Request Abort Case 3 decodes as Unknown(3)."
description = '''Greetings, Seems Wireshark Version 1.12.4 has issue decoding Abort Session Request Abort Cause (Rx Reference Point). How to Fix? Decode: AVP: Abort-Cause(500) l=16 f=VM- vnd=TGPP val=Unknown (3) Value 3 is: PS_TO_CS_HANDOVER (3) This value is used when the bearer has been deactivated due to PS to CS...'''
date = "2015-04-27T23:02:00Z"
lastmod = "2015-05-18T04:24:00Z"
weight = 41905
keywords = [ "diameter", "pcrf", "rx", "cscf" ]
aliases = [ "/questions/41905" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Diameter Rx Interface - PS\_TO\_CS\_Handover - Abort Session Request Abort Case 3 decodes as Unknown(3).](/questions/41905/diameter-rx-interface-ps_to_cs_handover-abort-session-request-abort-case-3-decodes-as-unknown3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41905-score" class="post-score" title="current number of votes">0</div><span id="post-41905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>Seems Wireshark Version 1.12.4 has issue decoding Abort Session Request Abort Cause (Rx Reference Point).</p><p>How to Fix?</p><p>Decode: AVP: Abort-Cause(500) l=16 f=VM- vnd=TGPP <strong>val=Unknown (3)</strong></p><p>Value 3 is:</p><p>PS_TO_CS_HANDOVER (3) This value is used when the bearer has been deactivated due to PS to CS handover.</p><p>Reference: ETSI TS 129 214 V11.10.0 (2013-09) 5.3.1 Abort-Cause AVP</p><p>The Abort-Cause AVP (AVP code 500) is of type Enumerated, and determines the cause of an abort session request (ASR) or of a RAR indicating a bearer release. The following values are defined:</p><p>BEARER_RELEASED (0) This value is used when the bearer has been deactivated as a result from normal signalling handling. For GPRS the bearer refers to the PDP Context.</p><p>INSUFFICIENT_SERVER_RESOURCES (1) This value is used to indicate that the server is overloaded and needs to abort the session.</p><p>INSUFFICIENT_BEARER_RESOURCES (2) This value is used when the bearer has been deactivated due to insufficient bearer resources at a transport gateway (e.g. GGSN for GPRS).</p><p><strong>PS_TO_CS_HANDOVER (3) This value is used when the bearer has been deactivated due to PS to CS handover.</strong></p><p>SPONSORED_DATA_CONNECTIVITY_ DISALLOWED (4) This value is used in the ASR when the PCRF needs to initiates the AF session termination due to the operator policy (e.g. disallowing the UE accessing the sponsored data connectivity in the roaming case).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-pcrf" rel="tag" title="see questions tagged &#39;pcrf&#39;">pcrf</span> <span class="post-tag tag-link-rx" rel="tag" title="see questions tagged &#39;rx&#39;">rx</span> <span class="post-tag tag-link-cscf" rel="tag" title="see questions tagged &#39;cscf&#39;">cscf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Apr '15, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/03f2f27531c964e2d1e381c2bfa207c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DazzaS&#39;s gravatar image" /><p><span>DazzaS</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DazzaS has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Apr '15, 23:10</strong> </span></p></div></div><div id="comments-container-41905" class="comments-container"></div><div id="comment-tools-41905" class="comment-tools"></div><div class="clear"></div><div id="comment-41905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41909"></span>

<div id="answer-container-41909" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41909-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41909-score" class="post-score" title="current number of votes">1</div><span id="post-41909-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DazzaS has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, The file diameter/TGPP.xml needs to be updated with the new enum values, only 0 - 2 is currently defined. Depending on your Wireshark version 3GPP AVP 500 might be located in a different file as the structure has been changed (dictionary.xml?).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-41909" class="comments-container"><span id="41910"></span><div id="comment-41910" class="comment"><div id="post-41910-score" class="comment-score"></div><div class="comment-text"><p>Updated the xml file in master <a href="https://code.wireshark.org/review/#/c/8216/">https://code.wireshark.org/review/#/c/8216/</a></p></div><div id="comment-41910-info" class="comment-info"><span class="comment-age">(28 Apr '15, 01:04)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="42497"></span><div id="comment-42497" class="comment"><div id="post-42497-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the hit.</p><p>AVP 500 is in gqpolicy.xml (Wireshark Version 1.12.5 - windows)</p><p>updated:</p><p><code> avp name="Abort-Cause" code="500" mandatory="must" vendor-bit="must" may-encrypt="yes" vendor-id="TGPP"     type type-name="Enumerated"/</code></p><p><code></code></p><pre><code>enum name=&quot;BEARER_RELEASED&quot; code=&quot;0&quot;/
enum name=&quot;INSUFFICIENT_SERVER_RESOURCES&quot; code=&quot;1&quot;/
enum name=&quot;INSUFFICIENT_BEARER_RESOURCES&quot; code=&quot;2&quot;/
enum name=&quot;PS_TO_CS_HANDOVER&quot; code=&quot;3&quot;/
enum name=&quot;SPONSORED_DATA_CONNECTIVITY_ DISALLOWED&quot; code=&quot;4&quot;/</code></pre><code></code><p><code>/avp</code></p><p>Now STR decodes as:</p><p>Abort-Cause: PS_TO_CS_HANDOVER (3)</p><p>Thanks.</p></div><div id="comment-42497-info" class="comment-info"><span class="comment-age">(18 May '15, 04:24)</span> <span class="comment-user userinfo">DazzaS</span></div></div></div><div id="comment-tools-41909" class="comment-tools"></div><div class="clear"></div><div id="comment-41909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

