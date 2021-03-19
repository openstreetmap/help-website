+++
type = "question"
title = "Mac OS X icon messed up"
description = '''So I recall in talking about a bug that caused Wireshark to crash, one of the developers mentioned the trouble he was having that the icon would not show up correctly in the Applications folder or the Dock. I found out why (well there may be more than one cause, but here is what caused it here). The...'''
date = "2013-08-24T11:50:00Z"
lastmod = "2013-08-24T13:19:00Z"
weight = 24002
keywords = [ "x", "mac", "os", "dock", "icon" ]
aliases = [ "/questions/24002" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Mac OS X icon messed up](/questions/24002/mac-os-x-icon-messed-up)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24002-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I recall in talking about a bug that caused Wireshark to crash, one of the developers mentioned the trouble he was having that the icon would not show up correctly in the Applications folder or the Dock. I found out why (well there may be more than one cause, but here is what caused it here).</p><p>The file inside the app that stores the icons located inside the app:(/Applications/Wireshark.app/Contents/Resources/Wireshark.icns) seems corrupt. Some of the small icons (32 pixels and below) look normal, but the larger icons are blank or just a field of gray. I've fixed my copy in the 'quick and dirty hack' sort of way, by scaling the 32 pixel version and copying the (jaggy) copies into the blank boxes for 128, 256 and 512 pixels. The real fix of course is to assure that the original artwork is not corrupted during packaging, download or whenever/wherever it went wrong.</p><p>So I guess this is more of an answer than a question, unless someone wants my hacked up .icns file or wants me to reassemble a new .icns file from the original artwork, in which case I believe my email address is registered here.</p></div><div id="question-tags" class="tags-container tags">x mac os dock icon</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '13, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/d0d7eb49c8a24a1860db62cba29f3bdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lubo%20Diakov&#39;s gravatar image" /><p>Lubo Diakov<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lubo Diakov has no accepted answers">0%</span></p></div></div><div id="comments-container-24002" class="comments-container"><span id="24003"></span><div id="comment-24003" class="comment"><div id="post-24003-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but the larger icons are blank or just a field of gray</p></blockquote><p>Is this on Leopard or is this on a later release (Snow Leopard or later)?</p></div><div id="comment-24003-info" class="comment-info"><span class="comment-age">(24 Aug '13, 11:56)</span> Guy Harris ♦♦</div></div><span id="24010"></span><div id="comment-24010" class="comment"><div id="post-24010-score" class="comment-score"></div><div class="comment-text"><p>Leopard (Mac OS X 10.5.8).</p></div><div id="comment-24010-info" class="comment-info"><span class="comment-age">(24 Aug '13, 13:06)</span> Lubo Diakov</div></div></div><div id="comment-tools-24002" class="comment-tools"></div><div class="clear"></div><div id="comment-24002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24011"></span>

<div id="answer-container-24011" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24011-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8993">Bug 8993</a>. Vote for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '13, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24011" class="comments-container"></div><div id="comment-tools-24011" class="comment-tools"></div><div class="clear"></div><div id="comment-24011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

