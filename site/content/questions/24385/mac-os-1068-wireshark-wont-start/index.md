+++
type = "question"
title = "Mac OS 10.6.8 Wireshark won&#x27;t start"
description = '''I just installed Wireshark on my MacBook Pro running 10.6.8. When I try to open Wireshark it closes immediately. Attempting to run it from the command line gives the error: $ ./Applications/Wireshark.app/Contents/MacOS/Wireshark   ...  dyld: Library not loaded: /usr/X11/lib/libcairo.2.dylib  Referen...'''
date = "2013-09-05T10:27:00Z"
lastmod = "2013-09-05T13:29:00Z"
weight = 24385
keywords = [ "mac" ]
aliases = [ "/questions/24385" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OS 10.6.8 Wireshark won't start](/questions/24385/mac-os-1068-wireshark-wont-start)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24385-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just installed Wireshark on my MacBook Pro running 10.6.8. When I try to open Wireshark it closes immediately. Attempting to run it from the command line gives the error:</p><pre><code>$ ./Applications/Wireshark.app/Contents/MacOS/Wireshark

    ...

dyld: Library not loaded: /usr/X11/lib/libcairo.2.dylib
  Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/wireshark-bin
  Reason: Incompatible library version: wireshark-bin requires version 11003.0.0 or later, but libcairo.2.dylib provides version 10803.0.0</code></pre><p>Assistance?</p></div><div id="question-tags" class="tags-container tags">mac</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '13, 10:27</strong></p><img src="https://secure.gravatar.com/avatar/6348753cd5f81344db602835ae5d208a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ekohlenberg&#39;s gravatar image" /><p>ekohlenberg<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ekohlenberg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Sep '13, 11:36</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-24385" class="comments-container"><span id="24389"></span><div id="comment-24389" class="comment"><div id="post-24389-score" class="comment-score"></div><div class="comment-text"><p>Which version of Wireshark did you download and install?</p></div><div id="comment-24389-info" class="comment-info"><span class="comment-age">(05 Sep '13, 11:36)</span> Guy Harris ♦♦</div></div><span id="24395"></span><div id="comment-24395" class="comment"><div id="post-24395-score" class="comment-score"></div><div class="comment-text"><p>I'm having the same issue, with WS 1.10.1 on 10.6.8, a colleague of mine ended up having to mess with XQuartz in order to get it working. but I haven't had much luck yet.</p></div><div id="comment-24395-info" class="comment-info"><span class="comment-age">(05 Sep '13, 12:55)</span> Hoss</div></div></div><div id="comment-tools-24385" class="comment-tools"></div><div class="clear"></div><div id="comment-24385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24396"></span>

<div id="answer-container-24396" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24396-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5937">bug 5937</a>; you will either have to wait for Wireshark 1.10.2 to come out or try one of the Wireshark-1.10.2pre1 builds from the <a href="http://www.wireshark.org/download/prerelease/">prerelease download directory</a> (unless you're on a 32-bit machine, you want to download one of the Wireshark 1.10.2pre1-XXX Intel 64.dmg builds once one shows up - there's currently no build of that sort there right now as I type this; if you're on a 32-bit machine, get one of the Wireshark 1.10.2pre1-XXX Intel 32.dmg builds, and pick the one with the largest value of XXX).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '13, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24396" class="comments-container"><span id="24398"></span><div id="comment-24398" class="comment"><div id="post-24398-score" class="comment-score"></div><div class="comment-text"><p>Like a charm that worked for me, Thanks!</p></div><div id="comment-24398-info" class="comment-info"><span class="comment-age">(05 Sep '13, 13:37)</span> Hoss</div></div></div><div id="comment-tools-24396" class="comment-tools"></div><div class="clear"></div><div id="comment-24396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

