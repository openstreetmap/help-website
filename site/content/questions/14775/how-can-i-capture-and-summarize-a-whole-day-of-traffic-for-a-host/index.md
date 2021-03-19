+++
type = "question"
title = "How can I capture and summarize a whole day of traffic for a host?"
description = '''I&#x27;m trying to help our server gang check if it&#x27;s safe to retire a particular server. They ask me (since I&#x27;m network support) who&#x27;s talking with this host over the course of a full day? I know I can have them run TSHARK, and use its conversation summary: tshark -i 1 -c ####### -z conv,&quot;ip&quot;,ip.addr==x...'''
date = "2012-10-08T08:59:00Z"
lastmod = "2012-10-08T12:44:00Z"
weight = 14775
keywords = [ "filter", "capture" ]
aliases = [ "/questions/14775" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I capture and summarize a whole day of traffic for a host?](/questions/14775/how-can-i-capture-and-summarize-a-whole-day-of-traffic-for-a-host)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14775-score" class="post-score" title="current number of votes">0</div><span id="post-14775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to help our server gang check if it's safe to retire a particular server. They ask me (since I'm network support) who's talking with this host over the course of a full day?</p><p>I know I can have them run TSHARK, and use its conversation summary:</p><pre><code>tshark -i 1 -c ####### -z conv,&quot;ip&quot;,ip.addr==x.y.z.w -q</code></pre><p>I don't know how many packets to expect. I suppose if some reasonable number (200,000?) gets exhausted quickly, they have some heavy flow activity they need to investigate first. Later runs of the same capture would detect infrequent and lighter flow activity over longer time.</p><p>Is there a better technique? Focus on just TCP-SYN to reduce what has to be captured? Does the conversation summarization feature work with filters such as TCP-SYN?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '12, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/7bb2a6bc57e437eb644353a639170430?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RichardBerke&#39;s gravatar image" /><p><span>RichardBerke</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RichardBerke has no accepted answers">0%</span></p></div></div><div id="comments-container-14775" class="comments-container"></div><div id="comment-tools-14775" class="comment-tools"></div><div class="clear"></div><div id="comment-14775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14791"></span>

<div id="answer-container-14791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14791-score" class="post-score" title="current number of votes">0</div><span id="post-14791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>if it's safe to retire a particular server.</p></blockquote><p>O.K. so they expect to have eliminated most (if no all) of the traffic to that host, so you should not see that much traffic right?</p><p>If so, I recommend running dumpcap with a capture filter on the ip address of the server and then, after a day (you should limit the captured data to some size), you can analyze the traffic with tshark.</p><blockquote><p><code>dumpcap -ni 1 -s 60 -w c:\temp\all-day.cap -a filesize:300000 host x.x.x.x</code><br />
</p></blockquote><p>Replace '1' with the interface ID you want to capture on (see dumpcap -D -M). Replace 'x.x.x.x' with the ip address of the server. This command will stop after 300 MByte (-a accepts the file size in KB). As you only capture the first few bytes of every packet, you can record quite a lot of conversations and 300 MByte should be sufficient for the whole day. If it is not, you can also use ring buffers with dumpcap (see man page).</p><p>Then you can analyze with thshark:</p><blockquote><p><code>tshark -r c:\temp\all-day.cap -q -z conv,tcp</code><br />
<code>tshark -r c:\temp\all-day.cap -q -z conv,udp</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14791" class="comments-container"></div><div id="comment-tools-14791" class="comment-tools"></div><div class="clear"></div><div id="comment-14791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

