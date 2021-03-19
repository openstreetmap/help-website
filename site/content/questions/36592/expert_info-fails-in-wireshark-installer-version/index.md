+++
type = "question"
title = "Expert_Info fails in wireshark installer version"
description = '''I&#x27;m working on a wireshark dissector, it works and I&#x27;m able to compile it. The dissector works on my development version of wireshark but not on the wireshark installer version. Both are used in the newest version. I get the error: Err field abbrev=foo.expert does not have a name Press any key to ex...'''
date = "2014-09-25T05:50:00Z"
lastmod = "2014-09-25T09:24:00Z"
weight = 36592
keywords = [ "expertinfo" ]
aliases = [ "/questions/36592" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Expert\_Info fails in wireshark installer version](/questions/36592/expert_info-fails-in-wireshark-installer-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36592-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working on a wireshark dissector, it works and I'm able to compile it. The dissector works on my development version of wireshark but not on the wireshark installer version. Both are used in the newest version.</p><p>I get the error: Err field abbrev=<code>foo.expert</code> does not have a name Press any key to exit</p><p>Do anybody know the reason?</p></div><div id="question-tags" class="tags-container tags">expertinfo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '14, 05:50</strong></p><img src="https://secure.gravatar.com/avatar/3c9a4994949fd9e12a2b60dc263d8f46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vcwm&#39;s gravatar image" /><p>vcwm<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vcwm has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '14, 05:56</p></div></div><div id="comments-container-36592" class="comments-container"></div><div id="comment-tools-36592" class="comment-tools"></div><div class="clear"></div><div id="comment-36592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36602"></span>

<div id="answer-container-36602" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36602-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are compiling a dissector plugin, isn't it? You probably tried to run the compiled library against another Wireshark version than the one you use on your development machine. Plugins must be compiled against the version you intend to use (for example a plugin compiled in master branch will not run with Wireshark 1.12 releases).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '14, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-36602" class="comments-container"><span id="36617"></span><div id="comment-36617" class="comment"><div id="post-36617-score" class="comment-score"></div><div class="comment-text"><p>ok thanks for the answer, but it just seems to be the expert info which causes the problems, if i commented out all line which deals with expert info, the plugin works on both versions.</p></div><div id="comment-36617-info" class="comment-info"><span class="comment-age">(25 Sep '14, 13:15)</span> vcwm</div></div><span id="36618"></span><div id="comment-36618" class="comment"><div id="post-36618-score" class="comment-score"></div><div class="comment-text"><p>Because the expert info API changed between master-1.12 and master branches. What I said remains valid.</p></div><div id="comment-36618-info" class="comment-info"><span class="comment-age">(25 Sep '14, 13:57)</span> Pascal Quantin</div></div></div><div id="comment-tools-36602" class="comment-tools"></div><div class="clear"></div><div id="comment-36602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

