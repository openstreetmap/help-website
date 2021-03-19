+++
type = "question"
title = "Mobile phone network operator name change in Wireshark"
description = '''Hi all, we have noticed that PLMN-ID 26601 is shown as &quot;Gibtel GSM&quot; However, this operator changed its name to &quot;Gibtel&quot;. How can we request this change to be considered in next Wireshark release? Thanks'''
date = "2017-04-03T01:24:00Z"
lastmod = "2017-04-03T04:30:00Z"
weight = 60539
keywords = [ "name", "change" ]
aliases = [ "/questions/60539" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mobile phone network operator name change in Wireshark](/questions/60539/mobile-phone-network-operator-name-change-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60539-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>we have noticed that PLMN-ID 26601 is shown as "Gibtel GSM" However, this operator changed its name to "Gibtel". How can we request this change to be considered in next Wireshark release?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">name change</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '17, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/8570b320da961eb88cbfd8b143da9904?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bermejal&#39;s gravatar image" /><p>bermejal<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bermejal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Apr '17, 00:50</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-60539" class="comments-container"></div><div id="comment-tools-60539" class="comment-tools"></div><div class="clear"></div><div id="comment-60539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60543"></span>

<div id="answer-container-60543" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60543-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is using the E.212 list provided by ITU (the current development release is based on ITU operational bulletin No. 1111 - 1.XI.2016). If the name change was notified to ITU, then it will be reflected in Wireshark once I (or someone else) updates the ITU version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '17, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-60543" class="comments-container"><span id="60544"></span><div id="comment-60544" class="comment"><div id="post-60544-score" class="comment-score"></div><div class="comment-text"><p>Assuming that <a href="http://numberportabilitylookup.com/networks?s=">Number Portability Lookup</a> tracks this list, this update already happened. So filing a bug is all that remains.</p></div><div id="comment-60544-info" class="comment-info"><span class="comment-age">(03 Apr '17, 04:51)</span> Jaap ♦</div></div><span id="60545"></span><div id="comment-60545" class="comment"><div id="post-60545-score" class="comment-score"></div><div class="comment-text"><p>I went up to bulletin 1121 (April 1st, 2017) and it is not updated yet.</p></div><div id="comment-60545-info" class="comment-info"><span class="comment-age">(03 Apr '17, 06:31)</span> Pascal Quantin</div></div><span id="60549"></span><div id="comment-60549" class="comment"><div id="post-60549-score" class="comment-score"></div><div class="comment-text"><p>Must have been changed after Operational Bulletin No. 1111 (1.XI.2016), the last one containing "Annexed List: Mobile Network Codes (MNC)".</p></div><div id="comment-60549-info" class="comment-info"><span class="comment-age">(03 Apr '17, 08:16)</span> Jaap ♦</div></div></div><div id="comment-tools-60543" class="comment-tools"></div><div class="clear"></div><div id="comment-60543-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60540"></span>

<div id="answer-container-60540" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60540-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>File a bug report with <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '17, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60540" class="comments-container"></div><div id="comment-tools-60540" class="comment-tools"></div><div class="clear"></div><div id="comment-60540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

