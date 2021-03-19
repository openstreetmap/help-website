+++
type = "question"
title = "What is backing_length, reported_length ?"
description = '''void tvb_set_subset  ( tvbuff_t * tvb,   tvbuff_t * backing,   const gint backing_offset,   const gint backing_length,   const gint reported_length  )  What is backing_length, reported_length here ? Please help.'''
date = "2013-02-28T23:28:00Z"
lastmod = "2013-03-01T03:05:00Z"
weight = 19015
keywords = [ "dissector", "tvb" ]
aliases = [ "/questions/19015" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is backing\_length, reported\_length ?](/questions/19015/what-is-backing_length-reported_length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19015-score" class="post-score" title="current number of votes">0</div><span id="post-19015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>void tvb_set_subset  
(   tvbuff_t *  tvb,    
    tvbuff_t *  backing,  
    const gint  backing_offset,  
    const gint  backing_length,  
    const gint  reported_length  
)</code></pre><p>What is backing_length, reported_length here ?</p><p>Please help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tvb" rel="tag" title="see questions tagged &#39;tvb&#39;">tvb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p><span>yogeshg</span><br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Mar '13, 02:54</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-19015" class="comments-container"></div><div id="comment-tools-19015" class="comment-tools"></div><div class="clear"></div><div id="comment-19015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19022"></span>

<div id="answer-container-19022" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19022-score" class="post-score" title="current number of votes">3</div><span id="post-19022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="yogeshg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This function makes <code>tvb</code> a subset of <code>backing</code>. It creates a window upon the backing tvb as it were. The boundaries of that window are given by <code>backing_offset</code> and <code>backing_length</code>. The <code>reported_length</code> is the length as optionally reported by a lower layer protocol. It may be that during capture only the first part of a frame is captured, whereby the data in a protocol header can indicate what the true length of the frame, or packet on that protocol layer would have been. Then, if you dissect your protocol, you can discern why you run out of data, either because it is not in the frame (which is a protocol violation), or it may have been there, but was not captured (which is not a protocol violation, just a limitation of the capture).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-19022" class="comments-container"></div><div id="comment-tools-19022" class="comment-tools"></div><div class="clear"></div><div id="comment-19022-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

