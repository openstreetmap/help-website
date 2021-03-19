+++
type = "question"
title = "Wireshark 32-bit vs 64-bit performance advantages"
description = '''Hello experts, I am running wirehark 1.8.12 32-bit wireshark on my linux machine. Are there any substantial performance advantages of tshark if I upgrade it to 2.0 64-bit? Ofcourse I would have all the enhancements but would like to upgrade only if there is a considerate performance advantage that w...'''
date = "2016-02-29T23:44:00Z"
lastmod = "2016-03-01T05:05:00Z"
weight = 50594
keywords = [ "performance", "32-bit", "vs", "64-bit" ]
aliases = [ "/questions/50594" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 32-bit vs 64-bit performance advantages](/questions/50594/wireshark-32-bit-vs-64-bit-performance-advantages)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50594-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello experts,</p><p>I am running wirehark 1.8.12 32-bit wireshark on my linux machine. Are there any substantial performance advantages of tshark if I upgrade it to 2.0 64-bit? Ofcourse I would have all the enhancements but would like to upgrade only if there is a considerate performance advantage that would speed up my tshark's capture and decode. Not conerned with the UI performance. I only need my back-end tshark's performance to improve. Thank you.</p><p>Best, Anirudh</p></div><div id="question-tags" class="tags-container tags">performance 32-bit vs 64-bit</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Feb '16, 23:44</strong></p><img src="https://secure.gravatar.com/avatar/87231d218f74e81eb665f2bd17ae0b60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anikastu&#39;s gravatar image" /><p>anikastu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anikastu has no accepted answers">0%</span></p></div></div><div id="comments-container-50594" class="comments-container"></div><div id="comment-tools-50594" class="comment-tools"></div><div class="clear"></div><div id="comment-50594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50605"></span>

<div id="answer-container-50605" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50605-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The biggest advantage of the 64 bit version is that it can handle larger files. It may be also faster in new version as the developers keep improving the core as well, not just dissectors.</p><p>Oh, and tshark ddoesn't capture, it's dumpcap that does it. For that, 64 bit can probably be ignored as it doesn't matter that much when writing packets to disk.</p><p>Last but not least 1.8 is years old now, so it has known vulnerabilities someone could try to exploit.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '16, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-50605" class="comments-container"><span id="50606"></span><div id="comment-50606" class="comment"><div id="post-50606-score" class="comment-score"></div><div class="comment-text"><p>Yes, there were some significant efforts at increasing efficiency between 1.8 and now. That's not to say it's sure to be faster for all work loads but there's a good chance (e.g., maybe Wireshark got faster for TCP traffic but you deal mostly with SCTP which /could have/--I'm not saying it did--gotten slower due to some other changes). The only real way to tell would be to try it out.</p></div><div id="comment-50606-info" class="comment-info"><span class="comment-age">(01 Mar '16, 06:02)</span> JeffMorriss ♦</div></div><span id="50625"></span><div id="comment-50625" class="comment"><div id="post-50625-score" class="comment-score"></div><div class="comment-text"><p>Great ! Thank you so much Jasper and Jeff. That helps. Yes will try out and see how it goes.</p></div><div id="comment-50625-info" class="comment-info"><span class="comment-age">(01 Mar '16, 11:08)</span> anikastu</div></div></div><div id="comment-tools-50605" class="comment-tools"></div><div class="clear"></div><div id="comment-50605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

