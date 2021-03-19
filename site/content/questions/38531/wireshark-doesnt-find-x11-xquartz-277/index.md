+++
type = "question"
title = "Wireshark doesn&#x27;t find X11 (XQuartz-2.7.7)"
description = '''Hello I upgraded my 10.6.8 MacBook Pro from 2009 to Yosemite (OS 10.10.1) and tried to start Wireshark 1.12.2 First I had to update my X11 which no longer works, so I installed XQuartz-2.7.7 I logged out and in but still when I start Wireshark, I get a dialog to find X11: Choose Application - Where ...'''
date = "2014-12-11T14:22:00Z"
lastmod = "2014-12-16T12:34:00Z"
weight = 38531
keywords = [ "x11", "xquartz", "yosemite" ]
aliases = [ "/questions/38531" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't find X11 (XQuartz-2.7.7)](/questions/38531/wireshark-doesnt-find-x11-xquartz-277)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38531-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I upgraded my 10.6.8 MacBook Pro from 2009 to Yosemite (OS 10.10.1) and tried to start Wireshark 1.12.2 First I had to update my X11 which no longer works, so I installed XQuartz-2.7.7 I logged out and in but still when I start Wireshark, I get a dialog to find X11:</p><p>Choose Application - Where is X11?</p><p>I cannot find XQuartz-2.7.7 in my application list. The link was already set from /usr/X11 to /opt/X11 this wasnt the issue.</p><p>What can I do? How can I find the XQuartz-2.7.7 application to point Wireshark on it? The 'Browse' doesn't allow me to set it to /usr/X11/...</p><p>Thanks</p><p>frank</p></div><div id="question-tags" class="tags-container tags">x11 xquartz yosemite</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '14, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/932f872b04b352a8f3d81288805f08be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="franc&#39;s gravatar image" /><p>franc<br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="franc has 2 accepted answers">40%</span></p></div></div><div id="comments-container-38531" class="comments-container"></div><div id="comment-tools-38531" class="comment-tools"></div><div class="clear"></div><div id="comment-38531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38606"></span>

<div id="answer-container-38606" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38606-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This helped:</p><p><a href="http:///Applications/Utilities/XQuartz.app/Contents/MacOS/X11">http://www.itechlounge.net/2013/10/mac-wireshark-wont-start-and-ask-for-x11-with-osx-mavericks/</a></p><p>I start firstly X11 with:</p><pre><code>/Applications/Utilities/XQuartz.app/Contents/MacOS/X11</code></pre><p>Then I just open Wireshark in my apps drawer and it will start normally. To start XQuartz-X11 I just did a symbolic link (or a little shellscript) to the app drawer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '14, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/932f872b04b352a8f3d81288805f08be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="franc&#39;s gravatar image" /><p>franc<br />
<span class="score" title="96 reputation points">96</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="franc has 2 accepted answers">40%</span></p></div></div><div id="comments-container-38606" class="comments-container"></div><div id="comment-tools-38606" class="comment-tools"></div><div class="clear"></div><div id="comment-38606-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

