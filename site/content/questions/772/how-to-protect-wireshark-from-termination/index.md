+++
type = "question"
title = "How to protect wireshark from termination?"
description = '''Some application shutdown after start using wireshark or terminate wireshark after it launced. How to protect wireshark from termination? Thank you.'''
date = "2010-11-01T18:35:00Z"
lastmod = "2010-11-03T19:35:00Z"
weight = 772
keywords = [ "protect", "wireshark" ]
aliases = [ "/questions/772" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to protect wireshark from termination?](/questions/772/how-to-protect-wireshark-from-termination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-772-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Some application shutdown after start using wireshark or terminate wireshark after it launced. How to protect wireshark from termination?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">protect wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '10, 18:35</strong></p><img src="https://secure.gravatar.com/avatar/d955b61ad91c6440c44121c7c4d6f0f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TSSENE&#39;s gravatar image" /><p>TSSENE<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TSSENE has no accepted answers">0%</span></p></div></div><div id="comments-container-772" class="comments-container"><span id="787"></span><div id="comment-787" class="comment"><div id="post-787-score" class="comment-score"></div><div class="comment-text"><p>It's not a virus or trojan. I was try to rename wireshark before posting this but it's can't help. Yes, It's prevent wireshark to capture, I know. So, How to protect wirehark from terminate?</p></div><div id="comment-787-info" class="comment-info"><span class="comment-age">(02 Nov '10, 19:52)</span> TSSENE</div></div></div><div id="comment-tools-772" class="comment-tools"></div><div class="clear"></div><div id="comment-772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="781"></span>

<div id="answer-container-781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-781-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is Wireshark is terminated immediately after you launch it? If so, your system may be infected with a trojan. <a href="http://www.theregister.co.uk/2009/03/07/conficker_upgrade/">Conficker</a> and the fake <a href="http://www.microsoft.com/security/portal/Threat/Encyclopedia/Entry.aspx?Name=WiresharkAntivirus">Wireshark Antivirus</a> will both kill any instances of Wireshark they find running, and I'd assume other malware does the same thing.</p><p>If that is the case you might be able to work around the problem by renaming the wireshark.exe executable but that won't fix the more serious underlying issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '10, 11:38</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-781" class="comments-container"></div><div id="comment-tools-781" class="comment-tools"></div><div class="clear"></div><div id="comment-781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="780"></span>

<div id="answer-container-780" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-780-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you up to something shady?????????</p><p>If something is hunting down WireShark specifically then it's probably trying to prevent you from gathering a capture. You can try to rename the WireShark.exe to something else before running it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '10, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-780" class="comments-container"></div><div id="comment-tools-780" class="comment-tools"></div><div class="clear"></div><div id="comment-780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="804"></span>

<div id="answer-container-804" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-804-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've seen this one as well - definitely a trojan.</p><p>Start off by using an up-to-date malware killer; I used Malwarebytes free anti-malware package. I then used Spybot S&amp;D to double-check and immunize.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '10, 19:35</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-804" class="comments-container"></div><div id="comment-tools-804" class="comment-tools"></div><div class="clear"></div><div id="comment-804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

