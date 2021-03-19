+++
type = "question"
title = "What does the 8 stand for in (tcp.stream eq 8)?"
description = '''I just can&#x27;t figure out what the 8 stands for in (tcp.stream eq 8)?'''
date = "2011-10-26T07:42:00Z"
lastmod = "2011-11-08T03:10:00Z"
weight = 7082
keywords = [ "filter", "ip", "udp", "stream", "tcp" ]
aliases = [ "/questions/7082" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What does the 8 stand for in (tcp.stream eq 8)?](/questions/7082/what-does-the-8-stand-for-in-tcpstream-eq-8)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7082-score" class="post-score" title="current number of votes">0</div><span id="post-7082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just can't figure out what the 8 stands for in (tcp.stream eq 8)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '11, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/ecd2bdd3d9d56b69971607da007b0485?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="0xffff0&#39;s gravatar image" /><p><span>0xffff0</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="0xffff0 has no accepted answers">0%</span></p></div></div><div id="comments-container-7082" class="comments-container"></div><div id="comment-tools-7082" class="comment-tools"></div><div class="clear"></div><div id="comment-7082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7084"></span>

<div id="answer-container-7084" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7084-score" class="post-score" title="current number of votes">2</div><span id="post-7084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="0xffff0 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It indicates that this is the 8th TCP or UDP stream found in the trace.</p><p>Before we had stream numbers a filter to identify the stream would specify a pair of IP addresses and port numbers, resulting in much longer display filters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '11, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-7084" class="comments-container"><span id="7086"></span><div id="comment-7086" class="comment"><div id="post-7086-score" class="comment-score"></div><div class="comment-text"><p>I.e., the 8 has no deep significance - it's just a number that Wireshark uses internally.</p></div><div id="comment-7086-info" class="comment-info"><span class="comment-age">(26 Oct '11, 10:53)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="7274"></span><div id="comment-7274" class="comment"><div id="post-7274-score" class="comment-score"></div><div class="comment-text"><p>When tcp.stream was implemented, the number had no significance and would show some gaps. In recent (development) versions of Wireshark the number represents order in which wireshark detected tcp streams, the first gets tcp.stream==0, the next tcp.stream==1 etc.</p></div><div id="comment-7274-info" class="comment-info"><span class="comment-age">(08 Nov '11, 03:10)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-7084" class="comment-tools"></div><div class="clear"></div><div id="comment-7084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

