+++
type = "question"
title = "Cant start Wireshark after new install"
description = '''After a new clean install of Wireshark tried latest version and 1.99 and niether will start. I clicked on the desktop shortcut or from Windows menu (have also tried the legacy option as well). In the new Windows it starts up, and the loading progress bar stops at ‘Loading module preferences’. The st...'''
date = "2017-01-13T02:48:00Z"
lastmod = "2017-01-14T02:09:00Z"
weight = 58727
keywords = [ "starting", "initializing" ]
aliases = [ "/questions/58727" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cant start Wireshark after new install](/questions/58727/cant-start-wireshark-after-new-install)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58727-score" class="post-score" title="current number of votes">0</div><span id="post-58727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After a new clean install of Wireshark tried latest version and 1.99 and niether will start. I clicked on the desktop shortcut or from Windows menu (have also tried the legacy option as well). In the new Windows it starts up, and the loading progress bar stops at ‘Loading module preferences’. The status bar reads ‘Please wait while Wireshark is initializing …’ If I click into the window at this point it goes grey and (Not Responding) appears in the title bar. I also see Dumpcap in Task Manager and cant kill this process. I'm running Windows 10.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-starting" rel="tag" title="see questions tagged &#39;starting&#39;">starting</span> <span class="post-tag tag-link-initializing" rel="tag" title="see questions tagged &#39;initializing&#39;">initializing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '17, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/3588f453fb61ef41e694db4a6c464df5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Russ&#39;s gravatar image" /><p><span>Russ</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Russ has no accepted answers">0%</span></p></div></div><div id="comments-container-58727" class="comments-container"></div><div id="comment-tools-58727" class="comment-tools"></div><div class="clear"></div><div id="comment-58727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58728"></span>

<div id="answer-container-58728" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58728-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58728-score" class="post-score" title="current number of votes">1</div><span id="post-58728-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Russ has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you describe really looks like a WinPcap issue on Windows 10 that has been discussed several times on this Q&amp;A site. See <a href="https://ask.wireshark.org/questions/48178/wireshark-fails-to-start-on-windows-10">this question</a> for example.</p><p>You could try to deinstall and reinstall WinPcap, running the installer with administrator privileges, or ultimately if it still does not work give a try to <a href="https://nmap.org/npcap/">Npcap</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '17, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jan '17, 03:50</strong> </span></p></div></div><div id="comments-container-58728" class="comments-container"><span id="58757"></span><div id="comment-58757" class="comment"><div id="post-58757-score" class="comment-score"></div><div class="comment-text"><p>When we install with admin privileges works ok until next reboot. Tried npcap and seems to work really well. Thanks</p></div><div id="comment-58757-info" class="comment-info"><span class="comment-age">(14 Jan '17, 02:09)</span> <span class="comment-user userinfo">Russ</span></div></div></div><div id="comment-tools-58728" class="comment-tools"></div><div class="clear"></div><div id="comment-58728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

