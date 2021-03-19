+++
type = "question"
title = "DNS fragment over TCP"
description = '''I captured some dns packets over tcp,some dns fragment packets are found.why these dns packets should be fragmented (not ip layer fragments,just dns payload fragment)but the length&amp;lt;1500? '''
date = "2012-12-06T22:19:00Z"
lastmod = "2012-12-10T14:25:00Z"
weight = 16670
keywords = [ "fragment", "tcp", "dns" ]
aliases = [ "/questions/16670" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DNS fragment over TCP](/questions/16670/dns-fragment-over-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16670-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I captured some dns packets over tcp,some dns fragment packets are found.why these dns packets should be fragmented (not ip layer fragments,just dns payload fragment)but the length&lt;1500?</p></div><div id="question-tags" class="tags-container tags">fragment tcp dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '12, 22:19</strong></p><img src="https://secure.gravatar.com/avatar/7fdbac8aac2e38813e1fc1da4c6efdf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chinasan&#39;s gravatar image" /><p>chinasan<br />
<span class="score" title="0 reputation points">0</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chinasan has no accepted answers">0%</span></p></div></div><div id="comments-container-16670" class="comments-container"><span id="16676"></span><div id="comment-16676" class="comment"><div id="post-16676-score" class="comment-score">1</div><div class="comment-text"><p>can you please post a screenshot of that "dns fragement" message?</p></div><div id="comment-16676-info" class="comment-info"><span class="comment-age">(07 Dec '12, 05:43)</span> Kurt Knochner ♦</div></div><span id="16740"></span><div id="comment-16740" class="comment"><div id="post-16740-score" class="comment-score"></div><div class="comment-text"><p>A picture can not be attached without reason,just description as follows: The first dns payload is "0x00"(just 1 bytes),The second payload is beging with "0x16........";Two bytes means the length of DNS payload part.The two tcp packets is also shown as one tcp segment in wireshark(like http get message:the reassembled tcp segments :No.1 and No.4 )</p></div><div id="comment-16740-info" class="comment-info"><span class="comment-age">(09 Dec '12, 22:07)</span> chinasan</div></div><span id="16746"></span><div id="comment-16746" class="comment"><div id="post-16746-score" class="comment-score"></div><div class="comment-text"><blockquote><p>A picture can not be attached without reason</p></blockquote><p>The reason is: you are asking for help, but you did not provide enough information in text form to fully understand the problem ;-))</p></div><div id="comment-16746-info" class="comment-info"><span class="comment-age">(10 Dec '12, 05:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16670" class="comment-tools"></div><div class="clear"></div><div id="comment-16670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16757"></span>

<div id="answer-container-16757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16757-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>why these dns packets should be fragmented (not ip layer fragments,just dns payload fragment)but the length&lt;1500?</p></blockquote><p>Because whoever wrote the DNS code that sent those packets is doing something silly, such as sending the first byte of the packet length with one "write to the network" call and the rest of the packet length in another "write to the network" call, and the TCP implementation isn't coalescing them into one TCP segment?</p><blockquote><p>The two tcp packets is also shown as one tcp segment in wireshark(like http get message:the reassembled tcp segments :No.1 and No.4 )</p></blockquote><p>That's not one TCP segment, that's <em>two</em> TCP segments - a TCP packet <em>is</em> a TCP segment. Wireshark is reassembling the two segments into a single chunk of data that holds the entire DNS packet and dissecting that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '12, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16757" class="comments-container"></div><div id="comment-tools-16757" class="comment-tools"></div><div class="clear"></div><div id="comment-16757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

