+++
type = "question"
title = "Unable to install Wireshark on OS X Mavericks"
description = '''I am unable to install Wireshark on Mavericks.'''
date = "2013-10-23T08:48:00Z"
lastmod = "2013-10-23T12:04:00Z"
weight = 26325
keywords = [ "mavericks" ]
aliases = [ "/questions/26325" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to install Wireshark on OS X Mavericks](/questions/26325/unable-to-install-wireshark-on-os-x-mavericks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26325-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am unable to install Wireshark on Mavericks.</p></div><div id="question-tags" class="tags-container tags">mavericks</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/698125f885100a75ad083dddeb790d85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tgreen&#39;s gravatar image" /><p>tgreen<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tgreen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Oct '13, 12:05</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-26325" class="comments-container"></div><div id="comment-tools-26325" class="comment-tools"></div><div class="clear"></div><div id="comment-26325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26331"></span>

<div id="answer-container-26331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26331-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Which version of Wireshark?</p><p>1.11.0 doesn't work on Mavericks, due to a problem with Qt.</p><p>1.10.2 does work (I just tried it), but the initial installation process is a bit of a pain:</p><ul><li>the installer package isn't signed, so you have to open it with control-click and say "yes, it's from an unknown developer, but I still want to open it";</li><li>when you try to open it, it'll ask you where X11 is, and you need to click "Browse..." and browse to /Applications/Utilities/XQuartz (which you have to have installed);</li><li>you may have to click the Wireshark icon a couple of times before it'll launch X11, and, even after that, you may have to quit the Wireshark app in the dock and restart it before it'll run the actual Wireshark binary.</li></ul><p>After that, it should Just Work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '13, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-26331" class="comments-container"></div><div id="comment-tools-26331" class="comment-tools"></div><div class="clear"></div><div id="comment-26331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

