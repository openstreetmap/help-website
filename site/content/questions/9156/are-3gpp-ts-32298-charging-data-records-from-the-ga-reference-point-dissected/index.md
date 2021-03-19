+++
type = "question"
title = "Are 3GPP TS 32.298 Charging Data Records from the Ga Reference Point dissected?"
description = '''Hello, does Ga interface is supported by any release of WireShark? If it does please, could you please give me the hint what version to use to have Charging Data Records decoded?'''
date = "2012-02-20T16:20:00Z"
lastmod = "2012-04-05T13:19:00Z"
weight = 9156
keywords = [ "records", "data", "charging", "ga" ]
aliases = [ "/questions/9156" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Are 3GPP TS 32.298 Charging Data Records from the Ga Reference Point dissected?](/questions/9156/are-3gpp-ts-32298-charging-data-records-from-the-ga-reference-point-dissected)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9156-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, does Ga interface is supported by any release of WireShark? If it does please, could you please give me the hint what version to use to have Charging Data Records decoded?</p></div><div id="question-tags" class="tags-container tags">records data charging ga</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '12, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/6f6b7c8c03b3343af09fc201341fb354?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emarina&#39;s gravatar image" /><p>emarina<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emarina has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Apr '12, 13:18</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-9156" class="comments-container"></div><div id="comment-tools-9156" class="comment-tools"></div><div class="clear"></div><div id="comment-9156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9157"></span>

<div id="answer-container-9157" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9157-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's GTP' right? Any recent stable Wireshark version should be able to dissect that. You may need to work the preferences somewhat.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Feb '12, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Feb '12, 00:31</p></div></div><div id="comments-container-9157" class="comments-container"><span id="9972"></span><div id="comment-9972" class="comment"><div id="post-9972-score" class="comment-score"></div><div class="comment-text"><p>It is, as noted in <a href="http://ask.wireshark.org/questions/9968/ga-reference-point">the second time emarina asked the question</a>, 3GPP TS 32.298, and, although the GTP' dissector does dissect the 8.30 Charging Characteristics IE, it doesn't dissect the parameters in detail, it just dissects them as "Remaining octets".</p><p>So there's currently no support for dissecting the CDR parameters.</p></div><div id="comment-9972-info" class="comment-info"><span class="comment-age">(05 Apr '12, 13:16)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9157" class="comment-tools"></div><div class="clear"></div><div id="comment-9157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9973"></span>

<div id="answer-container-9973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9973-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark GTP' dissector does dissect the 8.30 Charging Characteristics IE; however, it doesn't dissect the parameters in detail, it just dissects them as "Remaining octets", so there's currently no version of Wireshark that fully supports 3GPP TS 32.298.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '12, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9973" class="comments-container"><span id="10021"></span><div id="comment-10021" class="comment"><div id="post-10021-score" class="comment-score"></div><div class="comment-text"><p>In the development version some flavor of the CDR is dissected. In the charging data IE.</p></div><div id="comment-10021-info" class="comment-info"><span class="comment-age">(09 Apr '12, 00:16)</span> Anders ♦</div></div></div><div id="comment-tools-9973" class="comment-tools"></div><div class="clear"></div><div id="comment-9973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

