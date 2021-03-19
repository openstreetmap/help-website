+++
type = "question"
title = "How to make ANSI MAP ASN.1 spec compile-able in OSS ASN.1 studio"
description = '''I tried to compile ASN.1 spec in asn1/ansi_map /ansi_map.asn in OSS ASN.1 studio but failed. The error indicates there&#x27;re duplicated tags in several messages, for example: AuthenticationFailureReport ::= [PRIVATE 18] SET   {  ...  reportType [44] IMPLICIT ReportType,  ...  reportType2 [44] IMPLICIT ...'''
date = "2014-02-08T07:15:00Z"
lastmod = "2014-02-09T09:47:00Z"
weight = 29552
keywords = [ "asn.1", "ansi_map" ]
aliases = [ "/questions/29552" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to make ANSI MAP ASN.1 spec compile-able in OSS ASN.1 studio](/questions/29552/how-to-make-ansi-map-asn1-spec-compile-able-in-oss-asn1-studio)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29552-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to compile ASN.1 spec in asn1/ansi_map /ansi_map.asn in OSS ASN.1 studio but failed. The error indicates there're duplicated tags in several messages, for example:</p><pre><code>AuthenticationFailureReport ::= [PRIVATE 18] SET 
 {
    ...
    reportType  [44] IMPLICIT ReportType,
    ...
    reportType2 [44] IMPLICIT ReportType OPTIONAL,
    ...
 }</code></pre><p>It seems the tags here are used as unique type identifiers, but in my understanding, tag in a complex type (sequence,choice) should be used to mark the order of members. Can anyone suggest on how to make it fully compliant with ASN.1 standard syntax?</p></div><div id="question-tags" class="tags-container tags">asn.1 ansi_map</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '14, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/a120ef973932244517e794433d7e6eb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TB_BT&#39;s gravatar image" /><p>TB_BT<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TB_BT has no accepted answers">0%</span></p></div></div><div id="comments-container-29552" class="comments-container"></div><div id="comment-tools-29552" class="comment-tools"></div><div class="clear"></div><div id="comment-29552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29579"></span>

<div id="answer-container-29579" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29579-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The ansi_map.asn is hand crafted to make the Wireshark dissector. I'm not sure how useful it would be for any other purpose. The tags are listed in the order of apperance in the refered standard document.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '14, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-29579" class="comments-container"><span id="29657"></span><div id="comment-29657" class="comment"><div id="post-29657-score" class="comment-score"></div><div class="comment-text"><p>The implied info in your reply is enough for me, thanks.</p></div><div id="comment-29657-info" class="comment-info"><span class="comment-age">(10 Feb '14, 20:47)</span> TB_BT</div></div></div><div id="comment-tools-29579" class="comment-tools"></div><div class="clear"></div><div id="comment-29579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

