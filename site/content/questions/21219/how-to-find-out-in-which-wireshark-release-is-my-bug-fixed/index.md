+++
type = "question"
title = "How to find out in which wireshark release is my bug fixed?"
description = '''Hi! I had opened two Bugzillas a few months ago which got fixed. However, I just installed v 1.8.2 in my Debian machine and I still don&#x27;t see the fixes in there.  Is there a way to find out in which release will I get the fix? Is there a way to request for those fixes to be included to the next rele...'''
date = "2013-05-17T05:06:00Z"
lastmod = "2013-05-17T06:29:00Z"
weight = 21219
keywords = [ "bug" ]
aliases = [ "/questions/21219" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find out in which wireshark release is my bug fixed?](/questions/21219/how-to-find-out-in-which-wireshark-release-is-my-bug-fixed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21219-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi!</p><p>I had opened two Bugzillas a few months ago which got fixed. However, I just installed v 1.8.2 in my Debian machine and I still don't see the fixes in there.</p><p>Is there a way to find out in which release will I get the fix? Is there a way to request for those fixes to be included to the next release?</p><p>Thanks, Georgia</p></div><div id="question-tags" class="tags-container tags">bug</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '13, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/573d08aac5af4e90c0842df6d8a897ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeorgiaK&#39;s gravatar image" /><p>GeorgiaK<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeorgiaK has no accepted answers">0%</span></p></div></div><div id="comments-container-21219" class="comments-container"></div><div id="comment-tools-21219" class="comment-tools"></div><div class="clear"></div><div id="comment-21219-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21222"></span>

<div id="answer-container-21222" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21222-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually the bug will indicate that, it just may not do it in a very obvious way.</p><p>If the fix was just "checked in" then the fix would show up in the next <em>development</em> release after the fix was checked in (or the next "major" release--e.g., 1.10.0 is the next "major" release after the 1.8.x series). (Development releases have an odd minor-version number--e.g., 1.9.x.)</p><p>If the fix was checked in and a comment was made like "and scheduled to be back-ported to 1.8.x" then it should show up in the specified (or "next" if the exact version was not specified) release.</p><p>Another way to know would be to look at the list of bugs checked in to each release (for example, for the <a href="http://wiki.wireshark.org/Development/Trunk-1.8">1.8.x versions</a>).</p><p>As a general rule, only bug fixes are back-ported to the release branches. Any kind of enhancement usually wants for the next development/major release. For more information, see the <a href="http://wiki.wireshark.org/Development/ReleasePolicy">Release Policy</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 May '13, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-21222" class="comments-container"></div><div id="comment-tools-21222" class="comment-tools"></div><div class="clear"></div><div id="comment-21222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

