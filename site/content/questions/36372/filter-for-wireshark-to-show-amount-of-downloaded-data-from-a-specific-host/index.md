+++
type = "question"
title = "Filter for Wireshark to show amount of downloaded data from a specific host"
description = '''Need to check amount of downloaded data from some address when there are connection issues. Such issues are emulated with clumsy. All packets that are received from specific host are filtered by WireShark using following filter: http.host == &quot;mybucket.s3.amazonaws.com&quot;. Then I can view length of rec...'''
date = "2014-09-16T11:29:00Z"
lastmod = "2014-10-22T05:06:00Z"
weight = 36372
keywords = [ "data", "wireshark" ]
aliases = [ "/questions/36372" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter for Wireshark to show amount of downloaded data from a specific host](/questions/36372/filter-for-wireshark-to-show-amount-of-downloaded-data-from-a-specific-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36372-score" class="post-score" title="current number of votes">0</div><span id="post-36372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Need to check amount of downloaded data from some address when there are connection issues. Such issues are emulated with <a href="http://jagt.github.io/clumsy/">clumsy</a>. All packets that are received from specific host are filtered by WireShark using following filter: http.host == "mybucket.s3.amazonaws.com". Then I can view length of received packets in Summary (Statistic-&gt;Summary), but it shows only 'green' packets. So, is it not correct amount of downloaded data. How I can view amount of of downloaded data for a specific host?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '14, 11:29</strong></p><img src="https://secure.gravatar.com/avatar/013786becd46e2d2aac7039f4797b948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izdryk&#39;s gravatar image" /><p><span>izdryk</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izdryk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '14, 02:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-36372" class="comments-container"></div><div id="comment-tools-36372" class="comment-tools"></div><div class="clear"></div><div id="comment-36372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37272"></span>

<div id="answer-container-37272" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37272-score" class="post-score" title="current number of votes">0</div><span id="post-37272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but it <strong>shows only 'green' packets</strong>. So, is it not correct amount of downloaded data. How I can view amount of of downloaded data for a specific host?</p></blockquote><p>I'm not sure what you mean by 'green' packets, but your filter will only show frames that contain a HTTP Host: header with the mentioned content. That's of course not all frames of the TCP session! It will show just the HTTP <strong>request</strong> frames which contain that Host: header.</p><p>You could try filter on</p><blockquote><p>ip.src eq mybucket.s3.amazonaws.com</p></blockquote><p>HINT: Wireshark will resolve mybucket.s3.amazonaws.com to an IP address before it builds the filter. As Amazon might return several IP addresses for that name, even different ones for several DNS requests (DNS balancing), the filter might look for the wrong IP address. So, the best way would be to identify the session you are looking for with your first filter</p><blockquote><p>http.host == "mybucket.s3.amazonaws.com"</p></blockquote><p>Then try to figure out <strong>all</strong> server IP addresses matching that name (the destination IP addresses where the HTTP requests were sent to). Then take those IP addresses and build one or more filters to view all frames <strong>coming from those servers</strong>, aka. the downloaded data.</p><blockquote><p>ip.src eq 176.32.100.72 or ip.src eq 176.32.100.75 or ip.src eq 176.32.100.80</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Oct '14, 05:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37272" class="comments-container"></div><div id="comment-tools-37272" class="comment-tools"></div><div class="clear"></div><div id="comment-37272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

