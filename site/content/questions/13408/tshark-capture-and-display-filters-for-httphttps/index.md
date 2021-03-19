+++
type = "question"
title = "TShark: Capture and Display Filters for HTTP/HTTPS"
description = '''I am running CentOS v5.8 64bit. What are the correct capture and display filters to use in TShark to monitor and trace HTTP/HTTPS traffic similar to what is provided by HTTPWatch? Also, what is the safest value to use for snaplen if I only want the following information below:  Number Time Absolute ...'''
date = "2012-08-06T17:27:00Z"
lastmod = "2012-08-26T19:45:00Z"
weight = 13408
keywords = [ "capture-filter", "http", "tshark", "https", "display-filter" ]
aliases = [ "/questions/13408" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TShark: Capture and Display Filters for HTTP/HTTPS](/questions/13408/tshark-capture-and-display-filters-for-httphttps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13408-score" class="post-score" title="current number of votes">0</div><span id="post-13408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running CentOS v5.8 64bit. What are the correct capture and display filters to use in TShark to monitor and trace HTTP/HTTPS traffic similar to what is provided by <a href="http://www.httpwatch.com/" title="HTTPWatch">HTTPWatch</a>?</p><p>Also, what is the safest value to use for snaplen if I only want the following information below:</p><ul><li>Number</li><li>Time</li><li>Absolute Date and Time</li><li>Source IP Address</li><li>Source FQDN</li><li>Source Port</li><li>Destination IP Address</li><li>Destination FQDN</li><li>Destination Port</li><li>Protocol</li><li>URL</li></ul><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Aug '12, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/929188474427b5c0cd8e3de0670882f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bintut&#39;s gravatar image" /><p><span>bintut</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bintut has no accepted answers">0%</span></p></div></div><div id="comments-container-13408" class="comments-container"></div><div id="comment-tools-13408" class="comment-tools"></div><div class="clear"></div><div id="comment-13408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13565"></span>

<div id="answer-container-13565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13565-score" class="post-score" title="current number of votes">0</div><span id="post-13565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The safest snaplength to use would be 0 (to capture whole frames), as the URL might be very long and not fit within one packet. So you might need TCP reassembly and that only works when whole frames are captured.</p><p>The for the correct display and capture filters, HTTP watch is a different tool and it works differently. If all your HTTP traffic is on port 80, you can use the capture filter "tcp port 80". But of course it will give you the whole TCP session, including acks etc. If you just want to see the http-requests and responses, you can use the display filter "http.request or http.response" after capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '12, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-13565" class="comments-container"><span id="13899"></span><div id="comment-13899" class="comment"><div id="post-13899-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer. I just created a new question which is not specific to HTTP or HTTPS and you can find it at <a href="http://ask.wireshark.org/questions/13898/tshark-display-filter-and-statistics" title="http://ask.wireshark.org/questions/13898/tshark-display-filter-and-statistics">http://ask.wireshark.org/questions/13898/tshark-display-filter-and-statistics</a>.</p></div><div id="comment-13899-info" class="comment-info"><span class="comment-age">(26 Aug '12, 19:45)</span> <span class="comment-user userinfo">bintut</span></div></div></div><div id="comment-tools-13565" class="comment-tools"></div><div class="clear"></div><div id="comment-13565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

