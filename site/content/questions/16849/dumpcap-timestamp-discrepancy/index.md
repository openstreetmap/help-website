+++
type = "question"
title = "Dumpcap timestamp	discrepancy"
description = '''Hi, I am trying to capture packet data to a file using dumpcap script in libpcap format on centos 6.2. When left the capture script running for an extended period of time (weeks/months) it seems the timestamps recorded in our captures slowly drift backwards. The timestamp recorded in the filename as...'''
date = "2012-12-13T14:19:00Z"
lastmod = "2012-12-15T15:58:00Z"
weight = 16849
keywords = [ "tcpdump", "dumpcap", "wrongtimestamp" ]
aliases = [ "/questions/16849" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap timestamp discrepancy](/questions/16849/dumpcap-timestamp-discrepancy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16849-score" class="post-score" title="current number of votes">0</div><span id="post-16849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to capture packet data to a file using dumpcap script in libpcap format on centos 6.2.</p><p>When left the capture script running for an extended period of time (weeks/months) it seems the timestamps recorded in our captures slowly drift backwards. The timestamp recorded in the filename as each new file is created matches the system time relatively well (from observation; i.e. when BAT_99717_20090415222212.cap was created, the system clock showed 10:22 PM.) however the packet timestamps within the file are off by a significant amount. (In this particular example, the first packet in the file has a timestamp of 22:16:18, nearly 6 minutes earlier than when the file was opened.)</p><p>Stopping and restarting the service seems to correct this; after a restart, the first packet in the new file had a timestamp closely matching the timestamp in the filename (and the OS time.)</p><p>Is there any solution/way anyone knows how I keep the clock that dumpcap used constantly synchronized with the OS time?</p><p>Is it a bug?</p><p>Please help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-wrongtimestamp" rel="tag" title="see questions tagged &#39;wrongtimestamp&#39;">wrongtimestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '12, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/9b296b0c1a89a6d15e65215e5e6c69b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld0722&#39;s gravatar image" /><p><span>helloworld0722</span><br />
<span class="score" title="10 reputation points">10</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld0722 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Dec '12, 14:31</strong> </span></p></div></div><div id="comments-container-16849" class="comments-container"><span id="16890"></span><div id="comment-16890" class="comment"><div id="post-16890-score" class="comment-score"></div><div class="comment-text"><p>what is you dumpcap version (dumpcap -v)?</p></div><div id="comment-16890-info" class="comment-info"><span class="comment-age">(14 Dec '12, 07:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="16933"></span><div id="comment-16933" class="comment"><div id="post-16933-score" class="comment-score"></div><div class="comment-text"><p>it is Dumpcap 1.8.0rc2</p></div><div id="comment-16933-info" class="comment-info"><span class="comment-age">(15 Dec '12, 11:31)</span> <span class="comment-user userinfo">helloworld0722</span></div></div></div><div id="comment-tools-16849" class="comment-tools"></div><div class="clear"></div><div id="comment-16849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16892"></span>

<div id="answer-container-16892" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16892-score" class="post-score" title="current number of votes">3</div><span id="post-16892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://ask.wireshark.org/questions/3893/timestamps-drift-from-real-time">Timestamps drift from real time</a> (applies to Windows)</p><p>Update: I just realized that you are using centos (not Windows). So, I don't know if the winpcap timestamp drift issue also applies to libpcap (used on *nix systems).</p><p>If you haven't already done so, I suggest searching for something like "libpcap timestamp drift" or "libpcap timestamp"</p><p>In any case, Wireshark (dumpcap, etc) just uses the timestamps provided by the capture driver (winpcap, libpcap, etc).</p><p>So, this question is better directed to the maintainers of same.</p><p>For libpcap: see <a href="http://www.tcpdump.org/">www.tcpdump.org</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '12, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Dec '12, 08:25</strong> </span></p></div></div><div id="comments-container-16892" class="comments-container"></div><div id="comment-tools-16892" class="comment-tools"></div><div class="clear"></div><div id="comment-16892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16936"></span>

<div id="answer-container-16936" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16936-score" class="post-score" title="current number of votes">0</div><span id="post-16936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>it is Dumpcap 1.8.0rc2</p></blockquote><p>as I don't have that behaviour on Ubuntu 12.04 with dumpcap 1.8.4, I suggest you try the latest dumpcap release. If you see the problem there as well, we might need some additional information.</p><ul><li>is your Linux a virtual machine. If so, what is the Hypervisor?</li><li>how did you start dumpcap (parameters)?</li><li>Do you use an NTP server? If so, do you see any log entries about "NTP clock skew" (or similiar)?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '12, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16936" class="comments-container"><span id="16938"></span><div id="comment-16938" class="comment"><div id="post-16938-score" class="comment-score"></div><div class="comment-text"><p>I am downloading and trying new release 1.8.4. Will let you know the outcome. Thx.</p><p>Which libpcap version do you use ? I am using libpcap 1.1.1</p><p>Ans. 1) Its not a virtual machine 2) dumpcap is started by providing dumpcap -i eth0 -P -g -s 65536 -w /tmp/test.pcap -b files:100 -b filesize:1000000 -b duration:100 -q -t 3) NTP is in sync. No error found in logs.</p></div><div id="comment-16938-info" class="comment-info"><span class="comment-age">(15 Dec '12, 15:14)</span> <span class="comment-user userinfo">helloworld0722</span></div></div><span id="16940"></span><div id="comment-16940" class="comment"><div id="post-16940-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Which libpcap version do you use ? I am using libpcap 1.1.1</p></blockquote><p>same.</p><blockquote><p>Will let you know the outcome.</p></blockquote><p>O.K. we will see. Can you please record the time of your machine, just to make sure there are no time jumps caused by a faulty NTP server (I have seen this a few times).</p><blockquote><p><code>while true; do date &gt;&gt; date.txt; sleep 1; done</code><br />
</p></blockquote><p>Then check <a href="http://date.txt">date.txt</a> as soon as you see the libpcap 'time jumps' again.</p></div><div id="comment-16940-info" class="comment-info"><span class="comment-age">(15 Dec '12, 15:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16936" class="comment-tools"></div><div class="clear"></div><div id="comment-16936-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

