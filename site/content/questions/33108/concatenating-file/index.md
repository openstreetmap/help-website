+++
type = "question"
title = "Concatenating File"
description = '''I am working to debug our network here at my workplace and have just finished reading and working through the Wireshark 101 book by Laura Chappell. I hooked up a Blackbox copper tap close to one of our network switches and ran wireshark with no capture filters in place to capture ALL network traffic...'''
date = "2014-05-27T07:50:00Z"
lastmod = "2014-05-27T08:11:00Z"
weight = 33108
keywords = [ "9482433", "34" ]
aliases = [ "/questions/33108" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Concatenating File](/questions/33108/concatenating-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33108-score" class="post-score" title="current number of votes">0</div><span id="post-33108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working to debug our network here at my workplace and have just finished reading and working through the Wireshark 101 book by Laura Chappell. I hooked up a Blackbox copper tap close to one of our network switches and ran wireshark with no capture filters in place to capture ALL network traffic which I had plans to feed into Cascade Pilot PE to attempt to understand what issues currently exist in our network.</p><p>When I run wireshark, it seems to crash after approx 1/2 hour of capture. I am saving the file to an NTFS file system so am not sure what the problem is however if I switch to using Multiple Files and write a new file every 100MB everything seems to go ok. The problem now is I am left with many files that I want to analyze all at once in Cascade Pilot. Is it possible to concatenate all these files into one file that I can then open in Cascade Pilot for analysis?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-9482433" rel="tag" title="see questions tagged &#39;9482433&#39;">9482433</span> <span class="post-tag tag-link-34" rel="tag" title="see questions tagged &#39;34&#39;">34</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '14, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/e9cb265f7a384170179aa8d439993e2c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="profishark&#39;s gravatar image" /><p><span>profishark</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="profishark has no accepted answers">0%</span></p></div></div><div id="comments-container-33108" class="comments-container"></div><div id="comment-tools-33108" class="comment-tools"></div><div class="clear"></div><div id="comment-33108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33109"></span>

<div id="answer-container-33109" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33109-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33109-score" class="post-score" title="current number of votes">2</div><span id="post-33109-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Several questions in one here:</p><ol><li>Using Wireshark to make captures of massive traffic flows is inviting the <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory problem</a> to visit. In short, use dumpcap to make capture where the aim is purely to capture for later analysis.</li><li>Even using multiple files, capturing lots of traffic with Wireshark is problematic, see #1 above.</li><li>I believe Pilot will work quite happily with multiple captures, I used it like that once in the past, and I don't think it will have lost that capability. You'll just have to RTFM to see how to do that.</li><li>If you really want to concatenate all the files, then <a href="http://www.wireshark.org/docs/man-pages/mergecap.html">mergecap</a> (command line, installed along with Wireshark) will do the job. Subsequently opening such a huge file in Wireshark might be difficult though.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 May '14, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33109" class="comments-container"></div><div id="comment-tools-33109" class="comment-tools"></div><div class="clear"></div><div id="comment-33109-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

