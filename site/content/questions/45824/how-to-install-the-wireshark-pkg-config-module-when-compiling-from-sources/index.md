+++
type = "question"
title = "How to install the wireshark pkg-config module when compiling from sources"
description = '''I&#x27;m trying to compile libvirt sources with the &quot;--with-wireshark-dissector&quot;&quot; option. However, the configure process sends me the following error: &quot;You must install the wireshark &amp;gt;= 1.11.3 pkg-config module to compile libvirt&quot;. I have installed wireshark 1.21.7 from sources with the following opti...'''
date = "2015-09-14T01:20:00Z"
lastmod = "2015-09-14T07:25:00Z"
weight = 45824
keywords = [ "module", "pkg-config" ]
aliases = [ "/questions/45824" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to install the wireshark pkg-config module when compiling from sources](/questions/45824/how-to-install-the-wireshark-pkg-config-module-when-compiling-from-sources)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45824-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to compile libvirt sources with the "--with-wireshark-dissector"" option. However, the configure process sends me the following error: "You must install the wireshark &gt;= 1.11.3 pkg-config module to compile libvirt".</p><p>I have installed wireshark 1.21.7 from sources with the following options: ./configure --with-ssl --with-geoip</p><p>What should I do to "install the wireshark pkg-config module"?</p></div><div id="question-tags" class="tags-container tags">module pkg-config</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '15, 01:20</strong></p><img src="https://secure.gravatar.com/avatar/c86fb9accfde44bdbe661d8582c39b7b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="actionmystique&#39;s gravatar image" /><p>actionmystique<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="actionmystique has no accepted answers">0%</span></p></div></div><div id="comments-container-45824" class="comments-container"></div><div id="comment-tools-45824" class="comment-tools"></div><div class="clear"></div><div id="comment-45824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45827"></span>

<div id="answer-container-45827" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45827-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What distribution are you using? If it's Debian/Unbuntu then I think you can install the necessary files with some apt-get command but I haven't a clue which.</p><p>If you'd prefer to install it from source then you'll have to use cmake (rather than the autotools--meaning ./configure). Wireshark 1.12.x appears to have support for installing this file.</p><p>(There was a <a href="https://code.wireshark.org/review/8050">change</a> to make autotools install the .pc file but it was abandoned.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '15, 07:25</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-45827" class="comments-container"><span id="45842"></span><div id="comment-45842" class="comment"><div id="post-45842-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer. I use Ubuntu 15.04 - could you elaborate a little bit about how to use cmake to generate pkg-config module? There is not a single line about that in all Wireshark documentation.</p></div><div id="comment-45842-info" class="comment-info"><span class="comment-age">(15 Sep '15, 01:18)</span> actionmystique</div></div><span id="45843"></span><div id="comment-45843" class="comment"><div id="post-45843-score" class="comment-score"></div><div class="comment-text"><p>Have you looked at README.CMake in the source top level directory?</p><p>CMake will generate lots of things, including the Makefiles to build Wireshark, but I'm not sure about the pkg-config file.</p></div><div id="comment-45843-info" class="comment-info"><span class="comment-age">(15 Sep '15, 01:58)</span> grahamb ♦</div></div><span id="45851"></span><div id="comment-45851" class="comment"><div id="post-45851-score" class="comment-score"></div><div class="comment-text"><p>When you're in the source directory just do (for example):</p><pre><code>  mkdir _cmake_build
  cd _cmake_build
  cmake ..</code></pre><p>At this point there will be a wireshark.pc file which you could manually copy to the appropriate place (often /usr/share/pkgconfig/). Or you could probably do "make install" (I didn't try this because I don't want to pollute my system).</p></div><div id="comment-45851-info" class="comment-info"><span class="comment-age">(15 Sep '15, 06:33)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-45827" class="comment-tools"></div><div class="clear"></div><div id="comment-45827-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

