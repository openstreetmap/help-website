+++
type = "question"
title = "How to distinguish optional IEs with the same type in ANSI-MAP message TransferToNumberRequestRes"
description = '''Specially, this message has got two IEs with the same type, and they both are optional:  -- TransferToNumberRequest RETURN RESULT Parameters TransferToNumberRequestRes ::= [PRIVATE 18] SET {  digits-Destination [4] IMPLICIT Digits OPTIONAL,  -- (Destination) M 6.5.2.58 a ...  -- O 6.5.2.25 e, f  dig...'''
date = "2014-02-11T21:33:00Z"
lastmod = "2014-02-11T22:20:00Z"
weight = 29728
keywords = [ "ansi_map", "cdma", "3gpp2" ]
aliases = [ "/questions/29728" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to distinguish optional IEs with the same type in ANSI-MAP message TransferToNumberRequestRes](/questions/29728/how-to-distinguish-optional-ies-with-the-same-type-in-ansi-map-message-transfertonumberrequestres)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29728-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Specially, this message has got two IEs with the same type, and they both are optional:</p><pre><code>-- TransferToNumberRequest RETURN RESULT Parameters
TransferToNumberRequestRes ::= [PRIVATE 18] SET {
    digits-Destination                      [4] IMPLICIT Digits OPTIONAL,
    -- (Destination) M 6.5.2.58 a
...
    -- O 6.5.2.25 e, f
    digits-Carrier                          [4] IMPLICIT Digits OPTIONAL,
...
    }</code></pre><p>Given the nature of ASN.1 set type, the question is:</p><p>If there's only one IE with the tag value 4 appear in a BER-encoded PDU buffer, how can we judge its actual type (digits-Destination or digits-Carrier) ?</p><p>Thanks for any of your answers.</p></div><div id="question-tags" class="tags-container tags">ansi_map cdma 3gpp2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 21:33</strong></p><img src="https://secure.gravatar.com/avatar/a120ef973932244517e794433d7e6eb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TB_BT&#39;s gravatar image" /><p>TB_BT<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TB_BT has no accepted answers">0%</span></p></div></div><div id="comments-container-29728" class="comments-container"></div><div id="comment-tools-29728" class="comment-tools"></div><div class="clear"></div><div id="comment-29728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29731"></span>

<div id="answer-container-29731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29731-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you look at the document ref ("M 6.5.2.58 a") the first parameter is Mandatory in the specification. I don't remember if I had to make it optional in Wirehark for it to work properly or if that's a bug. This probably works for Wireshark as the tags are in a table and the mandatory parameter is found first. It might not work if there are 3 tags with the value of 4. I'm not sure to what extent ANSI MAP actually adhere to ASN1 specifications I haven't found a complete ASN1 document as you can for GSM MAP. The specification might say that each parameter may only occure once as well I suppose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '14, 22:20</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-29731" class="comments-container"></div><div id="comment-tools-29731" class="comment-tools"></div><div class="clear"></div><div id="comment-29731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

