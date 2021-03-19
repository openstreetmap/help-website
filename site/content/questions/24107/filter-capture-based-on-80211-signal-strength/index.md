+++
type = "question"
title = "Filter capture based on 802.11 signal strength"
description = '''I am trying to setup a capture filter that allows me to filter wireless traffic based on signal strength. This would be beneficial to do as it would allow me to cut out allot of the noise from AP&#x27;s outside of my area. I have been able to accomplish this as a display filter but would really like to l...'''
date = "2013-08-27T10:12:00Z"
lastmod = "2013-08-28T06:22:00Z"
weight = 24107
keywords = [ "wireless", "capture-filter-wlan", "capture-filter" ]
aliases = [ "/questions/24107" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter capture based on 802.11 signal strength](/questions/24107/filter-capture-based-on-80211-signal-strength)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24107-score" class="post-score" title="current number of votes">0</div><span id="post-24107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to setup a capture filter that allows me to filter wireless traffic based on signal strength. This would be beneficial to do as it would allow me to cut out allot of the noise from AP's outside of my area. I have been able to accomplish this as a display filter but would really like to limit the capture size. Is this possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-capture-filter-wlan" rel="tag" title="see questions tagged &#39;capture-filter-wlan&#39;">capture-filter-wlan</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '13, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/49fff37b25299569692d4c23d68e999a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chakachim&#39;s gravatar image" /><p><span>chakachim</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chakachim has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Aug '13, 10:13</strong> </span></p></div></div><div id="comments-container-24107" class="comments-container"></div><div id="comment-tools-24107" class="comment-tools"></div><div class="clear"></div><div id="comment-24107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24129"></span>

<div id="answer-container-24129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24129-score" class="post-score" title="current number of votes">1</div><span id="post-24129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I know there is no way to filter on the signal strength as that would require support for it in libpcap and there is no such thing (yet).</p><p>So, the short answer to your question:</p><blockquote><p>Is this possible?</p></blockquote><p>No.</p><p><strong>HOWEVER</strong>, as you only want to isolate the traffic of a certain AP, you can use it's MAC address and build a capture filter for that address.</p><blockquote><p>Capture filter: wlan host xx:xx:xx:xx:xx:xx</p></blockquote><p>This requires a version of libpcap that supports the <strong>wlan</strong> filter (see <strong>man pcap-filter</strong> on your Linux distro) and a wireless driver that returns the real 802.11 frames and not 'fake ethernet' frames.</p><p>See also here: <a href="http://wiki.wireshark.org/Wi-Fi">http://wiki.wireshark.org/Wi-Fi</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '13, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24129" class="comments-container"></div><div id="comment-tools-24129" class="comment-tools"></div><div class="clear"></div><div id="comment-24129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

