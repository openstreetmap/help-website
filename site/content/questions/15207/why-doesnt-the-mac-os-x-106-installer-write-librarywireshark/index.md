+++
type = "question"
title = "Why doesn&#x27;t the Mac OS X 10.6+ installer write /Library/Wireshark?"
description = '''From the installer&#x27;s README:  The installer writes to the following locations: ...  • /Library/Wireshark. A wrapper script and symbolic links which will let you run Wireshark and its associated utilities from the command line. You can access them directly or by adding /Library/Wireshark to your PATH...'''
date = "2012-10-23T22:53:00Z"
lastmod = "2013-10-01T17:15:00Z"
weight = 15207
keywords = [ "macosx", "install" ]
aliases = [ "/questions/15207" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why doesn't the Mac OS X 10.6+ installer write /Library/Wireshark?](/questions/15207/why-doesnt-the-mac-os-x-106-installer-write-librarywireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15207-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From the installer's README:</p><blockquote><p>The installer writes to the following locations:<br />
...<br />
• /Library/Wireshark. A wrapper script and symbolic links which will let you run Wireshark and its associated utilities from the command line. You can access them directly or by adding /Library/Wireshark to your PATH.<br />
...<br />
How do I uninstall?<br />
2. Remove /Library/Wireshark</p></blockquote><p>I'm on Mac OS X 10.7 and the installer created no /Library/Wireshark. However, "which wireshark" gives /usr/local/bin/wireshark! Is something going wrong with my system?</p></div><div id="question-tags" class="tags-container tags">macosx install</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '12, 22:53</strong></p><img src="https://secure.gravatar.com/avatar/23fa1d99f861f3b7507c982f8d99bc2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ignis&#39;s gravatar image" /><p>ignis<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ignis has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-15207" class="comments-container"></div><div id="comment-tools-15207" class="comment-tools"></div><div class="clear"></div><div id="comment-15207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25486"></span>

<div id="answer-container-25486" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25486-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, there's something wrong with the installer's README. I've checked in a fix, so the next 1.8.x and 1.10.x releases should have the correct README.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '13, 17:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-25486" class="comments-container"></div><div id="comment-tools-25486" class="comment-tools"></div><div class="clear"></div><div id="comment-25486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

