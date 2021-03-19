+++
type = "question"
title = "How can I get BT ATT parameters information details using Wireshark tool!"
description = '''Hi , I am using nRF51822 sniffer &amp;amp; anaylizing the capture data using wireshark tool . After Captured data when I tried to see the information using wireshark tool , I am getting the following information : it shows : .... .0.. = encrypted: No ,I guess it should show &quot;Yes&quot; , let me know how to en...'''
date = "2015-01-05T15:45:00Z"
lastmod = "2015-09-24T13:26:00Z"
weight = 38898
keywords = [ "wireshark" ]
aliases = [ "/questions/38898" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get BT ATT parameters information details using Wireshark tool!](/questions/38898/how-can-i-get-bt-att-parameters-information-details-using-wireshark-tool)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38898-score" class="post-score" title="current number of votes">0</div><span id="post-38898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi , I am using nRF51822 sniffer &amp; anaylizing the capture data using wireshark tool .</p><p>After Captured data when I tried to see the information using wireshark tool , I am getting the following information : it shows : .... .0.. = encrypted: No ,I guess it should show "Yes" , let me know how to enable flag . Also I am interested to see the PRU device parameters : but log shows : Bluetooth Attribute Protocol Opcode: Read Response (0x0b) Value: fc591bd0005c13ba005f7017581bbc3403000000</p><p>but above information I can't get PRU parameters details .</p><p>Regards Narendra</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '15, 15:45</strong></p><img src="https://secure.gravatar.com/avatar/fac02024ccd7c3f5077fd66d73d7d498?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Naren&#39;s gravatar image" /><p><span>Naren</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Naren has no accepted answers">0%</span></p></div></div><div id="comments-container-38898" class="comments-container"><span id="38906"></span><div id="comment-38906" class="comment"><div id="post-38906-score" class="comment-score"></div><div class="comment-text"><p>Without a sample capture there is little a developer can do. See if you can post one on cloudshark for instance.</p></div><div id="comment-38906-info" class="comment-info"><span class="comment-age">(06 Jan '15, 08:27)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="38930"></span><div id="comment-38930" class="comment"><div id="post-38930-score" class="comment-score"></div><div class="comment-text"><p>Please check attached screenshot imgs:</p><p>alt text</p><p><img src="https://osqa-ask.wireshark.org/upfiles/22_1uHhllI.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/11_CGy93U3.png" alt="alt text" /></p></div><div id="comment-38930-info" class="comment-info"><span class="comment-age">(07 Jan '15, 11:37)</span> <span class="comment-user userinfo">Naren</span></div></div><span id="38931"></span><div id="comment-38931" class="comment"><div id="post-38931-score" class="comment-score"></div><div class="comment-text"><p>I have attached screenshot img pls check it!!</p></div><div id="comment-38931-info" class="comment-info"><span class="comment-age">(07 Jan '15, 11:38)</span> <span class="comment-user userinfo">Naren</span></div></div></div><div id="comment-tools-38898" class="comment-tools"></div><div class="clear"></div><div id="comment-38898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39024"></span>

<div id="answer-container-39024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39024-score" class="post-score" title="current number of votes">0</div><span id="post-39024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should wait. Really. Currently I am working on that, see feature request [1]. Work in progress, I have a plan to push my patches in February or March 2015. You can help me by upload a number of different capture files (I think about different attributes) to [1]</p><p>[1] <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10524">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10524</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '15, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p><span>Michał Łabędzki</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></img></div></div><div id="comments-container-39024" class="comments-container"></div><div id="comment-tools-39024" class="comment-tools"></div><div class="clear"></div><div id="comment-39024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46123"></span>

<div id="answer-container-46123" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46123-score" class="post-score" title="current number of votes">0</div><span id="post-46123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please note Wireshark supports all (expect 3) attributes - all LE profiles are supported now. You can wait for Wireshark 2.0 or try Wireshark 1.99.10 (if...) or 1.99.9, but this development version does not support all attributes, but almost all popular attributes (in my opinion). I will continue works on BLE attributes to make it better then now (new milestone).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '15, 13:26</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p><span>Michał Łabędzki</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></img></div></div><div id="comments-container-46123" class="comments-container"></div><div id="comment-tools-46123" class="comment-tools"></div><div class="clear"></div><div id="comment-46123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

