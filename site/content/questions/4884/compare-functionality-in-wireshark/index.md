+++
type = "question"
title = "Compare functionality in Wireshark"
description = '''Hi I am attempting to use the Wireshark compare function to compare captures taken on client &amp;amp; server. I could do with come clarification on a few things please: Is it advisable for the 2 computers to have their times synchronised prior to taking the 2 captures, or does this make no difference? ...'''
date = "2011-07-01T08:46:00Z"
lastmod = "2011-07-01T09:29:00Z"
weight = 4884
keywords = [ "compare" ]
aliases = [ "/questions/4884" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Compare functionality in Wireshark](/questions/4884/compare-functionality-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4884-score" class="post-score" title="current number of votes">0</div><span id="post-4884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I am attempting to use the Wireshark compare function to compare captures taken on client &amp; server. I could do with come clarification on a few things please:</p><p>Is it advisable for the 2 computers to have their times synchronised prior to taking the 2 captures, or does this make no difference?</p><p>In the result dialog box, can you explain what the following mean:</p><p>Scopes: (is this the range of information matched up in each end's capture?)</p><p>Equal packets: (is this the number of packets that match up in the 2 merged captures?)</p><p>I see an average time difference of 1231.xxxxxx, but the RTT between the 2 computers is only 10ms. Is this due to the times not being synchronised on the 2 computers?</p><p>I am trying to compare a merged capture file of approx 171MB. When I start the comparison, usually the computer stops responding. Sometimes it recovers after around 10 mins, but other times it does not &amp; Wireshark has to be closed. any ideas?</p><p>Sorry about so many questions, but thought I'd try to get answers to all in one go..</p><p>Many Thanks Ian</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compare" rel="tag" title="see questions tagged &#39;compare&#39;">compare</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jul '11, 08:46</strong></p><img src="https://secure.gravatar.com/avatar/4dfdb30f4297c840a2cd7b3b6754fe34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ipittam&#39;s gravatar image" /><p><span>ipittam</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ipittam has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jul '11, 08:46</strong> </span></p></div></div><div id="comments-container-4884" class="comments-container"></div><div id="comment-tools-4884" class="comment-tools"></div><div class="clear"></div><div id="comment-4884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4886"></span>

<div id="answer-container-4886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4886-score" class="post-score" title="current number of votes">0</div><span id="post-4886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In my experience it is wise to have the servers/computers time synchronized by using NTP, network time protocol. I don't know what type server you're using, but for Windows Server 2008 you can enable this: http://computeradvisors.net/windows-server-2008/configure-ntp-(network-time-protocol)-on-windows-server-2008/</p><p>Kerberos' Ticket Granting Tickets system works more efficiently in authorization of users if systems time are synchronized, as tickets could effectively expire before they should based on incorrect times. However, there is an offset time which you can use to specify the offset in the Compare function of Wireshark if the time is not exactly the same.</p><p>A 171MB capture file is rather large for analyzing. I've found that keeping my cap files smaller than 50m makes it easier and less time consuming to analyze. I imagine your computer is stopping running because of the size of the files it is processing.</p><p>Hope this is somewhat helpful, John<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '11, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-4886" class="comments-container"></div><div id="comment-tools-4886" class="comment-tools"></div><div class="clear"></div><div id="comment-4886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

