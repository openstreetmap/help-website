+++
type = "question"
title = "How do you launch Wireshark from a remote shell?"
description = '''Hi,  I installed the wireshark-1.0.15-1.el5_6.4.x86_64.rpm packet on my server, and I expected to be able to use the &quot;export DISPLAY&quot; command then &quot;wireshark&quot; command in order to have a real time display of the packets traffic by Wireshark.  Instead, the &quot;wireshark&quot; commad gives back &quot;command not fo...'''
date = "2012-05-11T07:03:00Z"
lastmod = "2012-05-11T07:57:00Z"
weight = 10941
keywords = [ "remoteshell" ]
aliases = [ "/questions/10941" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How do you launch Wireshark from a remote shell?](/questions/10941/how-do-you-launch-wireshark-from-a-remote-shell)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10941-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I installed the wireshark-1.0.15-1.el5_6.4.x86_64.rpm packet on my server, and I expected to be able to use the "export DISPLAY" command then "wireshark" command in order to have a real time display of the packets traffic by Wireshark. Instead, the "wireshark" commad gives back "command not found"</p><h1 id="wireshark">wireshark</h1><p>-bash: wireshark: command not found.</p><p>The rpm installation was successful. So, what's wrong?</p><p>Thanks in advance for the support</p></div><div id="question-tags" class="tags-container tags">remoteshell</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '12, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/8b48b19068e4fb96fdc1a73a9811edc3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nouvelle&#39;s gravatar image" /><p>nouvelle<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nouvelle has no accepted answers">0%</span></p></div></div><div id="comments-container-10941" class="comments-container"></div><div id="comment-tools-10941" class="comment-tools"></div><div class="clear"></div><div id="comment-10941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10944"></span>

<div id="answer-container-10944" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10944-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I checked the content of that package. It <strong>does not contain the GUI version</strong> of wireshark, so that's the reason for the error message.</p><p>Please try this package:</p><blockquote><p><code>wireshark-gnome-1.0.15-1.el5_6.4.x86_64.rpm</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '12, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-10944" class="comments-container"><span id="10967"></span><div id="comment-10967" class="comment"><div id="post-10967-score" class="comment-score"></div><div class="comment-text"><p>Many thanks Kurt !!!!! You make me happy. Now I have my GUI.</p><p>Thanks for your time and your support.</p><p>Best regards,</p><p>lori</p></div><div id="comment-10967-info" class="comment-info"><span class="comment-age">(14 May '12, 02:10)</span> nouvelle</div></div><span id="10968"></span><div id="comment-10968" class="comment"><div id="post-10968-score" class="comment-score"></div><div class="comment-text"><p>@nouvelle,</p><p>I converted your "answer" to a comment as that's how this site works, please read the FAQ for more info.</p><p>Also, if the answer has solved your question, please accept it by clicking the check mark icon beside the answer, so others can see which answers helped you.</p></div><div id="comment-10968-info" class="comment-info"><span class="comment-age">(14 May '12, 02:17)</span> grahamb ♦</div></div></div><div id="comment-tools-10944" class="comment-tools"></div><div class="clear"></div><div id="comment-10944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

