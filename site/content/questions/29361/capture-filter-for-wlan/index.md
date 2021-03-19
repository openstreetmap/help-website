+++
type = "question"
title = "Capture filter for WLAN"
description = '''I am doing analysis of WiFi traffic between my device and the AP. I let wireshark run overnight, but my disk fills up and wireshark crashes. I was hoping someone could tell me how to build a filter that filters the capture for any traffic to/from a particular MAC? Thanks Anon'''
date = "2014-01-31T18:45:00Z"
lastmod = "2014-02-09T11:51:00Z"
weight = 29361
keywords = [ "wifi" ]
aliases = [ "/questions/29361" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter for WLAN](/questions/29361/capture-filter-for-wlan)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29361-score" class="post-score" title="current number of votes">0</div><span id="post-29361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am doing analysis of WiFi traffic between my device and the AP. I let wireshark run overnight, but my disk fills up and wireshark crashes. I was hoping someone could tell me how to build a filter that filters the capture for any traffic to/from a particular MAC?</p><p>Thanks Anon</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jan '14, 18:45</strong></p><img src="https://secure.gravatar.com/avatar/14c9ec57d5da1734cf50ec7bd17d31ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YIleKu&#39;s gravatar image" /><p><span>YIleKu</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YIleKu has no accepted answers">0%</span></p></div></div><div id="comments-container-29361" class="comments-container"></div><div id="comment-tools-29361" class="comment-tools"></div><div class="clear"></div><div id="comment-29361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29364"></span>

<div id="answer-container-29364" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29364-score" class="post-score" title="current number of votes">0</div><span id="post-29364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use a capture filter to capture data frames to/from a mac address:<br />
Example:<br />
wlan host 04:1e:64:ea:c3:ef and type data<br />
<br />
You can find more examples in my article <a href="http://www.lovemytool.com/blog/2010/07/wireshark-wireless-display-and-capture-filters-samples-part-2-by-joke-snelders.html#more">Wireshark: Wireless Display and Capture Filters Samples part 2</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '14, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-29364" class="comments-container"><span id="29373"></span><div id="comment-29373" class="comment"><div id="post-29373-score" class="comment-score"></div><div class="comment-text"><p>thank you. I want to capture all frames management and data to and from my host. Actually my host has two mac addresses. M</p></div><div id="comment-29373-info" class="comment-info"><span class="comment-age">(01 Feb '14, 08:49)</span> <span class="comment-user userinfo">YIleKu</span></div></div><span id="29581"></span><div id="comment-29581" class="comment"><div id="post-29581-score" class="comment-score"></div><div class="comment-text"><p>It looks like this filter captures traffic that has a source address of the mac listed. Is there a way to capture any traffic to or from this host? thank</p></div><div id="comment-29581-info" class="comment-info"><span class="comment-age">(09 Feb '14, 11:51)</span> <span class="comment-user userinfo">YIleKu</span></div></div></div><div id="comment-tools-29364" class="comment-tools"></div><div class="clear"></div><div id="comment-29364-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

