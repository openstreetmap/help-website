+++
type = "question"
title = "How do I capture iscsi traffic on a VLAN?"
description = '''I have a initiator with the VLAN ID of 1002, and both the switch and target are on the same VLAN. In order to capture this session with Wireshark, do I need to enable a specific capture filter? Or should I just be able to see it regardless and I&#x27;m doing something entirely wrong. Thanks'''
date = "2017-07-24T09:49:00Z"
lastmod = "2017-07-24T13:47:00Z"
weight = 63052
keywords = [ "iscsi", "vlan" ]
aliases = [ "/questions/63052" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I capture iscsi traffic on a VLAN?](/questions/63052/how-do-i-capture-iscsi-traffic-on-a-vlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63052-score" class="post-score" title="current number of votes">0</div><span id="post-63052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a initiator with the VLAN ID of 1002, and both the switch and target are on the same VLAN. In order to capture this session with Wireshark, do I need to enable a specific capture filter? Or should I just be able to see it regardless and I'm doing something entirely wrong. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iscsi" rel="tag" title="see questions tagged &#39;iscsi&#39;">iscsi</span> <span class="post-tag tag-link-vlan" rel="tag" title="see questions tagged &#39;vlan&#39;">vlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '17, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/7d9a9f0dcd958a44ea22b08a097a443f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartersnay&#39;s gravatar image" /><p><span>cartersnay</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartersnay has no accepted answers">0%</span></p></div></div><div id="comments-container-63052" class="comments-container"></div><div id="comment-tools-63052" class="comment-tools"></div><div class="clear"></div><div id="comment-63052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63053"></span>

<div id="answer-container-63053" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63053-score" class="post-score" title="current number of votes">0</div><span id="post-63053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Review your <a href="https://wiki.wireshark.org/CaptureSetup">capture setup</a> carefully with regards to capture point, span or monitor settings, etc. The information you provided on the setup is too scarce to make more detailed recommendations.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '17, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63053" class="comments-container"><span id="63055"></span><div id="comment-63055" class="comment"><div id="post-63055-score" class="comment-score"></div><div class="comment-text"><p>Okay, thanks for replying. A little more specifics is that I am remote desktopping to a windows server that is the host of the initiator. So my capture point is from the host, and I'm trying to capture traffic that runs through the Host Bus Adapter.</p></div><div id="comment-63055-info" class="comment-info"><span class="comment-age">(24 Jul '17, 10:39)</span> <span class="comment-user userinfo">cartersnay</span></div></div><span id="63061"></span><div id="comment-63061" class="comment"><div id="post-63061-score" class="comment-score"></div><div class="comment-text"><p>You talked about the switch and target being on the same clan, but what about the Windows Server?</p></div><div id="comment-63061-info" class="comment-info"><span class="comment-age">(24 Jul '17, 13:47)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-63053" class="comment-tools"></div><div class="clear"></div><div id="comment-63053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

