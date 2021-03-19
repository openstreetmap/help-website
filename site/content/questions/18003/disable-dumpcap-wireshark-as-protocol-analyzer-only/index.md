+++
type = "question"
title = "Disable dumpcap / WireShark as Protocol Analyzer only"
description = '''Hi, Is there any way to use WireShark as a Protocol Analyzer only and disable the hability to &quot;sniffing&quot; the network? My idea is to relase the software for some engeneer people here but I don&#x27;t want then to grab new data, only to analyze &quot;already captured data&quot; for Wireshark. Is that possible? '''
date = "2013-01-28T08:39:00Z"
lastmod = "2013-01-28T10:45:00Z"
weight = 18003
keywords = [ "winpcap", "sniffer", "disable", "dumpcap", "analyzer" ]
aliases = [ "/questions/18003" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Disable dumpcap / WireShark as Protocol Analyzer only](/questions/18003/disable-dumpcap-wireshark-as-protocol-analyzer-only)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18003-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Is there any way to use WireShark as a Protocol Analyzer only and disable the hability to "sniffing" the network?</p><p>My idea is to relase the software for some engeneer people here but I don't want then to grab new data, only to analyze "already captured data" for Wireshark.</p><p>Is that possible?</p></div><div id="question-tags" class="tags-container tags">winpcap sniffer disable dumpcap analyzer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '13, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/48bee93a50f9f34c231c278a91c03600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bonacordi&#39;s gravatar image" /><p>Bonacordi<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bonacordi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jan '13, 10:07</p></div></div><div id="comments-container-18003" class="comments-container"></div><div id="comment-tools-18003" class="comment-tools"></div><div class="clear"></div><div id="comment-18003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18004"></span>

<div id="answer-container-18004" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18004-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Don't install the actual traffic capture software, e.g. WinPCap for Windows. For other platforms you could either remove the capture software, e.g. lipcap on linux, or restrict their access to it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '13, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-18004" class="comments-container"><span id="18007"></span><div id="comment-18007" class="comment"><div id="post-18007-score" class="comment-score"></div><div class="comment-text"><p>Hey Grahamb, thanks for your answer... just wondering how I will be able to do that since I found in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html">Install Guide - Cap 2.8 - Session 2.8.1.3. "Install WinPcap?" page</a> that Wireshark installer contains the latest released WinPcap installer.</p><p>I couldn't test the install since I'm waiting a lab machine in order to test it in my company but I would like to ask, is this WinPcap like a checkbox during the install process?</p></div><div id="comment-18007-info" class="comment-info"><span class="comment-age">(28 Jan '13, 10:05)</span> Bonacordi</div></div></div><div id="comment-tools-18004" class="comment-tools"></div><div class="clear"></div><div id="comment-18004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18009"></span>

<div id="answer-container-18009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18009-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Based on your comments to <a href="http://ask.wireshark.org/users/1225/grahamb">grahamb</a> regarding <a href="http://www.winpcap.org/">WinPcap</a>, it looks like you're looking for a solution on the Windows platform. In that case, <em>in theory</em> you could compile and release your own installer without capture support, paying special attention to the following paragraph from <code>config.nmake</code>:</p><pre><code>#
# Optional: WinPcap developer&#39;s pack to capture network traffic.
#
# If you have the WinPcap developer&#39;s pack (at least version 3.0),
# set this to the directory in which the WinPcap developer&#39;s pack resides.
#
# If you don&#39;t have the WPdpack, comment this line out, so that
# PCAP_DIR isn&#39;t defined.
#
#PCAP_DIR=$(WIRESHARK_LIB_DIR)\WPdpack</code></pre><p>Unfortunately, just commenting out <code>PCAP_DIR</code> doesn't actually work. And when I renamed the <code>WpdPack</code> directory, compilation failed as follows:</p><pre><code>capture_if_details_dlg_win32.c
capture_if_details_dlg_win32.c(108) : fatal error C1083: Cannot open include file: &#39;Packet32.h&#39;: No such file or directory</code></pre><p>So this looks like a <a href="https://bugs.wireshark.org/bugzilla/">bug</a> that needs to be fixed first before this could be an option for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '13, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-18009" class="comments-container"></div><div id="comment-tools-18009" class="comment-tools"></div><div class="clear"></div><div id="comment-18009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

