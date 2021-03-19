+++
type = "question"
title = "2-pass filter in Wireshark/tshark"
description = '''The option -Y, -2 and -R in tshark confuse me a long time. After I read the manual, I know that -Y is used in single-pass filter and -2 in 2-pass filter (in case where we can not get some info until 1st pass filter is over) But I still can not understand what is the difference between -2 -Y &#x27;blabla&#x27;...'''
date = "2016-12-26T22:35:00Z"
lastmod = "2017-01-03T06:47:00Z"
weight = 58343
keywords = [ "tshark" ]
aliases = [ "/questions/58343" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [2-pass filter in Wireshark/tshark](/questions/58343/2-pass-filter-in-wiresharktshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58343-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58343-score" class="post-score" title="current number of votes">0</div><span id="post-58343-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The option <strong>-Y</strong>, <strong>-2</strong> and <strong>-R</strong> in <code>tshark</code> confuse me a long time.</p><p>After I read the manual, I know that <strong>-Y</strong> is used in single-pass filter and <strong>-2</strong> in 2-pass filter (in case where we can not get some info until 1st pass filter is over)</p><p>But I still can not understand what is the difference between <code>-2 -Y 'blabla'</code> and <code>-2 -R 'balabala'</code> and <code>-2 -Y 'blalal' -R 'blala'</code></p><p>And I also did an experiment that drive me crazy:</p><pre><code>tshark -n -r test.pcap -2 -R &#39;frame.number &gt; 0&#39;
  1   0.000000 10.140.28.17 -&gt; 10.74.68.58  TCP 80 62276 &gt; 8989 [SYN, ECN, CWR] Seq=0 Win=65535 Len=0 MSS=1460 WS=32 TSval=330325315 TSecr=0 SACK_PERM=1
  2   0.000056  10.74.68.58 -&gt; 10.140.28.17 TCP 76 8989 &gt; 62276 [SYN, ACK, ECN] Seq=0 Ack=1 Win=28960 Len=0 MSS=1460 SACK_PERM=1 TSval=2078759468 TSecr=330325315 WS=128
  3   0.000678 10.140.28.17 -&gt; 10.74.68.58  TCP 68 62276 &gt; 8989 [ACK] Seq=1 Ack=1 Win=131744 Len=0 TSval=330325316 TSecr=2078759468
  4   0.000756 10.140.28.17 -&gt; 10.74.68.58  HTTP 158 GET /index.html HTTP/1.1
  5   0.000770  10.74.68.58 -&gt; 10.140.28.17 TCP 68 8989 &gt; 62276 [ACK] Seq=1 Ack=91 Win=29056 Len=0 TSval=2078759468 TSecr=330325316</code></pre><p>But when I execute <code>tshark -n -r test.pcap -2 -R 'frame.number &gt; 1'</code>, there is nothing printed. How to explain this?</p><p>My tshark version is: TShark 1.10.6 (v1.10.6 from master-1.10)</p><p>Can you help me with this problem? Thank you in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Dec '16, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/32b68811c8e23407ddf05b9f11cb0d56?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kldzdj&#39;s gravatar image" /><p><span>kldzdj</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kldzdj has no accepted answers">0%</span></p></div></div><div id="comments-container-58343" class="comments-container"></div><div id="comment-tools-58343" class="comment-tools"></div><div class="clear"></div><div id="comment-58343-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58479"></span>

<div id="answer-container-58479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58479-score" class="post-score" title="current number of votes">0</div><span id="post-58479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>-R</code> specifies a <em>read</em> filter, so only matching packets from a file are read and processed; unmatched packets are essentially treated as if the file didn't contain them at all. Contrast this with <code>-Y</code>, which specifies a display filter, so only matching packets are displayed, but all packets are still read and processed.</p><p>The problem you're seeing with <code>frame.number</code> is a known bug that was determined not worth fixing long ago. See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=380">Bug 380</a>, <em>"wireshark -R doesn't support 'frame.number' as a read filter "</em>.</p><p>You can also follow along some of the history behind <code>-R</code> vs. <code>-Y</code> here:</p><ul><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8223">Bug 8223</a></li><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8316">Bug 8316</a></li><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8529">Bug 8529</a></li><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9048">Bug 9048</a></li><li>Wireshark-dev mailing list discussion:</li><li><a href="https://www.wireshark.org/lists/wireshark-dev/201303/msg00008.html">Local archive</a></li><li><a href="https://marc.info/?l=wireshark-dev&amp;m=136220351121519">MARC archives</a></li><li><a href="https://www.mail-archive.com/wireshark-dev@wireshark.org/msg27170.html">The Mail Archive</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '17, 06:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-58479" class="comments-container"></div><div id="comment-tools-58479" class="comment-tools"></div><div class="clear"></div><div id="comment-58479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

