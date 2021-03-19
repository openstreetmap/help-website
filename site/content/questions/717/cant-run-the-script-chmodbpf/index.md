+++
type = "question"
title = "can&#x27;t run the script chmodBPF"
description = '''the error is &quot;./ChmodBPF: line 35: $1: unbound variable&quot; in Snow leopard. after install. Do you have any recommendation? Right now I can&#x27;t detect any interfaces in wireshark.'''
date = "2010-10-27T20:33:00Z"
lastmod = "2010-10-28T14:15:00Z"
weight = 717
keywords = [ "chmodbpf" ]
aliases = [ "/questions/717" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [can't run the script chmodBPF](/questions/717/cant-run-the-script-chmodbpf)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-717-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>the error is "./ChmodBPF: line 35: $1: unbound variable" in Snow leopard. after install.</p><p>Do you have any recommendation? Right now I can't detect any interfaces in wireshark.</p></div><div id="question-tags" class="tags-container tags">chmodbpf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '10, 20:33</strong></p><img src="https://secure.gravatar.com/avatar/959289af9c12ca333eb8cee94e666a99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nataichi&#39;s gravatar image" /><p>Nataichi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nataichi has no accepted answers">0%</span></p></div></div><div id="comments-container-717" class="comments-container"></div><div id="comment-tools-717" class="comment-tools"></div><div class="clear"></div><div id="comment-717-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="730"></span>

<div id="answer-container-730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-730-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>ChmodBPF isn't a script you're supposed to run directly, it's a script that's supposed to be run by the SystemStarter mechanism in Mac OS X. Put both ChmodBPF and StartupParameters.plist into the directory /Library/StartupItems, make sure they're owned by user "root" and group "wheel" and are not writable by anybody other than "root", and then do "sudo SystemStarter start ChmodBPF" to cause SystemStarter to run the script. That should change the ownership and/or permissions on the existing BPF devices. After a reboot, the permissions should be set automatically.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '10, 14:15</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-730" class="comments-container"></div><div id="comment-tools-730" class="comment-tools"></div><div class="clear"></div><div id="comment-730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

