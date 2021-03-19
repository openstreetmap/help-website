+++
type = "question"
title = "Unknown AVP problem"
description = '''I am using wireshark version 1.10.0rc2. I want to capture Diameter stuffs for S6a interface. I am facing problem while decode the Trace-Data AVP having AVP code = 1458. In wireshark it is showing as  AVP Code: 1458 Unknown  Unknow AVP, if you know what this is you can add it to the dictionary.xml. C...'''
date = "2013-08-26T08:16:00Z"
lastmod = "2013-08-28T06:14:00Z"
weight = 24064
keywords = [ "unknown", "problem", "avp" ]
aliases = [ "/questions/24064" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unknown AVP problem](/questions/24064/unknown-avp-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24064-score" class="post-score" title="current number of votes">0</div><span id="post-24064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark version 1.10.0rc2. I want to capture Diameter stuffs for S6a interface. I am facing problem while decode the Trace-Data AVP having AVP code = 1458.</p><p>In wireshark it is showing as AVP Code: 1458 Unknown Unknow AVP, if you know what this is you can add it to the dictionary.xml.</p><p>Can any one have a look and please let me know.</p><p>Hope for your cooperation. Thanks in advance.</p><p>-- Regards Mrinal Aich Software Engineer-1, Dynamic Digital Technology, Kolkata</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unknown" rel="tag" title="see questions tagged &#39;unknown&#39;">unknown</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-avp" rel="tag" title="see questions tagged &#39;avp&#39;">avp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '13, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/6ac0d9e777e77faa8d859fc0f335919a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mrinal&#39;s gravatar image" /><p><span>Mrinal</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mrinal has no accepted answers">0%</span></p></div></div><div id="comments-container-24064" class="comments-container"></div><div id="comment-tools-24064" class="comment-tools"></div><div class="clear"></div><div id="comment-24064-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24065"></span>

<div id="answer-container-24065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24065-score" class="post-score" title="current number of votes">1</div><span id="post-24065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The AVP 1458 is in the diameter.xml in trunk, I'm not sure when it was added you could try the released version 1.10.1 which is newer than 1.10.0.rc2 or a development build from <a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a> Note that the AVP should have the vendor bit set and the vendor ID as 3GPP in your trace. You could also check if your dictionmary.xml have &lt;avp name="Trace-Data" code="1458" mandatory="must" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;grouped&gt; &lt;gavp name="Trace-Reference"/&gt; &lt;gavp name="Trace-Depth"/&gt; &lt;gavp name="Trace-NE-Type-List"/&gt; &lt;gavp name="Trace-Interface-List"/&gt; &lt;gavp name="Trace-Event-List"/&gt; &lt;gavp name="OMC-Id"/&gt; &lt;gavp name="Trace-Collection-Entity"/&gt; &lt;/grouped&gt; &lt;/avp&gt; &lt;avp name="Trace-Reference" code="1459" mandatory="must" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;type type-name="OctetString"/&gt; &lt;/avp&gt; &lt;avp name="Trace-Depth" code="1462" mandatory="must" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;type type-name="Enumerated"/&gt; &lt;enum name="Minimum" code="0"/&gt; &lt;enum name="Medium" code="1"/&gt; &lt;enum name="Maximum" code="2"/&gt; &lt;enum name="MinimumWithoutVendorSpecificExtension" code="3"/&gt; &lt;enum name="MediumWithoutVendorSpecificExtension" code="4"/&gt; &lt;enum name="MaximumWithoutVendorSpecificExtension" code="5"/&gt; &lt;/avp&gt; &lt;avp name="Trace-NE-Type-List" code="1463" mandatory="must" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;type type-name="OctetString"/&gt; &lt;/avp&gt; &lt;avp name="Trace-Interface-List" code="1464" mandatory="must" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;type type-name="OctetString"/&gt; &lt;/avp&gt; &lt;avp name="Trace-Event-List" code="1465" mandatory="must" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;type type-name="OctetString"/&gt; &lt;/avp&gt; &lt;avp name="OMC-Id" code="1466" mandatory="must" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;type type-name="OctetString"/&gt; &lt;/avp&gt; &lt;avp name="Trace-Collection-Entity" code="1452" mandatory="must" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;type type-name="IPAddress"/&gt; &lt;/avp&gt; And if not add them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '13, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-24065" class="comments-container"><span id="24125"></span><div id="comment-24125" class="comment"><div id="post-24125-score" class="comment-score"></div><div class="comment-text"><p>In dictionary.xml,the information about Trace Data AVP was already mentioned. I also set the vendor bit and assigned the vendor ID as 3GPP but still it is showing 1458 Unknown AVP.</p></div><div id="comment-24125-info" class="comment-info"><span class="comment-age">(28 Aug '13, 06:00)</span> <span class="comment-user userinfo">Mrinal</span></div></div><span id="24127"></span><div id="comment-24127" class="comment"><div id="post-24127-score" class="comment-score"></div><div class="comment-text"><p>If you can share a trace file thrugh bugzilla or some other means we might be able to figure out what the problem is.</p></div><div id="comment-24127-info" class="comment-info"><span class="comment-age">(28 Aug '13, 06:14)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-24065" class="comment-tools"></div><div class="clear"></div><div id="comment-24065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

