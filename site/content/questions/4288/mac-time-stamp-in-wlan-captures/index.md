+++
type = "question"
title = "MAC Time Stamp in WLAN captures"
description = '''Hi, I would like to capture an put a time stamp at the beginning of MPDU or before MPDU starts. Can anybody help me regarding this. Thanks you in advance, Best Regards, Amin'''
date = "2011-05-30T07:22:00Z"
lastmod = "2011-06-03T13:14:00Z"
weight = 4288
keywords = [ "timestamp", "mac", "wlan", "radioheader" ]
aliases = [ "/questions/4288" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAC Time Stamp in WLAN captures](/questions/4288/mac-time-stamp-in-wlan-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4288-score" class="post-score" title="current number of votes">0</div><span id="post-4288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,<br />
I would like to capture an put a time stamp at the beginning of MPDU or before MPDU starts. Can anybody help me regarding this. Thanks you in advance, Best Regards, Amin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span> <span class="post-tag tag-link-radioheader" rel="tag" title="see questions tagged &#39;radioheader&#39;">radioheader</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '11, 07:22</strong></p><img src="https://secure.gravatar.com/avatar/559f374efd2eaeaafac5616bbec62008?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AminGho&#39;s gravatar image" /><p><span>AminGho</span><br />
<span class="score" title="51 reputation points">51</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AminGho has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4288" class="comments-container"><span id="4368"></span><div id="comment-4368" class="comment"><div id="post-4368-score" class="comment-score"></div><div class="comment-text"><p>Are you looking for radiotap.mactime?</p><pre><code>$ tshark -i 1 -T fields -e frame.number -e radiotap.mactime
Capturing on AirPcap USB wireless capture adapter nr. 00
1       52586108
2       52669071
3       52673115</code></pre></div><div id="comment-4368-info" class="comment-info"><span class="comment-age">(03 Jun '11, 13:14)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-4288" class="comment-tools"></div><div class="clear"></div><div id="comment-4288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4331"></span>

<div id="answer-container-4331" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4331-score" class="post-score" title="current number of votes">0</div><span id="post-4331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Timestamps are retrieved from the libpcap/winpcap library, which in turn get the timestamp from the OS kernel.<br />
</p><p>This may be oversimplified for what you actually need but...</p><p>if you are using tshark you could use:</p><p>tshark -i (interface#) -T fields -e frame.time -e (whatever other fields you want to display)</p><p>For capturing, time stamp is already included in every packet, but you can output different formats using parameters as follows:</p><p>tshark -i (interface#) -t ad (absolute date and time) or -t a (absolute time) or -t r (relative time between 1st and current packet) or -t d (delta from previous packet) or -t dd (displayed delta) or -t e (epoch time since 1/1/1970).</p><p>Hope this is helpful,</p><p>John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '11, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4331" class="comments-container"></div><div id="comment-tools-4331" class="comment-tools"></div><div class="clear"></div><div id="comment-4331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

