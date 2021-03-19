+++
type = "question"
title = "How to find unreplied TCAP requests"
description = '''Is it possible to run any script in Wireshark to extend filter capabilities? I have a pcap file with requests/responses. Each request/response pair has unique id. I need to find all requests which don&#x27;t have response pair. What would be the best way to find such responses in Wireshark? The protocol ...'''
date = "2017-04-13T08:10:00Z"
lastmod = "2017-04-13T11:56:00Z"
weight = 60804
keywords = [ "filter", "tcap" ]
aliases = [ "/questions/60804" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to find unreplied TCAP requests](/questions/60804/how-to-find-unreplied-tcap-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60804-score" class="post-score" title="current number of votes">0</div><span id="post-60804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to run any script in Wireshark to extend filter capabilities? I have a pcap file with requests/responses. Each request/response pair has unique id. I need to find all requests which don't have response pair. What would be the best way to find such responses in Wireshark?</p><p>The protocol is TCAP. I'm analyzing Source Transaction ID and Destination Transaction ID fields.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-tcap" rel="tag" title="see questions tagged &#39;tcap&#39;">tcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '17, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/cc8719f48704de1a1123e967573bdfee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Soteric&#39;s gravatar image" /><p><span>Soteric</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Soteric has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Apr '17, 11:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-60804" class="comments-container"><span id="60807"></span><div id="comment-60807" class="comment"><div id="post-60807-score" class="comment-score"></div><div class="comment-text"><p>You need to tell us what requests and responses you're working with. There are some cases where Wireshark correlates the request packet with the response packet. Wireshark puts a link to the response in the request packet, and a link to the request in the response packet. In those cases, it is possible to build a filter to show requests with no responses. DNS and HTTP are examples where this can be done.</p></div><div id="comment-60807-info" class="comment-info"><span class="comment-age">(13 Apr '17, 09:03)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="60808"></span><div id="comment-60808" class="comment"><div id="post-60808-score" class="comment-score"></div><div class="comment-text"><p>Thanks for pointing this. I added protocol details. It is TCAP. And transaction ID is the field I'm looking at.</p></div><div id="comment-60808-info" class="comment-info"><span class="comment-age">(13 Apr '17, 09:11)</span> <span class="comment-user userinfo">Soteric</span></div></div></div><div id="comment-tools-60804" class="comment-tools"></div><div class="clear"></div><div id="comment-60804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60813"></span>

<div id="answer-container-60813" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60813-score" class="post-score" title="current number of votes">0</div><span id="post-60813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on your needs you may be able to do this by:</p><ol><li>Enabling the TCAP dissector's <code>Service Response Time Analyze</code> preference</li><li>Enabling the TCAP dissector's <code>Persistence stats for SRT</code> preference</li><li>Filtering for, for example, <code>tcap.begin_element &amp;&amp; !tcap.srt.begin</code></li></ol><p>If that doesn't work for your needs then you may have to use <a href="https://wiki.wireshark.org/Mate">MATE</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '17, 11:56</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-60813" class="comments-container"></div><div id="comment-tools-60813" class="comment-tools"></div><div class="clear"></div><div id="comment-60813-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

