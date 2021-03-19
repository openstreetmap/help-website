+++
type = "question"
title = "How to gradually encrypt the output capture file?"
description = '''How can I make past captured packet utterly unavailable without a certain password? My current strategy is to run tshark rotatively and run a background script that encrypt all those files. But there are security issues with this technique since the password is contained in the encrypting script.'''
date = "2016-11-24T07:02:00Z"
lastmod = "2016-11-24T07:23:00Z"
weight = 57608
keywords = [ "encryption", "security", "encrypted" ]
aliases = [ "/questions/57608" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to gradually encrypt the output capture file?](/questions/57608/how-to-gradually-encrypt-the-output-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I make past captured packet utterly unavailable without a certain password?</p><p>My current strategy is to run tshark rotatively and run a background script that encrypt all those files.</p><p>But there are security issues with this technique since the password is contained in the encrypting script.</p></div><div id="question-tags" class="tags-container tags">encryption security encrypted</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '16, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/463715dfacfa7a0e4d634cd6559ba12c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user987987987&#39;s gravatar image" /><p>user987987987<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user987987987 has no accepted answers">0%</span></p></div></div><div id="comments-container-57608" class="comments-container"></div><div id="comment-tools-57608" class="comment-tools"></div><div class="clear"></div><div id="comment-57608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57610"></span>

<div id="answer-container-57610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57610-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Create a Public/Private key pair and put the capture files through <a href="https://www.gnupg.org/gph/en/manual/x110.html">GPG</a></p><p>Where you capture the data use your Public key to encrypt the data, so that you can only decrypt it with your Private key, which you keep separate of course.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '16, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57610" class="comments-container"></div><div id="comment-tools-57610" class="comment-tools"></div><div class="clear"></div><div id="comment-57610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

