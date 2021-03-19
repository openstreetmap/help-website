+++
type = "question"
title = "TCP Window size"
description = '''What is the difference between Calculated Window Size (tcp_window_size) and Window Size Value(tcp_window_size_value) on Wireshark?'''
date = "2017-03-02T07:57:00Z"
lastmod = "2017-03-21T23:31:00Z"
weight = 59806
keywords = [ "tcpwindowsize", "tcp", "wireshark" ]
aliases = [ "/questions/59806" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Window size](/questions/59806/tcp-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59806-score" class="post-score" title="current number of votes">0</div><span id="post-59806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the difference between <strong>Calculated Window Size (tcp_window_size)</strong> and <strong>Window Size Value(tcp_window_size_value)</strong> on Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpwindowsize" rel="tag" title="see questions tagged &#39;tcpwindowsize&#39;">tcpwindowsize</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '17, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/6dd3e71b974fad46455a71063cb9c319?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="armodes&#39;s gravatar image" /><p><span>armodes</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="armodes has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Mar '17, 08:41</strong> </span></p></div></div><div id="comments-container-59806" class="comments-container"></div><div id="comment-tools-59806" class="comment-tools"></div><div class="clear"></div><div id="comment-59806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59807"></span>

<div id="answer-container-59807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59807-score" class="post-score" title="current number of votes">2</div><span id="post-59807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>tcp.window_size_value</code> is the raw window size value as read directly from the TCP header, whereas <code>tcp.window_size</code> is the calculated window size, which is based on whether window scaling is applicable or not. If window scaling is not used or the scaling factor is 1 or if it's unknown whether window scaling is applicable or not because the TCP 3-way handshake was not captured, then the two values will be the same. You can tell by the <code>tcp.window_size_scalefactor</code> which of these conditions is applicable - if its value is -1, then it's unknown, if its value is -2, then window scaling is not used, and all other values represent an actual window scaling size factor.</p><p>For more information on the TCP window scale option, refer to <a href="https://tools.ietf.org/html/rfc1323#section-2">RFC 1323</a> and/or <a href="https://tools.ietf.org/html/rfc7323#section-2">RFC 7323</a>, which obsoletes RFC 1323.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '17, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59807" class="comments-container"><span id="60242"></span><div id="comment-60242" class="comment"><div id="post-60242-score" class="comment-score"></div><div class="comment-text"><p>Which one has an impact on the congestion window (cwnd)?</p></div><div id="comment-60242-info" class="comment-info"><span class="comment-age">(21 Mar '17, 16:36)</span> <span class="comment-user userinfo">armodes</span></div></div><span id="60244"></span><div id="comment-60244" class="comment"><div id="post-60244-score" class="comment-score">1</div><div class="comment-text"><p>the calculated window size, because that's how big the window really is.</p></div><div id="comment-60244-info" class="comment-info"><span class="comment-age">(21 Mar '17, 16:51)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="60248"></span><div id="comment-60248" class="comment"><div id="post-60248-score" class="comment-score"></div><div class="comment-text"><p>As the cwnd is a stack internal value wihich says how much data can be sent the size can only be guessed. The value which helps you here Ivan be in some cases the "bytes in flight".</p><p>In fact the limitations for the session are the minimum value of the cwnd or the calculated window size, depends on which value is smaller.</p></div><div id="comment-60248-info" class="comment-info"><span class="comment-age">(21 Mar '17, 23:31)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-59807" class="comment-tools"></div><div class="clear"></div><div id="comment-59807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

