+++
type = "question"
title = "How can I sort my 822MB pcap file by IP source address, keeping all other fields."
description = '''How can I sort my 822MB pcap file by IP source address? I need to be able to see the display in groups of same IP source addresses, but without cutting the other fields displayed. I need to see which IP addresses have sent more than 100 packets, and, then determine if within those 100+ packet cluste...'''
date = "2016-11-19T14:56:00Z"
lastmod = "2016-11-19T16:35:00Z"
weight = 57464
keywords = [ "sort", "ip", "address", "by", "source" ]
aliases = [ "/questions/57464" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can I sort my 822MB pcap file by IP source address, keeping all other fields.](/questions/57464/how-can-i-sort-my-822mb-pcap-file-by-ip-source-address-keeping-all-other-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57464-score" class="post-score" title="current number of votes">0</div><span id="post-57464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I sort my 822MB pcap file by IP source address? I need to be able to see the display in groups of same IP source addresses, but without cutting the other fields displayed. I need to see which IP addresses have sent more than 100 packets, and, then determine if within those 100+ packet clusters the packets are at most 5 mins apart. This is to infer DDoS attack form backscattered traffic. Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sort" rel="tag" title="see questions tagged &#39;sort&#39;">sort</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-by" rel="tag" title="see questions tagged &#39;by&#39;">by</span> <span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '16, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/b3f6579bb81c4e2875f9293da09b05c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MaryR&#39;s gravatar image" /><p><span>MaryR</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MaryR has no accepted answers">0%</span></p></div></div><div id="comments-container-57464" class="comments-container"></div><div id="comment-tools-57464" class="comment-tools"></div><div class="clear"></div><div id="comment-57464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57466"></span>

<div id="answer-container-57466" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57466-score" class="post-score" title="current number of votes">0</div><span id="post-57466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MaryR has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To sort the display by source IP address, click once on the Source address column header to sort from low to high; click twice to sort from high to low.</p><p>To see how many packets were sent by different addresses, go to Statistics &gt; Endpoints and then click on the IPv4 tab. Click twice on the Packets column header to sort from high-to-low. All the hosts that sent 100 or more packets will be at the top of the list, in decreasing order.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '16, 15:15</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-57466" class="comments-container"><span id="57470"></span><div id="comment-57470" class="comment"><div id="post-57470-score" class="comment-score"></div><div class="comment-text"><p>I hope he can load the file. Maybe <a href="http://www.ntop.org/products/traffic-analysis/ntop/">ntopng</a> is a better approach?</p></div><div id="comment-57470-info" class="comment-info"><span class="comment-age">(19 Nov '16, 16:23)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="57471"></span><div id="comment-57471" class="comment"><div id="post-57471-score" class="comment-score"></div><div class="comment-text"><p>It is sorting now, and I am sure it will work, but how can I do this from command line, with tshark and other linux commands for two reasons: 1) because of the file size, wireshark is taking a,long time to do it, if it does it in the end, a 2) because I need to automate the process of inferring the DDoS attack from the original dataset. My original file was 8GB, I used some tcpdump filter and reduced to 822 MB, now I need to filter by number of packets and time. In the end I need to write bash script to automate the whole process. What commands could I use for sorting as Wireshark does? Is command line better approach? Help greatly appreciated.</p></div><div id="comment-57471-info" class="comment-info"><span class="comment-age">(19 Nov '16, 16:35)</span> <span class="comment-user userinfo">MaryR</span></div></div></div><div id="comment-tools-57466" class="comment-tools"></div><div class="clear"></div><div id="comment-57466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

