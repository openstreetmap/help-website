+++
type = "question"
title = "dumpcap - how to download the sources and build it on Windows"
description = '''Hi, currently i develop a program running on Windows that uses the library WinPcap to sniff some data traffic and write down the captured traffic into files with PCAP format.  My program needs to write down the traffic in the newer PcapNG format. As far as i could see, the WinPcap library doesn&#x27;t su...'''
date = "2013-09-17T03:49:00Z"
lastmod = "2013-09-17T08:38:00Z"
weight = 24804
keywords = [ "windows", "sources", "compile", "dumpcap", "build" ]
aliases = [ "/questions/24804" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [dumpcap - how to download the sources and build it on Windows](/questions/24804/dumpcap-how-to-download-the-sources-and-build-it-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24804-score" class="post-score" title="current number of votes">0</div><span id="post-24804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>currently i develop a program running on Windows that uses the library WinPcap to sniff some data traffic and write down the captured traffic into files with PCAP format. My program needs to write down the traffic in the newer PcapNG format. As far as i could see, the WinPcap library doesn't support the PcapNG format.</p><p>The Wireshark component dumpcap also uses the Winpcap library (on Windows) to capture traffic, and it writes down the capture in PcapNG format, so the sources from dumpcap is what i need to understand and work on (part of it: the pcapio.c file contains the code that writes down the captured packets in PcapNG).</p><p>On the wireshark.org front page the menu item "Develop-&gt;Browse the code" directs me to a list of files, among which dumpcap.vcproj. Downloading and opening it with Visual Studio, i see it requires a number of source files, some of them are in the same list, some not (e.g. capture_loop.c).</p><p>Has anyone lately tried to open, build and run this Visual Studio project? It would be great to run it in debug mode and see it working step by step. Otherwise, how can i gather the sources and build on Windows dumpcap.exe (and only this component)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-sources" rel="tag" title="see questions tagged &#39;sources&#39;">sources</span> <span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '13, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/0c4a0d3634bb05bf810ee1b5fe13ec54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ime-braun&#39;s gravatar image" /><p><span>ime-braun</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ime-braun has no accepted answers">0%</span></p></div></div><div id="comments-container-24804" class="comments-container"></div><div id="comment-tools-24804" class="comment-tools"></div><div class="clear"></div><div id="comment-24804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24805"></span>

<div id="answer-container-24805" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24805-score" class="post-score" title="current number of votes">1</div><span id="post-24805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Visual Studio project files are defunct and should be removed from the repository. Currently the only supported build mechanism on Windows is via command line using nmake.</p><p>You must follow all the steps in the Windows part of the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Developers Guide</a> exactly as written, until you get to step 2.2.10 where you can specify <code>dumpcap.exe</code> instead of <code>all</code> as the build target.</p><p>Once you have built dumpcap.exe, then you can debug it using Visual Studio following <a href="http://msdn.microsoft.com/en-us/library/vstudio/0bxe8ytt.aspx">this</a> guide. You may have to point Visual Studio to the source files the first time.</p><p>Also note that dumpcap (and the rest of the Wireshark suite) is licensed GPL2 or later, please respect that license.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '13, 03:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '13, 06:37</strong> </span></p></div></div><div id="comments-container-24805" class="comments-container"><span id="24813"></span><div id="comment-24813" class="comment"><div id="post-24813-score" class="comment-score"></div><div class="comment-text"><p>What do you mean with "dumpcap... uses libwiretap to actually handle the reading and writing of capture files"?, i can see among the sources of dumpcap the code that does the writing of capture files, it's wholly in pcapio.c (functions libpcap_write_session_header_block and the like)</p></div><div id="comment-24813-info" class="comment-info"><span class="comment-age">(17 Sep '13, 05:38)</span> <span class="comment-user userinfo">ime-braun</span></div></div><span id="24819"></span><div id="comment-24819" class="comment"><div id="post-24819-score" class="comment-score"></div><div class="comment-text"><p>My mistake, although that code is derived from libwiretap. I've updated my answer.</p></div><div id="comment-24819-info" class="comment-info"><span class="comment-age">(17 Sep '13, 06:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-24805" class="comment-tools"></div><div class="clear"></div><div id="comment-24805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24843"></span>

<div id="answer-container-24843" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24843-score" class="post-score" title="current number of votes">0</div><span id="post-24843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to understand the pcap-ng file format, you should reference the <a href="http://www.winpcap.org/ntar/draft/PCAP-DumpFileFormat.html">PCAP Next Generation Dump File Format</a> specification, rather than trying to reverse-engineer the format from dumpcap.</p><p>By the way, unless you plan to GPL your program, you should avoid using any code from dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '13, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24843" class="comments-container"></div><div id="comment-tools-24843" class="comment-tools"></div><div class="clear"></div><div id="comment-24843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

