+++
type = "question"
title = "Can SMB v1 vs. SMB v2 be detected in the header?"
description = '''Can one determine which version of SMB is being used by looking at the SMB header?'''
date = "2012-03-20T10:13:00Z"
lastmod = "2012-03-20T16:33:00Z"
weight = 9647
keywords = [ "smb" ]
aliases = [ "/questions/9647" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can SMB v1 vs. SMB v2 be detected in the header?](/questions/9647/can-smb-v1-vs-smb-v2-be-detected-in-the-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9647-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can one determine which version of SMB is being used by looking at the SMB header?</p></div><div id="question-tags" class="tags-container tags">smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '12, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/a1feffebe8015bb53af00f9d97157cda?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Janis%20Bishop&#39;s gravatar image" /><p>Janis Bishop<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Janis Bishop has no accepted answers">0%</span></p></div></div><div id="comments-container-9647" class="comments-container"></div><div id="comment-tools-9647" class="comment-tools"></div><div class="clear"></div><div id="comment-9647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9666"></span>

<div id="answer-container-9666" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9666-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes.</p><p>According to Microsoft's <a href="http://msdn.microsoft.com/en-us/library/ee442092(v=prot.13).aspx">[MS-CIFS] specification</a>, the first 4 bytes of the header for an SMB message "MUST contain the 4-byte literal string '\xFF', 'S', 'M', 'B', with the letters represented by their respective ASCII values in the order shown."</p><p>According to their <a href="http://msdn.microsoft.com/en-us/library/cc246482(v=prot.13).aspx">[MS-SMB2 specification]</a>, the first 4 bytes of the header for an SMB2 message "MUST be (in network order) 0xFE, 'S', 'M', and 'B'."</p><p>So the first byte of the message is 0xFF for SMB and 0xFE for SMB2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-9666" class="comments-container"></div><div id="comment-tools-9666" class="comment-tools"></div><div class="clear"></div><div id="comment-9666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

