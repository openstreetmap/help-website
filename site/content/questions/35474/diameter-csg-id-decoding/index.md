+++
type = "question"
title = "Diameter csg-id decoding"
description = '''3GPP spec 29.272 defines CSG-ID as below -     The CSG-Id-Data AVP is of type Unsigned32. The CSG ID shall be fix length 27 bit value. Unused bits (least significant) shall be padded with zeros. Wireshark however shows the value as 32 bit integer without indicating the padding bits unlike the S1AP d...'''
date = "2014-08-13T22:03:00Z"
lastmod = "2014-08-13T22:59:00Z"
weight = 35474
keywords = [ "diameter", "csg-id" ]
aliases = [ "/questions/35474" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter csg-id decoding](/questions/35474/diameter-csg-id-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35474-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>3GPP spec 29.272 defines CSG-ID as below -</p><ul><li></li></ul><p>The CSG-Id-Data AVP is of type Unsigned32. The CSG ID shall be fix length 27 bit value. Unused bits (least significant) shall be padded with zeros.</p><p>Wireshark however shows the value as 32 bit integer without indicating the padding bits unlike the S1AP decoder which clearly indicates the correct value. Can the diameter decoder be enhanced to show the correct 27-bit value?</p><pre><code>s1ap.CSG_Id
CSG-Id: 00000400 [bit length 27, 5 LSB pad bits, 0000 0000  0000 0000  0000 0100  000. .... decimal value 32]</code></pre></div><div id="question-tags" class="tags-container tags">diameter csg-id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '14, 22:03</strong></p><img src="https://secure.gravatar.com/avatar/ddb9249cc0cdfe72e4e220e89e48c6bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunildr&#39;s gravatar image" /><p>sunildr<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunildr has no accepted answers">0%</span></p></div></div><div id="comments-container-35474" class="comments-container"></div><div id="comment-tools-35474" class="comment-tools"></div><div class="clear"></div><div id="comment-35474-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35475"></span>

<div id="answer-container-35475" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35475-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure just add the AVP to packet-diameter-3gpp.c and add the sub decoding there ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '14, 22:59</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-35475" class="comments-container"></div><div id="comment-tools-35475" class="comment-tools"></div><div class="clear"></div><div id="comment-35475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

