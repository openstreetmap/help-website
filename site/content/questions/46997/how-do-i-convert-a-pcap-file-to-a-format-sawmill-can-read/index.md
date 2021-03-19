+++
type = "question"
title = "How do I convert a pcap file to a format Sawmill can read?"
description = '''hi  i&#x27;ve saved a log in a .pcap file, but i have to work with sawmill universal analisis, and every time i load the file, the program show this message &quot;This log data appears to be in Wireshark, Ethereal, or tcpdump Binary Log Format, which is a binary format not supported directly by Sawmill (Sawmi...'''
date = "2015-10-27T12:59:00Z"
lastmod = "2015-10-27T13:29:00Z"
weight = 46997
keywords = [ "binary", "tcpdump", "log", "sawmill" ]
aliases = [ "/questions/46997" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I convert a pcap file to a format Sawmill can read?](/questions/46997/how-do-i-convert-a-pcap-file-to-a-format-sawmill-can-read)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46997-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi</p><p>i've saved a log in a .pcap file, but i have to work with sawmill universal analisis, and every time i load the file, the program show this message</p><p>"This log data appears to be in Wireshark, Ethereal, or tcpdump Binary Log Format, which is a binary format not supported directly by Sawmill (Sawmill processes text files, and does not support binary formats). You can still analyze this data with Sawmill, but you need to export to a text format first, using the "Export as Plain Text File" dialog box in Wireshark or Ethereal, or using the tcpdump command line tool (tcpdump -r binaryfile.dat -tt &gt; textlog.txt). The resulting file should be autodetected as a tcpdump (-tt) log when you create a profile; choose that format when prompted."</p></div><div id="question-tags" class="tags-container tags">binary tcpdump log sawmill</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '15, 12:59</strong></p><img src="https://secure.gravatar.com/avatar/22190e87da4221754fd631ce34fced2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="buddhaa11&#39;s gravatar image" /><p>buddhaa11<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="buddhaa11 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '15, 13:30</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-46997" class="comments-container"></div><div id="comment-tools-46997" class="comment-tools"></div><div class="clear"></div><div id="comment-46997-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47000"></span>

<div id="answer-container-47000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47000-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're on a UN*X (Linux, *BSD, OS X, Solaris, HP-UX, AIX, etc.), then either your system comes with tcpdump, provides it as an optional install, or has an third-party package available, such as <a href="http://hpux.connect.org.uk/hppd/hpux/Networking/Admin/tcpdump-4.7.4/">the package on the HP-UX Porting and Archive Centre</a>.</p><p>So, on a UN*X, if your capture file is called "foo.pcap", you could do</p><pre><code>tcpdump -r foo.pcap -tt &gt;foo.txt</code></pre><p>and supply "foo.txt" to Sawmill.</p><p>If you're on Windows, <a href="http://www.winpcap.org/windump/default.htm">WinDump</a>, a port of tcpdump to Windows, is available.</p><p>So, if you're on Windows you could download WinDump, make sure your path includes the directory containing WinDump, and do</p><pre><code>windump -r foo.pcap -tt &gt;foo.txt</code></pre><p>from the command prompt.</p><p>See also <a href="http://www.sawmill.net/dcforum/DCForumID5/654.html">this answer to a similar question</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '15, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-47000" class="comments-container"></div><div id="comment-tools-47000" class="comment-tools"></div><div class="clear"></div><div id="comment-47000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

