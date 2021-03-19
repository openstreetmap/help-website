+++
type = "question"
title = "which to use Wireshark, dumpcap, tshark or tcpdump for capturing ?"
description = '''I need to automate capturing traffic (so a script will start the capturing not me) from a specific program on my machine to a remote server. It will also capture all the traffic that sent to that program on my machine. While Capturing I need to not drop any packets as every packet matters a lot in m...'''
date = "2014-09-03T11:34:00Z"
lastmod = "2014-09-04T13:18:00Z"
weight = 35968
keywords = [ "capture", "wireshark" ]
aliases = [ "/questions/35968" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [which to use Wireshark, dumpcap, tshark or tcpdump for capturing ?](/questions/35968/which-to-use-wireshark-dumpcap-tshark-or-tcpdump-for-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35968-score" class="post-score" title="current number of votes">0</div><span id="post-35968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to automate capturing traffic (so a script will start the capturing not me) from a specific program on my machine to a remote server. It will also capture all the traffic that sent to that program on my machine. While Capturing I need to not drop any packets as every packet matters a lot in my scenario. The capturing and the communication between my program and the remote server is taking place at the same machine.</p><p>I'm planning to use Wireshark to analyse the traffic as I've built my own dissector to help me with that. However, I'm not sure if it is a appropriate to use Wireshark in my settings also. As I need a command line interface rather than GUI and I also have read that that wireshark consumes a lot of the CPU.</p><p>I'm hesitating between tcpdump, tshark and dumpcap to do the capturing. Guy Harris mentioned in <a href="http://stackoverflow.com/questions/22218852/performance-and-efficiency-comparing-between-dump-tools-tcpdump-tshark-dumpca">this link</a> that tcpdump is dropping more than tcpdump is this still true? Is there a resource to find more comprehensive comparison between these tools?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '14, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-35968" class="comments-container"></div><div id="comment-tools-35968" class="comment-tools"></div><div class="clear"></div><div id="comment-35968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35984"></span>

<div id="answer-container-35984" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35984-score" class="post-score" title="current number of votes">0</div><span id="post-35984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the answer to <a href="https://ask.wireshark.org/questions/35973/which-is-best-to-use-wireshark-dumpcap-tshark-tcpdump-for-capturing">a similar question</a>.</p><p>And, no, we haven't changed anything in dumpcap that would make a significant difference, so tcpdump probably still has the best performance. There's also <a href="http://netsniff-ng.org">netsniff-ng</a> for Linux.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '14, 21:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-35984" class="comments-container"><span id="36012"></span><div id="comment-36012" class="comment"><div id="post-36012-score" class="comment-score"></div><div class="comment-text"><p>Actually #ifdef :ing the debug printout done per packet might have made a difference. But I haven't made any measurements.</p></div><div id="comment-36012-info" class="comment-info"><span class="comment-age">(04 Sep '14, 13:18)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-35984" class="comment-tools"></div><div class="clear"></div><div id="comment-35984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

