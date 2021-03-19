+++
type = "question"
title = "Reg COBS and Wireshark dissectors"
description = '''Hi, I am developing a dissector for a proprietary protocol. I would like to know how to handle packets that are encoded with COBS - Consistent Overhead Byte Stuffing. Are there any APIs available? Thanks in Advance Regards, Laser'''
date = "2011-01-18T19:23:00Z"
lastmod = "2011-01-19T00:01:00Z"
weight = 1799
keywords = [ "cobs" ]
aliases = [ "/questions/1799" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reg COBS and Wireshark dissectors](/questions/1799/reg-cobs-and-wireshark-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1799-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1799-score" class="post-score" title="current number of votes">0</div><span id="post-1799-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am developing a dissector for a proprietary protocol. I would like to know how to handle packets that are encoded with COBS - Consistent Overhead Byte Stuffing. Are there any APIs available?</p><p>Thanks in Advance</p><p>Regards, Laser</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cobs" rel="tag" title="see questions tagged &#39;cobs&#39;">cobs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '11, 19:23</strong></p><img src="https://secure.gravatar.com/avatar/51d79b551416f55d1a63a19b8a7a98dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Neo%20Laser&#39;s gravatar image" /><p><span>Neo Laser</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Neo Laser has no accepted answers">0%</span></p></div></div><div id="comments-container-1799" class="comments-container"></div><div id="comment-tools-1799" class="comment-tools"></div><div class="clear"></div><div id="comment-1799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1807"></span>

<div id="answer-container-1807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1807-score" class="post-score" title="current number of votes">0</div><span id="post-1807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Direct COBS support isn't available.</p><p>What you should look into is using tvb_*_real_data functions found in <a href="http://anonsvn.wireshark.org/wireshark/trunk/epan/tvbuff.h">tvbuff.h</a></p><pre><code>/** Attach a TVBUFF_REAL_DATA tvbuff to a parent tvbuff. This connection
 * is used during a tvb_free_chain()... the &quot;child&quot; TVBUFF_REAL_DATA acts
 * as if is part of the chain-of-creation of the parent tvbuff, although it
 * isn&#39;t. This is useful if you need to take the data from some tvbuff,
 * run some operation on it, like decryption or decompression, and make a new
 * tvbuff from it, yet want the new tvbuff to be part of the chain. The reality
 * is that the new tvbuff *is* part of the &quot;chain of creation&quot;, but in a way
 * that these tvbuff routines is ignorant of. Use this function to make
 * the tvbuff routines knowledgable of this fact. */</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '11, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1807" class="comments-container"></div><div id="comment-tools-1807" class="comment-tools"></div><div class="clear"></div><div id="comment-1807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

