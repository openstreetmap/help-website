+++
type = "question"
title = "libtool complains &quot;version mismatch&quot;"
description = '''Hello again, 1.6.3 build system fails under my distro. (related to libtool ?) here is the output from make: ../libtool: line 466: CDPATH: command not found ../libtool: line 1144: func_opt_split: command not found libtool: Version mismatch error. This is libtool 2.2.6b Debian-2.2.6b-2ubuntu1, but the...'''
date = "2011-11-15T08:57:00Z"
lastmod = "2011-11-15T12:01:00Z"
weight = 7448
keywords = [ "failure", "build" ]
aliases = [ "/questions/7448" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [libtool complains "version mismatch"](/questions/7448/libtool-complains-version-mismatch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7448-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello again,</p><p>1.6.3 build system fails under my distro. (related to libtool ?)</p><p>here is the output from make:</p><pre><code>../libtool: line 466: CDPATH: command not found
../libtool: line 1144: func_opt_split: command not found
libtool: Version mismatch error.  This is libtool 2.2.6b Debian-2.2.6b-2ubuntu1, but the
libtool: definition of this LT_INIT comes from an older release.
libtool: You should recreate aclocal.m4 with macros from libtool 2.2.6b Debian-2.2.6b-2ubuntu1
libtool: and run autoconf again.
make[2]: *** [mpeg-audio.lo] Error 1
make[2]: Leaving directory `/home/worker/wireshark/wireshark-1.6.3/wsutil&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/worker/wireshark/wireshark-1.6.3&#39;
make: *** [all] Error 2</code></pre><p>I reverted to the 1.4.10 version and the build went OK.</p><p>Since I'm not used to the GNU Autoconf, Automake, and Libtool family at all, I can't fix the build process...</p><p>Maybe Wireshark team will want to fix this...</p><p>hints:</p><ul><li>I run a 2.6.17 kernel from Mandriva,</li><li>with glib version 2.0.0.1200.11 installed</li><li>with libtool 2.4.2</li><li>2 Patches were applied from http://wiki.wireshark.org/Development/Roadmap "Rev 38045, Rev 38046 - Bug 6540 - Don't use g_mutex without having threads."</li></ul></div><div id="question-tags" class="tags-container tags">failure build</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Nov '11, 08:57</strong></p><img src="https://secure.gravatar.com/avatar/50fb2b078363521170dab88586426792?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wirebilly&#39;s gravatar image" /><p>wirebilly<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wirebilly has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Nov '11, 09:03</p></div></div><div id="comments-container-7448" class="comments-container"></div><div id="comment-tools-7448" class="comment-tools"></div><div class="clear"></div><div id="comment-7448-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7451"></span>

<div id="answer-container-7451" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7451-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>./autogen.sh &amp;&amp; ./configure &amp;&amp; make</code></p><p>That's the chain of commands you need to execute ... as documented in <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBuildFirstTime.html#id569233">section 3.5.1</a> of the developer's guide.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Nov '11, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Nov '11, 18:38</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-7451" class="comments-container"><span id="7463"></span><div id="comment-7463" class="comment"><div id="post-7463-score" class="comment-score"></div><div class="comment-text"><p>If you're building from a source tarball, and have modified nothing in the source tarball, the <code>./autogen.sh</code> should not be necessary; a source tarball is intended to Just Work with <code>./configure</code> and <code>make</code> - source tarballs are primarily intended to be used to install Wireshark if you don't just have a binary distribution to install.</p><p>If you're not just building from the source in the tarball, you should probably build from Subversion on the trunk or the appropriate branch, in which case you <em>do</em> need to do <code>./autogen.sh</code> after checking the tree out from Subversion.</p></div><div id="comment-7463-info" class="comment-info"><span class="comment-age">(15 Nov '11, 23:59)</span> Guy Harris ♦♦</div></div><span id="7472"></span><div id="comment-7472" class="comment"><div id="post-7472-score" class="comment-score"></div><div class="comment-text"><p>Right. Thank you very much.</p></div><div id="comment-7472-info" class="comment-info"><span class="comment-age">(16 Nov '11, 06:19)</span> wirebilly</div></div></div><div id="comment-tools-7451" class="comment-tools"></div><div class="clear"></div><div id="comment-7451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

