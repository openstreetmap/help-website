+++
type = "question"
title = "copy/paste?"
description = '''Hi, once I have spotted the relevant data in a capture (actually Referer lines in http GET requests), how could I get them into a file? When I click http, and then the line, it gets highlighted in the hexdump. Idid not find a way how I could copy that line and paste it into a text document'''
date = "2012-03-16T22:49:00Z"
lastmod = "2012-03-18T22:06:00Z"
weight = 9592
keywords = [ "copy-paste" ]
aliases = [ "/questions/9592" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [copy/paste?](/questions/9592/copypaste)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9592-score" class="post-score" title="current number of votes">0</div><span id="post-9592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>once I have spotted the relevant data in a capture (actually Referer lines in http GET requests), how could I get them into a file? When I click http, and then the line, it gets highlighted in the hexdump. Idid not find a way how I could copy that line and paste it into a text document</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-copy-paste" rel="tag" title="see questions tagged &#39;copy-paste&#39;">copy-paste</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '12, 22:49</strong></p><img src="https://secure.gravatar.com/avatar/2a0d9f17afa936fe9558e9e32ba91b92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wurzelsepp&#39;s gravatar image" /><p><span>Wurzelsepp</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wurzelsepp has no accepted answers">0%</span></p></div></div><div id="comments-container-9592" class="comments-container"></div><div id="comment-tools-9592" class="comment-tools"></div><div class="clear"></div><div id="comment-9592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9595"></span>

<div id="answer-container-9595" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9595-score" class="post-score" title="current number of votes">2</div><span id="post-9595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Find the Referer line in the Packet Details pane, not the Packet Bytes (hexdump) pane. Highlight the line, right-click, and select <em>Copy &gt; Description</em> or <em>Copy &gt; Value</em>, then paste it into your text document.</p><p>Copy &gt; Description will give you something like: <em>Referer: <a href="http://ask.wireshark.org/questions/\r\n">http://ask.wireshark.org/questions/\r\n</a></em></p><p>Copy &gt; Value will give you something like: <em><a href="http://ask.wireshark.org/questions/">http://ask.wireshark.org/questions/</a></em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '12, 23:41</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9595" class="comments-container"><span id="9603"></span><div id="comment-9603" class="comment"><div id="post-9603-score" class="comment-score"></div><div class="comment-text"><p>it seems I have no luck on that ... using a linux system with 2.6.27 kernel I have tried with both targets that read primary selection and targets that handle clipboard</p></div><div id="comment-9603-info" class="comment-info"><span class="comment-age">(17 Mar '12, 04:14)</span> <span class="comment-user userinfo">Wurzelsepp</span></div></div><span id="9611"></span><div id="comment-9611" class="comment"><div id="post-9611-score" class="comment-score"></div><div class="comment-text"><p>(The kernel is not involved with copy-and-paste beyond implementing interprocess communication, so the kernel version doesn't matter here.)</p><p>Wireshark built from a reasonably recent checkout from the SVN trunk, on Ubuntu 10.10, using the GLib and GTK+ installed as part of the system (GTK+ 2.22.0 and GLib 2.26.1) is able to copy with Copy -&gt; Description and Copy -&gt; Value and I can paste what's copied into a gedit document.</p><p>Wireshark doesn't, as far as I know, explicitly support setting the primary selection, so paste-current-selection may not work, but copying to the clipboard appears to work.</p></div><div id="comment-9611-info" class="comment-info"><span class="comment-age">(18 Mar '12, 12:37)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="9612"></span><div id="comment-9612" class="comment"><div id="post-9612-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>thanks for responding. In the end I found that export as text and grepping out the relevant lines did the job very vell</p><p>btw: this is wireshark as deployed on Suse 11.4: Compiled with GTK+ 2.14.4, with GLib 2.18.2, with libpcap 0.9-PRE-CVS, with libz 1.2.3, without POSIX capabilities, with libpcre 7.8, without SMI, with ADNS, without Lua, without GnuTLS, without Gcrypt, with MIT Kerberos, without PortAudio, without AirPcap.</p><p>Running on Linux 2.6.27.7-9-default, with libpcap version 0.9-PRE-CVS.</p></div><div id="comment-9612-info" class="comment-info"><span class="comment-age">(18 Mar '12, 22:06)</span> <span class="comment-user userinfo">Wurzelsepp</span></div></div></div><div id="comment-tools-9595" class="comment-tools"></div><div class="clear"></div><div id="comment-9595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

