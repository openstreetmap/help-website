+++
type = "question"
title = "TShark Export to Excel Filtering Question"
description = '''Hi, I am using TShark to export packets into excel. I need to print out the frame.time_delta_displayed for the packets before the filter is applied, However I only want to display the filtered packets. When I apply the filter, it changes the frame.time_delta_displayed, which I don&#x27;t want to happen. ...'''
date = "2016-01-30T18:06:00Z"
lastmod = "2016-01-31T00:31:00Z"
weight = 49647
keywords = [ "filter", "excel", "tshark" ]
aliases = [ "/questions/49647" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TShark Export to Excel Filtering Question](/questions/49647/tshark-export-to-excel-filtering-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49647-score" class="post-score" title="current number of votes">0</div><span id="post-49647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using TShark to export packets into excel. I need to print out the frame.time_delta_displayed for the packets before the filter is applied, However I only want to display the filtered packets. When I apply the filter, it changes the frame.time_delta_displayed, which I don't want to happen. Also, it can't be frame.time_delta</p><p>tshark -r EthernetPacket1.pcap -o rtp.heuristic_rtp:TRUE -R "ipv6.dst == fd00:0:20:1::35 &amp;&amp; amr.wb.toc.ft == 2" -T fields -e frame.time_delta_displayed &gt; test.csv</p><p>Here's a visual example of what I need. I am trying to filter out the ''30s':</p><p>Original Data (frame.time_delta_displayed)</p><p>10 10 10 30 30 10 10 10</p><p>After Filter is applied: 10 10 10 70(30+30+10) 10 10</p><p>What I want to print: 10 10 10 10 10 10</p><p>If you can help me overcome this struggle I'm having, that would be great!</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-excel" rel="tag" title="see questions tagged &#39;excel&#39;">excel</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '16, 18:06</strong></p><img src="https://secure.gravatar.com/avatar/70970378ceff3ad31256c40d8051890f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="atancr02&#39;s gravatar image" /><p><span>atancr02</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="atancr02 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '16, 18:07</strong> </span></p></div></div><div id="comments-container-49647" class="comments-container"></div><div id="comment-tools-49647" class="comment-tools"></div><div class="clear"></div><div id="comment-49647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49651"></span>

<div id="answer-container-49651" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49651-score" class="post-score" title="current number of votes">1</div><span id="post-49651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One possible way could be the of use</p><pre><code> frame.time_delta </code></pre>instead of<pre><code>frame.time_delta_captured</code></pre>.Which should display the delta to the prev captured frame regardless whether displayed or not.</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '16, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jan '16, 01:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-49651" class="comments-container"></div><div id="comment-tools-49651" class="comment-tools"></div><div class="clear"></div><div id="comment-49651-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

