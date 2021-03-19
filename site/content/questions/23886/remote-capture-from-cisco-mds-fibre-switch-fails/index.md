+++
type = "question"
title = "Remote capture from Cisco MDS Fibre Switch fails"
description = '''I&#x27;m attempting to capture fibre channel traffic from a Cisco MDS Fibre channel switch via pcap. While attempting to a remote capture I captured the traffic to see why it was failing. Looks like the list interfaces request and reply worked. The authentication worked also. During the remote capture st...'''
date = "2013-08-20T17:23:00Z"
lastmod = "2013-08-20T20:06:00Z"
weight = 23886
keywords = [ "capture", "cisco", "remote", "mds" ]
aliases = [ "/questions/23886" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remote capture from Cisco MDS Fibre Switch fails](/questions/23886/remote-capture-from-cisco-mds-fibre-switch-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23886-score" class="post-score" title="current number of votes">0</div><span id="post-23886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm attempting to capture fibre channel traffic from a Cisco MDS Fibre channel switch via pcap. While attempting to a remote capture I captured the traffic to see why it was failing. Looks like the list interfaces request and reply worked. The authentication worked also. During the remote capture start I got generic updatefilter error 7</p><p>I'll upload the trace. Has anyone done this before?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span> <span class="post-tag tag-link-mds" rel="tag" title="see questions tagged &#39;mds&#39;">mds</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '13, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p><span>gipper</span><br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div></div><div id="comments-container-23886" class="comments-container"><span id="23887"></span><div id="comment-23887" class="comment"><div id="post-23887-score" class="comment-score"></div><div class="comment-text"><p>Here's my capture. <a href="http://www.cloudshark.org/captures/b2e59aeb2e4c">http://www.cloudshark.org/captures/b2e59aeb2e4c</a></p><p>Windows host running wireshark and pcap IP = 172.31.110.40</p><p>Cisco MDS switch IP = 172.18.1.71</p></div><div id="comment-23887-info" class="comment-info"><span class="comment-age">(20 Aug '13, 17:32)</span> <span class="comment-user userinfo">gipper</span></div></div></div><div id="comment-tools-23886" class="comment-tools"></div><div class="clear"></div><div id="comment-23886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23889"></span>

<div id="answer-container-23889" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23889-score" class="post-score" title="current number of votes">0</div><span id="post-23889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I was able to figure this out.</p><p>Needed wireshark v 1.0.6.</p><p>fcanalyzer remote 172.31.110.40</p><p>RACK06-9124-01# show fcanalyzer PassiveClient = 172.31.110.40</p><p>Wireshark capture options rpcap://[172.18.1.71]/eth2</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '13, 20:06</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p><span>gipper</span><br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div></div><div id="comments-container-23889" class="comments-container"></div><div id="comment-tools-23889" class="comment-tools"></div><div class="clear"></div><div id="comment-23889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

