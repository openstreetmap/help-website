+++
type = "question"
title = "Filtering by mac is not working."
description = '''Hello everybody! I&#x27;m trying to filter a pcap file using the following command and filter: tshark -q -r capture.pcap -z io,stat,0,eth.addr==aa:bb:cc:dd:ee:ff  But I&#x27;m getting this error: tshark: invalid &quot;-z io,stat,&amp;lt;interval&amp;gt;[,&amp;lt;filter&amp;gt;][,&amp;lt;filter&amp;gt;]...&quot; argument  Does anyone know what...'''
date = "2016-12-05T07:17:00Z"
lastmod = "2016-12-06T02:37:00Z"
weight = 57865
keywords = [ "tshark", "display-filter" ]
aliases = [ "/questions/57865" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering by mac is not working.](/questions/57865/filtering-by-mac-is-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57865-score" class="post-score" title="current number of votes">0</div><span id="post-57865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everybody!</p><p>I'm trying to filter a pcap file using the following command and filter:</p><pre><code>tshark -q -r capture.pcap -z io,stat,0,eth.addr==aa:bb:cc:dd:ee:ff</code></pre><p>But I'm getting this error:</p><pre><code>tshark: invalid &quot;-z io,stat,&lt;interval&gt;[,&lt;filter&gt;][,&lt;filter&gt;]...&quot; argument</code></pre><p>Does anyone know what I'm doing wrong? Whether I use an ip filter (e.g. ip.addr==10.10.10.10) the result is ok.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '16, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/46d583abdee735d71a4f23dd40c01bef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohannesFerreira&#39;s gravatar image" /><p><span>JohannesFerr...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohannesFerreira has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Dec '16, 11:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-57865" class="comments-container"><span id="57871"></span><div id="comment-57871" class="comment"><div id="post-57871-score" class="comment-score"></div><div class="comment-text"><p>Works for me, what version of tshark and what shell are you running this in?</p></div><div id="comment-57871-info" class="comment-info"><span class="comment-age">(05 Dec '16, 09:05)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57872"></span><div id="comment-57872" class="comment"><div id="post-57872-score" class="comment-score"></div><div class="comment-text"><p>Hi grahamb, thanks for your quickly answer. I'm using terminator as shell and the version is "TShark (Wireshark) 2.2.2". I tried in a different PC and it worked, I'm wondering if it could be some library version. Any idea?</p><p>TShark (Wireshark) 2.2.2 (Git Rev Unknown from unknown)</p><p>Copyright 1998-2016 Gerald Combs <span><span class="__cf_email__" data-cfemail="f4939186959890b4839d8691879c95869fda9b8693">[email protected]</span></span> and contributors. License GPLv2+: GNU GPL version 2 or later <a href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.html">http://www.gnu.org/licenses/old-licenses/gpl-2.0.html</a> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with libpcap, with POSIX capabilities (Linux), with libnl 3, with GLib 2.48.1, with zlib 1.2.8, with SMI 0.4.8, with c-ares 1.10.0, with Lua 5.2.4, with GnuTLS 3.4.10, with Gcrypt 1.6.5, with MIT Kerberos, with GeoIP, with nghttp2 1.7.1.</p><p>Running on Linux 4.4.0-51-generic, with locale LC_CTYPE=pt_BR.UTF-8, LC_NUMERIC=pt_BR.UTF-8, LC_TIME=pt_BR.UTF-8, LC_COLLATE=en_US.UTF-8, LC_MONETARY=pt_BR.UTF-8, LC_MESSAGES=en_US.UTF-8, LC_PAPER=pt_BR.UTF-8, LC_NAME=pt_BR.UTF-8, LC_ADDRESS=pt_BR.UTF-8, LC_TELEPHONE=pt_BR.UTF-8, LC_MEASUREMENT=pt_BR.UTF-8, LC_IDENTIFICATION=pt_BR.UTF-8, with libpcap version 1.7.4, with GnuTLS 3.4.10, with Gcrypt 1.6.5, with zlib 1.2.8.</p><p>Built using gcc 5.4.0 20160609.</p></div><div id="comment-57872-info" class="comment-info"><span class="comment-age">(05 Dec '16, 10:21)</span> <span class="comment-user userinfo">JohannesFerr...</span></div></div><span id="57874"></span><div id="comment-57874" class="comment"><div id="post-57874-score" class="comment-score"></div><div class="comment-text"><p>Did you use the same shell on the other PC? I'm clutching at straws that it's an argument escaping error.</p></div><div id="comment-57874-info" class="comment-info"><span class="comment-age">(05 Dec '16, 11:03)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57875"></span><div id="comment-57875" class="comment"><div id="post-57875-score" class="comment-score"></div><div class="comment-text"><p>Yes, I used and I also tried a different shell, same thing.</p></div><div id="comment-57875-info" class="comment-info"><span class="comment-age">(05 Dec '16, 11:26)</span> <span class="comment-user userinfo">JohannesFerr...</span></div></div><span id="57876"></span><div id="comment-57876" class="comment"><div id="post-57876-score" class="comment-score"></div><div class="comment-text"><p>Do you know what library is responsible to parse the eth parameters?</p></div><div id="comment-57876-info" class="comment-info"><span class="comment-age">(05 Dec '16, 11:27)</span> <span class="comment-user userinfo">JohannesFerr...</span></div></div></div><div id="comment-tools-57865" class="comment-tools"></div><div class="clear"></div><div id="comment-57865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57892"></span>

<div id="answer-container-57892" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57892-score" class="post-score" title="current number of votes">0</div><span id="post-57892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I tried in a different PC and it works ok. Thanks for your time grahamb!!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '16, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/46d583abdee735d71a4f23dd40c01bef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohannesFerreira&#39;s gravatar image" /><p><span>JohannesFerr...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohannesFerreira has no accepted answers">0%</span></p></div></div><div id="comments-container-57892" class="comments-container"></div><div id="comment-tools-57892" class="comment-tools"></div><div class="clear"></div><div id="comment-57892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

