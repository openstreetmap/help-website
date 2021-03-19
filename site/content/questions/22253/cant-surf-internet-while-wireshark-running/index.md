+++
type = "question"
title = "Can&#x27;t surf internet while wireshark running"
description = '''I compiled Wireshark from source code on my debian 7 a few days ago and installed it. I can&#x27;t surf internet while Wireshark is running. Even pinging the gateway returns a &quot;Destination unreachable&quot; error. But I don&#x27;t have this issue on Windows. I tried to change capture modes and this didn&#x27;t work eit...'''
date = "2013-06-23T09:24:00Z"
lastmod = "2013-06-23T10:20:00Z"
weight = 22253
keywords = [ "compile", "debian", "wireshark" ]
aliases = [ "/questions/22253" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't surf internet while wireshark running](/questions/22253/cant-surf-internet-while-wireshark-running)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22253-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I compiled Wireshark from source code on my debian 7 a few days ago and installed it. I can't surf internet while Wireshark is running. Even pinging the gateway returns a "Destination unreachable" error. But I don't have this issue on Windows.</p><p>I tried to change capture modes and this didn't work either. Any idea how to solve this problem? Thanks in advance.</p><p>The following is what wireshark --version returns.</p><p>Version 1.10.0 (SVN Rev Unknown from unknown)</p><p>Copyright 1998-2013 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.24.10, with Cairo 1.12.2, with Pango 1.34.1, with GLib 2.34.1, with libpcap, with libz 1.2.7, without POSIX capabilities, without libnl, without SMI, without c-ares, without ADNS, without Lua, without Python, without GnuTLS, without Gcrypt, without Kerberos, without GeoIP, without PortAudio, with AirPcap.</p><p>Running on Linux 3.2.0-4-amd64, with locale en_US.UTF-8, with libpcap version 1.4.0, with libz 1.2.7, without AirPcap. Intel(R) Core(TM) i7-3630QM CPU @ 2.40GHz</p><p>Built using gcc 4.7.2.</p><p>Wireshark is Open Source Software released under the GNU General Public License.</p><p>Check the man page and <a href="http://www.wireshark.org">http://www.wireshark.org</a> for more information.</p></div><div id="question-tags" class="tags-container tags">compile debian wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '13, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/0ad0655f8a00c1df05ecb698877b673b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maoxin&#39;s gravatar image" /><p>maoxin<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maoxin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Jun '13, 19:45</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-22253" class="comments-container"></div><div id="comment-tools-22253" class="comment-tools"></div><div class="clear"></div><div id="comment-22253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22256"></span>

<div id="answer-container-22256" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22256-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks more like a bug report to take over to <a href="http://bugs.wireshark.org"></a><a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a> to me.</p><p>Instead of quoting version information you should give more details about what your network setup is like. Are you using a cable ethernet connection or Wifi? What kind of network cards do you use? I guess you're running a wireless connector, in which case capturing will most likely set your card to "receive only" - which will then lead to no connectivity. Windows will not allow you to set monitor mode which may be the reason why you can still use the card with that OS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '13, 10:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-22256" class="comments-container"><span id="22258"></span><div id="comment-22258" class="comment"><div id="post-22258-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your reply.I use wifi.My network cards is "Intel Corporation Centrino Wireless-N 2200".</p></div><div id="comment-22258-info" class="comment-info"><span class="comment-age">(23 Jun '13, 16:57)</span> maoxin</div></div><span id="22271"></span><div id="comment-22271" class="comment"><div id="post-22271-score" class="comment-score">1</div><div class="comment-text"><p>That's what I thought. You need to use a second card to keep Wireless connectivity on Linux while running monitor mode on the first one, because it will be put into receive-only mode.</p></div><div id="comment-22271-info" class="comment-info"><span class="comment-age">(24 Jun '13, 02:55)</span> Jasper ♦♦</div></div><span id="22306"></span><div id="comment-22306" class="comment"><div id="post-22306-score" class="comment-score"></div><div class="comment-text"><p>well,I still can't surf internet even if I change capture mode to promiscuous mode.Last night,I tried to install a previous version (1.8),this one works pretty well.</p></div><div id="comment-22306-info" class="comment-info"><span class="comment-age">(25 Jun '13, 00:59)</span> maoxin</div></div><span id="22327"></span><div id="comment-22327" class="comment"><div id="post-22327-score" class="comment-score"></div><div class="comment-text"><p>There is no "promiscuouos" mode for wireless NICs, you are either in monitor mode or managed mode where you can have an association to a specific wireless AP. How did you capture in 1.8 if you said it is "working"</p></div><div id="comment-22327-info" class="comment-info"><span class="comment-age">(25 Jun '13, 08:05)</span> Landi</div></div></div><div id="comment-tools-22256" class="comment-tools"></div><div class="clear"></div><div id="comment-22256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

