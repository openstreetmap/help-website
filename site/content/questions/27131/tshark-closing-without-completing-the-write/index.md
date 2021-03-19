+++
type = "question"
title = "Tshark closing without completing the write"
description = '''I have a pcap file of size 16 GB and I am using the following tshark command tshark -T fields -n -r testbed.pcap -E separator=, -e ip.proto -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e frame.number -e frame.time_epoch -e tcp.flags.urg -e tcp.checksum_bad &amp;gt;file.txt&quot; But after writing for o...'''
date = "2013-11-19T21:23:00Z"
lastmod = "2013-11-20T19:57:00Z"
weight = 27131
keywords = [ "tshark" ]
aliases = [ "/questions/27131" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark closing without completing the write](/questions/27131/tshark-closing-without-completing-the-write)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27131-score" class="post-score" title="current number of votes">0</div><span id="post-27131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a pcap file of size 16 GB and I am using the following tshark command</p><p><strong>tshark -T fields -n -r testbed.pcap -E separator=, -e ip.proto -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e frame.number -e frame.time_epoch -e tcp.flags.urg -e tcp.checksum_bad &gt;file.txt"</strong></p><p>But after writing for only 222MB, tshark is closing.</p><p>Please suggest how to write the entire content.</p><p>Your help will be highly appreciated.</p><p>Thank You</p><p>PUGLU</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '13, 21:23</strong></p><img src="https://secure.gravatar.com/avatar/303f85009d021cbeaa029f0731dc5d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="puglu&#39;s gravatar image" /><p><span>puglu</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="puglu has no accepted answers">0%</span></p></div></div><div id="comments-container-27131" class="comments-container"><span id="27134"></span><div id="comment-27134" class="comment"><div id="post-27134-score" class="comment-score"></div><div class="comment-text"><p>What verion of Wireshark/tshark are you using? tshark might be running out of memory 16GB is quite a big file you might need to split it in smaller pieces.</p></div><div id="comment-27134-info" class="comment-info"><span class="comment-age">(19 Nov '13, 22:39)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="27135"></span><div id="comment-27135" class="comment"><div id="post-27135-score" class="comment-score"></div><div class="comment-text"><p>i am using wireshark-win32-1.6.8. i have tried the same tshark command for a 4 GB pcap also. it is giving the same result.</p></div><div id="comment-27135-info" class="comment-info"><span class="comment-age">(19 Nov '13, 22:49)</span> <span class="comment-user userinfo">puglu</span></div></div><span id="27143"></span><div id="comment-27143" class="comment"><div id="post-27143-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and installed memory? As <span>@Anders</span> said, it's likely you are running out of memory.</p></div><div id="comment-27143-info" class="comment-info"><span class="comment-age">(20 Nov '13, 02:20)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="27146"></span><div id="comment-27146" class="comment"><div id="post-27146-score" class="comment-score"></div><div class="comment-text"><p>4 GB RAM</p><p>I am using windows xp sp3, 32 bit</p></div><div id="comment-27146-info" class="comment-info"><span class="comment-age">(20 Nov '13, 02:29)</span> <span class="comment-user userinfo">puglu</span></div></div></div><div id="comment-tools-27131" class="comment-tools"></div><div class="clear"></div><div id="comment-27131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27148"></span>

<div id="answer-container-27148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27148-score" class="post-score" title="current number of votes">2</div><span id="post-27148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you have a 32 bit OS, the tshark process is limited to 2GB RAM, unless you have enabled 4GB tuning as detailed <a href="http://msdn.microsoft.com/en-us/library/windows/desktop/bb613473%28v=vs.85%29.aspx">here</a>, which will then allow tshark to use 3GB RAM. You'll also need to use a version of tshark that has the large memory address aware flag set in the executable, I don't know when we started doing that but a recent (1.10.x) version will be OK.</p><p>If you have access to a 64 bit OS, then you can use the 64 bit version of tshark which will then be able to access most of the memory on the pc, even then this may not be enough to process all your capture in one go without splitting it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 02:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-27148" class="comments-container"><span id="27153"></span><div id="comment-27153" class="comment"><div id="post-27153-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much grahamb for the reply. i will try the tuning as well as download the latest version</p><p>Thank you once again.</p></div><div id="comment-27153-info" class="comment-info"><span class="comment-age">(20 Nov '13, 03:37)</span> <span class="comment-user userinfo">puglu</span></div></div><span id="27163"></span><div id="comment-27163" class="comment"><div id="post-27163-score" class="comment-score"></div><div class="comment-text"><p>Refer also to Wireshark's <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">OutOfMemory</a> wiki page for more information on that topic. And for splitting the large 16GB file into smaller files, which ought to help avoid this situation, refer to the <a href="http://www.wireshark.org/docs/man-pages/editcap.html">editcap</a> man page.</p></div><div id="comment-27163-info" class="comment-info"><span class="comment-age">(20 Nov '13, 07:29)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="27190"></span><div id="comment-27190" class="comment"><div id="post-27190-score" class="comment-score"></div><div class="comment-text"><p>Thank you cmaynard. I have done just that. i have split the file.</p></div><div id="comment-27190-info" class="comment-info"><span class="comment-age">(20 Nov '13, 19:57)</span> <span class="comment-user userinfo">puglu</span></div></div></div><div id="comment-tools-27148" class="comment-tools"></div><div class="clear"></div><div id="comment-27148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

