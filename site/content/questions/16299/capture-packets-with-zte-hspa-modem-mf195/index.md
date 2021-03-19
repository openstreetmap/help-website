+++
type = "question"
title = "capture packets with ZTE HSPA Modem MF195"
description = '''Hi All, I discovered wireshark tool since 2 weeks and i&#x27;m facing some issues to use that tool with ZTE Modem MF195. I try with Huawei E367, and the wireshark is detected the interface automatically.  I need help about to use wireshark tool with ZTE HSPA Modem (MF195). BR,'''
date = "2012-11-26T02:13:00Z"
lastmod = "2012-11-26T02:28:00Z"
weight = 16299
keywords = [ "captured" ]
aliases = [ "/questions/16299" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [capture packets with ZTE HSPA Modem MF195](/questions/16299/capture-packets-with-zte-hspa-modem-mf195)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16299-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I discovered wireshark tool since 2 weeks and i'm facing some issues to use that tool with ZTE Modem MF195. I try with Huawei E367, and the wireshark is detected the interface automatically.</p><p>I need help about to use wireshark tool with ZTE HSPA Modem (MF195).</p><p>BR,</p></div><div id="question-tags" class="tags-container tags">captured</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '12, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/e7aaa72d8005167a078f7736c39cf729?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Djo&#39;s gravatar image" /><p>Djo<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Djo has no accepted answers">0%</span></p></div></div><div id="comments-container-16299" class="comments-container"></div><div id="comment-tools-16299" class="comment-tools"></div><div class="clear"></div><div id="comment-16299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16301"></span>

<div id="answer-container-16301" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16301-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As both modems are USB sticks and as Wireshark detects the Huawei device, there is a chance to detect the MF195 as well. Winpcap is the interface for Wireshark regarding the access to the interfaces. So please try this:</p><ul><li>run <code>dumpcap -D -M</code>. If the MF195 is not on the list, try to restart the WinPcap service AFTER you have plugged in the MF195</li><li>restart Winpcap service: <code>sc stop npf</code> and then <code>sc start npf</code> (you need to do this from a <strong>DOS box</strong>, that was <strong>started with Admin privileges</strong>)</li><li>run dumpcap again. If the adapter is on the list. Good. If it's not on the list, you might try to re-install Winpcap. If it's then still not on the list, the driver of the MF195 is somehow incompatible with WinPcap and you're out of luck.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '12, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16301" class="comments-container"><span id="16303"></span><div id="comment-16303" class="comment"><div id="post-16303-score" class="comment-score"></div><div class="comment-text"><p>hi Kurt, Thank you for your help. it's working fine now. Thank you so much.</p><p>BR,</p></div><div id="comment-16303-info" class="comment-info"><span class="comment-age">(26 Nov '12, 03:07)</span> Djo</div></div><span id="16304"></span><div id="comment-16304" class="comment"><div id="post-16304-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-16304-info" class="comment-info"><span class="comment-age">(26 Nov '12, 03:09)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16301" class="comment-tools"></div><div class="clear"></div><div id="comment-16301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

