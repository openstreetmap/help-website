+++
type = "question"
title = "Child capture process exited: exited status 127"
description = '''I am working on Ubuntu 10.10 and wireshark 1.2.11. Every time I choose an interface to start captureing, i got the error ¨Child capture process exited: exited status 127¨. Does anybody have any solutions? thanks Levi'''
date = "2011-04-11T10:23:00Z"
lastmod = "2011-04-11T10:59:00Z"
weight = 3443
keywords = [ "capture" ]
aliases = [ "/questions/3443" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Child capture process exited: exited status 127](/questions/3443/child-capture-process-exited-exited-status-127)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3443-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on Ubuntu 10.10 and wireshark 1.2.11. Every time I choose an interface to start captureing, i got the error ¨Child capture process exited: exited status 127¨. Does anybody have any solutions?</p><p>thanks Levi</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '11, 10:23</strong></p><img src="https://secure.gravatar.com/avatar/d63022e61f1359d3e54de6b4a853e67d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LeviVic&#39;s gravatar image" /><p>LeviVic<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LeviVic has no accepted answers">0%</span></p></div></div><div id="comments-container-3443" class="comments-container"></div><div id="comment-tools-3443" class="comment-tools"></div><div class="clear"></div><div id="comment-3443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3444"></span>

<div id="answer-container-3444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3444-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since you are most likely using Bash, this is probably a "command not found" error. If I recall correctly, you should be getting a different error in the case that Wireshark can't start a capture, but it is possible that this is a path problem.</p><p>The "child capture process" is <code>dumpcap</code>, so the error likely means that <code>dumpcap</code> is not on your <code>PATH</code>. Try running <code>which dumpcap</code>. If there is no output then you need to add <code>dumpcap</code> to your path. The executable is usually in <code>/usr/bin/</code> (if you used <code>apt</code> or <code>synaptic</code> to install Wireshark) or <code>/usr/local/bin</code> if you compiled Wireshark yourself. Normally, these directories are on your path, so it may be that <code>dumpcap</code> is in a different directory (which may be the case if you compiled Wireshark with a custom prefix or installed it to a nonstandard directory).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '11, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-3444" class="comments-container"><span id="3445"></span><div id="comment-3445" class="comment"><div id="post-3445-score" class="comment-score"></div><div class="comment-text"><p>Thanks. But I installed Wireshark using Ubuntu Software Center and dumpcap file is just in /usr/bin as by default.</p></div><div id="comment-3445-info" class="comment-info"><span class="comment-age">(11 Apr '11, 11:15)</span> LeviVic</div></div><span id="3447"></span><div id="comment-3447" class="comment"><div id="post-3447-score" class="comment-score"></div><div class="comment-text"><p>In that case, can you be more specific about the error you encounter? Specifically, what specific steps reproduce the problem, how is the message presented, and is there any additional text with the error message?</p></div><div id="comment-3447-info" class="comment-info"><span class="comment-age">(11 Apr '11, 12:02)</span> multipleinte...</div></div></div><div id="comment-tools-3444" class="comment-tools"></div><div class="clear"></div><div id="comment-3444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

