+++
type = "question"
title = "Is sender&#x27;s send buffer throttled by tcp?"
description = '''I have a situation where the client is Ubuntu 12.04 and Mac OS X is the server. Now I took some dumps and saw that even when Linux is ready to receive more data, mac is not sending it. Note that the recv buffers of both Linux and Mac are enough to handle bigger amount of data. In all scenarios, I am...'''
date = "2012-11-20T08:51:00Z"
lastmod = "2012-11-20T23:01:00Z"
weight = 16120
keywords = [ "send", "tcp", "congestion" ]
aliases = [ "/questions/16120" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is sender's send buffer throttled by tcp?](/questions/16120/is-senders-send-buffer-throttled-by-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16120-score" class="post-score" title="current number of votes">0</div><span id="post-16120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a situation where the client is Ubuntu 12.04 and Mac OS X is the server. Now I took some dumps and saw that even when Linux is ready to receive more data, mac is not sending it. Note that the recv buffers of both Linux and Mac are enough to handle bigger amount of data.</p><p>In all scenarios, I am sure that mac always has more data to send then why is it not sending even when Bytes in flight is less than the receive window size of Linux.</p><p>Is there any tcp congestion control mechanism which can throttle the mac's send window? How do I change/optimize this value?</p><p>Main dump where this is visible is <a href="http://www.cloudshark.org/captures/af1d9b4517cc">here</a>. These two dumps <a href="http://www.cloudshark.org/captures/e82b17831916">here</a> and <a href="http://www.cloudshark.org/captures/33acdd5edd27">here</a> support this observation more.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-send" rel="tag" title="see questions tagged &#39;send&#39;">send</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-congestion" rel="tag" title="see questions tagged &#39;congestion&#39;">congestion</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '12, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/2df84c5f3698faf841410ada02c8e5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aditya%20Patawari&#39;s gravatar image" /><p><span>Aditya Patawari</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aditya Patawari has no accepted answers">0%</span></p></div></div><div id="comments-container-16120" class="comments-container"></div><div id="comment-tools-16120" class="comment-tools"></div><div class="clear"></div><div id="comment-16120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16121"></span>

<div id="answer-container-16121" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16121-score" class="post-score" title="current number of votes">2</div><span id="post-16121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aditya Patawari has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Beside the fact that you already opened two questions regarding tcp send / recieve window, keeping people busy trying to help you and you did not accept any of those answers yet but now open the third question -&gt; I will answer here too one more time, but I strongly suggest that you go back to reading about advanced TCP stack behaviour and related RFCs, since your questions are all about buffer management...</p><p>Back to your trace -&gt; the sending stack DOES very well send as much data as allowed by recv. window. See example frame 3794, where bytes in flight is close to 200k.</p><p>However, since I suppose those traces again come from whatever sort of simulated latency environment, I can only guess what happens here.</p><p>Normally you don't have data coming in minor-MSS blocks when you have a high throughput transmission. Depending on the size of data blocks passed to TCP, TCP will segment data to fit MSS and send it. In your trace(s), there are tons of sub-MSS packets, which in that form are not sent by a normally behaving application, nor by the stack. You can sometimes observe patterns of minor-MSS packets now-and-then based on fixed read blocks e.g. of 32768 bytes per block or something, but this is not what a regular behaviour looks like.</p><p>So if you have a precise question and are willing to share information about the background of this tracefiles feel free to ask... and Yes under normal circumstances you should see the stack using recv. window at a certain point if bandwidth, delay and application data delivery is not limiting it in any way or if there is packet loss of course.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '12, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Nov '12, 09:21</strong> </span></p></div></div><div id="comments-container-16121" class="comments-container"><span id="16142"></span><div id="comment-16142" class="comment"><div id="post-16142-score" class="comment-score"></div><div class="comment-text"><p>Hey, I apologize for not accepting any answers yet. Reason it that I just want to ensure that I accept the right answer. I have opened up a thread with UVNC a day before and I am following up with them and going through their code. I have read about tcp and these behaviors are weird to me that is why I am posting here.</p><p>I guess I have missed certain concepts and I am working hard to get things right. All the questions I asked are accompanied by 2-3 traces and I take a very hard look on the values before I ask anything.</p><p>I am really sorry if I offended you in any way.</p></div><div id="comment-16142-info" class="comment-info"><span class="comment-age">(20 Nov '12, 23:01)</span> <span class="comment-user userinfo">Aditya Patawari</span></div></div></div><div id="comment-tools-16121" class="comment-tools"></div><div class="clear"></div><div id="comment-16121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

