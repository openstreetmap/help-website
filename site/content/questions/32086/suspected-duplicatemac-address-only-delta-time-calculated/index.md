+++
type = "question"
title = "Suspected duplicate(MAC address) only delta time calculated"
description = '''I was trying to capture the packet of RTP flow, but for every packet, i captured it twice, so the analyst in wireshark say &quot;Suspected duplicate(MAC address) only delta time calculated&quot;. But when i captured it in another laptop, this problem is gone.  I tried to read the source code of wireshark and ...'''
date = "2014-04-23T00:28:00Z"
lastmod = "2014-04-23T11:58:00Z"
weight = 32086
keywords = [ "duplicate" ]
aliases = [ "/questions/32086" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Suspected duplicate(MAC address) only delta time calculated](/questions/32086/suspected-duplicatemac-address-only-delta-time-calculated)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32086-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was trying to capture the packet of RTP flow, but for every packet, i captured it twice, so the analyst in wireshark say "Suspected duplicate(MAC address) only delta time calculated". But when i captured it in another laptop, this problem is gone. I tried to read the source code of wireshark and found this code</p><pre><code>else if (statinfo-&gt;flags &amp; STAT_FLAG_DUP_PKT) {
    g_snprintf(status, sizeof(status), &quot;Suspected duplicate(MAC address) only delta time calculated&quot;);</code></pre><p>I still don't have any clue what is this about. Can anyone tell me? Thanks.</p><p>Regards</p><p>muyu</p></div><div id="question-tags" class="tags-container tags">duplicate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 00:28</strong></p><img src="https://secure.gravatar.com/avatar/0c85a53213894d856e72ab3630daca5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="muyu&#39;s gravatar image" /><p>muyu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="muyu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '14, 01:13</p></div></div><div id="comments-container-32086" class="comments-container"></div><div id="comment-tools-32086" class="comment-tools"></div><div class="clear"></div><div id="comment-32086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32117"></span>

<div id="answer-container-32117" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32117-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>i captured it twice</strong>, so the analyst in wireshark say</p></blockquote><p>You should stop capturing the frames twice, as that's (probably) causing the problem. Something seems to be wrong with your capture setup. As you did not add any information about your setup, it's impossible to give any advice what could have caused this. Please add more details.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '14, 11:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '14, 12:36</p></div></div><div id="comments-container-32117" class="comments-container"></div><div id="comment-tools-32117" class="comment-tools"></div><div class="clear"></div><div id="comment-32117-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

