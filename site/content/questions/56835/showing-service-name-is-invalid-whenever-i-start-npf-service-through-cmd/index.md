+++
type = "question"
title = "showing service name is invalid whenever  i start npf service through cmd"
description = '''Hello my name is Karan. I&#x27;m currently using windows 7 64-bit. npf.sys is there in drivers and winpcap is also installed in my laptop but whenever I try to start npf service in cmd it shows me the service name is invalid. so what should i do. I opened cmd in administrator mode still getting this outp...'''
date = "2016-10-30T14:09:00Z"
lastmod = "2016-10-31T12:36:00Z"
weight = 56835
keywords = [ "wireshark" ]
aliases = [ "/questions/56835" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [showing service name is invalid whenever i start npf service through cmd](/questions/56835/showing-service-name-is-invalid-whenever-i-start-npf-service-through-cmd)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56835-score" class="post-score" title="current number of votes">0</div><span id="post-56835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello my name is Karan. I'm currently using windows 7 64-bit. npf.sys is there in drivers and winpcap is also installed in my laptop but whenever I try to start npf service in cmd it shows me the service name is invalid. so what should i do. I opened cmd in administrator mode still getting this output. please provide a solution for it. first i downloaded winpcap because I was not sure that it is installed but when I open the .exe file of it, it was showing that you have a newer version of winpcap installed so installation is aborted.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '16, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/26cfc77e3e3c34b6ea1453dc6b3ae62c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karan9537&#39;s gravatar image" /><p><span>karan9537</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karan9537 has no accepted answers">0%</span></p></div></div><div id="comments-container-56835" class="comments-container"><span id="56838"></span><div id="comment-56838" class="comment"><div id="post-56838-score" class="comment-score"></div><div class="comment-text"><p>Can you please add to your question the <strong>exact</strong> command you are entering?</p></div><div id="comment-56838-info" class="comment-info"><span class="comment-age">(30 Oct '16, 14:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="56859"></span><div id="comment-56859" class="comment"><div id="post-56859-score" class="comment-score"></div><div class="comment-text"><p>What does the Help -&gt; About window in Wireshark report? (Please copy and paste the text, rather than trying to post a screenshot.)</p></div><div id="comment-56859-info" class="comment-info"><span class="comment-age">(31 Oct '16, 03:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-56835" class="comment-tools"></div><div class="clear"></div><div id="comment-56835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56839"></span>

<div id="answer-container-56839" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56839-score" class="post-score" title="current number of votes">1</div><span id="post-56839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="karan9537 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might run into difficulties if Wireshark encounters a different version of Winpcap than the one the is bundled in the installer.</p><p>I suggest the following steps:</p><ul><li>Make sure that the extra version of winpcap is not used by any other application</li><li>If another application is using winpcap, please try to "synchronize" the versions</li><li>If it is not possible to align the winpcap versions it might be necessary to use a separate computer for network analysis.</li></ul><p>In my opinion the best way to fix the version problem is:</p><ul><li>Make sure that you download Wireshark from the <a href="https://www.wireshark.org/download.html">original download site</a></li><li>Only use the latest version of Wireshark, as new versions occasionally fix security errors.</li><li>Remove all older instances of Wireshark, winpcap and usbpcap</li><li>Reboot. You should no longer find an npf service.</li><li>Install Wireshark and allow the Wireshark installer to deploy the accompanying version of winpcap</li><li>Given the current problems with the installer, I suggest to delay the installation of usbpcap until you really need it.</li></ul><p>If something fails, the system event log and application event log often give important hints and return codes.</p><p>One last hint: Make sure, that you have administrative rights.</p><p>Good luck and good hunting</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '16, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-56839" class="comments-container"><span id="56846"></span><div id="comment-56846" class="comment"><div id="post-56846-score" class="comment-score"></div><div class="comment-text"><p>Thx for the answer. I will try it and tell you the result</p></div><div id="comment-56846-info" class="comment-info"><span class="comment-age">(30 Oct '16, 23:30)</span> <span class="comment-user userinfo">karan9537</span></div></div></div><div id="comment-tools-56839" class="comment-tools"></div><div class="clear"></div><div id="comment-56839-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56877"></span>

<div id="answer-container-56877" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56877-score" class="post-score" title="current number of votes">0</div><span id="post-56877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>thank you for the concern all of you. i renamed the packet.dll with packet.dll.old and wpcap.dll with wpcap.dll.old and sucessfully installed winpcap and driver is also started. thank you once again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '16, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/26cfc77e3e3c34b6ea1453dc6b3ae62c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karan9537&#39;s gravatar image" /><p><span>karan9537</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karan9537 has no accepted answers">0%</span></p></div></div><div id="comments-container-56877" class="comments-container"></div><div id="comment-tools-56877" class="comment-tools"></div><div class="clear"></div><div id="comment-56877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

