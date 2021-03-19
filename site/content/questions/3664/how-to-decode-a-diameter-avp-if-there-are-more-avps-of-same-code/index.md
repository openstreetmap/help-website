+++
type = "question"
title = "How to decode a Diameter AVP if there are more AVPs of same code?"
description = '''Hi, I am trying to decode some Diameter AVPs using wireshark, but I found that same AVP code is defined at two places differently like below: imscxdx.xml: &amp;lt;avp name=&quot;SIP-Auth-Data-Item&quot; code=&quot;13&quot; mandatory=&quot;must&quot; vendor-bit=&quot;must&quot; vendor-id=&quot;TGPP&quot; may-encrypt=&quot;yes&quot;&amp;gt; TGPPGmb.xml: &amp;lt;avp name=&quot;...'''
date = "2011-04-20T15:29:00Z"
lastmod = "2011-04-20T21:43:00Z"
weight = 3664
keywords = [ "diameter" ]
aliases = [ "/questions/3664" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to decode a Diameter AVP if there are more AVPs of same code?](/questions/3664/how-to-decode-a-diameter-avp-if-there-are-more-avps-of-same-code)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3664-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to decode some Diameter AVPs using wireshark, but I found that same AVP code is defined at two places differently like below:</p><p>imscxdx.xml: &lt;avp name="SIP-Auth-Data-Item" code="13" mandatory="must" vendor-bit="must" vendor-id="TGPP" may-encrypt="yes"&gt;</p><p>TGPPGmb.xml: &lt;avp name="3GPP-Charging-Characteristics" code="13" mandatory="must" may-encrypt="yes" protected="may" vendor-bit="must" vendor-id="TGPP"&gt;</p><p>imscxdx.xml: &lt;avp name="Public-Identity" code="2" mandatory="must" vendor-bit="must" vendor-id="TGPP" may-encrypt="yes"&gt;</p><p>TGPPGmb.xml: &lt;avp name="3GPP-Charging ID" code="2" mandatory="must" may-encrypt="yes" protected="may" vendor-bit="must" vendor-id="TGPP"&gt;</p><p>imscxdx.xml: &lt;avp name="Mandatory-Capability" code="5" mandatory="must" vendor-bit="must" vendor-id="TGPP" may-encrypt="no"&gt;</p><p>TGPPGmb.xml: &lt;avp name="3GPP-GPRS Negotiated QoS profile" code="5" mandatory="must" may-encrypt="yes" protected="may" vendor-bit="must" vendor-id="TGPP"&gt;</p><p>I want to decode the AVPs as defined in file "TGPPGmb.xml". But currently the wireshark decode this as it is defined in file "imscxdx.xml" How can I change this, so that wireshark decode it as I wanted.</p></div><div id="question-tags" class="tags-container tags">diameter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '11, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/5edcb417f6ec8bf11e63a8f619d51ebe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunil&#39;s gravatar image" /><p>sunil<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunil has no accepted answers">0%</span></p></div></div><div id="comments-container-3664" class="comments-container"></div><div id="comment-tools-3664" class="comment-tools"></div><div class="clear"></div><div id="comment-3664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3666"></span>

<div id="answer-container-3666" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3666-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check out the comments at the beginning of the files: And &lt;!-- These AVP:s collide(share AVP code number) with other 3GPP AVP:s (TGPPGmb.xml) uncomment 1 - 28 here and uncomment the ones in TGPPGmb.xml if you want to use these.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 21:43</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-3666" class="comments-container"></div><div id="comment-tools-3666" class="comment-tools"></div><div class="clear"></div><div id="comment-3666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

