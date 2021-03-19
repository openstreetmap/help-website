+++
type = "question"
title = "How to use tvb_new_subset"
description = '''I have a packet as A:12 bytes, B:20 bytes. C:16 bytes In the dissector for B the whole tvb gets passed i.e. A, B, C. Now dissector for B calls dissector for C. C also handles the dissection of A. So in dissector B how will I use the tvb_new_subset. Currently all I am seeing are examples like tvb_new...'''
date = "2015-10-12T21:54:00Z"
lastmod = "2015-10-13T01:54:00Z"
weight = 46486
keywords = [ "dissector", "tvb", "tshark", "packet", "wireshark" ]
aliases = [ "/questions/46486" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use tvb\_new\_subset](/questions/46486/how-to-use-tvb_new_subset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46486-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a packet as A:12 bytes, B:20 bytes. C:16 bytes</p><p>In the dissector for B the whole tvb gets passed i.e. A, B, C. Now dissector for B calls dissector for C. C also handles the dissection of A. So in dissector B how will I use the tvb_new_subset.</p><p>Currently all I am seeing are examples like tvb_new_subset(tvb, 20, -1, -1)</p><p>But that would remove 12 bytes of A and 8 bytes of B. I want to remove 20 bytes of B only and pass it to C.</p></div><div id="question-tags" class="tags-container tags">dissector tvb tshark packet wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '15, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/5c6557bd7c8696a17e1c44bae9cd4217?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samprit&#39;s gravatar image" /><p>samprit<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samprit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Oct '15, 23:28</p></div></div><div id="comments-container-46486" class="comments-container"></div><div id="comment-tools-46486" class="comment-tools"></div><div class="clear"></div><div id="comment-46486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46492"></span>

<div id="answer-container-46492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46492-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have a packet as A:12 bytes, B:20 bytes. C:16 bytes</p></blockquote><p>I.e., there's a 12-byte header for protocol A, followed by 36 bytes of payload for A, with the 36 bytes of payload for A having 20 bytes of header for B and 16 bytes of payload for B, and with the 16 bytes of payload for B being a packet for C?</p><blockquote><p>In the dissector for B the whole tvb gets passed i.e. A, B, C.</p></blockquote><p>That's not how it's supposed to work. The dissector for A is supposed to dissect the 12-byte header, and then use <code>tvb_new_subset_remaining(tvb, 12)</code> to get a tvbuff for the payload for A, and pass that to the dissector for B.</p><blockquote><p>Now dissector for B calls dissector for C.</p></blockquote><p>And it should then dissect the header for B, and then use <code>tvb_new_subset_remaining(tvb, 20)</code>, where <code>tvb</code> here is the tvbuff handed to the dissector for B, to get a tvbuff for the payload for B, and pass that to the dissector for C.</p><blockquote><p>C also handles the dissection of A.</p></blockquote><p>That's not how it's supposed to work. Why cannot the dissector for A handle that?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-46492" class="comments-container"><span id="46493"></span><div id="comment-46493" class="comment"><div id="post-46493-score" class="comment-score"></div><div class="comment-text"><p>Actually there is no dissector for A. The dissector for A is being handled in the dissector for C. So I wanted to remove the 20bytes of B and pass it to C. Is there a way to remove the middle data fron tvbuff?</p></div><div id="comment-46493-info" class="comment-info"><span class="comment-age">(13 Oct '15, 01:57)</span> samprit</div></div><span id="46494"></span><div id="comment-46494" class="comment"><div id="post-46494-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Is there a way to remove the middle data fron tvbuff?</p></blockquote><p>No. Try not handling the dissector for A in the dissector for C, instead.</p></div><div id="comment-46494-info" class="comment-info"><span class="comment-age">(13 Oct '15, 02:09)</span> Guy Harris ♦♦</div></div><span id="46496"></span><div id="comment-46496" class="comment"><div id="post-46496-score" class="comment-score"></div><div class="comment-text"><p>...Or handle dissection of C in the dissector of A... Then all you have to do is create a tvb subset of B and hand that off the the dissector for B.</p></div><div id="comment-46496-info" class="comment-info"><span class="comment-age">(13 Oct '15, 06:06)</span> Jaap ♦</div></div></div><div id="comment-tools-46492" class="comment-tools"></div><div class="clear"></div><div id="comment-46492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

