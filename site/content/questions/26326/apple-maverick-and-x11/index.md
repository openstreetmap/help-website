+++
type = "question"
title = "Apple Maverick and X11"
description = '''Hi seems that after the new Apple update Maverick. wireshark is not working. Anyone else noticing it ?, better know how to fix it ?.  Error To open &quot;wireshark-bin&quot;you need isntall X11 Would likt ot install X11 now? 2 options 1) cancel 2) Continue --&amp;gt; http://support.apple.com/kb/HT5293 either via ...'''
date = "2013-10-23T09:02:00Z"
lastmod = "2014-05-14T06:26:00Z"
weight = 26326
keywords = [ "10.9", "osx", "pro", "maverick", "macbook" ]
aliases = [ "/questions/26326" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [Apple Maverick and X11](/questions/26326/apple-maverick-and-x11)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26326-score" class="post-score" title="current number of votes">3</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi seems that after the new Apple update Maverick. wireshark is not working. Anyone else noticing it ?, better know how to fix it ?. Error To open "wireshark-bin"you need isntall X11 Would likt ot install X11 now? 2 options 1) cancel 2) Continue --&gt; <a href="http://support.apple.com/kb/HT5293">http://support.apple.com/kb/HT5293</a></p><p>either via the app or command line same issue mac book pro 10.9</p><p>Wireshark 1.10.2 XQuartz 2.7.4 (xorg-server 1.13.0) Problem: X11 is not updated ( though it's the latest version)</p></div><div id="question-tags" class="tags-container tags">10.9 osx pro maverick macbook</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/bbfc7689016d203b00becddcebf7c751?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paisa4ever&#39;s gravatar image" /><p>Paisa4ever<br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paisa4ever has no accepted answers">0%</span></p></div></div><div id="comments-container-26326" class="comments-container"></div><div id="comment-tools-26326" class="comment-tools"></div><div class="clear"></div><div id="comment-26326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

6 Answers:

</div>

</div>

<span id="28351"></span>

<div id="answer-container-28351" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28351-score" class="post-score" title="current number of votes">6</div></div></td><td><div class="item-right"><div class="answer-body"><p>I am running Mavericks and the items suggested here did not work for me. I quit Wireshark and XQuartz and reinstalled XQuartz and saw no change in behaviour. Next, I deleted the '/opt/X11' hierarchy and reinstalled XQuartz. No change. What did work was a suggestion found here:</p><p><a href="http://www.itechlounge.net/2013/10/mac-wireshark-wont-start-and-ask-for-x11-with-osx-mavericks/">http://www.itechlounge.net/2013/10/mac-wireshark-wont-start-and-ask-for-x11-with-osx-mavericks/</a></p><p>I knew I had the latest XQuartz 2.7.5 so I launched it. In its Applications menu I added Wireshark as one of the items using the "/Applications/Wireshark.app/Contents/MacOS/Wireshark" path. After 12-20 seconds, Wireshark launched from that menu displayed its main window. I exited all and then double-clicked Wireshark in the Applications folder. Success. Tried a couple more times (from the Doc 'Applications', etc.) and saw success each time.</p><p>By the way, I later tried to get Wireshark running on another Mac running Mavericks. I finally got it running but wasn't sure what actions helped.</p><p>This morning I uninstalled XQuartz and Wireshark and restarted, returning to a clean state. I then re-installed XQuartz and Wireshark. Launching Wireshark nothing appeared to happen for 1 minute 24 seconds before the main window appeared. I did not have to add it to the XQuartz application list. I mention this because you have to be patient. I'm just not used to having no feedback while a background process sets itself up before displaying its application window. Be forewarned.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '13, 21:40</strong></p><img src="https://secure.gravatar.com/avatar/c6e95f7befe3d7b84f94071bd1e31d3b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pjcozsyd&#39;s gravatar image" /><p>pjcozsyd<br />
<span class="score" title="101 reputation points">101</span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pjcozsyd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Dec '13, 16:05</p></div></div><div id="comments-container-28351" class="comments-container"><span id="28490"></span><div id="comment-28490" class="comment"><div id="post-28490-score" class="comment-score"></div><div class="comment-text"><p>Thank you, I thought the program froze and quit it always before a minute was up. It turns out you are right! It took a minute, thirty to start up.</p></div><div id="comment-28490-info" class="comment-info"><span class="comment-age">(30 Dec '13, 18:13)</span> Dygear</div></div></div><div id="comment-tools-28351" class="comment-tools"></div><div class="clear"></div><div id="comment-28351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26328"></span>

