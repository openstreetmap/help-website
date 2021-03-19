+++
type = "question"
title = "What is the latest Wireshark for 2.6.18-348.12.1.el5 (Red Hat RHEL5)"
description = '''Hi Everyone, What is the latest Wireshark version for 2.6.18-348.12.1.el5'''
date = "2013-08-15T16:23:00Z"
lastmod = "2013-08-15T17:09:00Z"
weight = 23811
keywords = [ "rhel5", "redhat" ]
aliases = [ "/questions/23811" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What is the latest Wireshark for 2.6.18-348.12.1.el5 (Red Hat RHEL5)](/questions/23811/what-is-the-latest-wireshark-for-2618-348121el5-red-hat-rhel5)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23811-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone, What is the latest Wireshark version for 2.6.18-348.12.1.el5</p></div><div id="question-tags" class="tags-container tags">rhel5 redhat</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Aug '13, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/1b019c4fcd269a2a214adfb53655c77d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ESSTEAM&#39;s gravatar image" /><p>ESSTEAM<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ESSTEAM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Aug '13, 17:11</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-23811" class="comments-container"><span id="23812"></span><div id="comment-23812" class="comment"><div id="post-23812-score" class="comment-score"></div><div class="comment-text"><p>This is my current version. TShark 1.0.15</p><p>Compiled with GLib 2.12.3, with libpcap 0.9.4, with libz 1.2.3, without POSIX capabilities, with libpcre 6.6, with SMI 0.4.5, without ADNS, without Lua, with GnuTLS 1.4.1, with Gcrypt 1.4.4, with MIT Kerberos.</p><p>Running on Linux 2.6.18-348.12.1.el5, with libpcap version 0.9.4.</p><p>Built using gcc 4.1.2 20080704 (Red Hat 4.1.2-54).</p></div><div id="comment-23812-info" class="comment-info"><span class="comment-age">(15 Aug '13, 16:24)</span> ESSTEAM</div></div></div><div id="comment-tools-23811" class="comment-tools"></div><div class="clear"></div><div id="comment-23811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23814"></span>

<div id="answer-container-23814" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23814-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to their FTP server, it's <strong>wireshark-1.0.15-5.el5.src.rpm</strong></p><blockquote><p><a href="ftp://ftp.redhat.com/pub/redhat/linux/enterprise/5Server/en/os/SRPMS/">ftp://ftp.redhat.com/pub/redhat/linux/enterprise/5Server/en/os/SRPMS/</a></p></blockquote><p>If you need a newer Wireshark version, you can build it yourself.</p><blockquote><p><a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBuildFirstTime.html#id36130022">http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBuildFirstTime.html#id36130022</a><br />
</p></blockquote><p>Or upgrade to RHEL6. However, the latest Wireshark there is only 1.2.15.</p><p>So, if you need a current release of Wireshark and you don't have to run it on RHEL5, I suggest, you just capture the data on RHEL with tcpdump (options -w and -s0) and then use another machine (Windows, Ubuntu, MacOS, etc.) to analyze the capture file with the latest available Wireshark release.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Aug '13, 17:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23814" class="comments-container"></div><div id="comment-tools-23814" class="comment-tools"></div><div class="clear"></div><div id="comment-23814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

