+++
type = "question"
title = "Follow tcp stream with tshark still can not in batch mode?"
description = '''I tried to use the latest wireshark &amp;amp; tshark of version 1.90, I tried to follow tcp stream with tshark in following options: liunx@liunx-G41MT-S2PT:~/Work/NetWork/packets$ tshark -r follow_tcp.pcapng -z follow,tcp,ascii,127.0.0.1:12345,127.0.0.1:5678 But I just can get one session between the cl...'''
date = "2012-10-09T02:54:00Z"
lastmod = "2012-10-09T18:24:00Z"
weight = 14811
keywords = [ "follow", "tcp.stream", "tshark", "wireshark" ]
aliases = [ "/questions/14811" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Follow tcp stream with tshark still can not in batch mode?](/questions/14811/follow-tcp-stream-with-tshark-still-can-not-in-batch-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14811-score" class="post-score" title="current number of votes">0</div><span id="post-14811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to use the latest wireshark &amp; tshark of version 1.90, I tried to follow tcp stream with tshark in following options:<br />
<code>[email protected]:~/Work/NetWork/packets$ tshark -r follow_tcp.pcapng  -z follow,tcp,ascii,127.0.0.1:12345,127.0.0.1:5678</code></p><p>But I just can get one session between the client and server, and I want get all of the sessions, so any tips?<br />
It's easy to build the test environment with nc, we can use<br />
nc -p 12345 localhost 5678<br />
as client, -p option can specific the src port, we can use nc -lk 5678<br />
as server, then capture the tcp stream with wireshark or tshark, and the result is disappointment, I can just follow one stream, so any help?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-tcp.stream" rel="tag" title="see questions tagged &#39;tcp.stream&#39;">tcp.stream</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/d7511cd99041bcb5eda1ff4b6792b8c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="liunx&#39;s gravatar image" /><p><span>liunx</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="liunx has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Oct '12, 03:29</strong> </span></p></div></div><div id="comments-container-14811" class="comments-container"></div><div id="comment-tools-14811" class="comment-tools"></div><div class="clear"></div><div id="comment-14811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14826"></span>

<div id="answer-container-14826" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14826-score" class="post-score" title="current number of votes">1</div><span id="post-14826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="liunx has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But I just can get one session between the client and server, and I want get all of the sessions, so any tips?</p></blockquote><p>that's only possible with scripting. You can try this:</p><ol><li>print all TCP stream numbers for the desired server/port combination.</li><li>use that list to extract all streams.</li></ol><p><code> for stream in `tshark -r follow_tcp.pcap -R "ip.addr eq 127.0.0.1 and tcp.port eq 5678" -T fields -e tcp.stream | sort -n -u`; do echo Stream: $stream; tshark -r follow_tcp.pcap -q -z follow,tcp,ascii,$stream; done</code></p><p>The other option is to use <strong>tcpflow</strong></p><blockquote><p><code>http://ask.wireshark.org/questions/10023/command-line-option-for-follow-tcp-stream</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14826" class="comments-container"><span id="14845"></span><div id="comment-14845" class="comment"><div id="post-14845-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much!</p></div><div id="comment-14845-info" class="comment-info"><span class="comment-age">(09 Oct '12, 18:24)</span> <span class="comment-user userinfo">liunx</span></div></div></div><div id="comment-tools-14826" class="comment-tools"></div><div class="clear"></div><div id="comment-14826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

