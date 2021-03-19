+++
type = "question"
title = "removing duplicate packets from pcap"
description = '''I want to analyze packet capture file, but it has some duplicate packets.  For e.g., I am setting packet count to 10000 and seeing 11085 count in wireshark. So the goal is to remove duplicate packets which are 1085 in count. I am using latest wireshark version 1.10.2. I would like to know if there i...'''
date = "2013-10-15T06:43:00Z"
lastmod = "2013-10-15T07:17:00Z"
weight = 25998
keywords = [ "duplicate", "packets", "wireshark" ]
aliases = [ "/questions/25998" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [removing duplicate packets from pcap](/questions/25998/removing-duplicate-packets-from-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25998-score" class="post-score" title="current number of votes">0</div><span id="post-25998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to analyze packet capture file, but it has some duplicate packets.</p><p>For e.g., I am setting packet count to 10000 and seeing 11085 count in wireshark. So the goal is to remove duplicate packets which are 1085 in count. I am using latest wireshark version 1.10.2.</p><p>I would like to know if there is any way (command line option) using which I can discard duplicate packets and make new pcap with all unique packets.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '13, 06:43</strong></p><img src="https://secure.gravatar.com/avatar/963f2abedc2aff60ceae201a8f231d42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="npatel&#39;s gravatar image" /><p><span>npatel</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="npatel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Oct '13, 07:52</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-25998" class="comments-container"></div><div id="comment-tools-25998" class="comment-tools"></div><div class="clear"></div><div id="comment-25998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26000"></span>

<div id="answer-container-26000" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26000-score" class="post-score" title="current number of votes">2</div><span id="post-26000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jasper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use editcap to remove duplicate frames.</p><blockquote><p>editcap -d input.pcap output.pcap</p></blockquote><p>See the man page for editcap: <a href="http://www.wireshark.org/docs/man-pages/editcap.html">http://www.wireshark.org/docs/man-pages/editcap.html</a> Options: -d, -D or -w</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Oct '13, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26000" class="comments-container"><span id="26003"></span><div id="comment-26003" class="comment"><div id="post-26003-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt!</p></div><div id="comment-26003-info" class="comment-info"><span class="comment-age">(15 Oct '13, 07:17)</span> <span class="comment-user userinfo">npatel</span></div></div></div><div id="comment-tools-26000" class="comment-tools"></div><div class="clear"></div><div id="comment-26000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

