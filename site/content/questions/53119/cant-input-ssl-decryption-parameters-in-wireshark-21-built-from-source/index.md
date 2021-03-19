+++
type = "question"
title = "Can&#x27;t input SSL decryption parameters in Wireshark 2.1 built from source"
description = '''I created a wireshark 2.1.0 build in my local (Ubuntu 14.04). The problem is that I can&#x27;t set the SSL priviate key or session key in configuration:  Here is the version info on this Wireshark build. Wonder what&#x27;s wrong here. Version 2.1.0 (v2.1.0rc0-1613-gfdec865 from master)  Copyright 1998-2016 Ge...'''
date = "2016-06-01T15:36:00Z"
lastmod = "2016-06-02T06:43:00Z"
weight = 53119
keywords = [ "wireshark" ]
aliases = [ "/questions/53119" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can't input SSL decryption parameters in Wireshark 2.1 built from source](/questions/53119/cant-input-ssl-decryption-parameters-in-wireshark-21-built-from-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53119-score" class="post-score" title="current number of votes">0</div><span id="post-53119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I created a wireshark 2.1.0 build in my local (Ubuntu 14.04). The problem is that I can't set the SSL priviate key or session key in configuration: <img src="https://osqa-ask.wireshark.org/upfiles/2b_LANlFxO.png" alt="alt text" /></p><p>Here is the version info on this Wireshark build. Wonder what's wrong here.</p><pre><code>Version 2.1.0 (v2.1.0rc0-1613-gfdec865 from master)

Copyright 1998-2016 Gerald Combs &lt;[email protected]&gt; and contributors.
License GPLv2+: GNU GPL version 2 or later &lt;http://www.gnu.org/licenses/old-licenses/gpl-2.0.html&gt;
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with Qt 5.2.1, with libpcap, without POSIX capabilities,
without libnl, with libz 1.2.8, with GLib 2.40.2, without SMI, with c-ares
1.10.0, without Lua, without GnuTLS, without Gcrypt, without Kerberos, with
GeoIP, without QtMultimedia, without AirPcap.

Running on Linux 3.19.0-33-generic, with locale C, with libpcap version 1.6.2,
with libz 1.2.8.
      Intel(R) Core(TM) i7-2670QM CPU @ 2.20GHz (with SSE4.2)

Built using gcc 4.8.4.

Wireshark is Open Source Software released under the GNU General Public License.

Check the man page and http://www.wireshark.org for more information.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '16, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '16, 16:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-53119" class="comments-container"></div><div id="comment-tools-53119" class="comment-tools"></div><div class="clear"></div><div id="comment-53119-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53120"></span>

<div id="answer-container-53120" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53120-score" class="post-score" title="current number of votes">1</div><span id="post-53120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>without GnuTLS, without Gcrypt</p></blockquote><p>And, therefore, without the ability to decrypt SSL/TLS.</p><p>I'm assuming that you're building Wireshark with the Ubuntu developer packages for various libraries it requires. If so, you'll need to get the developer packages for GnuTLS and Gcrypt and install them, and then re-configure and rebuild, so that you get a version of Wireshark that <em>does</em> have the ability to decrypt SSL/TLS.</p><p>And, while we're at it:</p><blockquote><p>without SMI</p></blockquote><p>If you expect to be looking at SNMP traffic, a version built with libsmi would be able to read MIBs and do a better job of parsing SNMP requests and responses.</p><blockquote><p>without Lua</p></blockquote><p>A version built with the Lua library can run Lua scripts as packet dissectors, statistics taps, etc., so it's able to use some third-party tools that a version without Lua can't, and, if you're a Lua programmer, it'd let you write your own tools of that sort.</p><blockquote><p>without Kerberos</p></blockquote><p>Which may get in the way of decrypting some traffic encrypted with the aid of Kerberos.</p><blockquote><p>without QtMultimedia</p></blockquote><p>Which I think is what's used for the audio player for some VoIP protocols.</p><p>So you might want to load the appropriate versions of some other developer libraries.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-53120" class="comments-container"><span id="53141"></span><div id="comment-53141" class="comment"><div id="post-53141-score" class="comment-score"></div><div class="comment-text"><p>Thanks Guy for the analysis!</p></div><div id="comment-53141-info" class="comment-info"><span class="comment-age">(02 Jun '16, 06:43)</span> <span class="comment-user userinfo">pktUser1001</span></div></div></div><div id="comment-tools-53120" class="comment-tools"></div><div class="clear"></div><div id="comment-53120-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

