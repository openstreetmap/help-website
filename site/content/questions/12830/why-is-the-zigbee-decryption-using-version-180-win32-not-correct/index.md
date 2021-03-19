+++
type = "question"
title = "Why is the Zigbee decryption using Version 1.8.0 win32 not correct?"
description = '''I just installed version 1.8.0 and set the preconfigured key for the Zigbee Protocol to (39:30:65:63:6E:61:69:6C:6C:41:65:65:42:67:69:5A) and Byte order (normal). It is not decrypting my Zigbee packet properly. Can anyone help me?'''
date = "2012-07-18T07:25:00Z"
lastmod = "2012-07-25T12:56:00Z"
weight = 12830
keywords = [ "zigbee" ]
aliases = [ "/questions/12830" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why is the Zigbee decryption using Version 1.8.0 win32 not correct?](/questions/12830/why-is-the-zigbee-decryption-using-version-180-win32-not-correct)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12830-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just installed version 1.8.0 and set the preconfigured key for the Zigbee Protocol to <code>(39:30:65:63:6E:61:69:6C:6C:41:65:65:42:67:69:5A)</code> and <code>Byte order (normal)</code>. It is not decrypting my Zigbee packet properly. Can anyone help me?</p></div><div id="question-tags" class="tags-container tags">zigbee</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '12, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/68fa57913e23eae5ad9a41a97608097d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="April&#39;s gravatar image" /><p>April<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="April has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jul '12, 12:05</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-12830" class="comments-container"></div><div id="comment-tools-12830" class="comment-tools"></div><div class="clear"></div><div id="comment-12830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12999"></span>

<div id="answer-container-12999" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12999-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I just tried it with Win 7 and Win XP (Wireshark 1.8.0). It seems to work as expected. Can you please post a sample capture on <a href="http://cloudshark.org">cloudshark.org</a> for the mentioned key?</p><p>HINT: As you cannot delete an anonymously uploaded file on <a href="http://cloudshark.org">cloudshark.org</a>, you better don't post any private data. Post just those packets in a capture file, that are required to analyze the problem.</p><p>Some questions:</p><ol><li>Does it work with an older version of Wireshark. If yes, which one?</li><li>Did you choose the correct Encryption method (AES128, 32/64/128 Bit Integrity Protection)?</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '12, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jul '12, 13:50</p></div></div><div id="comments-container-12999" class="comments-container"></div><div id="comment-tools-12999" class="comment-tools"></div><div class="clear"></div><div id="comment-12999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

