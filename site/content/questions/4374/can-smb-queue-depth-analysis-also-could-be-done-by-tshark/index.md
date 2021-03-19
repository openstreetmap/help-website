+++
type = "question"
title = "Can SMB QUEUE DEPTH analysis also could be done by tshark?"
description = '''Hi All I am looking into SMB QUEUE DEPTH analysis with tshark. i know hot get smb.time statistics &quot;tshark -nlr c:smb.pcap -qz io,stat,10,&quot;COUNT(smb.time)smb.time&quot;,&quot;MIN(smb.time)smb.time&quot;,&quot;AVG(smb.time)smb.time&quot;,&quot;MAX(smb.time)smb.time&quot;  but i can&#x27;t find the right query for LOAD Please advice Thanks'''
date = "2011-06-04T12:03:00Z"
lastmod = "2011-06-09T01:41:00Z"
weight = 4374
keywords = [ "queue", "depth", "smb", "analysis" ]
aliases = [ "/questions/4374" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can SMB QUEUE DEPTH analysis also could be done by tshark?](/questions/4374/can-smb-queue-depth-analysis-also-could-be-done-by-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4374-score" class="post-score" title="current number of votes">0</div><span id="post-4374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All</p><p>I am looking into SMB QUEUE DEPTH analysis with tshark. i know hot get smb.time statistics "tshark -nlr c:smb.pcap -qz io,stat,10,"COUNT(smb.time)smb.time","MIN(smb.time)smb.time","AVG(smb.time)smb.time","MAX(smb.time)smb.time" but i can't find the right query for LOAD Please advice Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-queue" rel="tag" title="see questions tagged &#39;queue&#39;">queue</span> <span class="post-tag tag-link-depth" rel="tag" title="see questions tagged &#39;depth&#39;">depth</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '11, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p><span>tbaror</span><br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></div></div><div id="comments-container-4374" class="comments-container"><span id="4381"></span><div id="comment-4381" class="comment"><div id="post-4381-score" class="comment-score"></div><div class="comment-text"><p>anyone? LOAD(smb.time)smb.time</p></div><div id="comment-4381-info" class="comment-info"><span class="comment-age">(05 Jun '11, 02:35)</span> <span class="comment-user userinfo">tbaror</span></div></div><span id="4394"></span><div id="comment-4394" class="comment"><div id="post-4394-score" class="comment-score">2</div><div class="comment-text"><p>See thread at <a href="http://www.wireshark.org/lists/wireshark-users/201106/msg00015.html">Wireshark User's list</a>.</p></div><div id="comment-4394-info" class="comment-info"><span class="comment-age">(06 Jun '11, 00:45)</span> <span class="comment-user userinfo">joke</span></div></div></div><div id="comment-tools-4374" class="comment-tools"></div><div class="clear"></div><div id="comment-4374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4464"></span>

<div id="answer-container-4464" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4464-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4464-score" class="post-score" title="current number of votes">3</div><span id="post-4464-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tbaror has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>QUEUE DEPTH analysis can now be done by tshark.<br />
Thanks to Ronnie Sahlberg. He has checked in an enhancement to add LOAD() stats to tshark.<br />
<br />
Download <a href="http://www.wireshark.org/download.html">Wireshark version 1.6.0</a> and run this command:<br />
</p><pre><code>$ tshark -r test.pcap -qz &quot;io,stat,360,LOAD(smb.time)smb.time&quot;
===================================================================
IO Statistics
Interval: 360.000 secs
Column #0: LOAD(smb.time)smb.time
                |   Column #0
Time            |           LOAD
000.000-360.000       462.096794
360.000-720.000       100.718411
720.000-1080.000        96.485666
1080.000-1440.000        35.952216
1440.000-1800.000        80.976688
1800.000-2160.000         8.415044</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '11, 21:46</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-4464" class="comments-container"><span id="4467"></span><div id="comment-4467" class="comment"><div id="post-4467-score" class="comment-score"></div><div class="comment-text"><p>thanks :-)</p></div><div id="comment-4467-info" class="comment-info"><span class="comment-age">(09 Jun '11, 01:41)</span> <span class="comment-user userinfo">tbaror</span></div></div></div><div id="comment-tools-4464" class="comment-tools"></div><div class="clear"></div><div id="comment-4464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

