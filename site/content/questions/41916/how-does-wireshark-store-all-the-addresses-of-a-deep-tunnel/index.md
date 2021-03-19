+++
type = "question"
title = "How does Wireshark store all the addresses of a deep tunnel?"
description = '''Good day everyone. Currently I&#x27;m interested in tunneling. For example I have a tunnel with the following protocols stack: And my question is how does wireshrk store all the addresses for each packet (in my example there are three IPv4-addresses)? I thought of packet_info structure, but there are onl...'''
date = "2015-04-28T06:46:00Z"
lastmod = "2015-04-29T13:12:00Z"
weight = 41916
keywords = [ "tunnel", "addresses", "packet" ]
aliases = [ "/questions/41916" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How does Wireshark store all the addresses of a deep tunnel?](/questions/41916/how-does-wireshark-store-all-the-addresses-of-a-deep-tunnel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41916-score" class="post-score" title="current number of votes">0</div><span id="post-41916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good day everyone.</p><p>Currently I'm interested in tunneling. For example I have a tunnel with the following protocols stack:<img src="https://osqa-ask.wireshark.org/upfiles/1_ZUjXHAC.png" alt="alt text" /></p><p>And my question is how does wireshrk store all the addresses for each packet (in my example there are three IPv4-addresses)? I thought of packet_info structure, but there are only two fields:</p><pre><code>address net_src;                  /**&lt; network-layer source address */
address src;                      /**&lt; source address (net if present, DL otherwise )*/</code></pre><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tunnel" rel="tag" title="see questions tagged &#39;tunnel&#39;">tunnel</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '15, 06:46</strong></p><img src="https://secure.gravatar.com/avatar/c701a53dad43a1abbb8fc95d7b555e7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ustas&#39;s gravatar image" /><p><span>ustas</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ustas has no accepted answers">0%</span></p></img></div></div><div id="comments-container-41916" class="comments-container"></div><div id="comment-tools-41916" class="comment-tools"></div><div class="clear"></div><div id="comment-41916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41954"></span>

<div id="answer-container-41954" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41954-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41954-score" class="post-score" title="current number of votes">2</div><span id="post-41954-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ustas has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark will keep the outermost IP addresses in the packet_info struct, as there are the real addresses for the particular packet at the network layer. These addresses are used in the source and destination column.</p><p>However, for each IP address encountered in an IP header, it will add a ip.src or ip.dst field to the dissection tree (as well as an ip.addr for both of them). So when using the display filter <code>ip.src==10.0.0.1</code>, it will be interpreted as <em>"Display all packets for which there is at least one field with the name ip.src that has the value 10.0.0.1"</em>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '15, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-41954" class="comments-container"></div><div id="comment-tools-41954" class="comment-tools"></div><div class="clear"></div><div id="comment-41954-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

