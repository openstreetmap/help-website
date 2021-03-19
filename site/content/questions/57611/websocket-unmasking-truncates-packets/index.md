+++
type = "question"
title = "Websocket unmasking truncates packets"
description = '''(apologies if this is a repost, but I think the forum lost my initial post after I signed up) I&#x27;m debugging an application which sends websocket JSON packets up to 20MB in size. I&#x27;m filtering on (websocket). With unmasked (outbound) packets, unmasking appears to truncate the packet.  Outbound (maske...'''
date = "2016-11-24T07:26:00Z"
lastmod = "2017-01-04T11:42:00Z"
weight = 57611
keywords = [ "mask", "websocket", "truncated" ]
aliases = [ "/questions/57611" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Websocket unmasking truncates packets](/questions/57611/websocket-unmasking-truncates-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57611-score" class="post-score" title="current number of votes">0</div><span id="post-57611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>(apologies if this is a repost, but I think the forum lost my initial post after I signed up)</p><p>I'm debugging an application which sends websocket JSON packets up to 20MB in size. I'm filtering on <code>(websocket)</code>. With unmasked (outbound) packets, unmasking appears to truncate the packet.</p><hr /><h1 id="outbound-masked-packet">Outbound (masked) packet</h1><p>In the tabs below the dump:</p><pre><code>Frame (620 bytes) | Reassembled TCP (1483458 bytes) | Unmasked data (262144 bytes)</code></pre><p>In the Websocket header:</p><pre><code>Extended Payload length (64 bits): 1483444</code></pre><p>"Javascript Object Notation" can't be expanded.</p><hr /><h1 id="inbound-unmasked-packet">Inbound (unmasked) packet</h1><p>In contrast, when I view an unmasked (inbound) packet:</p><p>Tabs:</p><pre><code>Frame (1040 bytes) | Reassembled TCP (1477944)</code></pre><p>Websocket header:</p><pre><code>Extended Payload length (64 bits): 1477934</code></pre><p>"Javascript Object Notation" can be expanded.</p><hr /><p>I'm actually debugging a problem whereby my Java application cannot receive large messages (but is sending them OK), so this doesn't impede my work - but in case it's a bug, I figured I should post here.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mask" rel="tag" title="see questions tagged &#39;mask&#39;">mask</span> <span class="post-tag tag-link-websocket" rel="tag" title="see questions tagged &#39;websocket&#39;">websocket</span> <span class="post-tag tag-link-truncated" rel="tag" title="see questions tagged &#39;truncated&#39;">truncated</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '16, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/9f8008ca019e88e24dc5fd1ae1e1b336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="markkc&#39;s gravatar image" /><p><span>markkc</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="markkc has no accepted answers">0%</span></p></div></div><div id="comments-container-57611" class="comments-container"></div><div id="comment-tools-57611" class="comment-tools"></div><div class="clear"></div><div id="comment-57611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58513"></span>

<div id="answer-container-58513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58513-score" class="post-score" title="current number of votes">0</div><span id="post-58513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's actually not a bug. The Websocket dissector intentionally limits the unmasked data to 256 kbytes:</p><p><code>#define MAX_UNMASKED_LEN (1024 * 256)</code></p><p>I suppose it could be made more obvious that this is what has happened--maybe an expert info would be useful here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58513" class="comments-container"></div><div id="comment-tools-58513" class="comment-tools"></div><div class="clear"></div><div id="comment-58513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

