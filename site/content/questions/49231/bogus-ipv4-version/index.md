+++
type = "question"
title = "Bogus IPv4 version"
description = '''Hello all. Seems from time to time, people ask about this. I am trying to export traffic from a Cisco router and interestingly, while packets going out the router interface are correctly interpreted by Wireshark, all incoming packets fail as bogus ipv4 version. From what I found, the &quot;Support packet...'''
date = "2016-01-14T16:45:00Z"
lastmod = "2016-01-14T20:08:00Z"
weight = 49231
keywords = [ "bogus", "ipv4" ]
aliases = [ "/questions/49231" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bogus IPv4 version](/questions/49231/bogus-ipv4-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49231-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49231-score" class="post-score" title="current number of votes">0</div><span id="post-49231-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all. Seems from time to time, people ask about this. I am trying to export traffic from a Cisco router and interestingly, while packets going out the router interface are correctly interpreted by Wireshark, all incoming packets fail as bogus ipv4 version.</p><p>From what I found, the "Support packet capture from TSO-enabled hardware" should have been fixing this years ago, however it is not doing me any good.</p><p>Now, if I capture the traffic on the router, and export the capture file to be open by Wireshark, it decodes on both directions - exactly as it should.</p><p>The details, if they do any good: The router interface I'm trying to capture is a Dialer interface, receiving PPPoE data. The just updated Wireshark 2.0.1 (and previous v2.0.0) x64 runs on a Windows 10 x64. NIC is a Qualcomm Atheros AR-8161 (not a KillerNIC).</p><p>E: As a side note, IPv6 packets captured live from the same interface are decoded just right.</p><p>Thanks and regards,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bogus" rel="tag" title="see questions tagged &#39;bogus&#39;">bogus</span> <span class="post-tag tag-link-ipv4" rel="tag" title="see questions tagged &#39;ipv4&#39;">ipv4</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '16, 16:45</strong></p><img src="https://secure.gravatar.com/avatar/b168a4f0b3f6f596f789c0fdae17a1ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HQuest&#39;s gravatar image" /><p><span>HQuest</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HQuest has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jan '16, 17:31</strong> </span></p></div></div><div id="comments-container-49231" class="comments-container"></div><div id="comment-tools-49231" class="comment-tools"></div><div class="clear"></div><div id="comment-49231-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49234"></span>

<div id="answer-container-49234" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49234-score" class="post-score" title="current number of votes">0</div><span id="post-49234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>We'd have to see the capture to figure out what the problem is. Please file a bug on <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a> and attach a capture that shows this problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '16, 18:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49234" class="comments-container"><span id="49240"></span><div id="comment-49240" class="comment"><div id="post-49240-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12012">Bug 12012</a> submitted. Thanks for the guidance.</p></div><div id="comment-49240-info" class="comment-info"><span class="comment-age">(14 Jan '16, 20:08)</span> <span class="comment-user userinfo">HQuest</span></div></div></div><div id="comment-tools-49234" class="comment-tools"></div><div class="clear"></div><div id="comment-49234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

