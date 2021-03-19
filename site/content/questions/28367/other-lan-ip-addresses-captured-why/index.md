+++
type = "question"
title = "Other LAN IP addresses captured. Why?"
description = '''I conducted a capture from a workstation to troubleshoot an application. I built a filter to drop all traffic from the workstation and only show me TCP traffic. What I am seeing is the switch is forwarding TCP packets from the WAN to the workstation. I reviewed the configuration for the switchport a...'''
date = "2013-12-24T06:07:00Z"
lastmod = "2013-12-27T04:08:00Z"
weight = 28367
keywords = [ "layer", "2", "switchport" ]
aliases = [ "/questions/28367" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Other LAN IP addresses captured. Why?](/questions/28367/other-lan-ip-addresses-captured-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28367-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28367-score" class="post-score" title="current number of votes">0</div><span id="post-28367-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I conducted a capture from a workstation to troubleshoot an application. I built a filter to drop all traffic from the workstation and only show me TCP traffic. What I am seeing is the switch is forwarding TCP packets from the WAN to the workstation. I reviewed the configuration for the switchport and it is NOT trunked but rather configured for switchport mode access. Am at a loss as to why I am seeing this occurring on a switch that is doing layer 2 switching.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-layer" rel="tag" title="see questions tagged &#39;layer&#39;">layer</span> <span class="post-tag tag-link-2" rel="tag" title="see questions tagged &#39;2&#39;">2</span> <span class="post-tag tag-link-switchport" rel="tag" title="see questions tagged &#39;switchport&#39;">switchport</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '13, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/5b20990cd21bd091665e684410ebe9fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdJ&#39;s gravatar image" /><p><span>EdJ</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdJ has no accepted answers">0%</span></p></div></div><div id="comments-container-28367" class="comments-container"><span id="28431"></span><div id="comment-28431" class="comment"><div id="post-28431-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I built a filter to drop all traffic from the workstation and only show me TCP traffic.</p></blockquote><p>what is the filter you were using?</p></div><div id="comment-28431-info" class="comment-info"><span class="comment-age">(27 Dec '13, 04:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28367" class="comment-tools"></div><div class="clear"></div><div id="comment-28367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28416"></span>

<div id="answer-container-28416" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28416-score" class="post-score" title="current number of votes">0</div><span id="post-28416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is it broadcast traffic from the switch that you're seeing hitting the workstation? Most likely, the WAN is passing packets to the switch, the switch is not finding the destination for those packets in it's tables, and it is sending the traffic out all interfaces. I believe that would be the expected behavior for the scenario that you're describing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Dec '13, 21:27</strong></p><img src="https://secure.gravatar.com/avatar/c3503bfc7ff8f99752af69a25983d5ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frobbotzim&#39;s gravatar image" /><p><span>Frobbotzim</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frobbotzim has one accepted answer">33%</span></p></div></div><div id="comments-container-28416" class="comments-container"></div><div id="comment-tools-28416" class="comment-tools"></div><div class="clear"></div><div id="comment-28416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

