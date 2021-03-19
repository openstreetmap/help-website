+++
type = "question"
title = "missing player button"
description = '''Is there anyone who has problem with missing button player in wireshark? I have version 1.2.15 instaled on centos 6.2, instaled portaudio and portaudio-devel but still no success. Best Regards'''
date = "2012-04-03T06:51:00Z"
lastmod = "2012-04-03T07:59:00Z"
weight = 9912
keywords = [ "player" ]
aliases = [ "/questions/9912" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [missing player button](/questions/9912/missing-player-button)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9912-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there anyone who has problem with missing button player in wireshark? I have version 1.2.15 instaled on centos 6.2, instaled portaudio and portaudio-devel but still no success.</p><p>Best Regards</p></div><div id="question-tags" class="tags-container tags">player</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '12, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/00d1889fc025ca25fed3f3fc846dac4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="2cv6club&#39;s gravatar image" /><p>2cv6club<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="2cv6club has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Apr '12, 06:52</p></div></div><div id="comments-container-9912" class="comments-container"></div><div id="comment-tools-9912" class="comment-tools"></div><div class="clear"></div><div id="comment-9912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9913"></span>

<div id="answer-container-9913" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9913-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's a really old and unsupported version of Wireshark. You should look to upgrade to a supported version. The current stable version is 1.6.6, with a security fix only old version of 1.4.12. See the <a href="http://www.wireshark.org/download.html">Download</a> page for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '12, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-9913" class="comments-container"></div><div id="comment-tools-9913" class="comment-tools"></div><div class="clear"></div><div id="comment-9913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9914"></span>

<div id="answer-container-9914" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9914-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If "I have version 1.2.15 instaled on centos 6.2" means you installed a binary version of Wireshark built by somebody else (e.g., installed an RPM), then it's irrelevant whether <em>you</em> have portaudio or portaudio-devel installed - the only thing that matters is whether whoever <em>built</em> the binary version had portaudio-devel installed on the machine on which they built it. Wireshark doesn't attempt to load the portaudio library at run time; it's linked in (whether it's a static or dynamic library) at build time.</p><p>So if the binary package wasn't built with portaudio, you'll have to build your own version from source; you already have portaudio-devel installed, so you should be able to build a version with portaudio in it. As long as you're doing that, I'd suggest, as grahamb did, that you build a newer version, such as 1.6.6.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '12, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9914" class="comments-container"></div><div id="comment-tools-9914" class="comment-tools"></div><div class="clear"></div><div id="comment-9914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

