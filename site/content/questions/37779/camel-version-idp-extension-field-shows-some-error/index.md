+++
type = "question"
title = "Camel Version IDP Extension Field shows some error"
description = '''Hello, I tried to view the extension field value from wireshark but it showing some error (mentioned below) BER: Dissector for OID not implemented. Contact Wireshark developers if you want this supported How can I solve this ?? Thanks, Hanosh Varghese'''
date = "2014-11-12T02:38:00Z"
lastmod = "2014-11-12T04:17:00Z"
weight = 37779
keywords = [ "camel" ]
aliases = [ "/questions/37779" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Camel Version IDP Extension Field shows some error](/questions/37779/camel-version-idp-extension-field-shows-some-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37779-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I tried to view the extension field value from wireshark but it showing some error (mentioned below) BER: Dissector for OID not implemented. Contact Wireshark developers if you want this supported</p><p>How can I solve this ??</p><p>Thanks, Hanosh Varghese</p></div><div id="question-tags" class="tags-container tags">camel</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '14, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/947b7a306a061178060e0e2a11b93d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hanosh&#39;s gravatar image" /><p>Hanosh<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hanosh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Nov '14, 03:37</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-37779" class="comments-container"></div><div id="comment-tools-37779" class="comment-tools"></div><div class="clear"></div><div id="comment-37779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37783"></span>

<div id="answer-container-37783" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37783-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The OID "identifies" the ASN1 code in the extension, most probably it's a proprietarry extension and it can't be dissected/decoded unless the ASN1 description of the content is publically available. Using this tool <a href="http://oid-info.com/get/1">http://oid-info.com/get/1</a> you might be able to find to whom the OID belongs. What is the OID? The text "BER: Dissector for OID not implemented..." was added in case the OID pointed to an open standard missed or omitted by the dissector designer which dissection could be added by Wirehark developers.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '14, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-37783" class="comments-container"><span id="37803"></span><div id="comment-37803" class="comment"><div id="post-37803-score" class="comment-score"></div><div class="comment-text"><p>OID is..</p><p><a href="https://www.cloudshark.org/captures/54e1d4490326">link text</a></p></div><div id="comment-37803-info" class="comment-info"><span class="comment-age">(12 Nov '14, 20:01)</span> Hanosh</div></div><span id="37804"></span><div id="comment-37804" class="comment"><div id="post-37804-score" class="comment-score"></div><div class="comment-text"><p>Oke I didn't find any information about it, but it probably defines a proprietarry extension made by the manufacturer of the node sending the message - what vendors node is it?</p></div><div id="comment-37804-info" class="comment-info"><span class="comment-age">(13 Nov '14, 00:28)</span> Anders ♦</div></div></div><div id="comment-tools-37783" class="comment-tools"></div><div class="clear"></div><div id="comment-37783-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

