+++
type = "question"
title = "WinPcap sample application crashed"
description = '''Got wireshark with wpcap 4.1.3 installed on my win7 (64bit) PC. I downloaded wpcap developer pack 4.1.2 (the top one, it claims to be compatible with 4.1.3). I unzipped it and went to directory &quot;WpdPack&#92;Examples-pcap&#92;UDPdump&quot; and made an exe UDPDump.exe using MinGW Gcc (64bit). However, when I ran i...'''
date = "2016-05-04T13:29:00Z"
lastmod = "2016-05-06T02:46:00Z"
weight = 52238
keywords = [ "winpcap" ]
aliases = [ "/questions/52238" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [WinPcap sample application crashed](/questions/52238/winpcap-sample-application-crashed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52238-score" class="post-score" title="current number of votes">0</div><span id="post-52238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Got wireshark with wpcap 4.1.3 installed on my win7 (64bit) PC.</p><p>I downloaded wpcap developer pack 4.1.2 (the top one, it claims to be compatible with 4.1.3). I unzipped it and went to directory "WpdPack\Examples-pcap\UDPdump" and made an exe UDPDump.exe using MinGW Gcc (64bit). However, when I ran it, it crashed. GDB showed that it failed at the call to pcap_findalldevs. Any ideas why?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '16, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 May '16, 03:36</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-52238" class="comments-container"></div><div id="comment-tools-52238" class="comment-tools"></div><div class="clear"></div><div id="comment-52238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52244"></span>

<div id="answer-container-52244" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52244-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52244-score" class="post-score" title="current number of votes">0</div><span id="post-52244-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Somewhat off topic for this site, but works for me using VS2013 Community Edition and converting the old solution and project files.</p><p>I'm not sure that compilers other than VS and Cygwin gcc are supported.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '16, 03:12</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 May '16, 03:37</strong> </span></p></div></div><div id="comments-container-52244" class="comments-container"><span id="52275"></span><div id="comment-52275" class="comment"><div id="post-52275-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure Cygwin GCC is supported; unfortunately, <a href="http://stackoverflow.com/questions/36526071/cygwin-and-winpcap-4-1-3-timestamp-microsecond-issue-header-ts-tv-usec-not/36560608#36560608">Cygwin and MSVC differ on what a <code>struct timeval</code> looks like, and WinPcap uses MSVC's definition, causing Bad Things to happen if you try to use WinPcap from Cygwin</a>.</p><p>MinGW might actually be <em>better</em>, as it might not "helpfully" supply UN*X-style definitions of structures that MSVC or various Microsoft SDKs also define in a not-necessarily-compatible fashion. If it <em>does</em> do so, however, it might have the same problem as Cygwin does.</p></div><div id="comment-52275-info" class="comment-info"><span class="comment-age">(06 May '16, 01:03)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="52278"></span><div id="comment-52278" class="comment"><div id="post-52278-score" class="comment-score"></div><div class="comment-text"><p>I only mentioned Cygwin gcc as there is a Makefile for that in the WinPcap Devpack. I haven't tested it though.</p></div><div id="comment-52278-info" class="comment-info"><span class="comment-age">(06 May '16, 02:46)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-52244" class="comment-tools"></div><div class="clear"></div><div id="comment-52244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

