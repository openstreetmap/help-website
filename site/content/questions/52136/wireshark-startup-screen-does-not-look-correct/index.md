+++
type = "question"
title = "Wireshark Startup Screen Does Not Look Correct"
description = '''I installed the 64bit version of Wireshark on Windows 10. This screenshot shows what I see when I launch Wireshark which does not look at all like the GUI expected. After restarting my computer, it then went through about a minute of &quot;registering dissectors&quot;. For example &quot;registering dissectors cmd&quot;...'''
date = "2016-05-01T22:22:00Z"
lastmod = "2016-05-03T07:32:00Z"
weight = 52136
keywords = [ "gui", "registering", "dissectors" ]
aliases = [ "/questions/52136" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Startup Screen Does Not Look Correct](/questions/52136/wireshark-startup-screen-does-not-look-correct)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52136-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed the 64bit version of Wireshark on Windows 10. <a href="http://dan-m.com/images/startup-screen.jpg">This screenshot</a> shows what I see when I launch Wireshark which does not look at all like the GUI expected. After restarting my computer, it then went through about a minute of "registering dissectors". For example "registering dissectors cmd" and a whole lot more. Is any of this normal? The startup screen still does not look normal, the same as the first launch of the software.</p></div><div id="question-tags" class="tags-container tags">gui registering dissectors</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '16, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/fe6561bb907e1f798d819ef1dc821fc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanMiller&#39;s gravatar image" /><p>DanMiller<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanMiller has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 May '16, 23:02</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-52136" class="comments-container"><span id="52137"></span><div id="comment-52137" class="comment"><div id="post-52137-score" class="comment-score"></div><div class="comment-text"><p>So what's unusual or incorrect about that screenshot? Nothing looks wrong to me. "It's different from what I see with 1.12" isn't "it's not correct" - the main screen changed significantly between Wireshark 1.12 and Wireshark 2.0, and that's a perfectly normal 2.0 main screen.</p><p>And "registering dissectors" is one of the stages of starting up, and has been before 2.0 - the only difference between the old GTK+ interface in 1.12 and the new Qt interface in 2.0 is that the startup progress indications are part of the main screen in 2.0 but part of a separate splash screen window in 1.12. I'm surprised it takes about a minute on your machine, but maybe that's a Windows vs. OS X issue, or a "your machine vs. my machine" issue.</p></div><div id="comment-52137-info" class="comment-info"><span class="comment-age">(01 May '16, 23:12)</span> Guy Harris ♦♦</div></div><span id="52138"></span><div id="comment-52138" class="comment"><div id="post-52138-score" class="comment-score"></div><div class="comment-text"><p>Request you to create shortcut of wireshark-gtk.exe on your desktop which is the part of installation directory to look same as wireshark older version.</p></div><div id="comment-52138-info" class="comment-info"><span class="comment-age">(01 May '16, 23:29)</span> Dinesh Babu ...</div></div><span id="52147"></span><div id="comment-52147" class="comment"><div id="post-52147-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick reply. I was following along with a training course to learn Wireshark and the opening screen looked much different. I launched the legacy version and that interface looks the way I was expecting. I didn't realize they had changed the interface. Sounds like all is well, thanks!</p></div><div id="comment-52147-info" class="comment-info"><span class="comment-age">(02 May '16, 06:35)</span> DanMiller</div></div><span id="52152"></span><div id="comment-52152" class="comment"><div id="post-52152-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-52152-info" class="comment-info"><span class="comment-age">(02 May '16, 07:16)</span> Jaap ♦</div></div></div><div id="comment-tools-52136" class="comment-tools"></div><div class="clear"></div><div id="comment-52136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52143"></span>

<div id="answer-container-52143" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52143-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Wireshark 2.0.3 default GUI is Qt based, while the 1.x series was GTK+ based by default. The switch to the <a href="https://blog.wireshark.org/2015/11/let-me-tell-you-about-wireshark-2-0/">Qt based default interface</a> has been <a href="https://blog.wireshark.org/2013/10/switching-to-qt/">in the works for quite some time</a> and was the main reason to bump the major release number to 2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '16, 01:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52143" class="comments-container"></div><div id="comment-tools-52143" class="comment-tools"></div><div class="clear"></div><div id="comment-52143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52179"></span>

<div id="answer-container-52179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52179-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To make it easier on yourself, and not have to translate your video training windows over the new interface while learning, re-install Wireshark 2.0.3 and select the "Wireshark Legacy Desktop Icon" from the shortcuts. <img src="https://osqa-ask.wireshark.org/upfiles/sc_cA3ogvY.png" alt="alt text" /></p><p>Then you'll get a Wireshark Legacy icon on the desktop that runs the interface you'll be able to use and follow your video with ease. <img src="https://osqa-ask.wireshark.org/upfiles/sc2.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '16, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/bfa53b64ea6967e45a614981c461a638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coloncm&#39;s gravatar image" /><p>coloncm<br />
<span class="score" title="76 reputation points">76</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coloncm has 2 accepted answers">66%</span></p></img></div></div><div id="comments-container-52179" class="comments-container"></div><div id="comment-tools-52179" class="comment-tools"></div><div class="clear"></div><div id="comment-52179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

