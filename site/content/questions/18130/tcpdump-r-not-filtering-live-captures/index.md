+++
type = "question"
title = "tcpdump -R not filtering live captures"
description = '''The man page for tshark implies -R will work on live captures but my output files are not filtered. tshark -b filesize:50000 -R &#x27;(mgcp||sip||sdp||rtpevent)&#x27; -i any -w tshark.cap  tshark is not filtering the dumpcap data at all. I would like to filter the data to limit the size of the pcap files. Tha...'''
date = "2013-01-30T13:56:00Z"
lastmod = "2013-01-31T07:21:00Z"
weight = 18130
keywords = [ "capture", "live", "tcpdump", "-r" ]
aliases = [ "/questions/18130" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [tcpdump -R not filtering live captures](/questions/18130/tcpdump-r-not-filtering-live-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18130-score" class="post-score" title="current number of votes">0</div><span id="post-18130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The man page for tshark implies -R will work on live captures but my output files are not filtered.</p><p>tshark -b filesize:50000 -R '(mgcp||sip||sdp||rtpevent)' -i any -w tshark.cap</p><p>tshark is not filtering the dumpcap data at all. I would like to filter the data to limit the size of the pcap files.</p><p>Thanks</p><p>CentOS 2.6.18-238.9.1.el5 #1 SMP Tue Apr 12 18:10:13 EDT 2011 x86_64 x86_64 x86_64 GNU/Linux</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-live" rel="tag" title="see questions tagged &#39;live&#39;">live</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link--r" rel="tag" title="see questions tagged &#39;-r&#39;">-r</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '13, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/d1a591769b2fb0dfcfe5c850fb4dc959?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GnuBomb&#39;s gravatar image" /><p><span>GnuBomb</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GnuBomb has no accepted answers">0%</span></p></div></div><div id="comments-container-18130" class="comments-container"></div><div id="comment-tools-18130" class="comment-tools"></div><div class="clear"></div><div id="comment-18130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18131"></span>

<div id="answer-container-18131" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18131-score" class="post-score" title="current number of votes">3</div><span id="post-18131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to apply <strong>capture filters</strong> not <strong>display filters</strong>. "-R" is used for display filters, so you need to use "-f" instead. Unfortunately, the filter syntax for capture filters is quite different from the syntax of display filters, so you need to adjust it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '13, 14:04</strong> </span></p></div></div><div id="comments-container-18131" class="comments-container"><span id="18133"></span><div id="comment-18133" class="comment"><div id="post-18133-score" class="comment-score"></div><div class="comment-text"><p>This is from the man page (it states read filters can be used during live capture):</p><p>Capture filters are supported only when doing a live capture; read filters are supported when doing a live capture and when reading a capture file, but require TShark to do more work when filtering, so you might be more likely to lose packets under heavy load if you're using a read filter</p></div><div id="comment-18133-info" class="comment-info"><span class="comment-age">(30 Jan '13, 14:14)</span> <span class="comment-user userinfo">GnuBomb</span></div></div><span id="18134"></span><div id="comment-18134" class="comment"><div id="post-18134-score" class="comment-score"></div><div class="comment-text"><p>Yes, you can use read filters, but they will limit what tshark <strong>shows</strong> on the screen, not what goes into the file - if you only use read filters, <strong>all</strong> packets will still be written to file. They will just not be shown while filtering. To limit packets in the file, you need to apply capture filters.</p></div><div id="comment-18134-info" class="comment-info"><span class="comment-age">(30 Jan '13, 14:21)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="18135"></span><div id="comment-18135" class="comment"><div id="post-18135-score" class="comment-score"></div><div class="comment-text"><p>Okay, thanks for the reply.</p></div><div id="comment-18135-info" class="comment-info"><span class="comment-age">(30 Jan '13, 14:33)</span> <span class="comment-user userinfo">GnuBomb</span></div></div></div><div id="comment-tools-18131" class="comment-tools"></div><div class="clear"></div><div id="comment-18131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18181"></span>

<div id="answer-container-18181" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18181-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18181-score" class="post-score" title="current number of votes">1</div><span id="post-18181-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2234">bug</a> open which tracks this... deficiency; in fact the bug has been listed in the KnownProblems section of the <a href="https://www.wireshark.org/docs/relnotes/wireshark-1.8.5.html">release notes</a> for each release for many years now.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '13, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-18181" class="comments-container"><span id="18183"></span><div id="comment-18183" class="comment"><div id="post-18183-score" class="comment-score"></div><div class="comment-text"><p>And see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2234#c22">comment 22</a> in the bug that shows how you can filter via a pipe with some restrictions.</p></div><div id="comment-18183-info" class="comment-info"><span class="comment-age">(31 Jan '13, 07:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-18181" class="comment-tools"></div><div class="clear"></div><div id="comment-18181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

