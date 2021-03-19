+++
type = "question"
title = "Capture filter to filter SCTP heartbeak chunks"
description = '''We have setup a wireshark monitoring server in our lab. We have used capture filter to filter traffic from specific ports. However there is a lot of SCTP heartbeat exchange between the nodes and this is causing overload on the server and the wireshark application is slowing down.  Is it possible to ...'''
date = "2014-08-07T13:24:00Z"
lastmod = "2014-08-07T14:54:00Z"
weight = 35313
keywords = [ "capture", "sctp", "filters" ]
aliases = [ "/questions/35313" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter to filter SCTP heartbeak chunks](/questions/35313/capture-filter-to-filter-sctp-heartbeak-chunks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35313-score" class="post-score" title="current number of votes">0</div><span id="post-35313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have setup a wireshark monitoring server in our lab. We have used capture filter to filter traffic from specific ports. However there is a lot of SCTP heartbeat exchange between the nodes and this is causing overload on the server and the wireshark application is slowing down.</p><p>Is it possible to use capture filter on SCTP level to filter out SCTP heartbeat chhunks? Is this supported yet by the wireshark application? I tried to search this online but couldnt find any info on this.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-sctp" rel="tag" title="see questions tagged &#39;sctp&#39;">sctp</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '14, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/581bac4fff7c1939f6eb32569ee491dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudhir_shet&#39;s gravatar image" /><p><span>sudhir_shet</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudhir_shet has no accepted answers">0%</span></p></div></div><div id="comments-container-35313" class="comments-container"></div><div id="comment-tools-35313" class="comment-tools"></div><div class="clear"></div><div id="comment-35313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35315"></span>

<div id="answer-container-35315" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35315-score" class="post-score" title="current number of votes">0</div><span id="post-35315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that your SCTP stack does not send any other chunk types in the same IP packet as the heartbeat and acks, you can do that with a filter including a statement like 'not ip[x:1]=04 and not ip[x:1]=05', where "x" is the byte to start in out of the begining of the IP header of the packet. Basically, you're telling the capture filter to go "x" bytes into the packet and check to see if the next one byte (the chunk type byte in the SCTP header) is equal to 4 or 5 (heartbeat or acks).</p><p>I don't have a working example on hand at the moment but I've worked out a filter like that in the past with some success. I did run up against one (uncommon?) stack that was including other chunk types in heartbeats though so by filtering them you risk filtering data chunks also.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '14, 14:54</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Aug '14, 14:55</strong> </span></p></div></div><div id="comments-container-35315" class="comments-container"></div><div id="comment-tools-35315" class="comment-tools"></div><div class="clear"></div><div id="comment-35315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

