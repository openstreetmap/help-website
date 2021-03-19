+++
type = "question"
title = "unknown inap"
description = '''I&#x27;m sending a INAP Initial DP message with an opCode or extension value of 59 but the wireshark trace shows &#x27;Unknown INAP (59)&#x27;. What is the reason'''
date = "2011-11-16T03:57:00Z"
lastmod = "2011-11-17T12:13:00Z"
weight = 7469
keywords = [ "unknown", "inap" ]
aliases = [ "/questions/7469" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unknown inap](/questions/7469/unknown-inap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7469-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm sending a INAP Initial DP message with an opCode or extension value of 59 but the wireshark trace shows 'Unknown INAP (59)'. What is the reason</p></div><div id="question-tags" class="tags-container tags">unknown inap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Nov '11, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/33965977f4fe192c0dce5e4b5b9cdbbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rks2k1&#39;s gravatar image" /><p>rks2k1<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rks2k1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Nov '11, 05:56</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-7469" class="comments-container"><span id="7479"></span><div id="comment-7479" class="comment"><div id="post-7479-score" class="comment-score"></div><div class="comment-text"><p>Not sure what you mean opcode-initialDP Code ::= local:0 There is no opcode 59 defined in IN-operationcodes.asn Regards Anders</p></div><div id="comment-7479-info" class="comment-info"><span class="comment-age">(16 Nov '11, 22:09)</span> Anders ♦</div></div></div><div id="comment-tools-7469" class="comment-tools"></div><div class="clear"></div><div id="comment-7469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7492"></span>

<div id="answer-container-7492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7492-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That has nothing to do with the INAP opcodes. This is the ASN1 spec of that field ExtensionField ::= SEQUENCE { type EXTENSION.&amp;id({SupportedExtensions}), -- shall identify the value of an EXTENSION type criticality CriticalityType DEFAULT ignore, value [1] EXTENSION.&amp;ExtensionType({SupportedExtensions}{@type}) } So the extension is of the local type 59, as this seems to be a Simens INAP trace that's probably a Simens proprietary extension.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '11, 12:13</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-7492" class="comments-container"><span id="7495"></span><div id="comment-7495" class="comment"><div id="post-7495-score" class="comment-score"></div><div class="comment-text"><p>Probably not without Simens specification of the extension.</p></div><div id="comment-7495-info" class="comment-info"><span class="comment-age">(17 Nov '11, 14:06)</span> Anders ♦</div></div></div><div id="comment-tools-7492" class="comment-tools"></div><div class="clear"></div><div id="comment-7492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

