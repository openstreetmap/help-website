+++
type = "question"
title = "total delay by all packets with more than 10 ms delta"
description = '''Hi, Question is related to delay calculation,lets say in a one session i have RTT of 1 ms and total time taken for session is 32 seconds due to delay,retransmission etc.Is there any way to find out total time taken by packets who have more than 10ms delay or accumulated time of all packets with more...'''
date = "2014-05-08T00:25:00Z"
lastmod = "2014-05-16T22:16:00Z"
weight = 32634
keywords = [ "delay", "calculation" ]
aliases = [ "/questions/32634" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [total delay by all packets with more than 10 ms delta](/questions/32634/total-delay-by-all-packets-with-more-than-10-ms-delta)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32634-score" class="post-score" title="current number of votes">0</div><span id="post-32634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, Question is related to delay calculation,lets say in a one session i have RTT of 1 ms and total time taken for session is 32 seconds due to delay,retransmission etc.Is there any way to find out total time taken by packets who have more than 10ms delay or accumulated time of all packets with more than 10ms delay.I can find out packets with more than 10ms delay with tcp.time_delta but it doesnt not show total time by all such packet but it just shows percentage of such packet.Help is really appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-delay" rel="tag" title="see questions tagged &#39;delay&#39;">delay</span> <span class="post-tag tag-link-calculation" rel="tag" title="see questions tagged &#39;calculation&#39;">calculation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '14, 00:25</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-32634" class="comments-container"><span id="32674"></span><div id="comment-32674" class="comment"><div id="post-32674-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, but I don't understand what you are asking. As nobody answered, I'm probably not the only one.</p><p>Please add or more details or a better description of your 'problem'.</p></div><div id="comment-32674-info" class="comment-info"><span class="comment-age">(09 May '14, 11:25)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32702"></span><div id="comment-32702" class="comment"><div id="post-32702-score" class="comment-score"></div><div class="comment-text"><p>What i want to know is that in a one tcp stream if we do summary it shows us multiple details like total conversation time,bytes/sec,packets/sec etc but if i add a filter tcp.time_delta ge 0.200 and if i see summary again it only shows total no. of displayed packet but not the accumulated time of all those filtered packets.This is just to see that how much delay is being added by all packets with more than 200 ms delay.</p></div><div id="comment-32702-info" class="comment-info"><span class="comment-age">(10 May '14, 02:51)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-32634" class="comment-tools"></div><div class="clear"></div><div id="comment-32634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32706"></span>

<div id="answer-container-32706" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32706-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32706-score" class="post-score" title="current number of votes">3</div><span id="post-32706-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="kishan pandey has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could filter for the tcp stream, export the packets as CSV and calculate the total delay in Excel or if you want something more complex use tshark in a script. For a quick sum under Linux try this command:</p><pre><code>tshark -r file.pcap -R &quot;tcp.stream eq 0&quot; -T fields -e &quot;tcp.time_delta&quot; |  sort -rn | awk &#39;$1 &gt; 0.200&#39; | awk &#39;{sum += $1;} END {print sum;}&#39;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '14, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 May '14, 11:23</strong> </span></p></div></div><div id="comments-container-32706" class="comments-container"><span id="32777"></span><div id="comment-32777" class="comment"><div id="post-32777-score" class="comment-score"></div><div class="comment-text"><p>Thanks roland,can we do the same thing with tshark in windows</p></div><div id="comment-32777-info" class="comment-info"><span class="comment-age">(13 May '14, 23:10)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="32797"></span><div id="comment-32797" class="comment"><div id="post-32797-score" class="comment-score"></div><div class="comment-text"><p>You should be able to do it in PowerShell, but I don't know the exact syntax.</p></div><div id="comment-32797-info" class="comment-info"><span class="comment-age">(14 May '14, 09:31)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="32813"></span><div id="comment-32813" class="comment"><div id="post-32813-score" class="comment-score">2</div><div class="comment-text"><p>Powershell:</p><p>Define your limit and stream index:</p><p><code>$limit = 0.2 $strm  = 0</code></p><p>Then execute:</p><p><code>tshark -r file.pcap -Y "tcp.stream eq $strm" -T fields -e "tcp.time_delta" | sort | where { $_ -ge $limit } | Measure-Object -Sum | select -Expand Sum</code></p><p>Note I've switched to -Y for the filter expression as -R requires a <code>-2</code> for a two pass read, and you also need the default profile to have set the option for TCP to calculate conversation timestamps.</p></div><div id="comment-32813-info" class="comment-info"><span class="comment-age">(15 May '14, 03:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="32851"></span><div id="comment-32851" class="comment"><div id="post-32851-score" class="comment-score"></div><div class="comment-text"><p>Excellent,thanks graham,for your valuable help</p></div><div id="comment-32851-info" class="comment-info"><span class="comment-age">(16 May '14, 22:16)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-32706" class="comment-tools"></div><div class="clear"></div><div id="comment-32706-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

