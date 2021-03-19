+++
type = "question"
title = "Obtaining 802.11 RSSI value on Windows"
description = '''The capture session could not be initiated (failed to set hardware filter to promiscuous mode). Please check that &quot;&#92;Device&#92;NPF_{5EDA4C43-AB8B-42A7-A83F-447F77167D48}&quot; is the proper interface. I tried to capture tthe RSSI value but above error appears... what should I do? please help...'''
date = "2013-06-27T00:25:00Z"
lastmod = "2013-06-27T13:33:00Z"
weight = 22394
keywords = [ "windows", "rssi", "wifi" ]
aliases = [ "/questions/22394" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Obtaining 802.11 RSSI value on Windows](/questions/22394/obtaining-80211-rssi-value-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22394-score" class="post-score" title="current number of votes">0</div><span id="post-22394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The capture session could not be initiated (failed to set hardware filter to promiscuous mode).</p><p>Please check that "\Device\NPF_{5EDA4C43-AB8B-42A7-A83F-447F77167D48}" is the proper interface.</p><p>I tried to capture tthe RSSI value but above error appears... what should I do? please help...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-rssi" rel="tag" title="see questions tagged &#39;rssi&#39;">rssi</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '13, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/93201f4bbe62fc2f6a7b8007703476ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zekar&#39;s gravatar image" /><p><span>zekar</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zekar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jun '13, 13:33</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22394" class="comments-container"><span id="22399"></span><div id="comment-22399" class="comment"><div id="post-22399-score" class="comment-score"></div><div class="comment-text"><p><span>@zekar</span></p><p>I've converted your "answer" to another question to a question of its own as that's how this site works. Please see the FAQ for more info.</p></div><div id="comment-22399-info" class="comment-info"><span class="comment-age">(27 Jun '13, 02:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="22403"></span><div id="comment-22403" class="comment"><div id="post-22403-score" class="comment-score"></div><div class="comment-text"><p>What type of interface is that?</p><p>Do you see that interface ("\Device\NPF_{5EDA4C43-AB8B-42A7-A83F-447F77167D48}") in the output of the following command:</p><blockquote><p><code>dumpcap -D -M</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div id="comment-22403-info" class="comment-info"><span class="comment-age">(27 Jun '13, 05:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22394" class="comment-tools"></div><div class="clear"></div><div id="comment-22394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22422"></span>

<div id="answer-container-22422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22422-score" class="post-score" title="current number of votes">0</div><span id="post-22422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Capturing on Wi-Fi interfaces on WIndows, with WinPcap-based applications such as Wireshark, doesn't work very well. In particular:</p><ol><li>sometimes attempting to capture in promiscuous mode fails in the fashion you indicate;</li><li>sometimes attempting to capture in promiscuous mode silently fails to provide any packets;</li><li>no matter what mode you capture in, you can't get any radio information such as the RSSI.</li></ol><p>Your alternatives are:</p><ol><li>use <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a> (which can be downloaded for free) - Wireshark can read Network Monitor capture files;</li><li>buy an <a href="http://www.riverbed.com/products-solutions/products/performance-management/wireshark-enhancement-products/Wireless-Traffic-Packet-Capture.html">AirPcap adapter</a>;</li><li>run Wireshark on Linux or *BSD or OS X instead of Windows.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '13, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jun '13, 13:34</strong> </span></p></div></div><div id="comments-container-22422" class="comments-container"></div><div id="comment-tools-22422" class="comment-tools"></div><div class="clear"></div><div id="comment-22422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

