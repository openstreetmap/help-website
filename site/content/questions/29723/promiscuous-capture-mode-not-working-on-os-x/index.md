+++
type = "question"
title = "Promiscuous capture mode not working on OS X"
description = '''I just downloaded and started using Wireshark 1.10.5 on OS X 10.8.5 (Macbook Pro Retina), but Promiscuous Mode capture doesn&#x27;t seem to be working; I only see packets to/from my laptop. I&#x27;ve been consulting the wiki. The Wi-Fi network I&#x27;m associated with is what I&#x27;m interested in capturing. It uses W...'''
date = "2014-02-11T18:27:00Z"
lastmod = "2014-02-12T16:55:00Z"
weight = 29723
keywords = [ "osx", "promiscuous", "monitor" ]
aliases = [ "/questions/29723" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Promiscuous capture mode not working on OS X](/questions/29723/promiscuous-capture-mode-not-working-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29723-score" class="post-score" title="current number of votes">0</div><span id="post-29723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just downloaded and started using Wireshark 1.10.5 on OS X 10.8.5 (Macbook Pro Retina), but Promiscuous Mode capture doesn't seem to be working; I only see packets to/from my laptop.</p><p>I've been consulting <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Mac_OS_X">the wiki</a>. The Wi-Fi network I'm associated with is what I'm interested in capturing. It uses WPA2 but <a href="http://ask.wireshark.org/questions/19413/wireshark-only-sniffs-my-devices-mac-os-x-traffic-on-my-wifi-network-monitor-mode-not-helping">this question</a> suggests I should still be able to see the physical packets listed, just as encrypted. (This is fine as I'm mainly interested in monitoring network bandwidth usage by MAC address.)</p><p>I'm probably missing something basic. Thanks in advance for any help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-promiscuous" rel="tag" title="see questions tagged &#39;promiscuous&#39;">promiscuous</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 18:27</strong></p><img src="https://secure.gravatar.com/avatar/ea84d0dfebeb61249ff37e31a689b4ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yang&#39;s gravatar image" /><p><span>yang</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yang has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '14, 18:28</strong> </span></p></div></div><div id="comments-container-29723" class="comments-container"></div><div id="comment-tools-29723" class="comment-tools"></div><div class="clear"></div><div id="comment-29723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29806"></span>

<div id="answer-container-29806" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29806-score" class="post-score" title="current number of votes">0</div><span id="post-29806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Promiscuous mode often doesn't work on 802.11 devices. <em>Monitor</em> mode - which is what the question to which you referred was talking about - is more likely to work there. Promiscuous mode and monitor mode are not the same thing (at least not from the point of view of the OS APIs for turning them on and off).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 16:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29806" class="comments-container"></div><div id="comment-tools-29806" class="comment-tools"></div><div class="clear"></div><div id="comment-29806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

