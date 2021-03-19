+++
type = "question"
title = "“irc.request ” filter for libpcap"
description = '''i have to filter out the &quot;IRC request&quot; packet form the list of capture packet in wireshark the filter expression is &quot;irc.request&quot;,but i am not able to write the same filter expression for lipcap so please provide me the filter expression for libpcap Thank you'''
date = "2014-04-16T09:18:00Z"
lastmod = "2014-04-19T16:19:00Z"
weight = 31895
keywords = [ "irc", "tcp", "wireshark" ]
aliases = [ "/questions/31895" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [“irc.request ” filter for libpcap](/questions/31895/ircrequest-filter-for-libpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31895-score" class="post-score" title="current number of votes">0</div><span id="post-31895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have to filter out the "IRC request" packet form the list of capture packet</p><p>in wireshark the filter expression is "irc.request",but i am not able to write the same filter expression for lipcap</p><p>so please provide me the filter expression for libpcap</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-irc" rel="tag" title="see questions tagged &#39;irc&#39;">irc</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '14, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/24de282117020d8da9b53ff5c7b45dd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deepak19911&#39;s gravatar image" /><p><span>deepak19911</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deepak19911 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Apr '14, 21:03</strong> </span></p></div></div><div id="comments-container-31895" class="comments-container"></div><div id="comment-tools-31895" class="comment-tools"></div><div class="clear"></div><div id="comment-31895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32003"></span>

<div id="answer-container-32003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32003-score" class="post-score" title="current number of votes">0</div><span id="post-32003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Based on the IRC dissector code (packet-irc.c), a <strong>request</strong> is determined only by the <strong>direction of communication</strong>, meaning everything that is <strong>sent to the IRC server</strong> is a REQUEST and everything that is <strong>received from the IRC server</strong> is a RESPONSE.</p><p>So, a valid capture filter, that mimics the same behavior like <strong>irc.request</strong> would be</p><blockquote><p>tcpdump -ni eth0 <strong>'dst port 6667'</strong></p></blockquote><p>assuming port 6667 is the standard IRC port.</p><p>You could also use the IP address of an IRC server</p><blockquote><p>tcpdump -ni eth0 <strong>'dst host x.x.x.x'</strong> (please replace x.x.x.x with an IP address)</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '14, 16:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Apr '14, 16:27</strong> </span></p></div></div><div id="comments-container-32003" class="comments-container"></div><div id="comment-tools-32003" class="comment-tools"></div><div class="clear"></div><div id="comment-32003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

