+++
type = "question"
title = "Wireshark shows only PPI protocols"
description = '''When I connect to WiFi network and try to capture packets, I only see PPI protocols in Wireshark and nothing else. How do I get Wireshark to show me more than just PPI?'''
date = "2011-11-23T13:46:00Z"
lastmod = "2011-11-24T01:24:00Z"
weight = 7589
keywords = [ "capture", "wifi", "troubleshooting" ]
aliases = [ "/questions/7589" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark shows only PPI protocols](/questions/7589/wireshark-shows-only-ppi-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7589-score" class="post-score" title="current number of votes">0</div><span id="post-7589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I connect to WiFi network and try to capture packets, I only see PPI protocols in Wireshark and nothing else. How do I get Wireshark to show me more than just PPI?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '11, 13:46</strong></p><img src="https://secure.gravatar.com/avatar/99e18917c63ace8db7e883d456de0ecd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rajvirg&#39;s gravatar image" /><p><span>rajvirg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rajvirg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Nov '11, 14:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-7589" class="comments-container"><span id="7604"></span><div id="comment-7604" class="comment"><div id="post-7604-score" class="comment-score"></div><div class="comment-text"><p>By "I only see PPI protocols in Wireshark and nothing else" do you mean that Wireshark shows a dissection of the PPI pseudo-header but doesn't show anything running atop PPI, such as 802.11? If so, could you show a detailed dissection of one of the packets? There are some cases for 802.11n where the PPI dissector won't pass on the payload to the 802.11 dissector; this might be one of them.</p></div><div id="comment-7604-info" class="comment-info"><span class="comment-age">(24 Nov '11, 01:24)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-7589" class="comment-tools"></div><div class="clear"></div><div id="comment-7589-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7599"></span>

<div id="answer-container-7599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7599-score" class="post-score" title="current number of votes">0</div><span id="post-7599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go for <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a> and please use the search function on this Q&amp;A site e.g. with the string "wireless" and check if you already set everything up right.</p><p>If you don't manage to get it running then please give more input and details about your capture setup by editing your question here.</p><p>thankx</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Nov '11, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Nov '11, 00:26</strong> </span></p></div></div><div id="comments-container-7599" class="comments-container"></div><div id="comment-tools-7599" class="comment-tools"></div><div class="clear"></div><div id="comment-7599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

