+++
type = "question"
title = "what is the 1-step method to test if you have &quot;sufficient CapturePrivileges&quot;?"
description = '''http://wiki.wireshark.org/CaptureSetup/CapturePrivileges http://wiki.wireshark.org/CaptureSetup none of these tell us how to test if we do or not on win xp system'''
date = "2012-05-15T18:35:00Z"
lastmod = "2012-05-16T00:03:00Z"
weight = 11011
keywords = [ "wireshark" ]
aliases = [ "/questions/11011" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [what is the 1-step method to test if you have "sufficient CapturePrivileges"?](/questions/11011/what-is-the-1-step-method-to-test-if-you-have-sufficient-captureprivileges)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11011-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">http://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a> <a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a></p><p>none of these tell us how to test if we do or not</p><p>on win xp system</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '12, 18:35</strong></p><img src="https://secure.gravatar.com/avatar/b2a4006b4a0252f8be292c57acde97ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiresharkhelpers&#39;s gravatar image" /><p>wiresharkhel...<br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiresharkhelpers has no accepted answers">0%</span></p></div></div><div id="comments-container-11011" class="comments-container"></div><div id="comment-tools-11011" class="comment-tools"></div><div class="clear"></div><div id="comment-11011-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11023"></span>

<div id="answer-container-11023" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11023-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think that it's somewhat difficult on XP to not have capture privs. A simple test is to run <code>tshark -D</code>, if any interfaces are listed then you have capture privs. Note that the absence of any interfaces might just mean that there aren't interfaces that can be captured on not that you lack capture privs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '12, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11023" class="comments-container"></div><div id="comment-tools-11023" class="comment-tools"></div><div class="clear"></div><div id="comment-11023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

