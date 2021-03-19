+++
type = "question"
title = "How to find SIP password for the existing account in Linksys SPA2102 phone adapter?"
description = '''How to find SIP password for the existing account in Linksys SPA2102 phone adapter with Wireshark? What should be setup/connection scheme between modem, SPA2102 and PC?'''
date = "2015-10-09T14:15:00Z"
lastmod = "2015-10-11T04:58:00Z"
weight = 46439
keywords = [ "connectivity", "password", "packets", "sniff", "voip" ]
aliases = [ "/questions/46439" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to find SIP password for the existing account in Linksys SPA2102 phone adapter?](/questions/46439/how-to-find-sip-password-for-the-existing-account-in-linksys-spa2102-phone-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to find SIP password for the existing account in Linksys SPA2102 phone adapter with Wireshark? What should be setup/connection scheme between modem, SPA2102 and PC?</p></div><div id="question-tags" class="tags-container tags">connectivity password packets sniff voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '15, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/246308319911b02b765397caa24b76c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quantex&#39;s gravatar image" /><p>quantex<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quantex has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '15, 16:42</p></div></div><div id="comments-container-46439" class="comments-container"></div><div id="comment-tools-46439" class="comment-tools"></div><div class="clear"></div><div id="comment-46439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46451"></span>

<div id="answer-container-46451" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46451-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please read the <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture Setup Wiki</a>. It explains how to capture ethernet frames.</p><blockquote><p><a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a><br />
</p></blockquote><p>In your case, a <a href="https://ask.wireshark.org/questions/13892/port-mirror-switch">small switch with port mirroring capabilities</a>, would be the best option.</p><p><strong>Hint</strong>: You you are using <strong><a href="http://wiki.linuxwall.info/doku.php/en:ressources:dossiers:voip:tls_sips_rtps">secure SIP</a></strong> the whole SIP communication, including the password will be encrypted, and you won't see it!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '15, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-46451" class="comments-container"><span id="46471"></span><div id="comment-46471" class="comment"><div id="post-46471-score" class="comment-score"></div><div class="comment-text"><p>Thank you for advice. Will the <strong>Hub</strong> be suitable for this purpose?</p></div><div id="comment-46471-info" class="comment-info"><span class="comment-age">(12 Oct '15, 13:44)</span> quantex</div></div><span id="46474"></span><div id="comment-46474" class="comment"><div id="post-46474-score" class="comment-score"></div><div class="comment-text"><p>Sure, but it's hard to get a hub these days....</p></div><div id="comment-46474-info" class="comment-info"><span class="comment-age">(12 Oct '15, 14:00)</span> Kurt Knochner ♦</div></div><span id="46477"></span><div id="comment-46477" class="comment"><div id="post-46477-score" class="comment-score"></div><div class="comment-text"><p>Luckily, I have a true Hub.</p></div><div id="comment-46477-info" class="comment-info"><span class="comment-age">(12 Oct '15, 14:28)</span> quantex</div></div><span id="46478"></span><div id="comment-46478" class="comment"><div id="post-46478-score" class="comment-score"></div><div class="comment-text"><p>Good luck!</p></div><div id="comment-46478-info" class="comment-info"><span class="comment-age">(12 Oct '15, 14:38)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46451" class="comment-tools"></div><div class="clear"></div><div id="comment-46451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

