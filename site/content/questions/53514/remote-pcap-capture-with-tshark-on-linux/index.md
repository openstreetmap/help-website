+++
type = "question"
title = "Remote pcap capture with tshark on Linux"
description = '''I&#x27;m trying to set up tshark to do a remote capture on Linux. I compiled git head tshark against winpcap 4.1.3 (which involved disabling -Werror) and I can now run tshark -i rpcap://10.70.255.193/wifi0. But when I do, it connects to the rpcapd, passes anon auth, sends an rpcap open request and gets a...'''
date = "2016-06-16T19:09:00Z"
lastmod = "2016-07-25T22:12:00Z"
weight = 53514
keywords = [ "winpcap", "tshark", "linux" ]
aliases = [ "/questions/53514" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Remote pcap capture with tshark on Linux](/questions/53514/remote-pcap-capture-with-tshark-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53514-score" class="post-score" title="current number of votes">0</div><span id="post-53514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to set up tshark to do a remote capture on Linux. I compiled git head tshark against winpcap 4.1.3 (which involved disabling -Werror) and I can now run <code>tshark -i rpcap://10.70.255.193/wifi0</code>. But when I do, it connects to the rpcapd, passes anon auth, sends an rpcap open request and gets a reply, but never sends an rpcap start capture command, so I get no packets. Should this work or am I ending up in unsupported territory?</p><p>I'm thinking the problem is somewhere in caputils/ and differences between pcap 0.8 and winpcap, but I can't work out where.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '16, 19:09</strong></p><img src="https://secure.gravatar.com/avatar/7838ca8bcdfdc99e04610c875bf01260?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TRS-80&#39;s gravatar image" /><p><span>TRS-80</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TRS-80 has no accepted answers">0%</span></p></div></div><div id="comments-container-53514" class="comments-container"><span id="53516"></span><div id="comment-53516" class="comment"><div id="post-53516-score" class="comment-score"></div><div class="comment-text"><p>By "on Linux" do you mean "I've compiled the libpcap source from WinPcap on Linux to make a version of libpcap with remote capture support, and compiled TShark with that version of libpcap", so that the host running TShark is a Linux machine, not just the remote machine with the rpcap daemon (which is presumably a Linux, given the interface name <code>wifi0</code>)?</p></div><div id="comment-53516-info" class="comment-info"><span class="comment-age">(16 Jun '16, 23:01)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="53519"></span><div id="comment-53519" class="comment"><div id="post-53519-score" class="comment-score"></div><div class="comment-text"><p>That is precisely correct. The remote machine is an enterprise wireless access point running rpcapd, so I can't just ssh in and run dumpcap.</p></div><div id="comment-53519-info" class="comment-info"><span class="comment-age">(16 Jun '16, 23:09)</span> <span class="comment-user userinfo">TRS-80</span></div></div></div><div id="comment-tools-53514" class="comment-tools"></div><div class="clear"></div><div id="comment-53514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53522"></span>

<div id="answer-container-53522" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53522-score" class="post-score" title="current number of votes">1</div><span id="post-53522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TRS-80 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Then you're definitely in unsupported territory.</p><p>There might be, for example, an issue with the UN*X-socket code in WinPcap's remote-capture code, so that your libpcap-built-with-WinPcap's-remote-capture-code doesn't work right (there are wrappers to cover up the differences between UN*X Berkeley sockets APIs and the Winsock variants of those APIs, and there might be some code rot in the UN*X-socket side).</p><p>The Wireshark code also hasn't been rigorously tested with a pcap on UN*X with <code>pcap_open()</code>, either.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '16, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53522" class="comments-container"><span id="54323"></span><div id="comment-54323" class="comment"><div id="post-54323-score" class="comment-score"></div><div class="comment-text"><p>It looks like it used to work: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2809">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2809</a> but I tried doing that (just adding --with-remote-pcap to configure, the LD_PRELOAD WinPcap's libpcap) and it fails in the same fashion.</p></div><div id="comment-54323-info" class="comment-info"><span class="comment-age">(25 Jul '16, 22:12)</span> <span class="comment-user userinfo">TRS-80</span></div></div></div><div id="comment-tools-53522" class="comment-tools"></div><div class="clear"></div><div id="comment-53522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

