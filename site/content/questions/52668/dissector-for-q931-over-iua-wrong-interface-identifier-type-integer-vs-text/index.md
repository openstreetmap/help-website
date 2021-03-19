+++
type = "question"
title = "Dissector for q931 over iua (wrong interface identifier type - integer vs text)"
description = '''Hi all! My capture of &quot;q931 over iua over sctp&quot; traffic is displayed incorrectly because at q921 layer my equipment sends &quot;Interface identifier&quot; parameter tag = 1 (integer), but parameter length is 37 (must be 8 for integer according to RFC 3057; might be anything else if parameter tag = 3 (text)). ...'''
date = "2016-05-17T05:33:00Z"
lastmod = "2016-05-17T07:23:00Z"
weight = 52668
keywords = [ "iua", "iuaparameter", "q931", "wrongparametertype", "q921" ]
aliases = [ "/questions/52668" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissector for q931 over iua (wrong interface identifier type - integer vs text)](/questions/52668/dissector-for-q931-over-iua-wrong-interface-identifier-type-integer-vs-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52668-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all!</p><p>My capture of "q931 over iua over sctp" traffic is displayed incorrectly because at q921 layer my equipment sends "Interface identifier" parameter tag = 1 (integer), but parameter length is 37 (must be 8 for integer according to RFC 3057; might be anything else if parameter tag = 3 (text)). Since that everything below this point interpretes as malformed IUA packet. I can do nothing with my equipment (in fact it works!), but I want to be able to capture and analyze signalling traffic.</p><p>My question is - is there a way to ignore this misbehavior and analyze the rest of the packet with offset equal to parameter length (a way other than writing alternate dissector for IUA)?</p><p>I use wireshark Version 2.0.3 (v2.0.3-0-geed34f0 from master-2.0) on windows 8.1.</p><p>Appreciate any help! Dmitry</p></div><div id="question-tags" class="tags-container tags">iua iuaparameter q931 wrongparametertype q921</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '16, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/eb104f0812555b7664941047b96d12eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dmitryd&#39;s gravatar image" /><p>dmitryd<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dmitryd has no accepted answers">0%</span></p></div></div><div id="comments-container-52668" class="comments-container"></div><div id="comment-tools-52668" class="comment-tools"></div><div class="clear"></div><div id="comment-52668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52674"></span>

<div id="answer-container-52674" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52674-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can't natively do this. Either:</p><ol><li>Get the equipment (which works incorrectly) to output the correct tag</li><li>Use a tool to process the packets and correct the tag</li><li>Build your own Wireshark, where you can patch the dissector</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '16, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52674" class="comments-container"><span id="52899"></span><div id="comment-52899" class="comment"><div id="post-52899-score" class="comment-score">1</div><div class="comment-text"><p>Jaap, thank you for your quick answer!</p><p>Finally, it took some time reading and then following very exact instructions (thanks to guys who wrote wireshark documentations!) of how to build wireshark from src code on windows. But after all, with some changes in original dissector it worked!</p><p>Dmitry</p></div><div id="comment-52899-info" class="comment-info"><span class="comment-age">(25 May '16, 01:32)</span> dmitryd</div></div></div><div id="comment-tools-52674" class="comment-tools"></div><div class="clear"></div><div id="comment-52674-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

