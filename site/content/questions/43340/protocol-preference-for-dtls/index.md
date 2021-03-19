+++
type = "question"
title = "Protocol preference for DTLS"
description = '''Hi:  I built wireshark 1.12.5 from source on my ubuntu Linux, trying to use the DTLS decryption function. From &quot;Enabled Protocol&quot; i can see DTLS is enabled, but in the protocol preference tab, i don&#x27;t see &quot;DTLS&quot;, and right click on a captured DTLS packet, the &quot;protocol preference&quot; menu is grayed out...'''
date = "2015-06-18T13:11:00Z"
lastmod = "2015-06-18T13:36:00Z"
weight = 43340
keywords = [ "dtls", "protocol", "preferences" ]
aliases = [ "/questions/43340" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Protocol preference for DTLS](/questions/43340/protocol-preference-for-dtls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43340-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi: I built wireshark 1.12.5 from source on my ubuntu Linux, trying to use the DTLS decryption function. From "Enabled Protocol" i can see DTLS is enabled, but in the protocol preference tab, i don't see "DTLS", and right click on a captured DTLS packet, the "protocol preference" menu is grayed out. The downloaded windows version 1.12.5 works fine though. Unfortunately i have to use Linux to capture packets. Any idea why i can't set DTLS protocol preferences?</p><p>Thanks lei</p></div><div id="question-tags" class="tags-container tags">dtls protocol preferences</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '15, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/6c39cdd586a6e713b4457ee65309c4cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lei%20Sun&#39;s gravatar image" /><p>Lei Sun<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lei Sun has no accepted answers">0%</span></p></div></div><div id="comments-container-43340" class="comments-container"></div><div id="comment-tools-43340" class="comment-tools"></div><div class="clear"></div><div id="comment-43340-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43341"></span>

<div id="answer-container-43341" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43341-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ensure to install libgcrypt and libgnutls development packages and recompile Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '15, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43341" class="comments-container"><span id="43348"></span><div id="comment-43348" class="comment"><div id="post-43348-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer, i will try that. Meanwhile, How do I perform decrypt after capturing packet? my DTLS is pre-shared-key, and i put the psk in the protocol preference of the wireshark, but the packet still show as "encryped application data".</p><p>Thanks Lei</p></div><div id="comment-43348-info" class="comment-info"><span class="comment-age">(18 Jun '15, 14:52)</span> Lei Sun</div></div></div><div id="comment-tools-43341" class="comment-tools"></div><div class="clear"></div><div id="comment-43341-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

