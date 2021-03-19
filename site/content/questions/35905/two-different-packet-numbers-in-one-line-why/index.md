+++
type = "question"
title = "Two different packet numbers in one line. Why?"
description = '''Can anybody explain why do tshark shows two different packet numbers in one line? root@linaro-nano:~# tshark -a duration:10 -ni eth0 -f &quot;host not 192.168.88.28&quot; tshark: Lua: Error during loading:  [string &quot;/usr/share/wireshark/init.lua&quot;]:46: dofile has been disabled due to running Wireshark as super...'''
date = "2014-09-01T04:22:00Z"
lastmod = "2014-09-12T05:01:00Z"
weight = 35905
keywords = [ "tshark" ]
aliases = [ "/questions/35905" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Two different packet numbers in one line. Why?](/questions/35905/two-different-packet-numbers-in-one-line-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35905-score" class="post-score" title="current number of votes">0</div><span id="post-35905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can anybody explain why do tshark shows two different packet numbers in one line?</p><p><code>[email protected]:~# tshark -a duration:10 -ni eth0 -f "host not 192.168.88.28" tshark: Lua: Error during loading:  [string "/usr/share/wireshark/init.lua"]:46: dofile has been disabled due to running Wireshark as superuser. See http://wiki.wireshark.org/CaptureSetup/CapturePrivileges for help in running Wireshark as an unprivileged user. Running as user "root" and group "root". This could be dangerous. Capturing on 'eth0'   1   0.000000 192.168.8.153 -&gt; 188.226.182.180 ICMP 98 Echo (ping) request  id=0x2b13, seq=2/512, ttl=64   2   0.041023 188.226.182.180 -&gt; 192.168.8.153 ICMP 98 Echo (ping) reply    id=0x2b13, seq=2/512, ttl=53 (request in 1) 2   3   2.002165 192.168.8.153 -&gt; 188.226.182.180 ICMP 98 Echo (ping) request  id=0x2b13, seq=3/768, ttl=64   4   2.043022 188.226.182.180 -&gt; 192.168.8.153 ICMP 98 Echo (ping) reply    id=0x2b13, seq=3/768, ttl=53 (request in 3) 4   5   4.004166 192.168.8.153 -&gt; 188.226.182.180 ICMP 98 Echo (ping) request  id=0x2b13, seq=4/1024, ttl=64</code></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '14, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/4bb5f53b35c799847b0c7415f270ff02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="insekt&#39;s gravatar image" /><p><span>insekt</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="insekt has no accepted answers">0%</span></p></div></div><div id="comments-container-35905" class="comments-container"><span id="35906"></span><div id="comment-35906" class="comment"><div id="post-35906-score" class="comment-score"></div><div class="comment-text"><p><code> [email protected]:~# tshark -v tshark: Lua: Error during loading:  [string "/usr/share/wireshark/init.lua"]:46: dofile has been disabled due to running Wireshark as superuser. See http://wiki.wireshark.org/CaptureSetup/CapturePrivileges for help in running Wireshark as an unprivileged user. TShark 1.10.6 (v1.10.6 from master-1.10)</code></p><p><code></code></p><p><code>Copyright 1998-2014 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</code></p><code></code><p>Compiled (32-bit) with GLib 2.39.91, with libpcap, with libz 1.2.8, with POSIX capabilities (Linux), without libnl, with SMI 0.4.8, with c-ares 1.10.0, with Lua 5.2, without Python, with GnuTLS 2.12.23, with Gcrypt 1.5.3, with MIT Kerberos, with GeoIP.</p><p>Running on Linux 3.13.0+, with locale C.UTF-8, with libpcap version 1.5.3, with libz 1.2.8.</p></code><p><code>Built using gcc 4.8.2.</code></p></div><div id="comment-35906-info" class="comment-info"><span class="comment-age">(01 Sep '14, 04:23)</span> <span class="comment-user userinfo">insekt</span></div></div><span id="35911"></span><div id="comment-35911" class="comment"><div id="post-35911-score" class="comment-score"></div><div class="comment-text"><p>It seems it's a bug. The second number is a overall counter of captured packets.</p></div><div id="comment-35911-info" class="comment-info"><span class="comment-age">(01 Sep '14, 07:40)</span> <span class="comment-user userinfo">insekt</span></div></div></div><div id="comment-tools-35905" class="comment-tools"></div><div class="clear"></div><div id="comment-35905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35918"></span>

<div id="answer-container-35918" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35918-score" class="post-score" title="current number of votes">0</div><span id="post-35918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is a bug that's fixed in 1.12 but not in 1.10; for some reason I didn't backport the fix, perhaps because I thought it might not work in the older version.</p><p>It's actually a straightforward fix, so I backported it. The next 1.10 release, 1.10.10, should have the fix whenever it comes out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Sep '14, 15:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-35918" class="comments-container"><span id="36259"></span><div id="comment-36259" class="comment"><div id="post-36259-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to install 1.12 on ubuntu 14.04 armhf? This bug is very annoying me and force me to invent strange workarounds in my scripts, I've started to use tshark on a daily basis. Or at least push the next 1.10 release.</p></div><div id="comment-36259-info" class="comment-info"><span class="comment-age">(12 Sep '14, 04:47)</span> <span class="comment-user userinfo">insekt</span></div></div><span id="36260"></span><div id="comment-36260" class="comment"><div id="post-36260-score" class="comment-score"></div><div class="comment-text"><p>Using a a distro release (e.g. Ubuntu) of Wireshark means you are generally going to be running behind the current Wireshark releases.</p><p>To get up to date on Ubuntu you'll likely have to build it yourself, the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a> gives full details for doing that.</p></div><div id="comment-36260-info" class="comment-info"><span class="comment-age">(12 Sep '14, 04:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="36261"></span><div id="comment-36261" class="comment"><div id="post-36261-score" class="comment-score"></div><div class="comment-text"><p>Even if 1.10.10 is pushed Ubuntu 14.04 LTS will probably not pick it up as they only do sequrity fixes :-(</p><p>You could build 1.12 or the development version from source.</p></div><div id="comment-36261-info" class="comment-info"><span class="comment-age">(12 Sep '14, 05:01)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-35918" class="comment-tools"></div><div class="clear"></div><div id="comment-35918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

