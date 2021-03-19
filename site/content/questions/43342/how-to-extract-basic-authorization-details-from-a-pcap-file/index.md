+++
type = "question"
title = "How to extract basic authorization details from a pcap file ?"
description = '''I am currently doing pen-testing on a local proxy server that I have setup using Squid. I initiated a MITM attack to get packets from the compromised hosts. I have over hundred thousand packets in my pcap file from which I need to extract the basic proxy authorization fields of username and pass. Wi...'''
date = "2015-06-18T13:44:00Z"
lastmod = "2015-06-19T04:24:00Z"
weight = 43342
keywords = [ "filter", "tshark" ]
aliases = [ "/questions/43342" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to extract basic authorization details from a pcap file ?](/questions/43342/how-to-extract-basic-authorization-details-from-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43342-score" class="post-score" title="current number of votes">1</div><span id="post-43342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently doing pen-testing on a local proxy server that I have setup using Squid. I initiated a MITM attack to get packets from the compromised hosts. I have over hundred thousand packets in my pcap file from which I need to extract the basic proxy authorization fields of username and pass. Within the pcap file I can apply "http.authbasic" as a filter to get all the packets sent with username and pass, but how do I extract this info automatically for all the packets ,and prerably output the result to a text file ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '15, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/4541634d61685ddb3a8aa77299713c7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Backspace&#39;s gravatar image" /><p><span>Backspace</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Backspace has no accepted answers">0%</span></p></div></div><div id="comments-container-43342" class="comments-container"></div><div id="comment-tools-43342" class="comment-tools"></div><div class="clear"></div><div id="comment-43342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43343"></span>

<div id="answer-container-43343" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43343-score" class="post-score" title="current number of votes">2</div><span id="post-43343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Backspace has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark.</p><blockquote><p>tshark -nr http.pcap -T fields -e frame.number -e ip.src -e ip.dst -e http.authbasic -Y "http.proxy_authorization"</p></blockquote><p><strong>Sample output:</strong></p><pre><code>21      172.16.101.2    172.16.101.1    user1:password1
28      172.16.101.2    172.16.101.1    user2:secret2</code></pre><p>Please read the <a href="https://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> and the <a href="https://www.wireshark.org/docs/dfref/">display filter reference guide</a> for more options and fields.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '15, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43343" class="comments-container"><span id="43345"></span><div id="comment-43345" class="comment"><div id="post-43345-score" class="comment-score"></div><div class="comment-text"><p>Is there a way to do this on a live packet capture stream ? the above command works perfectly for pcap files. We can also print distinct combinations using |sort |uniq</p></div><div id="comment-43345-info" class="comment-info"><span class="comment-age">(18 Jun '15, 14:25)</span> <span class="comment-user userinfo">Backspace</span></div></div><span id="43359"></span><div id="comment-43359" class="comment"><div id="post-43359-score" class="comment-score"></div><div class="comment-text"><p>please try this:</p><p><strong>-ni eth0</strong> instead of <strong>-nr http.cap</strong>. On Windows it's <strong>-ni &lt;id&gt;</strong> while &lt;id&gt; is the interfaces ID you'll see with <strong>dumpcap -D -M</strong></p></div><div id="comment-43359-info" class="comment-info"><span class="comment-age">(19 Jun '15, 04:24)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-43343" class="comment-tools"></div><div class="clear"></div><div id="comment-43343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

