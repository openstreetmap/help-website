+++
type = "question"
title = "Feature Request: Bad Checksum 0x00000000"
description = '''Why is it in this day and age that wireshark is still telling me that an Ethernet/TCP/UDP checksum of 0x00000000 is an error? Documentation right from the wireshark website says it has to do with checksum offloading and I need to change a setting in wireshark to stop validating checksums. Why doesn&#x27;...'''
date = "2014-11-10T06:47:00Z"
lastmod = "2014-11-10T06:51:00Z"
weight = 37725
keywords = [ "badchecksum" ]
aliases = [ "/questions/37725" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Feature Request: Bad Checksum 0x00000000](/questions/37725/feature-request-bad-checksum-0x00000000)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37725-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why is it in this day and age that wireshark is still telling me that an Ethernet/TCP/UDP checksum of 0x00000000 is an error? Documentation right from the wireshark website says it has to do with checksum offloading and I need to change a setting in wireshark to stop validating checksums. Why doesn't wireshark automatically see 0x00000000 and mark it as a Note or less in the expert infos so if there is actually a checksum error it doesn't get missed? I do realize I can create a display filter for this, I just feel I shouldn't have to.</p></div><div id="question-tags" class="tags-container tags">badchecksum</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '14, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/2455b9712c85bd90c7221973275db4f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ex1580&#39;s gravatar image" /><p>ex1580<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ex1580 has no accepted answers">0%</span></p></div></div><div id="comments-container-37725" class="comments-container"></div><div id="comment-tools-37725" class="comment-tools"></div><div class="clear"></div><div id="comment-37725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37726"></span>

<div id="answer-container-37726" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37726-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Because different drivers\OS's will place different values in the uninitialized field. Should we just guess that some checksums are not an error and mark them as "possible error"?</p><p>Apart from that, feature requests are best directed at the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a> marking the item as an "enhancement".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '14, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37726" class="comments-container"><span id="37727"></span><div id="comment-37727" class="comment"><div id="post-37727-score" class="comment-score"></div><div class="comment-text"><p>Grahamb, thanks for the answer, I will post a feature request over on bugzilla.</p></div><div id="comment-37727-info" class="comment-info"><span class="comment-age">(10 Nov '14, 06:55)</span> ex1580</div></div></div><div id="comment-tools-37726" class="comment-tools"></div><div class="clear"></div><div id="comment-37726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

