+++
type = "question"
title = "How to run wireshark as a non-root user while logged in as a root user?"
description = '''Hey, I am new to arch linux and wireshark. Its a noob question i know, but jsut wanted to know. Basically, i am using arch linux with Linux kernel 4.2.2. I have downloaded and installed wireshark as a root user using pacman. Additionally i made a new non-root user (username: wiresharktest) and added...'''
date = "2015-10-13T14:51:00Z"
lastmod = "2015-10-13T15:00:00Z"
weight = 46527
keywords = [ "root", "wireshark" ]
aliases = [ "/questions/46527" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to run wireshark as a non-root user while logged in as a root user?](/questions/46527/how-to-run-wireshark-as-a-non-root-user-while-logged-in-as-a-root-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46527-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I am new to arch linux and wireshark. Its a noob question i know, but jsut wanted to know. Basically, i am using arch linux with Linux kernel 4.2.2. I have downloaded and installed wireshark as a root user using pacman. Additionally i made a new non-root user (username: wiresharktest) and added it to the default wireshark group. I have limited the permissions only to the root user and users in the wireshark group.</p><p>Now i wanted to know if i can run wireshark as a non-root user (username: wiresharktest) while I am logged in as root. Is it possible? If yes, How?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">root wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '15, 14:51</strong></p><img src="https://secure.gravatar.com/avatar/0dd99396cb8dea974cafcd1eef0b0e3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="archskynet&#39;s gravatar image" /><p>archskynet<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="archskynet has no accepted answers">0%</span></p></div></div><div id="comments-container-46527" class="comments-container"></div><div id="comment-tools-46527" class="comment-tools"></div><div class="clear"></div><div id="comment-46527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46529"></span>

<div id="answer-container-46529" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46529-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Now i wanted to know if i can run wireshark as a non-root user (username: wiresharktest) while I am logged in as root.</p></blockquote><p>Please try this:</p><blockquote><p>su -l wiresharktest -c /usr/bin/wireshark</p></blockquote><p>Please replace the path to Wireshark with the path on your system.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46529" class="comments-container"><span id="46532"></span><div id="comment-46532" class="comment"><div id="post-46532-score" class="comment-score"></div><div class="comment-text"><p>su -l wiresharktest -c /usr/bin/wireshark-qt wireshark-qt: cannot connect to X server. :( I'm sorry if i am going in a wrong direction, you can ask me to refer any instructions which i may understand first, rather than blindly asking here. I understood that running an X server is required for displaying programs from su. I read it that i can create a symlink. Please Explain.</p></div><div id="comment-46532-info" class="comment-info"><span class="comment-age">(13 Oct '15, 15:30)</span> archskynet</div></div><span id="46539"></span><div id="comment-46539" class="comment"><div id="post-46539-score" class="comment-score"></div><div class="comment-text"><p>Do you have a graphical interface on your OS, or is this a pure "server installation" with ssh/telnet access?</p></div><div id="comment-46539-info" class="comment-info"><span class="comment-age">(13 Oct '15, 16:42)</span> Kurt Knochner ♦</div></div><span id="46552"></span><div id="comment-46552" class="comment"><div id="post-46552-score" class="comment-score"></div><div class="comment-text"><p>Hey, I do have a GUI for my OS. And this is not a server installation. It works if i start wireshark-qt from terminal , and I can login as a non-root user as well, but cannot start a the application as a non-root user from root.</p></div><div id="comment-46552-info" class="comment-info"><span class="comment-age">(14 Oct '15, 07:44)</span> archskynet</div></div><span id="46553"></span><div id="comment-46553" class="comment"><div id="post-46553-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but cannot start a the application as a non-root user from root.</p></blockquote><p>Then you should follow the dscriptions in the following question, recently asked:</p><blockquote><p><a href="https://ask.wireshark.org/questions/46504/how-to-set-environment-variables-in-kubuntu">https://ask.wireshark.org/questions/46504/how-to-set-environment-variables-in-kubuntu</a></p></blockquote></div><div id="comment-46553-info" class="comment-info"><span class="comment-age">(14 Oct '15, 07:49)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46529" class="comment-tools"></div><div class="clear"></div><div id="comment-46529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

