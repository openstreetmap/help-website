+++
type = "question"
title = "Total Bandwidth usage while file download"
description = '''Hi, I am playing a youtube video. I have collected the tcpdump. How can I check the total bandwidth using wireshark for the particular youtube video.'''
date = "2013-10-06T23:22:00Z"
lastmod = "2013-10-07T08:04:00Z"
weight = 25693
keywords = [ "bandwidth", "total" ]
aliases = [ "/questions/25693" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Total Bandwidth usage while file download](/questions/25693/total-bandwidth-usage-while-file-download)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25693-score" class="post-score" title="current number of votes">0</div><span id="post-25693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am playing a youtube video. I have collected the tcpdump. How can I check the total bandwidth using wireshark for the particular youtube video.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-total" rel="tag" title="see questions tagged &#39;total&#39;">total</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '13, 23:22</strong></p><img src="https://secure.gravatar.com/avatar/e7d54e7cb1e5cf7cab4a56f53beebcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sysadm270180&#39;s gravatar image" /><p><span>sysadm270180</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sysadm270180 has no accepted answers">0%</span></p></div></div><div id="comments-container-25693" class="comments-container"></div><div id="comment-tools-25693" class="comment-tools"></div><div class="clear"></div><div id="comment-25693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25697"></span>

<div id="answer-container-25697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25697-score" class="post-score" title="current number of votes">0</div><span id="post-25697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use the statistics menu, e.g. the summary which gives you a total over the whole file or (if you applied a filter to the Youtube stream) also the throughput of the conversation. The other thing you could look at is the conversation statistics - if you can identify the youtube stream it gives you the bandwidth for the connection as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25697" class="comments-container"></div><div id="comment-tools-25697" class="comment-tools"></div><div class="clear"></div><div id="comment-25697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25711"></span>

<div id="answer-container-25711" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25711-score" class="post-score" title="current number of votes">0</div><span id="post-25711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How can I check the <strong>total bandwidth</strong> using wireshark for the particular youtube video.</p></blockquote><p>The bandwidth is most certainly not static throughout the connection, so you should look at the IO graphs for that conversation.</p><p>Find the video stream:</p><blockquote><p>Statistics -&gt; Conversations -&gt; TCP (a Tab)</p></blockquote><p>Pick the one with a destination IP of Youtube or the conversation with the most transferred bytes (works only if you did not download anything else during the video stream).</p><p>Click on the stream and select "Follow Stream" (Button).</p><p>Wireshark will now auto-create a display filter like this:</p><blockquote><p>tcp.stream eq 12</p></blockquote><p>Copy-Paste that filter and then open the IO graphs.</p><blockquote><p>Statistics -&gt; IO Graph</p></blockquote><p>Paste your filter into the first Filter: field. Then choose "Bits/Tick" as <strong>Unit</strong> and click on the Button "Graph 1". You will now see the bandwidth used by that stream throughout the whole conversation.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 08:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25711" class="comments-container"></div><div id="comment-tools-25711" class="comment-tools"></div><div class="clear"></div><div id="comment-25711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

