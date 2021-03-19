+++
type = "question"
title = "Collect expert.message from tshark"
description = '''Is there some way to extract expert.message from a pcap using tshark? I&#x27;d like to do something like this in an automated script to get the number of packets with an expert message of severity Warn: tshark -R &quot;expert.severity eq Warn&quot; -r eth1.pcap | wc -l  That just errs: tshark: Neither &quot;expert.seve...'''
date = "2012-01-20T14:01:00Z"
lastmod = "2012-01-20T20:09:00Z"
weight = 8518
keywords = [ "expert-info", "tshark" ]
aliases = [ "/questions/8518" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Collect expert.message from tshark](/questions/8518/collect-expertmessage-from-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8518-score" class="post-score" title="current number of votes">0</div><span id="post-8518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there some way to extract <code>expert.message</code> from a pcap using tshark?</p><p>I'd like to do something like this in an automated script to get the number of packets with an expert message of severity <code>Warn</code>:</p><pre><code>tshark -R &quot;expert.severity eq Warn&quot; -r eth1.pcap | wc -l</code></pre><p>That just errs:</p><pre><code>tshark: Neither &quot;expert.severity&quot; nor &quot;Warn&quot; are field or protocol names.</code></pre><p>Any suggestions would be very much appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-expert-info" rel="tag" title="see questions tagged &#39;expert-info&#39;">expert-info</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '12, 14:01</strong></p><img src="https://secure.gravatar.com/avatar/68047c85c11d2fe8dcfaaddca7fc6270?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alienrobotninja&#39;s gravatar image" /><p><span>alienrobotninja</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alienrobotninja has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jan '12, 15:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-8518" class="comments-container"><span id="8521"></span><div id="comment-8521" class="comment"><div id="post-8521-score" class="comment-score">1</div><div class="comment-text"><p>What version of Wireshark are you using? And what OS? Your command worked for me (no errors) in SVN 40615, Windows 7 and OSX Lion.</p></div><div id="comment-8521-info" class="comment-info"><span class="comment-age">(20 Jan '12, 15:12)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="8526"></span><div id="comment-8526" class="comment"><div id="post-8526-score" class="comment-score">1</div><div class="comment-text"><p>Even if that filter had worked, it would tell you the number of frames that had at least one warning of a given severity, rather than the actual number of expert items reported.</p><p>Current SVN tshark has "-z expert". "-z expert,error" would only show you the errors, whereas "-z expert,warn" would give you expert errors + warnings. Here is an example and the resulting output. See the total count for a given severity in the first line of output.</p><p>./tshark -z expert,warn -r ../captures/logfile_norlc.out_00000_20120120095148.split -q</p><h1 id="errors-10026">Errors (10026)</h1><p>Frequency Group Protocol Summary 1 Sequence DCT2000 &gt;&gt; ERR ALL: Not processing DL doorbell as already 20259 us old: (deadline is 8000) 1 Sequence DCT2000 &gt;&gt; ERR ALL: Took longer than 8000 usecs to process DL doorbell (20346) 1 Sequence DCT2000 &gt;&gt; ERR MAC: Unexpected UL-Grant buffer number; expected 0, got 1 8323 Sequence MAC-LTE UE 1: SR results in neither a grant nor a failure indication 1586 Malformed MAC-LTE DL Frame has CRC error problem (Duplicate_nonzero_rv) 1 Sequence DCT2000-CStats Duplicate seen (2) 73 Malformed MAC-LTE DL Frame has CRC error problem (Failed) 1 Sequence DCT2000-CStats CRC errors seen (7) 1 Sequence DCT2000-CStats Duplicate seen (155) 29 Malformed MAC-LTE DL Frame has CRC error problem (High Code Rate) 1 Sequence DCT2000-CStats CRC errors seen (20) 1 Sequence DCT2000-CStats CRC errors seen (2) 1 Sequence DCT2000-CStats Duplicate seen (404) 1 Sequence DCT2000-CStats CRC errors seen (17) 1 Sequence DCT2000-CStats CRC errors seen (4) 1 Sequence DCT2000-CStats Duplicate seen (446) 1 Sequence DCT2000-CStats CRC errors seen (19) 1 Sequence DCT2000-CStats CRC errors seen (16) 1 Sequence DCT2000-CStats Duplicate seen (440)</p><h1 id="warns-4">Warns (4)</h1><p>Frequency Group Protocol Summary 1 Malformed MAC-LTE Should not see more than 2 padding subheaders in one frame 1 Sequence DCT2000-CStats Retx seen (131072) 1 Sequence DCT2000-CStats Retx seen (262144) 1 Sequence DCT2000-CStats Retx seen (1048576)</p></div><div id="comment-8526-info" class="comment-info"><span class="comment-age">(20 Jan '12, 18:06)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="8528"></span><div id="comment-8528" class="comment"><div id="post-8528-score" class="comment-score"></div><div class="comment-text"><p>Thanks Gents. Looks like an update will do the trick.</p></div><div id="comment-8528-info" class="comment-info"><span class="comment-age">(20 Jan '12, 20:05)</span> <span class="comment-user userinfo">alienrobotninja</span></div></div></div><div id="comment-tools-8518" class="comment-tools"></div><div class="clear"></div><div id="comment-8518-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8529"></span>

<div id="answer-container-8529" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8529-score" class="post-score" title="current number of votes">0</div><span id="post-8529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="alienrobotninja has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not up to date.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 20:09</strong></p><img src="https://secure.gravatar.com/avatar/68047c85c11d2fe8dcfaaddca7fc6270?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alienrobotninja&#39;s gravatar image" /><p><span>alienrobotninja</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alienrobotninja has one accepted answer">100%</span></p></div></div><div id="comments-container-8529" class="comments-container"></div><div id="comment-tools-8529" class="comment-tools"></div><div class="clear"></div><div id="comment-8529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

