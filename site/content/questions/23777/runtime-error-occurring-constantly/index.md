+++
type = "question"
title = "Runtime error occurring constantly."
description = '''I am running wireshark version 1.10.1; and capturing layer 2 data. I have capture options configured for local interface, single channel with multiple files enabled. The next file is enabled to start after 1Mb. All other options are disabled. The capture duration between failure is 20 files =/- 3 fi...'''
date = "2013-08-14T10:25:00Z"
lastmod = "2013-08-15T07:06:00Z"
weight = 23777
keywords = [ "failure", "runtime", "error" ]
aliases = [ "/questions/23777" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Runtime error occurring constantly.](/questions/23777/runtime-error-occurring-constantly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23777-score" class="post-score" title="current number of votes">0</div><span id="post-23777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running wireshark version 1.10.1; and capturing layer 2 data. I have capture options configured for local interface, single channel with multiple files enabled. The next file is enabled to start after 1Mb. All other options are disabled. The capture duration between failure is 20 files =/- 3 files. The runtime error is - This application has requested the Runtime to terminate it in an unusual way.</p><p>Please advise what is required to resolve this issue.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-failure" rel="tag" title="see questions tagged &#39;failure&#39;">failure</span> <span class="post-tag tag-link-runtime" rel="tag" title="see questions tagged &#39;runtime&#39;">runtime</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Aug '13, 10:25</strong></p><img src="https://secure.gravatar.com/avatar/074c04ae91fd49bb4b17b21af8983643?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eanderson&#39;s gravatar image" /><p><span>eanderson</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eanderson has no accepted answers">0%</span></p></div></div><div id="comments-container-23777" class="comments-container"></div><div id="comment-tools-23777" class="comment-tools"></div><div class="clear"></div><div id="comment-23777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23781"></span>

<div id="answer-container-23781" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23781-score" class="post-score" title="current number of votes">0</div><span id="post-23781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How long was the capture running before the crash? If it was running for a long period of time (where <em>long</em> is not well-defined, unfortunately), then perhaps it was an "<a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">Out of memory</a>" condition that caused it? If so, consider using <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Aug '13, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-23781" class="comments-container"><span id="23797"></span><div id="comment-23797" class="comment"><div id="post-23797-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much cmaynard! command line tshark -i 2 -b filesize:100000 -b files:50 -b duration:7200 -f "ether dst host ff:04:ff:ff:ff:ff" -w d:\test.pcap is the string my Support Team provided and it's working fine now. Only problem is the command line execution can't be viewed thru the wireshark interface on the fly.</p></div><div id="comment-23797-info" class="comment-info"><span class="comment-age">(15 Aug '13, 07:06)</span> <span class="comment-user userinfo">eanderson</span></div></div></div><div id="comment-tools-23781" class="comment-tools"></div><div class="clear"></div><div id="comment-23781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

