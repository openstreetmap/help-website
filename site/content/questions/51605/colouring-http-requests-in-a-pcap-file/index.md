+++
type = "question"
title = "colouring HTTP requests in a pcap file"
description = '''I&#x27;d like to color all the http requests in my pcap file in purple. I&#x27;ve added a colour rule as the attached window shows. However, none of the packets that contain the requests becomes purple. They have a different color that I previously chose to apply based on the TCP converstaion. Any clue why th...'''
date = "2016-04-12T07:55:00Z"
lastmod = "2016-04-12T08:49:00Z"
weight = 51605
keywords = [ "color-rules", "http.request", "display-filter", "wireshark" ]
aliases = [ "/questions/51605" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [colouring HTTP requests in a pcap file](/questions/51605/colouring-http-requests-in-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51605-score" class="post-score" title="current number of votes">0</div><span id="post-51605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to color all the http requests in my pcap file in purple. I've added a colour rule as the attached window shows. However, none of the packets that contain the requests becomes purple. They have a different color that I previously chose to apply based on the TCP converstaion.</p><p>Any clue why the purple rule color has not been applied?</p><p>Thank you.<img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2016-04-12_at_10.35.27_AM_(2).png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-color-rules" rel="tag" title="see questions tagged &#39;color-rules&#39;">color-rules</span> <span class="post-tag tag-link-http.request" rel="tag" title="see questions tagged &#39;http.request&#39;">http.request</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '16, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></img></div></div><div id="comments-container-51605" class="comments-container"></div><div id="comment-tools-51605" class="comment-tools"></div><div class="clear"></div><div id="comment-51605-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51607"></span>

<div id="answer-container-51607" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51607-score" class="post-score" title="current number of votes">1</div><span id="post-51607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are two possibilities why your new coloring rule is not triggering:</p><ol><li>You applied temporary coloring based on a conversation, and your temporary coloring is is still in place. Temporary coloring overrides coloring rules. You can clear temporary coloring with Ctrl-Space.</li><li>Your coloring rules are for HTTP requests. Beginning with Wireshark v1.12.0 and continuing to the current version (2.0.2), Wireshark does not always identify HTTP packets correctly. This is a known bug. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10335">Bug 10335</a> on the Wireshark Bugzilla.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '16, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51607" class="comments-container"><span id="51608"></span><div id="comment-51608" class="comment"><div id="post-51608-score" class="comment-score"></div><div class="comment-text"><p>Awesome! My current problem is 1 and your suggestion Ctrl-Space has worked perfectly for me. Thank you so much.</p></div><div id="comment-51608-info" class="comment-info"><span class="comment-age">(12 Apr '16, 08:49)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-51607" class="comment-tools"></div><div class="clear"></div><div id="comment-51607-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

