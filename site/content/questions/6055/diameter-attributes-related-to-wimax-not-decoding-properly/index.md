+++
type = "question"
title = "Diameter attributes related to WiMAX not decoding properly"
description = '''Hello Support, I have Diameter trace which includes attributes related EAP and WiMAX.  All the WiMAX attributes are not decoding and the AVP&#x27;s are shown as &quot;Unknown&quot;. I am running latest version 1.6.1 Wireshark. Can you please let me know how can I fix it. Thank you, Vijay'''
date = "2011-09-02T00:15:00Z"
lastmod = "2011-09-02T07:27:00Z"
weight = 6055
keywords = [ "attribute", "wimax" ]
aliases = [ "/questions/6055" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Diameter attributes related to WiMAX not decoding properly](/questions/6055/diameter-attributes-related-to-wimax-not-decoding-properly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6055-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Support,</p><p>I have Diameter trace which includes attributes related EAP and WiMAX.</p><p>All the WiMAX attributes are not decoding and the AVP's are shown as "Unknown". I am running latest version 1.6.1 Wireshark.</p><p>Can you please let me know how can I fix it.</p><p>Thank you, Vijay</p></div><div id="question-tags" class="tags-container tags">attribute wimax</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '11, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/6f698592e01b53ac02b99c5997377d66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vijayakumarpc&#39;s gravatar image" /><p>vijayakumarpc<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vijayakumarpc has no accepted answers">0%</span></p></div></div><div id="comments-container-6055" class="comments-container"></div><div id="comment-tools-6055" class="comment-tools"></div><div class="clear"></div><div id="comment-6055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6063"></span>

<div id="answer-container-6063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6063-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I suppose those AVP:s has the vendor bit set and a vendor specified? Wireshark dissects AVP:s with the aid of xml files most probably ther is no .xml file for "EAP" or "WiMAX" look in the Diameter directory. You can make your own .xml files and add them by editing dictionary.xml (refers the files) Then send us the files by making bug report in <a href="https://bugs.wireshark.org/bugzilla/">bugzilla</a> attaching the file(s) for inclusion in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '11, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-6063" class="comments-container"></div><div id="comment-tools-6063" class="comment-tools"></div><div class="clear"></div><div id="comment-6063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

