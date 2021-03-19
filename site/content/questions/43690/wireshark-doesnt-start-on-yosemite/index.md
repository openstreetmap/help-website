+++
type = "question"
title = "Wireshark doesn&#x27;t start on Yosemite"
description = '''I have a MACBook Pro (intel i7 / OSX-10 /Yosemite 10.10.3) I downloaded the 64bit version and installed it and it said the installation was successful but the software doesn&#x27;t start???'''
date = "2015-06-29T16:30:00Z"
lastmod = "2015-06-30T16:18:00Z"
weight = 43690
keywords = [ "yosemite" ]
aliases = [ "/questions/43690" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't start on Yosemite](/questions/43690/wireshark-doesnt-start-on-yosemite)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43690-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a MACBook Pro (intel i7 / OSX-10 /Yosemite 10.10.3) I downloaded the 64bit version and installed it and it said the installation was successful but the software doesn't start???</p></div><div id="question-tags" class="tags-container tags">yosemite</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '15, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/50dc0921222f5f9a10318c8ed8bc39a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blebrane&#39;s gravatar image" /><p>blebrane<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blebrane has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jun '15, 20:28</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-43690" class="comments-container"><span id="43691"></span><div id="comment-43691" class="comment"><div id="post-43691-score" class="comment-score"></div><div class="comment-text"><p>Which exact version of Wireshark?</p><p>I know this sounds crazy, but try clicking the app icon and waiting several minutes (yes, <em>minutes</em>). With the Qt-based version of Wireshark (which the Mac OS-X one can be), the first time it runs sometimes takes a very, very long time. I don't know what the holdup is exactly, but Qt does some initialization apparently the first time it runs - though given the length of time, it's probably something timing out/expiring.</p><p>After that first time, it should launch pretty fast from then on.</p></div><div id="comment-43691-info" class="comment-info"><span class="comment-age">(29 Jun '15, 16:56)</span> Hadriel</div></div><span id="43749"></span><div id="comment-43749" class="comment"><div id="post-43749-score" class="comment-score"></div><div class="comment-text"><p>I downloaded and installed version 1.12.6 three times. I also started it and waited for about an hour for it to start. When I start it on my MACbook Pro the menu bar at the top has the Wireshark main title but none of the other menu options. Also when I click wireshark menu title I do not get anything useful in the dropdown menu? Also there is no Help or preference menu items?</p></div><div id="comment-43749-info" class="comment-info"><span class="comment-age">(30 Jun '15, 14:57)</span> blebrane</div></div><span id="43751"></span><div id="comment-43751" class="comment"><div id="post-43751-score" class="comment-score"></div><div class="comment-text"><p>Could it be for some kind of reason, that there is a further dialog open? But you are not able to see this. Try right click at the Wireshark symbol at the dock and look if there are more windows open. -&gt; Just a guess, but I had this behaviour once myself.</p></div><div id="comment-43751-info" class="comment-info"><span class="comment-age">(30 Jun '15, 15:18)</span> Christian_R</div></div><span id="43752"></span><div id="comment-43752" class="comment"><div id="post-43752-score" class="comment-score"></div><div class="comment-text"><p>No, I checked all of that. I even shut down the pc and start it up again and it still doesn't work.</p></div><div id="comment-43752-info" class="comment-info"><span class="comment-age">(30 Jun '15, 15:27)</span> blebrane</div></div><span id="43754"></span><div id="comment-43754" class="comment"><div id="post-43754-score" class="comment-score"></div><div class="comment-text"><p>I just tried 1.12.6, and it's still GTK-based for now, which means it's based on X11/XQuartz, so the menu bar you should see at the top of the screen would be the X11 one. It will show "Wireshark" as the left-most menu name of the top-screen at startup, but should then open a window of the Wireshark application, and the left-most menu item on the top-screen bar will change to "X11". (the actual Wireshark menu items will be in a menu bar inside the application window, as opposed to the top-screen menu bar, unlike most Mac applications)</p><p>So, if that's not happening... what version of OS X are your running? Some people have reported they had to install XQuartz manually. (though I'd do that as a last resort)</p><p>When you installed 1.12.6, did you have a previous version? You usually need to remove it first, by dragging it to the Trash.</p><p>Also check if you already have a "<code>.wireshark</code>" or "<code>.wireshark-etc</code>" folders in your home directory and if so then delete them - note the leading "<code>.</code>" which means they're hidden, and if you can't see them in Finder then delete them through the Terminal ("<code>rm -rf ~/.wireshark; rm-rf ~/.wireshark-etc</code>"). One note with this is deleting these folders will remove your previous preferences, if you had any.</p></div><div id="comment-43754-info" class="comment-info"><span class="comment-age">(30 Jun '15, 15:48)</span> Hadriel</div></div></div><div id="comment-tools-43690" class="comment-tools"></div><div class="clear"></div><div id="comment-43690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43756"></span>

<div id="answer-container-43756" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43756-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There has been a similar question to non starting wireshark: <a href="https://ask.wireshark.org/questions/36367/wireshark-doesnt-start-after-upgrading-to-mac-os-x-yosemite">Wireshark doesnt start after upgrading to yosemite</a> There are a lot of hints where and what you could check. Hope it is usefull to you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 16:18</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-43756" class="comments-container"></div><div id="comment-tools-43756" class="comment-tools"></div><div class="clear"></div><div id="comment-43756-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

