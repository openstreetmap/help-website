+++
type = "question"
title = "IO graphs - TCP Delta"
description = '''Hi Folks, can someone please tell me where I&#x27;m going wrong with the IO graph please? I know I&#x27;ve got to be doing something wrong, most likely something obvious.  I&#x27;m trying to graph tcp.time_delta, something I was able to do in a previous version of Wireshark but when I apply the filter in the IO gr...'''
date = "2017-02-01T09:14:00Z"
lastmod = "2017-02-10T09:16:00Z"
weight = 59226
keywords = [ "iographs", "io", "tcp.time_delta" ]
aliases = [ "/questions/59226" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [IO graphs - TCP Delta](/questions/59226/io-graphs-tcp-delta)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59226-score" class="post-score" title="current number of votes">0</div><span id="post-59226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks,</p><p>can someone please tell me where I'm going wrong with the IO graph please? I know I've got to be doing something wrong, most likely something obvious. I'm trying to graph tcp.time_delta, something I was able to do in a previous version of Wireshark but when I apply the filter in the IO graph in WS 2.2.4 nothing appears in the graph. The graph parameters accept my input and even the legend shows the tcp.time_delta MIN, MAX and AVG as display reference but there is no visibility of the tcp.time_delta in the graph any where. please see example below of my filters etc. Any advice would be greatly appreciated.</p><p>thanks Ciaran</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IO_Grpah_TCP_time_Delta.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iographs" rel="tag" title="see questions tagged &#39;iographs&#39;">iographs</span> <span class="post-tag tag-link-io" rel="tag" title="see questions tagged &#39;io&#39;">io</span> <span class="post-tag tag-link-tcp.time_delta" rel="tag" title="see questions tagged &#39;tcp.time_delta&#39;">tcp.time_delta</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '17, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/55af0207b10dbbd15ebb9f852822a294?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ciag&#39;s gravatar image" /><p><span>Ciag</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ciag has no accepted answers">0%</span></p></img></div></div><div id="comments-container-59226" class="comments-container"></div><div id="comment-tools-59226" class="comment-tools"></div><div class="clear"></div><div id="comment-59226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59229"></span>

<div id="answer-container-59229" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59229-score" class="post-score" title="current number of votes">1</div><span id="post-59229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ciag has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think it may be an issue with the scale of your graph. When I just tried your filters on a small capture I have of a single SSH session I get graphs of everything, but the range of values is quite large with most of them between abut 500 and 10^6. Have you tried a log scale to see if that helps?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '17, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/a446b2537577b08421cfd0c9b544b19e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djdawson&#39;s gravatar image" /><p><span>djdawson</span><br />
<span class="score" title="46 reputation points">46</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djdawson has one accepted answer">25%</span></p></div></div><div id="comments-container-59229" class="comments-container"><span id="59335"></span><div id="comment-59335" class="comment"><div id="post-59335-score" class="comment-score"></div><div class="comment-text"><p>you hit the nail on the head. the file was too big I tried the same graph on another file and they worked as expected.</p><p>thanks</p></div><div id="comment-59335-info" class="comment-info"><span class="comment-age">(10 Feb '17, 09:16)</span> <span class="comment-user userinfo">Ciag</span></div></div></div><div id="comment-tools-59229" class="comment-tools"></div><div class="clear"></div><div id="comment-59229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

