+++
type = "question"
title = "What are the core dependencies for building wireshark?"
description = '''Trying to build wireshark with our companies build system. Just wondering what are the core deps for building it. As in what are the minimum requirements I can get away with?&#x27; Edit: reading this http://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallBeforeBuild.html it says GTK and libpcap ar...'''
date = "2011-03-14T09:50:00Z"
lastmod = "2011-03-15T16:53:00Z"
weight = 2804
keywords = [ "core", "dependencies", "requirements", "minimal" ]
aliases = [ "/questions/2804" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What are the core dependencies for building wireshark?](/questions/2804/what-are-the-core-dependencies-for-building-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2804-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to build wireshark with our companies build system. Just wondering what are the core deps for building it. As in what are the minimum requirements I can get away with?'</p><p>Edit: reading this</p><p>http://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallBeforeBuild.html</p><p>it says GTK and libpcap are required for the build. But running "apt-rdepends wireshark" gives me a massive dep-tree. What does this mean?</p></div><div id="question-tags" class="tags-container tags">core dependencies requirements minimal</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '11, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/3d3535b19a6debac9e2b855465a2027b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rodayo&#39;s gravatar image" /><p>Rodayo<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rodayo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '11, 09:53</p></div></div><div id="comments-container-2804" class="comments-container"></div><div id="comment-tools-2804" class="comment-tools"></div><div class="clear"></div><div id="comment-2804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2811"></span>

<div id="answer-container-2811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2811-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>From the <a href="http://wiki.wireshark.org/Development">Wiki</a>, this should bring you a long way:</p><pre><code>sudo aptitude install build-essential automake autoconf libgtk2.0-dev libglib2.0-dev libpcap0.8-dev flex bison</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '11, 15:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2811" class="comments-container"></div><div id="comment-tools-2811" class="comment-tools"></div><div class="clear"></div><div id="comment-2811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="2849"></span>

<div id="answer-container-2849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2849-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"apt-rdepends wireshark" will report what the version of Wireshark that Debian/Ubuntu/whoever made your (presumably Debian-based) distribution built requires; they might have built it with all the "use this" configuration options turned on, so it might be using libz and SMI and Lua and some asynchronous DNS resolver and GnuTLS and Gcrypt and Kerberos and GeoIP and PortAudio and a big jam doughnut with cream on top....</p><p>The minimum requirements for a Linux build would be GTK+ - which, in turn, requires GLib (not glibc, GLib) - and libpcap, as well as Flex and Bison. You need GTK+ for the GUI; you need GLib for the GUI <em>and</em> for Wireshark's own internals, and you need libpcap in order to capture network traffic. You might need Flex and Bison (I forget whether we ship pre-built output for Flex and YACC files or not); you probably won't need automake or autoconf <em>if</em> you're just building from one of the source tarballs, as they already include the generated configure script - if you want to build from Subversion, you'll need automake and autoconf and libtool (as well as, obviously, Subversion itself :-)). All the other libraries you can build Wireshark with just add capabilities to Wireshark, such as decryption, decompression of compressed network traffic and of compressed capture files, and so on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '11, 16:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-2849" class="comments-container"></div><div id="comment-tools-2849" class="comment-tools"></div><div class="clear"></div><div id="comment-2849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

