+++
type = "question"
title = "IPv4 options"
description = '''I have a IPv4 packet which has encapsulated over IPv6. tunneling setup protocol is used. Now i want to check which options from IPv4 header are being used in a packet. What is the way to do that? How can I identify which options are being used?'''
date = "2017-04-21T16:13:00Z"
lastmod = "2017-04-21T18:36:00Z"
weight = 60955
keywords = [ "header", "ipv4", "headers" ]
aliases = [ "/questions/60955" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IPv4 options](/questions/60955/ipv4-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60955-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a IPv4 packet which has encapsulated over IPv6. tunneling setup protocol is used. Now i want to check which options from IPv4 header are being used in a packet. What is the way to do that? How can I identify which options are being used?</p></div><div id="question-tags" class="tags-container tags">header ipv4 headers</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '17, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/b50437b9c7e5ff0320d685251c2e8e04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Prashantvaria9&#39;s gravatar image" /><p>Prashantvaria9<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Prashantvaria9 has no accepted answers">0%</span></p></div></div><div id="comments-container-60955" class="comments-container"></div><div id="comment-tools-60955" class="comment-tools"></div><div class="clear"></div><div id="comment-60955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60956"></span>

<div id="answer-container-60956" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60956-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can apply a Wireshark display filter of <code>ip.hdr_len &gt; 20</code> or <code>ip.opt.type</code>, which will isolate those packets that contain IPv4 options, and then expand the IPv4 protocol details within the packet details pane to reveal the packet details. You should see the <em>"Options"</em> listed, and you can expand those too if you like.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '17, 18:36</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-60956" class="comments-container"></div><div id="comment-tools-60956" class="comment-tools"></div><div class="clear"></div><div id="comment-60956-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

