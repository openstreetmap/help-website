+++
type = "question"
title = "Can TShark be used without WireShark"
description = '''I am interested in capturing traffic on our network from a range of devices as part of a device trial. The devices will not have wireshark installed on them. Is it possible to still capture data from these trial devices using TShark?'''
date = "2012-01-10T07:20:00Z"
lastmod = "2012-02-27T14:01:00Z"
weight = 8301
keywords = [ "trial", "data", "tshark", "capture" ]
aliases = [ "/questions/8301" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can TShark be used without WireShark](/questions/8301/can-tshark-be-used-without-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8301-score" class="post-score" title="current number of votes">0</div><span id="post-8301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am interested in capturing traffic on our network from a range of devices as part of a device trial. The devices will not have wireshark installed on them. Is it possible to still capture data from these trial devices using TShark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-trial" rel="tag" title="see questions tagged &#39;trial&#39;">trial</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jan '12, 07:20</strong></p><img src="https://secure.gravatar.com/avatar/a09c18d19a17f41fcbe1ee33875975bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike4G&#39;s gravatar image" /><p><span>Mike4G</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike4G has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '12, 20:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-8301" class="comments-container"><span id="8307"></span><div id="comment-8307" class="comment"><div id="post-8307-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "capture data from these trial devices"? You can capture traffic from a device using Wireshark, or TShark, or tcpdump, or snoop, or..., without having Wireshark, or TShark, or tcpdump, or snoop, or... running on the device itself, as long as you're on the same network as the device.</p></div><div id="comment-8307-info" class="comment-info"><span class="comment-age">(10 Jan '12, 12:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-8301" class="comment-tools"></div><div class="clear"></div><div id="comment-8301-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8303"></span>

<div id="answer-container-8303" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8303-score" class="post-score" title="current number of votes">0</div><span id="post-8303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, probably. But remember that you will still need to have installed the libpcap (or winpcap, depending of your target platform) device driver.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '12, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/b260fb38b621169269b5030f1ed6b766?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="griff&#39;s gravatar image" /><p><span>griff</span><br />
<span class="score" title="361 reputation points">361</span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="griff has 2 accepted answers">10%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jan '12, 21:16</strong> </span></p></div></div><div id="comments-container-8303" class="comments-container"><span id="9261"></span><div id="comment-9261" class="comment"><div id="post-9261-score" class="comment-score"></div><div class="comment-text"><p>Fortunately, on most if not all UN*X platforms, there's no device driver to install - libpcap uses a mechanism built into the OS.</p><p>Windows is different - it requires a driver to connect NDIS to the WinPcap library. That driver is part of WinPcap.</p></div><div id="comment-9261-info" class="comment-info"><span class="comment-age">(27 Feb '12, 14:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-8303" class="comment-tools"></div><div class="clear"></div><div id="comment-8303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

