+++
type = "question"
title = "global preference file"
description = '''wireshark is installed in the &quot;/usr/local/bin&quot; directory but global preference file is not in &quot;/usr/local/share&quot;  do i need to create it.. if yes. please provide a sample file format.. it&#x27;ll be great help thanks!'''
date = "2012-01-31T04:49:00Z"
lastmod = "2012-01-31T06:21:00Z"
weight = 8727
keywords = [ "development", "preferences", "wireshark" ]
aliases = [ "/questions/8727" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [global preference file](/questions/8727/global-preference-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8727-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>wireshark is installed in the "/usr/local/bin" directory</p><p>but global preference file is not in "/usr/local/share"</p><p>do i need to create it.. if yes. please provide a sample file format.. it'll be great help</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags">development preferences wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '12, 04:49</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p>Sanny_D<br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-8727" class="comments-container"></div><div id="comment-tools-8727" class="comment-tools"></div><div class="clear"></div><div id="comment-8727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8728"></span>

<div id="answer-container-8728" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8728-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Correct: the global preferences does not exist by default.</p><p>It takes the same format as the options in your ~/.wireshark/preferences file. So, for example, you could put:</p><pre><code># Ask to save unsaved capture files?
# TRUE or FALSE (case-insensitive).
gui.ask_unsaved: TRUE</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '12, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-8728" class="comments-container"></div><div id="comment-tools-8728" class="comment-tools"></div><div class="clear"></div><div id="comment-8728-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

