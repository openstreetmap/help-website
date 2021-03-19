+++
type = "question"
title = "Parser Error?"
description = '''I&#x27;m running a packet capture on a x64 Windows Server 2008 R2 system running the latest version of x64 wireshark (1.6.7). Everytime I see the following packet, all traffic that is to follow is [Malformed Packet]. This particular packet is categorized as SMB2 and is connecting to this server on port 4...'''
date = "2012-04-16T13:40:00Z"
lastmod = "2012-04-16T17:01:00Z"
weight = 10199
keywords = [ "packet", "malformed", "smb" ]
aliases = [ "/questions/10199" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Parser Error?](/questions/10199/parser-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10199-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running a packet capture on a x64 Windows Server 2008 R2 system running the latest version of x64 wireshark (1.6.7). Everytime I see the following packet, all traffic that is to follow is [Malformed Packet].</p><p>This particular packet is categorized as SMB2 and is connecting to this server on port 445. There are only two things that jump out at me as they are different from the other captured packets.</p><pre><code>Info Level: SMB2_FIND_ID_BOTH_DIRECTORY_INFO
Search Pattern: *</code></pre><p>When I restart wireshark, all is back to normal and I see traffic as expected. Until this particular packet hits.<br />
</p><p>Is this a symptom of a parser error?</p></div><div id="question-tags" class="tags-container tags">packet malformed smb</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '12, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/087244b91ee35c922ff86ba226bc9cde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pjhan&#39;s gravatar image" /><p>pjhan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pjhan has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-10199" class="comments-container"></div><div id="comment-tools-10199" class="comment-tools"></div><div class="clear"></div><div id="comment-10199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10204"></span>

<div id="answer-container-10204" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10204-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's possible that there is a bug in the SMB2 dissector. We'd probably have to see a sample capture to determine whether that's the case and, if it is, to determine what the bug is and to fix it.</p><p>File a bug about this on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach a capture to the bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '12, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-10204" class="comments-container"></div><div id="comment-tools-10204" class="comment-tools"></div><div class="clear"></div><div id="comment-10204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

