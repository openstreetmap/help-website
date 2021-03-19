+++
type = "question"
title = "How is wireshark validating this incomplete checksum?"
description = '''I have a IPv6 network. I sent a big, non-fragmentable ping. The packet tried to cross over a small link, and I got a &quot;Packet too Big&quot; ICMP error out of it. So far, so good. Here is some relevant background data I&#x27;d like you make sure you&#x27;re considering:  An ICMP error contains as &quot;payload&quot; the origi...'''
date = "2014-10-24T08:26:00Z"
lastmod = "2014-10-24T15:34:00Z"
weight = 37337
keywords = [ "icmpv6", "badchecksum", "ipv6", "checksum" ]
aliases = [ "/questions/37337" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How is wireshark validating this incomplete checksum?](/questions/37337/how-is-wireshark-validating-this-incomplete-checksum)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37337-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a IPv6 network. I sent a big, non-fragmentable ping. The packet tried to cross over a small link, and I got a "Packet too Big" ICMP error out of it. So far, so good.</p><p>Here is some relevant background data I'd like you make sure you're considering:</p><ul><li>An ICMP error contains as "payload" the original packet which caused the error.</li><li>This "inner" packet can be truncated. This is perfectly legal.</li></ul><p>The "Packet too Big" is the fourth packet in the listing below. As you can see, Wireshark is complaining because the checksum of the <strong>inner packet</strong> (ie. the <em>original packet</em>) is incorrect.</p><p><img src="https://dl.dropboxusercontent.com/u/95836775/StackOverflows/J16.png" alt="capture pic" /></p><p><strong>Why is Wireshark complaining?</strong></p><p>The inner packet's IPv6 header reports there should be 1408 bytes of payload, but this data was largely truncated, as you can see, so it shouldn't be possible to validate that particular checksum.<br />
Is there some checksum computation black magic I'm not aware of?</p><p>Incidentally, the original packet (the ping) is also present in the capture, but its checksum is not 0xc30e either. <a href="https://dl.dropboxusercontent.com/u/95836775/StackOverflows/J16.wsk">Here is the capture</a>.</p><p>My About says I'm using Wireshark "Version 1.10.6 (v1.10.6 from master-1.10)", Ubuntu 14.04.</p></div><div id="question-tags" class="tags-container tags">icmpv6 badchecksum ipv6 checksum</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '14, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/45ad4e19f178f150d44ef1e74189daa7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ydahhrk&#39;s gravatar image" /><p>ydahhrk<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ydahhrk has no accepted answers">0%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '14, 08:28</p></div></div><div id="comments-container-37337" class="comments-container"></div><div id="comment-tools-37337" class="comment-tools"></div><div class="clear"></div><div id="comment-37337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37338"></span>

<div id="answer-container-37338" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37338-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>Why is Wireshark complaining?</strong></p></blockquote><p>If it's calculating a checksum for an incomplete packet, it's complaining because it's buggy.</p><p>Please file a bug on this on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach the capture to it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '14, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Oct '14, 15:34</p></div></div><div id="comments-container-37338" class="comments-container"><span id="37340"></span><div id="comment-37340" class="comment"><div id="post-37340-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10620">Here goes nothing</a>.</p></div><div id="comment-37340-info" class="comment-info"><span class="comment-age">(24 Oct '14, 17:02)</span> ydahhrk</div></div></div><div id="comment-tools-37338" class="comment-tools"></div><div class="clear"></div><div id="comment-37338-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

