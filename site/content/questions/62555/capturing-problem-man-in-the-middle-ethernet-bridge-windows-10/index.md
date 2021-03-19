+++
type = "question"
title = "Capturing problem Man-in-the-middle ethernet bridge windows 10"
description = '''Hello, I&#x27;m trying to capture in promiscuous mode the traffic to a host on a windows 10 laptop. I have 2 ethernet interface binded each other with the bridge utility of windows. So I&#x27;ve putted my laptop in the middle of communication of my test device. the device is working well, so the bridge is fin...'''
date = "2017-07-06T01:29:00Z"
lastmod = "2017-07-06T01:39:00Z"
weight = 62555
keywords = [ "ethernet", "promiscuous", "capture", "bridge" ]
aliases = [ "/questions/62555" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing problem Man-in-the-middle ethernet bridge windows 10](/questions/62555/capturing-problem-man-in-the-middle-ethernet-bridge-windows-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62555-score" class="post-score" title="current number of votes">0</div><span id="post-62555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm trying to capture in promiscuous mode the traffic to a host on a windows 10 laptop. I have 2 ethernet interface binded each other with the bridge utility of windows. So I've putted my laptop in the middle of communication of my test device. the device is working well, so the bridge is fine. When I try to capture the packets in promiscuous mode to this host I can capture only packet from or to my address. Anyone can figure out why? Thanks</p><p>Federico</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '17, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/d9f6f98b3df6807c3c14f4f8214452fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fmusso&#39;s gravatar image" /><p><span>fmusso</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fmusso has no accepted answers">0%</span></p></div></div><div id="comments-container-62555" class="comments-container"><span id="62556"></span><div id="comment-62556" class="comment"><div id="post-62556-score" class="comment-score"></div><div class="comment-text"><p>Do you use WinPcap or NPcap? WinPcap allows you to capture at one of the physical interfaces forming up the bridge, which is what you need to do to capture the transit traffic; NPcap only allows you to capture at the virtual interface representing the bridge to the rest of the OS, so only packets to/from this interface can be captured, not those transiting between the physical ports.</p></div><div id="comment-62556-info" class="comment-info"><span class="comment-age">(06 Jul '17, 01:39)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-62555" class="comment-tools"></div><div class="clear"></div><div id="comment-62555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

