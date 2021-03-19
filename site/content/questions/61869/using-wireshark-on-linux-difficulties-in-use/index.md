+++
type = "question"
title = "Using wireshark on linux - Difficulties in use"
description = '''Hi, I have problems using wireshark on linux - I am using wireshark verision 1.8.10 on linux, and version 2.2.6 on windows. I imported same packet on windows and linux - while wireshark on windows was able to analyze the whole packets, linux couldnt analyze geneve (Generic Network Virtualization Enc...'''
date = "2017-06-08T08:47:00Z"
lastmod = "2017-06-17T07:34:00Z"
weight = 61869
keywords = [ "unix", "tshark" ]
aliases = [ "/questions/61869" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using wireshark on linux - Difficulties in use](/questions/61869/using-wireshark-on-linux-difficulties-in-use)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61869-score" class="post-score" title="current number of votes">0</div><span id="post-61869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have problems using wireshark on linux - I am using wireshark verision 1.8.10 on linux, and version 2.2.6 on windows.</p><p>I imported same packet on windows and linux - while wireshark on windows was able to analyze the whole packets, linux couldnt analyze geneve (Generic Network Virtualization Encapsulation) and gre (Generic Routing Encapsulation) packets protocols.</p><p>What is the solution for my problem? Do I need to install an updated version on my linux server?</p><p>Thanks, Aya</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unix" rel="tag" title="see questions tagged &#39;unix&#39;">unix</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '17, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/3cca087c83f55798a15e19db6111ce67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aya%20dagan&#39;s gravatar image" /><p><span>aya dagan</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aya dagan has no accepted answers">0%</span></p></div></div><div id="comments-container-61869" class="comments-container"></div><div id="comment-tools-61869" class="comment-tools"></div><div class="clear"></div><div id="comment-61869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61870"></span>

<div id="answer-container-61870" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61870-score" class="post-score" title="current number of votes">2</div><span id="post-61870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That is very likely, yes. I haven't checked, but at least Geneve is a pretty new tunneling protocol that 1.8 probably doesn't know about. I can recommend always staying up to date with the Wireshark versions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '17, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61870" class="comments-container"><span id="62061"></span><div id="comment-62061" class="comment"><div id="post-62061-score" class="comment-score"></div><div class="comment-text"><p>Some versions of Linux come with really old versions of Wireshark, and people tend to use what the distribution vendor supplies. Windows and macOS, for example, <em>don't</em> provide Windows, so people have to get it themselves, and end up getting newer versions.</p><p>I'll bet the server is running something such as RHEL 6 or CentOS 6, which I think supply Wireshark 1.8. It would be really nice if there were <em>some</em> way of getting up-to-date Wireshark RPMs for RHEL/CentOS 6; does anybody know of a source of that?</p></div><div id="comment-62061-info" class="comment-info"><span class="comment-age">(16 Jun '17, 12:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="62070"></span><div id="comment-62070" class="comment"><div id="post-62070-score" class="comment-score"></div><div class="comment-text"><p><a href="http://rpm.pbone.net/">http://rpm.pbone.net/</a> has <em>slightly</em> newer RHEL6 rpms of Wireshark 1.10.0. I'm by no means a Redhat packager, but I've built RHEL6 rpms for Wireshark 2.2.7 that I could possibly post somewhere for anyone who might be interested?</p><p><code> TShark (Wireshark) 2.2.7 (wireshark-2.2.7)</code></p><p><code></code></p><p><code>Copyright 1998-2017 Gerald Combs [email protected] and contributors. License GPLv2+: GNU GPL version 2 or later http://www.gnu.org/licenses/old-licenses/gpl-2.0.html This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</code></p><code></code><p>Compiled (64-bit) with libpcap, with POSIX capabilities (Linux), with libnl 1, with GLib 2.26.1, with zlib 1.2.3, without SMI, without c-ares, with Lua 5.1.4, without GnuTLS, with Gcrypt 1.4.5, with MIT Kerberos, without GeoIP.</p><p>Running on Linux 2.6.32-431.el6.x86_64, with locale en_US.UTF-8, with libpcap version 1.8.1, with Gcrypt 1.4.5, with zlib 1.2.3. Intel(R) Xeon(R) CPU E5405 @ 2.00GHz</p></code><p><code>Built using gcc 4.4.7 20120313 (Red Hat 4.4.7-4).</code></p></div><div id="comment-62070-info" class="comment-info"><span class="comment-age">(17 Jun '17, 07:34)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-61870" class="comment-tools"></div><div class="clear"></div><div id="comment-61870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

