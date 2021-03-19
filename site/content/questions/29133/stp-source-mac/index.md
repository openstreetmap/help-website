+++
type = "question"
title = "STP - source mac"
description = '''Sir, I must Thank to Wireshark team ,For Developing Such a Master Class tool &quot;the wireshark&quot; Query: i am Capturing STP (spanning tree) traffic and Surprised about why source mac is Unique not exist In My Network Where Destination and Root bridge mac is Known  2,i capture on another switch this time ...'''
date = "2014-01-23T21:07:00Z"
lastmod = "2014-01-24T00:13:00Z"
weight = 29133
keywords = [ "spanningtree", "stp" ]
aliases = [ "/questions/29133" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [STP - source mac](/questions/29133/stp-source-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29133-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29133-score" class="post-score" title="current number of votes">0</div><span id="post-29133-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sir,</p><p>I must Thank to Wireshark team ,For Developing Such a Master Class tool "the wireshark"</p><p>Query:</p><p>i am Capturing STP (spanning tree) traffic and Surprised about why source mac is Unique not exist In My Network Where Destination and Root bridge mac is Known 2,i capture on another switch this time another Source mac address is not exist on my device neither switch...whosse mac is this</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-spanningtree" rel="tag" title="see questions tagged &#39;spanningtree&#39;">spanningtree</span> <span class="post-tag tag-link-stp" rel="tag" title="see questions tagged &#39;stp&#39;">stp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '14, 21:07</strong></p><img src="https://secure.gravatar.com/avatar/1dae1e58a0613c5b11c41ed0a25f6e21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sandeep&#39;s gravatar image" /><p><span>sandeep</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sandeep has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '14, 01:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-29133" class="comments-container"></div><div id="comment-tools-29133" class="comment-tools"></div><div class="clear"></div><div id="comment-29133-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29134"></span>

<div id="answer-container-29134" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29134-score" class="post-score" title="current number of votes">1</div><span id="post-29134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When sending BPDU frames, a switch uses the MAC address of each single switch port as source MAC. It should be quite close to the base mac (which is part of the bridge ID), incremented by one for each port number.</p><p>So if your base MAC of your switch is 00:01:02:03:04:00 the first port usually has 00:01:02:03:04:<strong>01</strong>, port two has 00:01:02:03:04:<strong>02</strong>,..., port 10 has 00:01:02:03:04:<strong>0a</strong>, and so on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '14, 00:13</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '14, 00:13</strong> </span></p></div></div><div id="comments-container-29134" class="comments-container"></div><div id="comment-tools-29134" class="comment-tools"></div><div class="clear"></div><div id="comment-29134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

