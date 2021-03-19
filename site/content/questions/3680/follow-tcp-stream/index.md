+++
type = "question"
title = "Follow TCP stream"
description = '''I understand that &quot;follow tcp stream&quot; allows packets from a single tcp stream to be displayed in order. I captured a Bittorrent traffic that contains more than 30 tcp streams. How can I display all packets from all the tcp streams in order at the same time?'''
date = "2011-04-21T07:47:00Z"
lastmod = "2014-02-12T07:02:00Z"
weight = 3680
keywords = [ "tcp" ]
aliases = [ "/questions/3680" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Follow TCP stream](/questions/3680/follow-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3680-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3680-score" class="post-score" title="current number of votes">0</div><span id="post-3680-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I understand that "follow tcp stream" allows packets from a single tcp stream to be displayed in order. I captured a Bittorrent traffic that contains more than 30 tcp streams. How can I display all packets from all the tcp streams in order at the same time?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '11, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/cfd1cee9d96dbbb7addc561e46887ad9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="catfish&#39;s gravatar image" /><p><span>catfish</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="catfish has no accepted answers">0%</span></p></div></div><div id="comments-container-3680" class="comments-container"></div><div id="comment-tools-3680" class="comment-tools"></div><div class="clear"></div><div id="comment-3680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3681"></span>

<div id="answer-container-3681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3681-score" class="post-score" title="current number of votes">0</div><span id="post-3681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Follow TCP Stream" selects one TCP conversation and opens an additional window with the payload of that one conversation. So I think what you want to do is to have all conversations display their reconstructed payload, and not just the packets themselves (because for that I'd simply answer: "just filter on tcp" :-))</p><p>As far as I know there is now way to open multiple payload windows without manual interaction; maybe tshark can help. Synbit? Any ideas? :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '11, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3681" class="comments-container"><span id="3682"></span><div id="comment-3682" class="comment"><div id="post-3682-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply.</p><p>What I really want to do is to put all the packets from all the tcp streams shown in the packet list pane IN ORDER (as seen at application level), so my program can analyze them. I don't need to open multiple payload windows. Using filter "tcp" does not resolve packet ordering problem, right?</p></div><div id="comment-3682-info" class="comment-info"><span class="comment-age">(21 Apr '11, 08:19)</span> <span class="comment-user userinfo">catfish</span></div></div><span id="3684"></span><div id="comment-3684" class="comment"><div id="post-3684-score" class="comment-score"></div><div class="comment-text"><p>Using a filter like this, "tcp.stream eq 0 or tcp.stream eq 1 ... or tcp.stream eq n" seems to do the trick.</p></div><div id="comment-3684-info" class="comment-info"><span class="comment-age">(21 Apr '11, 09:12)</span> <span class="comment-user userinfo">catfish</span></div></div><span id="3685"></span><div id="comment-3685" class="comment"><div id="post-3685-score" class="comment-score"></div><div class="comment-text"><p>I don't think that filter is eliminating retransmissions or reordering out-of-order packets for you though...</p></div><div id="comment-3685-info" class="comment-info"><span class="comment-age">(21 Apr '11, 09:44)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="3688"></span><div id="comment-3688" class="comment"><div id="post-3688-score" class="comment-score"></div><div class="comment-text"><p>(@catfish: I converted your "answers" to "comments, as that is the way this Q&amp;A site works best, see the FAQ)</p></div><div id="comment-3688-info" class="comment-info"><span class="comment-age">(21 Apr '11, 14:06)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="3689"></span><div id="comment-3689" class="comment"><div id="post-3689-score" class="comment-score"></div><div class="comment-text"><p>Follow TCP stream does not put the packet list in tcp sequence number order. It just filters out one tcp stream and then, for that stream, puts the tcp payload in order as the application would have received it from the tcp buffers.</p><p>Does your program need the network packets as input, or does it need the tcp payload as input. In case of the first, that is really not easily done when there are out-of-order packets, duplicates, retransmissions and maybe even missing packets.</p><p>In case of the latter, you could use <a href="http://www.circlemud.org/~jelson/software/tcpflow/">tcpflow</a></p></div><div id="comment-3689-info" class="comment-info"><span class="comment-age">(21 Apr '11, 14:10)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="29763"></span><div id="comment-29763" class="comment not_top_scorer"><div id="post-29763-score" class="comment-score"></div><div class="comment-text"><p>I know this conversation is quite old, but SYN-bit's answer caught my attention, because I really need a solution like the one he called "really not easily done" and I'd like to know whether somebody knows how to do thos with missing packets, retransmissions, etc</p></div><div id="comment-29763-info" class="comment-info"><span class="comment-age">(12 Feb '14, 06:34)</span> <span class="comment-user userinfo">tonivalac</span></div></div><span id="29764"></span><div id="comment-29764" class="comment not_top_scorer"><div id="post-29764-score" class="comment-score"></div><div class="comment-text"><p>what about the mentioned tcpflow?</p></div><div id="comment-29764-info" class="comment-info"><span class="comment-age">(12 Feb '14, 06:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29767"></span><div id="comment-29767" class="comment not_top_scorer"><div id="post-29767-score" class="comment-score"></div><div class="comment-text"><p>According to the documentation this tool can only capture data not analyse cap/pcap files or did I miss something?</p></div><div id="comment-29767-info" class="comment-info"><span class="comment-age">(12 Feb '14, 06:50)</span> <span class="comment-user userinfo">tonivalac</span></div></div><span id="29768"></span><div id="comment-29768" class="comment not_top_scorer"><div id="post-29768-score" class="comment-score"></div><div class="comment-text"><p>it can also read pcap files (option -r).</p><p>Anyway, I believe the current wireshark/tshark "Follow TCP stream" function, does take care about missing and out-of-order frames, at least that's what I have seen with a small test capture file.</p></div><div id="comment-29768-info" class="comment-info"><span class="comment-age">(12 Feb '14, 06:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29773"></span><div id="comment-29773" class="comment not_top_scorer"><div id="post-29773-score" class="comment-score"></div><div class="comment-text"><p>Okay, I missed that there is a new branch of tcpflow. Well, I guess I'll try the current version of wireshark first. By the way is there a tcpflow version for windows?</p></div><div id="comment-29773-info" class="comment-info"><span class="comment-age">(12 Feb '14, 06:59)</span> <span class="comment-user userinfo">tonivalac</span></div></div><span id="29775"></span><div id="comment-29775" class="comment not_top_scorer"><div id="post-29775-score" class="comment-score"></div><div class="comment-text"><p>google says so ;-))</p><blockquote><p><a href="https://www.google.com/?q=tcpflow%20windows">https://www.google.com/?q=tcpflow%20windows</a></p></blockquote></div><div id="comment-29775-info" class="comment-info"><span class="comment-age">(12 Feb '14, 07:02)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-3681" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-3681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

