+++
type = "question"
title = "Wireshark OS X install / X11 / permissions question"
description = '''I&#x27;m preparing WS OS X install hints for an international Cisco teachers conf next week.  In the past, the WS OSX installer has had a utilities folder with a script / readme for setting up a first time install.  I notice the current installer has a single file - no utilities folder.  Also, in the pas...'''
date = "2011-06-21T09:34:00Z"
lastmod = "2011-06-24T15:07:00Z"
weight = 4646
keywords = [ "osx", "installation" ]
aliases = [ "/questions/4646" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark OS X install / X11 / permissions question](/questions/4646/wireshark-os-x-install-x11-permissions-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4646-score" class="post-score" title="current number of votes">0</div><span id="post-4646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm preparing WS OS X install hints for an international Cisco teachers conf next week. In the past, the WS OSX installer has had a utilities folder with a script / readme for setting up a first time install. I notice the current installer has a single file - no utilities folder. Also, in the past the readme has not been accurate, and the startup script did not work, so I've handheld my students through first time WS installs. There were several BASH commands that had to be run. So - my questions - 1 I presume x11 still must be installed /before/ wireshark is installed 2 Does the current installer properly put everything in running order with perms on the right folders, or is there still that dance to do on first installs, creating foldes and setting permissions?</p><p>Thanks very much in advance - wish I had a Mac without WS to verify -</p><p>Regards, John Gonder</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '11, 09:34</strong></p><img src="https://secure.gravatar.com/avatar/52ff5d6b59bd5798a667a6f346a52421?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packetlevel&#39;s gravatar image" /><p><span>packetlevel</span><br />
<span class="score" title="1 reputation points">1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packetlevel has no accepted answers">0%</span></p></div></div><div id="comments-container-4646" class="comments-container"></div><div id="comment-tools-4646" class="comment-tools"></div><div class="clear"></div><div id="comment-4646-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4704"></span>

<div id="answer-container-4704" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4704-score" class="post-score" title="current number of votes">0</div><span id="post-4704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Yes, you still need X11 to run Wireshark, so you must install it before you run Wireshark.</li><li>The current installer should properly install the ChmodBPF startup item in the right folder with the proper permissions, and even add the user doing the installation to the right group and run the startup item, so Wireshark should be ready to use once it's installed. If you requested them, it should also install the command-line tools. (That's why we went with an installer rather than drag-install.)</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '11, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4704" class="comments-container"><span id="4708"></span><div id="comment-4708" class="comment"><div id="post-4708-score" class="comment-score"></div><div class="comment-text"><p>Thanks for chiming in - after posting the other day I did some testing. I did an install of 1.6 on a new macmini. X11, being part of the default install these days is not a problem anymore, yes. The current installer 1) puts the app in 2) creates the Library/local/bin folder, although with /aliases/ to the command line binaries, not they themselves. WS did not run, even after a reboot. It would appear in the dock for a second then disappear, even if x11 was already running (which was once a problem - WS could not load x11 by itself - hence my checking for this). This unit was 10.6.4 out of the box - so, I updated it to 10.6.7, all updates, cold booted, removed then re-installed WS1.6, checked perms on Library/local/bin, cold booted and WS ran and saw all NICs. The last installer that ran first time with no need for CLI help was 1.4.0 (I put it on our new iMacs previously). Hope this helps in seeing what variable there might be in this process. My problem is I run out of new machines to test install variations on. Once WS has run, subsequent updates work. It's just at the start of semesters as new groups of students put it in for the first time that I see the current gotchas. It makes it hard for me to be scientific about troubleshooting - we just shotgun it til it works; e.g. install 1.4.0, then update. Sorry I don't have anything more precise to offer in terms of data. If you have a specific test that might be helpful, I could do that on one of the remaining new Macs in July. Regards, John Gonder</p></div><div id="comment-4708-info" class="comment-info"><span class="comment-age">(23 Jun '11, 13:41)</span> <span class="comment-user userinfo">packetlevel</span></div></div><span id="4709"></span><div id="comment-4709" class="comment"><div id="post-4709-score" class="comment-score"></div><div class="comment-text"><p>(The only things that should be posted as answers are answers to the original question; this is a Q&amp;A site, not a forum. I converted your reply to a comment.)</p><p>The problem you're seeing is a <em>separate</em> problem, due to a number of issues; if all of the support libraries used by Wireshark, including GTK+, were built against the SDK rather than the libraries on the build system, that wouldn't happen. The update to 10.6.7 probably would have sufficed, as it would have updated libfreetype to the same version as the one on the Wireshark Snow Leopard buildbot.</p></div><div id="comment-4709-info" class="comment-info"><span class="comment-age">(23 Jun '11, 13:47)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4704" class="comment-tools"></div><div class="clear"></div><div id="comment-4704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4745"></span>

<div id="answer-container-4745" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4745-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4745-score" class="post-score" title="current number of votes">0</div><span id="post-4745-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A comment, perhaps not an answer. I experienced the same "...It would appear in the dock for a second then disappear" issue on a MacBook Pro running 10.6.7 (and now 10.6.8) and discovered my problem: I have an older MBP and it's a Core Duo 32bit CPU. The Wireshark 1.6.0 download labeled as OS X 10.6 (Snow Leopard) Intel 64-bit .dmg did <em>not</em> work, despite reading all help articles here. What <em>did</em> work immediately is the download labeled OS X 10.5 (Leopard) Intel 32-bit .dmg. Having used Wireshark successfully, including the various install issues with permissions etc. prior to a clean re-install/full update cycle I was a bit baffled. Perhaps the download that works on the Core Duo CPUs without any issues could be amended to note that it works with Snow leopard, on 32 bit CPUs (like my early 2006 MBP, and a similar mini)...</p><p>jb</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '11, 15:07</strong></p><img src="https://secure.gravatar.com/avatar/04079086e0c64af1e86408b2b8d6b872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exmixer&#39;s gravatar image" /><p><span>exmixer</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exmixer has no accepted answers">0%</span></p></div></div><div id="comments-container-4745" class="comments-container"></div><div id="comment-tools-4745" class="comment-tools"></div><div class="clear"></div><div id="comment-4745-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

