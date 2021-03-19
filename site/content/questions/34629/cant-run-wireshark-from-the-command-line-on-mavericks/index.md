+++
type = "question"
title = "Can&#x27;t run Wireshark from the command line on Mavericks"
description = '''Hi, it seems I can&#x27;t install wireshark on my mac running Mavericks. I have downloaded and linked it to Quartz. However, when I run the command /Applications/Wireshark.app/Contents/MacOs/Wireshark a pop-up comes up saying &quot;Error loading MenuBar.nib&quot;. What is it? Does anyone know how to overcome this ...'''
date = "2014-07-14T08:11:00Z"
lastmod = "2014-07-14T18:11:00Z"
weight = 34629
keywords = [ "run", "command-line", "mavericks", "wireshark" ]
aliases = [ "/questions/34629" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't run Wireshark from the command line on Mavericks](/questions/34629/cant-run-wireshark-from-the-command-line-on-mavericks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34629-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>it seems I can't install wireshark on my mac running Mavericks. I have downloaded and linked it to Quartz. However, when I run the command /Applications/Wireshark.app/Contents/MacOs/Wireshark a pop-up comes up saying "Error loading MenuBar.nib".</p><p>What is it? Does anyone know how to overcome this issue?</p><p>Thanks guys!</p></div><div id="question-tags" class="tags-container tags">run command-line mavericks wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jul '14, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/3417257ae78ec81e54f524e1291950c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NikasB&#39;s gravatar image" /><p>NikasB<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NikasB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Jul '14, 18:12</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-34629" class="comments-container"></div><div id="comment-tools-34629" class="comment-tools"></div><div class="clear"></div><div id="comment-34629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34639"></span>

<div id="answer-container-34639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34639-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What is it?</p></blockquote><p>An indication that, for better or worse, you can't directly run the program <code>/Applications/Wireshark.app/Contents/MacOS/Wireshark</code> from the command line.</p><blockquote><p>Does anyone know how to overcome this issue?</p></blockquote><p>Either run it by opening up your Applications folder and double-clicking the Wireshark icon or by running the command <code>open /Applications/Wireshark.app</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jul '14, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34639" class="comments-container"><span id="34646"></span><div id="comment-34646" class="comment"><div id="post-34646-score" class="comment-score"></div><div class="comment-text"><p>Still not working... The terminal tells me something like this: <em>Jul 15 11:30:53 localhost Wireshark[2427] &lt;error&gt;: The function `CGContextErase' is obsolete and will be removed in an upcoming update. Unfortunately, this application, or a library it uses, is using this obsolete function, and is thereby contributing to an overall degradation of system performance.</em></p><p>I'm about to give up</p></div><div id="comment-34646-info" class="comment-info"><span class="comment-age">(15 Jul '14, 02:37)</span> NikasB</div></div><span id="34675"></span><div id="comment-34675" class="comment"><div id="post-34675-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark is this? Is this a version from wireshark.org or is it a version from MacPorts or Fink?</p></div><div id="comment-34675-info" class="comment-info"><span class="comment-age">(15 Jul '14, 11:57)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-34639" class="comment-tools"></div><div class="clear"></div><div id="comment-34639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

