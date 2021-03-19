+++
type = "question"
title = "Wireshark 2.0.2 install error - close associated program"
description = '''I&#x27;m trying to install 2.0.2 64 bit and I get the error: Wireshark or one of its associated programs is running. Please close it first. I also tried uninstalling the older 32 bit program and I get the same error.'''
date = "2016-03-21T11:02:00Z"
lastmod = "2016-03-21T13:38:00Z"
weight = 51075
keywords = [ "install", "error" ]
aliases = [ "/questions/51075" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.0.2 install error - close associated program](/questions/51075/wireshark-202-install-error-close-associated-program)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51075-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to install 2.0.2 64 bit and I get the error: Wireshark or one of its associated programs is running. Please close it first.</p><p>I also tried uninstalling the older 32 bit program and I get the same error.</p></div><div id="question-tags" class="tags-container tags">install error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '16, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/e12134161af2534b5ed58692ed94ef5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rod%20Carty&#39;s gravatar image" /><p>Rod Carty<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rod Carty has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jul '16, 15:50</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-51075" class="comments-container"></div><div id="comment-tools-51075" class="comment-tools"></div><div class="clear"></div><div id="comment-51075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51076"></span>

<div id="answer-container-51076" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51076-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Likely to be dumpcap.exe. Can you check via Task Manager for a running instance? If found, try to stop it, if you can't, reboot and check again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '16, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51076" class="comments-container"><span id="51082"></span><div id="comment-51082" class="comment"><div id="post-51082-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that was it.</p></div><div id="comment-51082-info" class="comment-info"><span class="comment-age">(22 Mar '16, 05:00)</span> Rod Carty</div></div><span id="51083"></span><div id="comment-51083" class="comment"><div id="post-51083-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-51083-info" class="comment-info"><span class="comment-age">(22 Mar '16, 05:13)</span> grahamb ♦</div></div><span id="56233"></span><div id="comment-56233" class="comment"><div id="post-56233-score" class="comment-score"></div><div class="comment-text"><p>I have the same problem. There is no dumpcap.exe of or anything related to WireSharp running and after a reboot the problem is still there. I also am unable to install Winpcap. I can't find any process or DLL in Proces Explorer which can cause this error.</p></div><div id="comment-56233-info" class="comment-info"><span class="comment-age">(08 Oct '16, 09:30)</span> Daytona12</div></div><span id="56235"></span><div id="comment-56235" class="comment"><div id="post-56235-score" class="comment-score"></div><div class="comment-text"><p>Have you downloaded the Wireshark installer from the web browser, or has a running Wireshark downloaded the installer and offered you to upgrade?</p></div><div id="comment-56235-info" class="comment-info"><span class="comment-age">(08 Oct '16, 10:04)</span> sindy</div></div></div><div id="comment-tools-51076" class="comment-tools"></div><div class="clear"></div><div id="comment-51076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

