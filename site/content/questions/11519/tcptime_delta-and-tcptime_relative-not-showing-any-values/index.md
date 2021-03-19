+++
type = "question"
title = "tcp.time_delta and tcp.time_relative not showing any values"
description = '''Is it just me or do the display-filter for tcp.time_delta and tcp.time_relative don&#x27;t show any values ...? tested with:  Version 1.6.8 (SVN Rev 42761 from /trunk-1.6) Copyright 1998-2012 Gerald Combs gerald@wireshark.org and contributors. This is free software; see the source for copying conditions....'''
date = "2012-06-01T00:29:00Z"
lastmod = "2012-06-01T01:31:00Z"
weight = 11519
keywords = [ "display-filter" ]
aliases = [ "/questions/11519" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tcp.time\_delta and tcp.time\_relative not showing any values](/questions/11519/tcptime_delta-and-tcptime_relative-not-showing-any-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11519-score" class="post-score" title="current number of votes">3</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Is it just me or do the display-filter for tcp.time_delta and tcp.time_relative don't show any values ...?</p><p>tested with:</p><hr /><p>Version 1.6.8 (SVN Rev 42761 from /trunk-1.6)</p><p>Copyright 1998-2012 Gerald Combs [email protected] and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.24.5, with GLib 2.29.8, with libpcap (version unknown), with libz 1.2.3, without POSIX capabilities, without libpcre, with SMI 0.4.8, without c-ares, without ADNS, with Lua 5.1, without Python, with GnuTLS 2.12.7, with Gcrypt 1.4.6, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Sep 30 2011 11:17:29), without AirPcap.</p><p>Running on Mac OS 10.6.8 (Darwin 10.8.0), with libpcap version 1.0.0, with libz 1.2.3, GnuTLS 2.12.7, Gcrypt 1.4.6.</p><p>Built using gcc 4.2.1 (Apple Inc. build 5666) (dot 3).</p><p>Wireshark is Open Source Software released under the GNU General Public License.</p><p>Check the man page and <a href="http://www.wireshark.org">http://www.wireshark.org</a> for more information.</p><hr /></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '12, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/812f7dddfcfb20fc1990cfc3cba54c22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teoh&#39;s gravatar image" /><p>teoh<br />
<span class="score" title="51 reputation points">51</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teoh has no accepted answers">0%</span></p></div></div><div id="comments-container-11519" class="comments-container"></div><div id="comment-tools-11519" class="comment-tools"></div><div class="clear"></div><div id="comment-11519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11520"></span>

<div id="answer-container-11520" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11520-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please enable TCP timestamp calculation (disabled by default)</p><blockquote><p><code>Edit -&gt; Preferences -&gt; Protocols -&gt; TCP -&gt; Calculate conversation timestamps</code><br />
</p></blockquote><p>with thshark</p><blockquote><p><code>tshark.exe -r input.cap</code> <strong><code>-o tcp.calculate_timestamps:true</code></strong> <code>-T fields -e frame.number -e tcp.time_delta -e &lt;whatever you need&gt; -E header=y -E separator=;</code><br />
</p></blockquote><p>Rgards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '12, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '12, 01:47</p></div></div><div id="comments-container-11520" class="comments-container"><span id="11624"></span><div id="comment-11624" class="comment"><div id="post-11624-score" class="comment-score"></div><div class="comment-text"><p>That did the trick, thanks</p></div><div id="comment-11624-info" class="comment-info"><span class="comment-age">(04 Jun '12, 08:22)</span> teoh</div></div></div><div id="comment-tools-11520" class="comment-tools"></div><div class="clear"></div><div id="comment-11520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

