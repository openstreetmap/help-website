+++
type = "question"
title = "Can I write a filter to locate sequence number inconsistencies?"
description = '''Consider the following. I believe that one of my rouers is failing to pass an ICMP response back very intermittently (maybe 1:10,000). While I do not care about the ICMP packets themselves this issue is causing intermittent transmission failure. What I have been doing is runnning a capture for a per...'''
date = "2012-06-25T14:49:00Z"
lastmod = "2012-06-26T00:00:00Z"
weight = 12154
keywords = [ "icmp", "sequence" ]
aliases = [ "/questions/12154" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I write a filter to locate sequence number inconsistencies?](/questions/12154/can-i-write-a-filter-to-locate-sequence-number-inconsistencies)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12154-score" class="post-score" title="current number of votes">0</div><span id="post-12154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Consider the following. I believe that one of my rouers is failing to pass an ICMP response back very intermittently (maybe 1:10,000). While I do not care about the ICMP packets themselves this issue is causing intermittent transmission failure.</p><p>What I have been doing is runnning a capture for a period of time and checking the sequence number for skips. So far this is the only way I have been able to confirm that this is happening.</p><p>example:<br />
icmp.seq == 18<br />
icmp.seq == 19<br />
icmp.seq == 20<br />
icmp.seq == 22 &lt;--Sequence break</p><p>I'd like to be able to write a filter or batch file or something that would look for these automatically so I dont have to spend as much time doing it myself. Any thoughts or advice would be much appreciated.</p><p>Thank you so much.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-sequence" rel="tag" title="see questions tagged &#39;sequence&#39;">sequence</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '12, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/b9a14b2571009f0bd50c337e7c6e4a78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dsltnangel&#39;s gravatar image" /><p><span>Dsltnangel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dsltnangel has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-12154" class="comments-container"></div><div id="comment-tools-12154" class="comment-tools"></div><div class="clear"></div><div id="comment-12154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12157"></span>

<div id="answer-container-12157" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12157-score" class="post-score" title="current number of votes">0</div><span id="post-12157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you can use this command:</p><blockquote><p><code>tshark -r icmp.cap -R "ip.src == x.x.x.x" -T fields -e frame.number -eip.src -e icmp.seq -E header=y -E separator=;</code><br />
</p></blockquote><p>Output will be:</p><pre><code>frame.number;ip.src;icmp.seq
1;x.x.x.x;10
3;x.x.x.x;11
5;x.x.x.x;12
7;x.x.x.x;13
9;x.x.x.x;15
11;x.x.x.x;16</code></pre><p>Then write a script to calculate the difference of the SEQ numbers. Whenever the SEQ number is &gt; 1 you <strong>might</strong> have found a missing ICMP packet. Please consider packets arriving out of order, even if it may be unlikely!</p><p>Instead of a script, you can also use MS Excel. Import the output as CSV and calculate the SUM in column E2: =SUM(C2-C1), E3: =SUM(C3-C2). Then duplicate that formula to all other columns in E (click and drag - see Excel manual).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jun '12, 04:13</strong> </span></p></div></div><div id="comments-container-12157" class="comments-container"></div><div id="comment-tools-12157" class="comment-tools"></div><div class="clear"></div><div id="comment-12157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

