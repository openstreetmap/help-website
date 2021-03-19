+++
type = "question"
title = "How do i watch resolved and unresolved MAC simultaneously?"
description = '''how do i watch resolved and unresolved MAC simultaneously? all columns i add are either resolved or unresolved...'''
date = "2011-10-27T02:02:00Z"
lastmod = "2011-10-27T18:45:00Z"
weight = 7091
keywords = [ "mac", "resolve", "oui" ]
aliases = [ "/questions/7091" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do i watch resolved and unresolved MAC simultaneously?](/questions/7091/how-do-i-watch-resolved-and-unresolved-mac-simultaneously)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7091-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how do i watch resolved and unresolved MAC simultaneously? all columns i add are either resolved or unresolved...</p></div><div id="question-tags" class="tags-container tags">mac resolve oui</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '11, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/9f35f936774f93794a223288437c89a1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Daniil%20Kharkov&#39;s gravatar image" /><p>Daniil Kharkov<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Daniil Kharkov has no accepted answers">0%</span></p></div></div><div id="comments-container-7091" class="comments-container"></div><div id="comment-tools-7091" class="comment-tools"></div><div class="clear"></div><div id="comment-7091-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7121"></span>

<div id="answer-container-7121" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7121-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean "how can I see both the resolved and unresolved MAC in the same column?", the answer is "you can't". Wireshark doesn't support that.</p><p>If you mean "how can I see both the resolved and unresolved MAC in different columns", the answer is "add one column for the resolved address and another column for the unresolved address".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '11, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7121" class="comments-container"><span id="7129"></span><div id="comment-7129" class="comment"><div id="post-7129-score" class="comment-score"></div><div class="comment-text"><p>The thing I realized when testing for Daniils question was that</p><ol><li>There is only resolved or unresolved MAC addresses depending on name resolution setting (both coloumns in 1.6.2 on my machine show the same results)</li><li>There is the IP address being displayed in the coloumn as soon as there is an IP header in the frame</li></ol><p>Is this wanted?</p></div><div id="comment-7129-info" class="comment-info"><span class="comment-age">(28 Oct '11, 00:24)</span> Landi</div></div><span id="7131"></span><div id="comment-7131" class="comment"><div id="post-7131-score" class="comment-score"></div><div class="comment-text"><p>Is <em>what</em> wanted?</p><p>You can have "resolved", "unresolved", or unspecified columns; "resolved" and unspecified currently mean "show the resolved value if resolution is enabled and it could be resolved" (I think the intention was that "resolved" resolves regardless of whether resolution is enabled" and "unresolved" always shows the unresolved value.</p><p>You can have source or destination columns.</p><p>You can have the link-layer ("Hw") address, the network-layer address, or just an address, which is "network-layer if it has one, link-layer otherwise.</p><p>All of those can be selected independently.</p></div><div id="comment-7131-info" class="comment-info"><span class="comment-age">(28 Oct '11, 02:13)</span> Guy Harris ♦♦</div></div><span id="7134"></span><div id="comment-7134" class="comment"><div id="post-7134-score" class="comment-score"></div><div class="comment-text"><p>I see same results in Hw src addr(resolved) and Hw src addr(unresolved), thats what I'm talking about ! Both coloumns just change from resolved to unresolved via name resolution setting in general on my current test setup with 1.6.2</p></div><div id="comment-7134-info" class="comment-info"><span class="comment-age">(28 Oct '11, 02:25)</span> Landi</div></div><span id="7136"></span><div id="comment-7136" class="comment"><div id="post-7136-score" class="comment-score">1</div><div class="comment-text"><p>Link-layer addresses are resolved by looking in the <code>ethers</code> file in the Wireshark install directory, if one exists, and in your Wireshark configuration directory, if it exists, and by Wireshark looking at ARP replies and associating whatever host name is found for the IP address with the corresponding Ethernet address. Without any information from those sources, it just shows the MAC address for a "resolved" address.</p></div><div id="comment-7136-info" class="comment-info"><span class="comment-age">(28 Oct '11, 02:56)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-7121" class="comment-tools"></div><div class="clear"></div><div id="comment-7121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

