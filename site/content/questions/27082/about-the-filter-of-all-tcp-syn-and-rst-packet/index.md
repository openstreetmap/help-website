+++
type = "question"
title = "about the filter of all tcp SYN and RST packet"
description = '''Hi, I found a display filter expression &quot;tcp[13]&amp;amp;6&quot; which can filter out all the tcp SYN and RST packet, but I don&#x27;t understand how does it work. I know the 13 is a offset and &quot;&amp;amp;&quot; is the bit_wise operator, what is the &quot;6&quot;? Why can this expression filter out the result mentioned above? thank ...'''
date = "2013-11-18T20:30:00Z"
lastmod = "2013-11-19T23:41:00Z"
weight = 27082
keywords = [ "bit_wise" ]
aliases = [ "/questions/27082" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [about the filter of all tcp SYN and RST packet](/questions/27082/about-the-filter-of-all-tcp-syn-and-rst-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27082-score" class="post-score" title="current number of votes">0</div><span id="post-27082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I found a display filter expression "tcp[13]&amp;6" which can filter out all the tcp SYN and RST packet, but I don't understand how does it work. I know the 13 is a offset and "&amp;" is the bit_wise operator, what is the "6"? Why can this expression filter out the result mentioned above?</p><p>thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bit_wise" rel="tag" title="see questions tagged &#39;bit_wise&#39;">bit_wise</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '13, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/2d1a8885858c8435654658b25f489bd9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveZhou&#39;s gravatar image" /><p><span>SteveZhou</span><br />
<span class="score" title="191 reputation points">191</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveZhou has no accepted answers">0%</span></p></div></div><div id="comments-container-27082" class="comments-container"></div><div id="comment-tools-27082" class="comment-tools"></div><div class="clear"></div><div id="comment-27082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27083"></span>

<div id="answer-container-27083" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27083-score" class="post-score" title="current number of votes">5</div><span id="post-27083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SteveZhou has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The last 3 bits of the TCP flags are</p><pre><code>0000 0000 
      ||&#39;---&gt; FIN 
      |&#39;----&gt; SYN 
      &#39;-----&gt; RST</code></pre><p>13 is the decimal byte offset of the flags-byte into the TCP header. So a &amp;6 (0000 0110) tests whether SYN or RST bit are set. <code>tcp.flags.syn==1 or tcp.flags.reset==1</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '13, 21:55</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Nov '13, 01:49</strong> </span></p></div></div><div id="comments-container-27083" class="comments-container"><span id="27088"></span><div id="comment-27088" class="comment"><div id="post-27088-score" class="comment-score"></div><div class="comment-text"><p>got it, but why tcp[13] rather than any other number?</p></div><div id="comment-27088-info" class="comment-info"><span class="comment-age">(19 Nov '13, 00:42)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="27089"></span><div id="comment-27089" class="comment"><div id="post-27089-score" class="comment-score">1</div><div class="comment-text"><p>13 is the decimal byte offset of the flags-byte into the TCP header</p></div><div id="comment-27089-info" class="comment-info"><span class="comment-age">(19 Nov '13, 01:47)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="27128"></span><div id="comment-27128" class="comment"><div id="post-27128-score" class="comment-score"></div><div class="comment-text"><p>all right, its decimal byte offset. thanks</p><p>Another question is, how can I get to know this number quickly? Is there any reference document?</p></div><div id="comment-27128-info" class="comment-info"><span class="comment-age">(19 Nov '13, 17:07)</span> <span class="comment-user userinfo">SteveZhou</span></div></div><span id="27132"></span><div id="comment-27132" class="comment"><div id="post-27132-score" class="comment-score"></div><div class="comment-text"><p><a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol">http://en.wikipedia.org/wiki/Transmission_Control_Protocol</a></p></div><div id="comment-27132-info" class="comment-info"><span class="comment-age">(19 Nov '13, 21:28)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="27136"></span><div id="comment-27136" class="comment"><div id="post-27136-score" class="comment-score"></div><div class="comment-text"><p>thank you!</p></div><div id="comment-27136-info" class="comment-info"><span class="comment-age">(19 Nov '13, 23:41)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-27083" class="comment-tools"></div><div class="clear"></div><div id="comment-27083-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

