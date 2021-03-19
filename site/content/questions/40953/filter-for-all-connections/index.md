+++
type = "question"
title = "Filter for all connections"
description = '''So I have two pcaps and I need to get the length of each connection in them and graph them against the connection start times (so y axis is duration and x axis is time). I also need to find connections that did not end with an ACK after a FIN-ACK. I am new to working with pcaps so I am unsure how to...'''
date = "2015-03-28T07:25:00Z"
lastmod = "2015-03-28T23:20:00Z"
weight = 40953
keywords = [ "filter", "tcpdump", "pcap" ]
aliases = [ "/questions/40953" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Filter for all connections](/questions/40953/filter-for-all-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40953-score" class="post-score" title="current number of votes">0</div><span id="post-40953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>So I have two pcaps and I need to get the length of each connection in them and graph them against the connection start times (so y axis is duration and x axis is time). I also need to find connections that did not end with an ACK after a FIN-ACK. I am new to working with pcaps so I am unsure how to do this. I assume wireshark would be easiest but if tcpdump or some other utility would be better that is fine as well. Can anyone help me with a filter?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '15, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/1192c6dcea3298e7c3f2b4dd581253d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thaweatherman&#39;s gravatar image" /><p><span>thaweatherman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thaweatherman has no accepted answers">0%</span></p></div></div><div id="comments-container-40953" class="comments-container"></div><div id="comment-tools-40953" class="comment-tools"></div><div class="clear"></div><div id="comment-40953-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40958"></span>

<div id="answer-container-40958" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40958-score" class="post-score" title="current number of votes">0</div><span id="post-40958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use the conversations statistics to create a list of all conversations. It has columns for the relative start and duration, so you could export those statistics to graph something in Excel or any other graphical program.</p><p>The other problem is finding FINs without a following ACK - this is next to impossible, because you can't filter on packet dependencies. There are some tricks to do this for the session start, but not for the session termination. May I ask why you need to find conversations like this?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '15, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40958" class="comments-container"><span id="40960"></span><div id="comment-40960" class="comment"><div id="post-40960-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. How do I pull up the conversations statistics? It looks like there should be a Conversations option under the Statistics menu but I don't see one (version 1.12.4). As for the FIN without ACK (to keep it simple), I want to record those conversations' lengths as well by assigning a specific time length.</p></div><div id="comment-40960-info" class="comment-info"><span class="comment-age">(28 Mar '15, 11:20)</span> <span class="comment-user userinfo">thaweatherman</span></div></div><span id="40965"></span><div id="comment-40965" class="comment"><div id="post-40965-score" class="comment-score"></div><div class="comment-text"><p>yes, the conversation statistics are found in the statistics menu, and it is definitely available in 1.12.4. its the third options from the top, called "conversations".</p></div><div id="comment-40965-info" class="comment-info"><span class="comment-age">(28 Mar '15, 15:33)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-40958" class="comment-tools"></div><div class="clear"></div><div id="comment-40958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40974"></span>

<div id="answer-container-40974" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40974-score" class="post-score" title="current number of votes">0</div><span id="post-40974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can filter on all completing TCP connections (SYN-&gt;FIN/RST) and use Statistics -&gt; IOGraph to draq the tcp.time_relative on the y axis using y Axis -&gt; Unit advanced. The filter would be<br />
<code>tcp[13]&amp;5 and !tcp.window_size_scalefactor==-1</code></p><p>For the second part of your question wireshark would have to keep track of the tcp session's state in a variable which you could then filter on tcp.state=="FINWAIT2". It currently doesn't do this but certainly sounds like it could be done - but I'm not a coder so maybe easier said than done ;-)</p><p>Regards Matthias <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-2.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '15, 23:20</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div></div><div id="comments-container-40974" class="comments-container"></div><div id="comment-tools-40974" class="comment-tools"></div><div class="clear"></div><div id="comment-40974-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

