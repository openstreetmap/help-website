+++
type = "question"
title = "How can you monitor multiple switches?"
description = '''Suppose I had two connected Ethernet switches, and many hosts communicating across them that I wanted to monitor traffic on. If I only have one available port on one of the two switches, is there some way I can configure them (using e.g. mirroring, etc) to show me all of the traffic on both switches...'''
date = "2014-07-15T12:39:00Z"
lastmod = "2014-07-15T12:39:00Z"
weight = 34679
keywords = [ "ethernet", "switch", "mirroring", "capture-setup" ]
aliases = [ "/questions/34679" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can you monitor multiple switches?](/questions/34679/how-can-you-monitor-multiple-switches)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34679-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34679-score" class="post-score" title="current number of votes">1</div><span id="post-34679-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Suppose I had two connected Ethernet switches, and many hosts communicating across them that I wanted to monitor traffic on. If I only have one available port on one of the two switches, is there some way I can configure them (using e.g. mirroring, etc) to show me all of the traffic on both switches on the monitor port?</p><p>This is roughly what I mean:</p><pre><code>    B    D
    |    |
A--S1----S2--E
    |    |
    C    Monitor</code></pre>I'm interested in traffic between any two hosts (e.g. A-B, D-C, E-D, etc) and can only connect to the monitor port.</div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-mirroring" rel="tag" title="see questions tagged &#39;mirroring&#39;">mirroring</span> <span class="post-tag tag-link-capture-setup" rel="tag" title="see questions tagged &#39;capture-setup&#39;">capture-setup</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '14, 12:39</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-34679" class="comments-container"></div><div id="comment-tools-34679" class="comment-tools"></div><div class="clear"></div><div id="comment-34679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

