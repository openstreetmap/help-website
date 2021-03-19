+++
type = "question"
title = "problem capturing remotely by running tshark on the remote machine and piping it to Wireshark"
description = '''I am having a few problems running tshark via ssh  SSH host # uname -rpo FreeBSD 10.1-RC1 amd64 # tshark -v TShark 1.12.1 (Git Rev Unknown from unknown) # cat /etc/resolv.conf nameserver 127.0.0.1 options edns0   Client $ tshark -v TShark (Wireshark) 1.99.0-2027-g9c1225f (v1.99.0-rc1-2027-g9c1225f f...'''
date = "2014-10-06T08:45:00Z"
lastmod = "2014-10-06T15:17:00Z"
weight = 36872
keywords = [ "pipe", "tshark", "freebsd", "ssh" ]
aliases = [ "/questions/36872" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [problem capturing remotely by running tshark on the remote machine and piping it to Wireshark](/questions/36872/problem-capturing-remotely-by-running-tshark-on-the-remote-machine-and-piping-it-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36872-score" class="post-score" title="current number of votes">0</div><span id="post-36872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having a few problems running tshark via ssh</p><hr /><h2 id="ssh-host">SSH host</h2><pre><code># uname -rpo
FreeBSD 10.1-RC1 amd64
# tshark -v
TShark 1.12.1 (Git Rev Unknown from unknown)
# cat /etc/resolv.conf
nameserver 127.0.0.1
options edns0</code></pre><hr /><h2 id="client">Client</h2><pre><code>$ tshark -v
TShark (Wireshark) 1.99.0-2027-g9c1225f (v1.99.0-rc1-2027-g9c1225f from unknown)
$ sw_vers
ProductName:    Mac OS X
ProductVersion: 10.10
BuildVersion:   14A379a</code></pre><hr /><h2 id="connect">Connect</h2><pre><code>$ ssh server1 &#39;tshark -f &quot;port not 22&quot; -w -&#39; | wireshark -k -i -
adns: /etc/resolv.conf:2: unknown option `edns0&#39;
Capturing on &#39;re0&#39;
FIX: packet list heading menu sensitivity
FIX: packet list heading menu sensitivity
FIX: packet list heading menu sensitivity</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/2014-10-06.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pipe" rel="tag" title="see questions tagged &#39;pipe&#39;">pipe</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-freebsd" rel="tag" title="see questions tagged &#39;freebsd&#39;">freebsd</span> <span class="post-tag tag-link-ssh" rel="tag" title="see questions tagged &#39;ssh&#39;">ssh</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '14, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/39e96ae1f236a9fac27f1e6c06480c32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="denji&#39;s gravatar image" /><p><span>denji</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="denji has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Oct '14, 16:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-36872" class="comments-container"></div><div id="comment-tools-36872" class="comment-tools"></div><div class="clear"></div><div id="comment-36872-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36876"></span>

<div id="answer-container-36876" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36876-score" class="post-score" title="current number of votes">2</div><span id="post-36876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="denji has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TShark 1.12.x, by default, doesn't write libpcap format with <code>-w</code>, it writes pcap-ng format, and dumpcap (which is what Wireshark uses to do capturing) <em>ONLY</em> reads libpcap format.</p><p><em>If</em> you want to use TShark to capture on the server, you'd need to do <code>tshark -F pcap -f "port not 22" -w -</code>.</p><p>However, in your example, there is no good reason to use TShark; dumpcap would do better, and tcpdump would probably do even better:</p><pre><code>ssh server1 &#39;tcpdump -w - port not 22&#39; | wireshark -k -i -</code></pre><p>Furthermore, as your server is running FreeBSD 10, its tcpdump supports the <code>-U</code> flag, which causes the standard output buffers to be flushed after each packet batch, so the entire packet batch gets written to the standard output at that point rather than part of the last packet being written only when the <em>next</em> packet is seen, so you probably want to do</p><pre><code>ssh server1 &#39;tcpdump -U -w - port not 22&#39; | wireshark -k -i -</code></pre><p>(Note that <code>-U</code> should not be used if the remote machine's tcpdump is earlier than tcpdump 3.8 or if the libpcap is uses is earlier than libpcap 0.8; this means you will probably be able to use it on most machines these days.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Oct '14, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36876" class="comments-container"></div><div id="comment-tools-36876" class="comment-tools"></div><div class="clear"></div><div id="comment-36876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

