+++
type = "question"
title = "Decryption of ISKAMP Packets in wireshark version 1.8.0"
description = '''Hi, Decrypting of the ISKAMP packet results in expert info/malformed Packet. When we are decrypting the ISKAMP Packet in wireshark it results in a MALFORMED Packet. Can anyone please help me with this. Regards, Sharad'''
date = "2012-07-17T11:00:00Z"
lastmod = "2012-07-23T09:15:00Z"
weight = 12803
keywords = [ "isakmp", "ike", "decryption" ]
aliases = [ "/questions/12803" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decryption of ISKAMP Packets in wireshark version 1.8.0](/questions/12803/decryption-of-iskamp-packets-in-wireshark-version-180)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Decrypting of the ISKAMP packet results in expert info/malformed Packet. When we are decrypting the ISKAMP Packet in wireshark it results in a MALFORMED Packet. Can anyone please help me with this.</p><p>Regards, Sharad</p></div><div id="question-tags" class="tags-container tags">isakmp ike decryption</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '12, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/b7e480867b734821fc9ba4d05e973872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharad%20Kodkani&#39;s gravatar image" /><p>Sharad Kodkani<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharad Kodkani has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jul '12, 12:49</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-12803" class="comments-container"><span id="12894"></span><div id="comment-12894" class="comment"><div id="post-12894-score" class="comment-score"></div><div class="comment-text"><p>Sharad how did you decrypt ISKAMP packet, I need a little help here: <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets">http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets</a></p></div><div id="comment-12894-info" class="comment-info"><span class="comment-age">(21 Jul '12, 11:06)</span> chetan1989</div></div></div><div id="comment-tools-12803" class="comment-tools"></div><div class="clear"></div><div id="comment-12803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12917"></span>

<div id="answer-container-12917" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12917-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'd suggest you open a <a href="https://bugs.wireshark.org">bug report</a>, including a sample capture complete with any keys necessary to decrypt it so someone with some free time can take a look.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-12917" class="comments-container"><span id="12927"></span><div id="comment-12927" class="comment"><div id="post-12927-score" class="comment-score"></div><div class="comment-text"><p>Hi jeff and kurt,</p><p>Thanks a lot for the reply, Please let me know how do i raise a bug in Wireshark.</p><p>Regards, Sharad</p></div><div id="comment-12927-info" class="comment-info"><span class="comment-age">(23 Jul '12, 11:32)</span> Sharad Kodkani</div></div><span id="12929"></span><div id="comment-12929" class="comment"><div id="post-12929-score" class="comment-score"></div><div class="comment-text"><p>please follow the instructions on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p></div><div id="comment-12929-info" class="comment-info"><span class="comment-age">(23 Jul '12, 12:25)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12917" class="comment-tools"></div><div class="clear"></div><div id="comment-12917-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12925"></span>

<div id="answer-container-12925" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12925-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>During my tests (see <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets">this answer</a>) I had some MALFORMED packets too.</p><p><strong>After I restarted</strong> Wireshark, the MALFORMED packets were gone. So, it looks like a bug for me. As @JeffMorriss said, please file a bug report with sample data. Actually, you can use my sample data from <a href="http://ask.wireshark.org/questions/12019/how-can-i-decrypt-ikev1-packets">this answer</a>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jul '12, 12:33</p></div></div><div id="comments-container-12925" class="comments-container"></div><div id="comment-tools-12925" class="comment-tools"></div><div class="clear"></div><div id="comment-12925-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

