+++
type = "question"
title = "How do i fix error &quot;Lua:Error during loading:? See screenshot"
description = '''OS: Ubuntu mate 16.04 Couple questions? How to run Wireshark as root user from desktop icon? When i run wireshark as &quot;sudo wireshark&quot; it opens and give following error, how do i fix it? '''
date = "2017-10-11T21:11:00Z"
lastmod = "2017-10-12T01:16:00Z"
weight = 63830
keywords = [ "root", "user", "wireshark" ]
aliases = [ "/questions/63830" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do i fix error "Lua:Error during loading:? See screenshot](/questions/63830/how-do-i-fix-error-luaerror-during-loading-see-screenshot)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63830-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OS: Ubuntu mate 16.04 Couple questions? How to run Wireshark as root user from desktop icon? When i run wireshark as "sudo wireshark" it opens and give following error, how do i fix it?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_at_2017-10-11_21:05:06.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">root user wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '17, 21:11</strong></p><img src="https://secure.gravatar.com/avatar/4f84884fbd57b2bb469471885adaa5e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A1-Guy&#39;s gravatar image" /><p>A1-Guy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A1-Guy has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63830" class="comments-container"></div><div id="comment-tools-63830" class="comment-tools"></div><div class="clear"></div><div id="comment-63830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63835"></span>

<div id="answer-container-63835" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63835-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do <strong>NOT</strong> run Wireshark as root, this is a potential security risk. Instead configure your system to allow non-root users to capture, see <a href="https://anonscm.debian.org/viewvc/collab-maint/ext-maint/wireshark/trunk/debian/README.Debian?view=markup">here</a> for info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '17, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63835" class="comments-container"><span id="63858"></span><div id="comment-63858" class="comment"><div id="post-63858-score" class="comment-score"></div><div class="comment-text"><p>If i do not run wireshark as "sudo wireshark" from terminal it will not detect the interface to packet captures on?</p></div><div id="comment-63858-info" class="comment-info"><span class="comment-age">(12 Oct '17, 16:54)</span> A1-Guy</div></div><span id="63864"></span><div id="comment-63864" class="comment"><div id="post-63864-score" class="comment-score">1</div><div class="comment-text"><p>That's because you haven't followed the instruction in the link I gave that tell you how to configure your system to allow non-root users to capture.</p></div><div id="comment-63864-info" class="comment-info"><span class="comment-age">(13 Oct '17, 01:40)</span> grahamb ♦</div></div></div><div id="comment-tools-63835" class="comment-tools"></div><div class="clear"></div><div id="comment-63835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

