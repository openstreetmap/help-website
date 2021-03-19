+++
type = "question"
title = "Understanding the RTP Stream Analysis"
description = '''Hi I would like to understand the the output of the RTP Streams Analysis I get here by going to: Telephony &amp;gt; RTP &amp;gt; Show All Streams. In the output, under the &#x27;Lost Column&#x27; I have -1722(-100.0%). Also seen when you click the Analyze Button, the bottom reads: Total RTP packets = 1722 (expected 1...'''
date = "2013-12-06T06:36:00Z"
lastmod = "2013-12-10T02:28:00Z"
weight = 27870
keywords = [ "analysis", "rtp", "stream" ]
aliases = [ "/questions/27870" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Understanding the RTP Stream Analysis](/questions/27870/understanding-the-rtp-stream-analysis)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27870-score" class="post-score" title="current number of votes">0</div><span id="post-27870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I would like to understand the the output of the RTP Streams Analysis</p><p>I get here by going to: Telephony &gt; RTP &gt; Show All Streams.</p><p>In the output, under the '<em>Lost Column</em>' I have <strong>-1722(-100.0%)</strong>.</p><p>Also seen when you click the <strong>Analyze</strong> Button, the bottom reads: <strong>Total RTP packets = 1722 (expected 1722) Lost RTP packets = -1722 (-100.00%) Sequence errors = 1722</strong></p><p>I dont understand Lost -1722 (the negative value). I dont understand -100% (the negative value). I dont understand the expectation of 1722, the loss of -1722, the sequence errors of 1722. Yet there was no problem with this test call/RTP stream.</p><p>Your explanation/advise will be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '13, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/3fd14e224ed7c1462677eabc7735c7aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahmedn&#39;s gravatar image" /><p><span>ahmedn</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahmedn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '13, 06:38</strong> </span></p></div></div><div id="comments-container-27870" class="comments-container"><span id="27874"></span><div id="comment-27874" class="comment"><div id="post-27874-score" class="comment-score"></div><div class="comment-text"><p>what is your:</p><ul><li>OS and OS version</li><li>Wireshark version</li></ul><p>Is it possible to post the capture file somewhere (google drive, dropbox, cloudshark.org or mega.co.nz)?</p></div><div id="comment-27874-info" class="comment-info"><span class="comment-age">(06 Dec '13, 08:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27870" class="comment-tools"></div><div class="clear"></div><div id="comment-27870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27968"></span>

<div id="answer-container-27968" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27968-score" class="post-score" title="current number of votes">1</div><span id="post-27968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you see if the effect of duplicate packets in your capture. The fact that you have -100% lost means you have 100% packets too many. Then there's the fact that you have 1722 (=100%) sequence errors, because every duplicate (which has the same sequence number) adds to the seq# error count. This is prone to happen when you monitor a VLAN on a switch, which captures both ingress and egress. Either capture only one direction, or sanitize your capture file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '13, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-27968" class="comments-container"></div><div id="comment-tools-27968" class="comment-tools"></div><div class="clear"></div><div id="comment-27968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

