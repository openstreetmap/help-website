+++
type = "question"
title = "How do I search a capture for a string?"
description = '''First, apologies for the newbie question, I&#x27;ve purchased the excellent Wireshark Book, but need to figure this out faster than I can read through the large book. I&#x27;m trying to determine where a hostname is being incorrectly provided, on a multi-protocol network. Looking up the hostname returns an IP...'''
date = "2011-06-23T14:39:00Z"
lastmod = "2011-06-23T18:52:00Z"
weight = 4710
keywords = [ "filter", "search" ]
aliases = [ "/questions/4710" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I search a capture for a string?](/questions/4710/how-do-i-search-a-capture-for-a-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4710-score" class="post-score" title="current number of votes">2</div><span id="post-4710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>First, apologies for the newbie question, I've purchased the excellent Wireshark Book, but need to figure this out faster than I can read through the large book.</p><p>I'm trying to determine where a hostname is being incorrectly provided, on a multi-protocol network. Looking up the hostname returns an IP other than what appears this name is associated with locally. Nslookup does not have PTR (Reverse) records defined, so "nslookup ip.add.re.ss" just gives the error about not knowing the in-addr.arpa domain. nmblookup also does not return the expected name and IP pair, but the hostname in question is found in a capture file I've saved. How do I find what record this name is in, when I don't know what protocol or how it appears?</p><p>Oh, and I've tried 'grep -n "string" file.cap', but obviously, with a binary capture file, you don't get much readable content; same with 'vim file.cap'.</p><p>Thank you, Dragongeek</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '11, 14:39</strong></p><img src="https://secure.gravatar.com/avatar/79a8449f484e149b072c523b65b7aa3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dragongeek&#39;s gravatar image" /><p><span>dragongeek</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dragongeek has no accepted answers">0%</span></p></div></div><div id="comments-container-4710" class="comments-container"></div><div id="comment-tools-4710" class="comment-tools"></div><div class="clear"></div><div id="comment-4710-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4711"></span>

<div id="answer-container-4711" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4711-score" class="post-score" title="current number of votes">2</div><span id="post-4711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To find a string within a packet, click on Edit &gt; Find Packet. Under "Find By:" select "string" and enter your search string in the text entry box. You'll probably want to leave "Case sensitive" unchecked. Under "Search in", the default is "Packet list" but that will only find a string that appears in the Info column of the Packet List pane, which is the one-line-per-packet summary view. There is a lot more information in most packets than what appears in the packet list Info column, so try "Packet details" and "Packet bytes".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '11, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-4711" class="comments-container"><span id="4712"></span><div id="comment-4712" class="comment"><div id="post-4712-score" class="comment-score"></div><div class="comment-text"><p>Fantastic, thank you!</p></div><div id="comment-4712-info" class="comment-info"><span class="comment-age">(23 Jun '11, 18:52)</span> <span class="comment-user userinfo">dragongeek</span></div></div></div><div id="comment-tools-4711" class="comment-tools"></div><div class="clear"></div><div id="comment-4711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

