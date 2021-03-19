+++
type = "question"
title = "Wireshark(dumpcap, tshark), ringbuffer problem from command line"
description = '''Hello, Please help me with the following problem. I&#x27;m using ringbuffer to limit the number of files and size. Unfortunately this option is not working or I&#x27;m doing something wrong. The below command should make only 5 files, but actually like is displayed is not deleting the files that are exceeded ...'''
date = "2010-12-09T02:22:00Z"
lastmod = "2010-12-09T04:56:00Z"
weight = 1297
keywords = [ "dumpcap", "ringbuffer", "tshark" ]
aliases = [ "/questions/1297" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark(dumpcap, tshark), ringbuffer problem from command line](/questions/1297/wiresharkdumpcap-tshark-ringbuffer-problem-from-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1297-score" class="post-score" title="current number of votes">1</div><span id="post-1297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Please help me with the following problem.</p><p>I'm using ringbuffer to limit the number of files and size. Unfortunately this option is not working or I'm doing something wrong.</p><p>The below command should make only 5 files, but actually like is displayed is not deleting the files that are exceeded the number configured.</p><p>I'm using the wireshark Version 1.4.0 (SVN Rev 34005 from /trunk-1.4), it is a portable version, but this error is happening also under Linux Sles11.</p><p>.dumpcap.exe -i 6 -b filesize:10 -b files:5 -w D:wiresharktest.pcap</p><p>File: D:wiresharktest_00001_20101209112524.pcap</p><p>Packets: 116 File: D:wiresharktest_00002_20101209112539.pcap</p><p>Packets: 167 File: D:wiresharktest_00003_20101209112539.pcap</p><p>Packets: 238 File: D:wiresharktest_00004_20101209112547.pcap</p><p>Packets: 322 File: D:wiresharktest_00005_20101209112559.pcap</p><p>Packets: 380 File: D:wiresharktest_00006_20101209112607.pcap</p><p>Packets: 442 File: D:wiresharktest_00007_20101209112615.pcap</p><p>Packets: 544 File: D:wiresharktest_00008_20101209112637.pcap</p><p>Packets: 621 Packets dropped: 0</p><p>Thank you,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-ringbuffer" rel="tag" title="see questions tagged &#39;ringbuffer&#39;">ringbuffer</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '10, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/ce2a3f9a3bbcd664adefe1cdf6089ed9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="longelas&#39;s gravatar image" /><p><span>longelas</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="longelas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Dec '10, 02:53</strong> </span></p></div></div><div id="comments-container-1297" class="comments-container"><span id="1298"></span><div id="comment-1298" class="comment"><div id="post-1298-score" class="comment-score"></div><div class="comment-text"><p>I'm using tshark that is installed with "Version 1.4.2 (SVN Rev 34959 from /trunk-1.4)". This works properly for me (only creating the five files at about 10K each. I'm not running Linux at the moment. I tested this on Windows.</p></div><div id="comment-1298-info" class="comment-info"><span class="comment-age">(09 Dec '10, 03:34)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div></div><div id="comment-tools-1297" class="comment-tools"></div><div class="clear"></div><div id="comment-1297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1300"></span>

<div id="answer-container-1300" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1300-score" class="post-score" title="current number of votes">0</div><span id="post-1300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>Thank you is working now. I dont think it was an wireshark(dumpcap, thsark) error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Dec '10, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/ce2a3f9a3bbcd664adefe1cdf6089ed9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="longelas&#39;s gravatar image" /><p><span>longelas</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="longelas has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Dec '10, 04:58</strong> </span></p></div></div><div id="comments-container-1300" class="comments-container"></div><div id="comment-tools-1300" class="comment-tools"></div><div class="clear"></div><div id="comment-1300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

