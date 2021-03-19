+++
type = "question"
title = "tshark: how to limit packet to beginning of data"
description = '''I found that &quot;-e data&quot; can be use to display the packet content. Is there a modified to limit it to only certain bytes of a packet? In fact, what I&#x27;m looking for is the beginning of the UDP payload Here&#x27;s the command I&#x27;m currently using: tshark -r [file] -T fields -e frame.time_relative -e data'''
date = "2014-12-11T21:33:00Z"
lastmod = "2014-12-11T21:33:00Z"
weight = 38536
keywords = [ "tshark", "display-filter" ]
aliases = [ "/questions/38536" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark: how to limit packet to beginning of data](/questions/38536/tshark-how-to-limit-packet-to-beginning-of-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38536-score" class="post-score" title="current number of votes">0</div><span id="post-38536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I found that "-e data" can be use to display the packet content. Is there a modified to limit it to only certain bytes of a packet? In fact, what I'm looking for is the beginning of the UDP payload</p><p>Here's the command I'm currently using:</p><p><code>tshark -r [file] -T fields -e frame.time_relative -e data</code></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '14, 21:33</strong></p><img src="https://secure.gravatar.com/avatar/78d586a6dd20a19a7164910902f95718?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fseto&#39;s gravatar image" /><p><span>fseto</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fseto has no accepted answers">0%</span></p></div></div><div id="comments-container-38536" class="comments-container"></div><div id="comment-tools-38536" class="comment-tools"></div><div class="clear"></div><div id="comment-38536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

