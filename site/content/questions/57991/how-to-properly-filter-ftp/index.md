+++
type = "question"
title = "How to properly filter FTP"
description = '''Hi all, how do i specifically filter FTP? I can use the filter below but it would also show me the other&#x27;s normal FTP traffic.  tcp.port==21 || tcp.port==20 ftp'''
date = "2016-12-10T10:12:00Z"
lastmod = "2016-12-10T10:52:00Z"
weight = 57991
keywords = [ "ftp" ]
aliases = [ "/questions/57991" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to properly filter FTP](/questions/57991/how-to-properly-filter-ftp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57991-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, how do i specifically filter FTP? I can use the filter below but it would also show me the other's normal FTP traffic.</p><p>tcp.port==21 || tcp.port==20 ftp</p></div><div id="question-tags" class="tags-container tags">ftp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '16, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/149d6f8eb0595bad31c406551c9654a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doran_lum&#39;s gravatar image" /><p>doran_lum<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doran_lum has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Dec '16, 23:13</p></div></div><div id="comments-container-57991" class="comments-container"></div><div id="comment-tools-57991" class="comment-tools"></div><div class="clear"></div><div id="comment-57991-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57993"></span>

<div id="answer-container-57993" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57993-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>An FTP dictionary attack is a normal login attempt, except the logins are being done by a program instead of a human being, the passwords and possibly the user names come from a text file, and the login is tried repeatedly until it succeeds or the username/password lists are exhausted. The way to distinguish a dictionary attack from normal logins is that the dictionary attack will normally be repeated many times until one of the logins finally succeeds, if it ever does. A human being might require two or three login attempts if he mistypes his password, but not dozens of attempts. Also, since the login attempts are being done by a program, they will happen more quickly that if a user was manually initiating each one.</p><p>So, to see all login attempts, try this filter: ftp.request.command==USER || ftp.request.command==PASS</p><p>You will have to determine if the login attempts you see are normal or are part of a dictionary attack. If you see multiple login attempts with the same user name, but different passwords each time, that's a strong clue that it could be a dictionary attack.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '16, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-57993" class="comments-container"><span id="58006"></span><div id="comment-58006" class="comment"><div id="post-58006-score" class="comment-score"></div><div class="comment-text"><p>Editing your original question has caused the reply to not make any sense, since the question now being asked is different from the original question.</p><p>It's better to start a new topic if you have a different question, or to add comments to the original question if you need additional information. Editing is usually reserved for fixing typos or improving the wording, not for making a new question.</p></div><div id="comment-58006-info" class="comment-info"><span class="comment-age">(11 Dec '16, 10:17)</span> Jim Aragon</div></div></div><div id="comment-tools-57993" class="comment-tools"></div><div class="clear"></div><div id="comment-57993-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