<div id="answer-container-26328" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26328-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ran across the same issue due to a Mac OS Mavericks update. My solution was to reinstall XQuartz (2.7.4) then relaunch Wireshark via the app. It took longer than previously to start, though within 10 seconds (MacBook Air Mid 2011) Wireshark came up. I've run it to confirm all is well.</p><p>Good luck with your situation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '13, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/f8c9295de767e10e7cfe22381e79cbad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SwiftAero&#39;s gravatar image" /><p>SwiftAero<br />
<span class="score" title="56 reputation points">56</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SwiftAero has no accepted answers">0%</span></p></div></div><div id="comments-container-26328" class="comments-container"><span id="26330"></span><div id="comment-26330" class="comment"><div id="post-26330-score" class="comment-score"></div><div class="comment-text"><p>Hi SwiftAreo</p><p>Thanks your tip works also on macbook proI did some succesful tests see below.</p><p>in opended Terminal.app open /opt</p><p>x11 folder visible -trashed it</p><p>Down loaded and reinstalled <a href="http://xquartz.macosforge.org/landing/">http://xquartz.macosforge.org/landing/</a></p><p>Wireshark Version 1.10.0</p><p>Status : it works!</p><p>checks: open /Applications/Wireshark.app/ OK Working with saved file OK working with capturing interface OK</p></div><div id="comment-26330-info" class="comment-info"><span class="comment-age">(23 Oct '13, 12:02)</span> Paisa4ever</div></div><span id="26344"></span><div id="comment-26344" class="comment"><div id="post-26344-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-26344-info" class="comment-info"><span class="comment-age">(23 Oct '13, 18:08)</span> grahamb ♦</div></div><span id="26390"></span><div id="comment-26390" class="comment"><div id="post-26390-score" class="comment-score"></div><div class="comment-text"><p>I had the same problem with X11 not working after Mavericks install. I re-installed X11 (XQuartz 2.7.4) and that <em>sort of</em> worked. But now, if I start up an xterm, it comes up on the left side of my left-most monitor and is NOT movable across my screen! So, something else is broken here now, probably when then changed the multi-screen behavior.<br />
</p></div><div id="comment-26390-info" class="comment-info"><span class="comment-age">(24 Oct '13, 21:28)</span> Christopher ...</div></div><span id="26401"></span><div id="comment-26401" class="comment"><div id="post-26401-score" class="comment-score"></div><div class="comment-text"><p>The problem seem to that X11Quartz does not know that on the second screen a menu bar exists. And the window decoration is hinding under the menu bar. Lets hope for a new xquartz version soon.</p></div><div id="comment-26401-info" class="comment-info"><span class="comment-age">(25 Oct '13, 08:30)</span> plaisthos</div></div></div><div id="comment-tools-26328" class="comment-tools"></div><div class="clear"></div><div id="comment-26328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31778"></span>

<div id="answer-container-31778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31778-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well the answer for me is pretty simple. After starting X11 and Wireshark, Wiresharks asks where Quartz is. I did not found it on the list of programs, so I pressed the Browse Button on the bottom left of the program window and found Quartz in the program-&gt;Utilities Folder. I clicked on it, pressed open, and after a few seconds Wireshark started up.</p><p>Hope this helps others, now I have to understand Wireshark:-)</p><p>OS X 10.9.2 / Quartz 2.7.5 / Wireshark Version 1.10.6 (v1.10.6 from master-1.10)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '14, 01:12</strong></p><img src="https://secure.gravatar.com/avatar/7afe0c3788697f1c779a2c83d4017144?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Beni&#39;s gravatar image" /><p>Beni<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Beni has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Apr '14, 01:14</p></div></div><div id="comments-container-31778" class="comments-container"><span id="31918"></span><div id="comment-31918" class="comment"><div id="post-31918-score" class="comment-score"></div><div class="comment-text"><p>This is the solution. Just browse to Applications → Utilities → Quartz.</p></div><div id="comment-31918-info" class="comment-info"><span class="comment-age">(17 Apr '14, 02:49)</span> Mathias Bynens</div></div></div><div id="comment-tools-31778" class="comment-tools"></div><div class="clear"></div><div id="comment-31778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32794"></span>

<div id="answer-container-32794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32794-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may have a ".wireshark" or a ".wireshark-etc" folder in your home folder, I deleted both and restarted wireshark. Runs fine from now on ... and nicely told me that the first startup may take a little time to build the font-cache.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '14, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/5af174bfe178280b6c4e3f611a6ba1d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hwde&#39;s gravatar image" /><p>hwde<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hwde has no accepted answers">0%</span></p></div></div><div id="comments-container-32794" class="comments-container"><span id="33985"></span><div id="comment-33985" class="comment"><div id="post-33985-score" class="comment-score"></div><div class="comment-text"><p>This worked for me.</p></div><div id="comment-33985-info" class="comment-info"><span class="comment-age">(20 Jun '14, 04:10)</span> abd3721</div></div></div><div id="comment-tools-32794" class="comment-tools"></div><div class="clear"></div><div id="comment-32794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26566"></span>

<div id="answer-container-26566" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26566-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Christopher, an alternative is to use the 4 fingers up trick with mac, and drag your window to the other screen. I guess you're already using this trick, but I found useful to remind it for other users. :)</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '13, 02:44</strong></p><img src="https://secure.gravatar.com/avatar/ce1699691e312636608aa875ccf9d86d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amid&#39;s gravatar image" /><p>amid<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amid has no accepted answers">0%</span></p></div></div><div id="comments-container-26566" class="comments-container"></div><div id="comment-tools-26566" class="comment-tools"></div><div class="clear"></div><div id="comment-26566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27369"></span>

<div id="answer-container-27369" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27369-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is a new update of XQuartz and its made for Mavericks</p><p><a href="http://xquartz.macosforge.org/landing/">http://xquartz.macosforge.org/landing/</a></p><p>Good Luck :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '13, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/37fac151832360c11bf6f3ca9750a12e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sindri%20%C3%9E%C3%B3r&#39;s gravatar image" /><p>Sindri Þór<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sindri Þór has no accepted answers">0%</span></p></div></div><div id="comments-container-27369" class="comments-container"><span id="31917"></span><div id="comment-31917" class="comment"><div id="post-31917-score" class="comment-score"></div><div class="comment-text"><p>I’m still having the issue with that version (2.7.5).</p></div><div id="comment-31917-info" class="comment-info"><span class="comment-age">(17 Apr '14, 02:48)</span> Mathias Bynens</div></div></div><div id="comment-tools-27369" class="comment-tools"></div><div class="clear"></div><div id="comment-27369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

