+++
type = "question"
title = "nmake -f Makefile.nmake all"
description = '''I am getting a fatal error. can i change this path as microsoft visual studio is in different location or i had to reinstall the microsoft visual studio 9.0 in that location..? set copycmd=/y if not exist wireshark-gtk2 mkdir wireshark-gtk2 xcopy &quot;C:&#92;Program Files&#92;Microsoft Visual Studio 9.0&#92;VC&#92;redi...'''
date = "2015-03-04T19:36:00Z"
lastmod = "2015-03-05T01:47:00Z"
weight = 40264
keywords = [ "build", "wireshrk" ]
aliases = [ "/questions/40264" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nmake -f Makefile.nmake all](/questions/40264/nmake-f-makefilenmake-all)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40264-score" class="post-score" title="current number of votes">0</div><span id="post-40264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am getting a fatal error.</p><p>can i change this path as microsoft visual studio is in different location or i had to reinstall the microsoft visual studio 9.0 in that location..?</p><p>set copycmd=/y if not exist wireshark-gtk2 mkdir wireshark-gtk2 xcopy "C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Micros oft.VC90.CRT*.<em>" wireshark-gtk2*.</em> /d</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-wireshrk" rel="tag" title="see questions tagged &#39;wireshrk&#39;">wireshrk</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '15, 19:36</strong></p><img src="https://secure.gravatar.com/avatar/302a32bb6a6f237c61731914f3657167?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dhruv%20Gupta&#39;s gravatar image" /><p><span>Dhruv Gupta</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dhruv Gupta has no accepted answers">0%</span></p></div></div><div id="comments-container-40264" class="comments-container"></div><div id="comment-tools-40264" class="comment-tools"></div><div class="clear"></div><div id="comment-40264-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40268"></span>

<div id="answer-container-40268" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40268-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40268-score" class="post-score" title="current number of votes">0</div><span id="post-40268-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends on what version of the sources you're running from.</p><p>Until a recent <a href="https://code.wireshark.org/review/#/c/7426/">change</a> in master, the paths were hard-coded in config.nmake depending on the version of Visual Studio you were using. After that change, the path automatically tracks the VS install location.</p><p>So, if building with sources from before that commit, you'll have to modify config.nmake to set the correct path for your installation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40268" class="comments-container"></div><div id="comment-tools-40268" class="comment-tools"></div><div class="clear"></div><div id="comment-40268-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

