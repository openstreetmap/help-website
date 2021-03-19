+++
type = "question"
title = "OS X 10.6 Install Error"
description = '''Hi, Any thoughts on OS X 10.6 error on Wireshark launch error: root# Wireshark  dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/Wireshark-bin Reason: Incompatible library version: Wireshark-bin requires version 13.0.0 or ...'''
date = "2011-03-13T03:29:00Z"
lastmod = "2011-11-03T03:43:00Z"
weight = 2792
keywords = [ "dylib", "osx", "error", "13.0.0", "launch" ]
aliases = [ "/questions/2792" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [OS X 10.6 Install Error](/questions/2792/os-x-106-install-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2792-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Any thoughts on OS X 10.6 error on Wireshark launch error:</p><pre><code>root# Wireshark 
dyld: Library not loaded: /usr/X11/lib/libfreetype.6.dylib   Referenced from: /Applications/Wireshark.app/Contents/Resources/bin/Wireshark-bin Reason: Incompatible library version: Wireshark-bin requires version 13.0.0 or later, but libfreetype.6.dylib provides version 10.0.0 Trace/BPT trap</code></pre><p>OS has Xcode/X11/XQuartz - app just won't launch.</p></div><div id="question-tags" class="tags-container tags">dylib osx error 13.0.0 launch</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '11, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/fedf6852dfe82e51099fab5b847a01db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gowrann&#39;s gravatar image" /><p>gowrann<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gowrann has no accepted answers">0%</span></p></div></div><div id="comments-container-2792" class="comments-container"></div><div id="comment-tools-2792" class="comment-tools"></div><div class="clear"></div><div id="comment-2792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2823"></span>

<div id="answer-container-2823" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2823-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try running X11 by itself. Then go under the X11 menu and choose "About X11" and let us know the version #. I would ASSume that the latest WireShark would work with the stock X11 that comes with 10.6. It's possible that you've installed other libraries that have overwritten newer libs with older ones. You can get the latest X11 from the XQuartz project here http://xquartz.macosforge.org/trac/wiki</p><p>You have to reinstall the XQuartz project's X11 after every OS update.</p><p>Good Luck</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-2823" class="comments-container"></div><div id="comment-tools-2823" class="comment-tools"></div><div class="clear"></div><div id="comment-2823-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7216"></span>

<div id="answer-container-7216" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7216-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've already tried everything mentioned on this an other threads but the only thing that fixed the issue was using macports to install the app. following instructions found here http://www.csc.gatech.edu/~copeland/3076/info/Wireshark-OS_10.6.txt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '11, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/33ea6457b2390af9ca9b3c1d66ed1f93?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elhtmlnoexiste&#39;s gravatar image" /><p>elhtmlnoexiste<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elhtmlnoexiste has no accepted answers">0%</span></p></div></div><div id="comments-container-7216" class="comments-container"></div><div id="comment-tools-7216" class="comment-tools"></div><div class="clear"></div><div id="comment-7216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

