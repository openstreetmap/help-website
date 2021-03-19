+++
type = "question"
title = "Is it possible to filter out specific fields of specific packet types in a live capture?"
description = '''Hi, I am using tshark and I would like to store 802.11 header traffic in text format of a live capture. That means that I would like to &quot;cut&quot; the data portion of data frames so that it won&#x27;t be written to my text file but keep everything else (headers of all data, management and control frames).  I ...'''
date = "2013-08-31T05:46:00Z"
lastmod = "2013-08-31T14:26:00Z"
weight = 24224
keywords = [ "filter", "capture-filter", "pcap", "tshark", "dumpcap" ]
aliases = [ "/questions/24224" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to filter out specific fields of specific packet types in a live capture?](/questions/24224/is-it-possible-to-filter-out-specific-fields-of-specific-packet-types-in-a-live-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24224-score" class="post-score" title="current number of votes">0</div><span id="post-24224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using tshark and I would like to store 802.11 header traffic in text format of a live capture. That means that I would like to "cut" the data portion of data frames so that it won't be written to my text file but keep everything else (headers of all data, management and control frames).</p><p>I figure that since I am mostly interested on the headers this will dramatically reduce the size of my output files. As of now a 10MB pcap gets translated to a 100MB txt file.</p><p>Is it possible to do that with some capture filter option or shall I have to settle using a perl script to cut that portion of the output file in a second phase?</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '13, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/d4fa52d2dc8365c040d9ed0cf1bbe9ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whiteshark&#39;s gravatar image" /><p><span>whiteshark</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whiteshark has no accepted answers">0%</span></p></div></div><div id="comments-container-24224" class="comments-container"></div><div id="comment-tools-24224" class="comment-tools"></div><div class="clear"></div><div id="comment-24224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24241"></span>

<div id="answer-container-24241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24241-score" class="post-score" title="current number of votes">0</div><span id="post-24241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I figure that since I am mostly interested on the headers this will dramatically reduce the size of my output files.</p></blockquote><p>The best way is to limit the capture size during the capture phase.</p><blockquote><p>tcpdump -ni eth0 <strong>-s 100</strong> .....<br />
dumpcap -ni eth0 <strong>-s 100</strong> .....<br />
wireshark -ni eth0 <strong>-s 100</strong> ....</p></blockquote><p>If you want to truncate a capture file later, you can use editcap.</p><blockquote><p>editcap <strong>-s 100</strong> input.pcap output.pcap</p></blockquote><p>The actual capture size depends on your needs, so maybe you just open the current capture file and count the bytes you need.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '13, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-24241" class="comments-container"></div><div id="comment-tools-24241" class="comment-tools"></div><div class="clear"></div><div id="comment-24241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

