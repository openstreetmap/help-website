+++
type = "question"
title = "How to find response times for an HTTP call to specific ip."
description = '''Hi, Do we have any specific filter to use to find response times for an HTTP call to/from specific ip. Thanks,'''
date = "2012-10-09T15:16:00Z"
lastmod = "2012-10-09T18:42:00Z"
weight = 14843
keywords = [ "wireshark" ]
aliases = [ "/questions/14843" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to find response times for an HTTP call to specific ip.](/questions/14843/how-to-find-response-times-for-an-http-call-to-specific-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14843-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Do we have any specific filter to use to find response times for an HTTP call to/from specific ip.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 15:16</strong></p><img src="https://secure.gravatar.com/avatar/301e8556a334719019209711cdbfd439?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dvsrk&#39;s gravatar image" /><p>dvsrk<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dvsrk has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '12, 22:40</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-14843" class="comments-container"></div><div id="comment-tools-14843" class="comment-tools"></div><div class="clear"></div><div id="comment-14843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14846"></span>

<div id="answer-container-14846" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14846-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"call" in what sense? Voice over IP phone call? HTTP request/response call? ONC RPC or DCE RPC or CORBA or... call?</p><p>There's no way to determine calls and responses at the IP or TCP layer, so call/response times have to be determined at the call/response protocol layer. Several dissectors for Wireshark <em>do</em> match calls and responses, and provide response times; the time for a particular call will show up in the protocol details for the response, and some statistics for all calls and responses for some protocols are available under the "Service response time" submenu of the "Statistics" menu.</p><p>Unfortunately, there is currently no request/response tracking for HTTP, so the best you can do is to look at the HTTP requests and replies, match them up yourself, and compute the difference between the request and response packet time stamps yourself.</p><p>You might want to file a bug at the <a href="http://bugs.wireshark.org/">Wireshark Bugzilla</a> requesting that HTTP request/response tracking be added as a feature.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '12, 18:42</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '12, 22:43</p></div></div><div id="comments-container-14846" class="comments-container"><span id="14847"></span><div id="comment-14847" class="comment"><div id="post-14847-score" class="comment-score"></div><div class="comment-text"><p>It's my apology to be not clear. I'm referring to HTTP req/resp call. Is there any way we can track down using wireshark.</p><p>I want to track down the calls from specific ip which are taking greater then 1 sec. Anyway possible using wireshark ?</p><p>Thanks.</p></div><div id="comment-14847-info" class="comment-info"><span class="comment-age">(09 Oct '12, 19:59)</span> dvsrk</div></div><span id="14851"></span><div id="comment-14851" class="comment"><div id="post-14851-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Anyway possible using wireshark ?</p></blockquote><p>Not easily, unfortunately. I've updated my answer to reflect that and give more details.</p></div><div id="comment-14851-info" class="comment-info"><span class="comment-age">(09 Oct '12, 22:44)</span> Guy Harris ♦♦</div></div><span id="14884"></span><div id="comment-14884" class="comment"><div id="post-14884-score" class="comment-score"></div><div class="comment-text"><p>There's already an enhancement bug asking for HTTP response times: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7394">bug 7394</a>.</p></div><div id="comment-14884-info" class="comment-info"><span class="comment-age">(10 Oct '12, 06:16)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-14846" class="comment-tools"></div><div class="clear"></div><div id="comment-14846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

