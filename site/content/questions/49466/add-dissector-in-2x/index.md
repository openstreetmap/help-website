+++
type = "question"
title = "Add dissector in 2.X"
description = '''I am finally able to build Wirshark 2.X. Now it absolutely refuses to find my dissector.  In the past I simply deleted register.c, added things to Makefile.Common and python magically created register.c with my dissector. That doesn&#x27;t work anymore. I&#x27;m doing my best not to go on a rant about the new...'''
date = "2016-01-22T13:07:00Z"
lastmod = "2016-01-22T13:32:00Z"
weight = 49466
keywords = [ "2", "register", "dissector", "wireshark" ]
aliases = [ "/questions/49466" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Add dissector in 2.X](/questions/49466/add-dissector-in-2x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49466-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am finally able to build Wirshark 2.X. Now it absolutely refuses to find my dissector.</p><p>In the past I simply deleted register.c, added things to Makefile.Common and python magically created register.c with my dissector. That doesn't work anymore.</p><p>I'm doing my best not to go on a rant about the new build process.</p><p>Thanks, Brian</p></div><div id="question-tags" class="tags-container tags">2 register dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '16, 13:07</strong></p><img src="https://secure.gravatar.com/avatar/ca4d08b00778143dab07e2cde30f653c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brwiese&#39;s gravatar image" /><p>brwiese<br />
<span class="score" title="26 reputation points">26</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brwiese has one accepted answer">50%</span></p></div></div><div id="comments-container-49466" class="comments-container"><span id="49493"></span><div id="comment-49493" class="comment"><div id="post-49493-score" class="comment-score"></div><div class="comment-text"><p>Rather than rant, maybe let us know if there anything wrong with the documentation?</p><p>The Developers Guide section on <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChapterDissection.html">Packet Dissection</a> directs readers to README.dissector, and README.dissector Section 1.8 notes, as @Guy Harris answered, that a built-in dissector has to be added to <code>epan/CMakeLists.txt</code>.</p></div><div id="comment-49493-info" class="comment-info"><span class="comment-age">(24 Jan '16, 07:29)</span> grahamb ♦</div></div></div><div id="comment-tools-49466" class="comment-tools"></div><div class="clear"></div><div id="comment-49466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49470"></span>

<div id="answer-container-49470" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49470-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To which "new build process" are you referring? Building with CMake? On UN*Xes, you can still use autotools rather than CMake; are you building on Windows?</p><p>If you're building with CMake, add your dissector to the <code>DISSECTOR_SRC</code> variable in <code>epan/CMakeLists.txt</code>; you'll need to put <code>dissector/</code> in front of the name.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '16, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '16, 13:32</p></div></div><div id="comments-container-49470" class="comments-container"></div><div id="comment-tools-49470" class="comment-tools"></div><div class="clear"></div><div id="comment-49470-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

