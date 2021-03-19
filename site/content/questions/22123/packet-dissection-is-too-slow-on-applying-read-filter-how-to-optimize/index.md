+++
type = "question"
title = "packet dissection is too slow, on applying read filter, how to optimize"
description = '''so basically i have written a tool,and what it does is 1- capture the packets,write this into a file, initialize epan module 2- open the file using pcap_open_offline(...), then call pcap_loop(...)and in handler function for this apply read filter(for any identity present in request message) on it, c...'''
date = "2013-06-17T13:27:00Z"
lastmod = "2013-06-17T13:27:00Z"
weight = 22123
keywords = [ "development", "dissection", "optimize", "libpcap", "wireshark" ]
aliases = [ "/questions/22123" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet dissection is too slow, on applying read filter, how to optimize](/questions/22123/packet-dissection-is-too-slow-on-applying-read-filter-how-to-optimize)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22123-score" class="post-score" title="current number of votes">0</div><span id="post-22123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>so basically i have written a tool,and what it does is</p><p>1- capture the packets,write this into a file, initialize epan module</p><p>2- open the file using pcap_open_offline(...), then call pcap_loop(...)and in handler function for this apply read filter(for any identity present in request message) on it, call dissection utilities.</p><p>3- go to print the packet data, extract message_id.</p><p>4- now open the file again using pcap_open_offline() then call pcap_loop() and in handler function, apply this message_id as read filter to print both request and response(req and res have same message_id),call dissection utilities.</p><p>5- go to print the output.</p><p>now i have this network, messages coming at approx rate of 5k per sec., and this application is taking too much time to print for any identity corresponding to read_filter.how to optimize it, as i have seen,wireshark doing same stuff, capturing then applying read_filter to print the desired output.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span> <span class="post-tag tag-link-optimize" rel="tag" title="see questions tagged &#39;optimize&#39;">optimize</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '13, 13:27</strong></p><img src="https://secure.gravatar.com/avatar/425d250364423a7595a3eb9dea779cb2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanny_D&#39;s gravatar image" /><p><span>Sanny_D</span><br />
<span class="score" title="0 reputation points">0</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanny_D has 3 accepted answers">50%</span></p></div></div><div id="comments-container-22123" class="comments-container"></div><div id="comment-tools-22123" class="comment-tools"></div><div class="clear"></div><div id="comment-22123-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

