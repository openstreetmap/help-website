+++
type = "question"
title = "linking dissector plugin against shared library (OpenSSL)"
description = '''Hi all. Due to the numerous tutorials I found in web, I managed to compile a dissector plugin on Linux. The raw implementation of my plugin works fine now. My new goal is to extend the plugin providing an ECDDSA-signature check &quot;on the fly&quot; of the received data packages. Therefore I tried to link my...'''
date = "2013-08-13T04:54:00Z"
lastmod = "2013-09-03T07:54:00Z"
weight = 23743
keywords = [ "shared", "linker", "openssl", "library", "plugin" ]
aliases = [ "/questions/23743" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [linking dissector plugin against shared library (OpenSSL)](/questions/23743/linking-dissector-plugin-against-shared-library-openssl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23743-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all. Due to the numerous tutorials I found in web, I managed to compile a dissector plugin on Linux. The raw implementation of my plugin works fine now. My new goal is to extend the plugin providing an ECDDSA-signature check "on the fly" of the received data packages. Therefore I tried to link my dissector plugin against the crypto library of OpenSSL, but at his point all my efforts unfortunately failed. I didn't find anything in web dealing with such kind of problem so I decided to post this question here. My efforts until now:</p><p>1 . I edited Makefile.am in my plugin directory and added the following to the "LIB" line:</p><pre><code>LIBS = -L/usr/lib/i386-linux-gnu -lcrypto \
-lssl</code></pre><p>after that I did configure, make clean and make but the plugin didn't linked against the OpenSSL lib.</p><p>2 . I tried to edit Makefile of the plugin but again with no result.</p><p>There aren't any errors during Compilation, but when I start Wireshark, there is "Couldn't load module error". In addition when i call ldd on .so file of my plugin i can't find crypto-library there. So my guess is it's a linker error, but I have no idea how to solve it. Any help is highly appreciated.</p><p>Many thx,</p><p>Arthur</p><p>EDIT: strangly i can't post a comment below, so I'm writing it here: My plugin compiles and works nice without the ECDSA-stuff I want to add. But I'm not able to link my plugin against the extern OpenSSL library, so I can use its EC(DSA)-functions: <a href="http://www.openssl.org/docs/crypto/ecdsa.html.">http://www.openssl.org/docs/crypto/ecdsa.html.</a> I couldn't find any information on how to link against external libraries in readme.plugins or do I miss something important here? Thx</p></div><div id="question-tags" class="tags-container tags">shared linker openssl library plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Aug '13, 04:54</strong></p><img src="https://secure.gravatar.com/avatar/4d0f1f7eeb5c80f659413b34da3dd344?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arthur%20Giss&#39;s gravatar image" /><p>Arthur Giss<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arthur Giss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Aug '13, 08:33</p></div></div><div id="comments-container-23743" class="comments-container"><span id="23744"></span><div id="comment-23744" class="comment"><div id="post-23744-score" class="comment-score"></div><div class="comment-text"><p>Did you run ./configure --with-ssl ?</p></div><div id="comment-23744-info" class="comment-info"><span class="comment-age">(13 Aug '13, 05:03)</span> Anders ♦</div></div><span id="23745"></span><div id="comment-23745" class="comment"><div id="post-23745-score" class="comment-score"></div><div class="comment-text"><p>Thx for the fast help Anders! I tried it again with ./configure --with-ssl, but still the same error. When running ./configure, I realized that Makefile of my plugin isn't generated, e.g. there is no line saying something like "config.status: creating plugins/profinet/Makefile". Is my problem maybe related with it?</p></div><div id="comment-23745-info" class="comment-info"><span class="comment-age">(13 Aug '13, 05:14)</span> Arthur Giss</div></div><span id="23746"></span><div id="comment-23746" class="comment"><div id="post-23746-score" class="comment-score"></div><div class="comment-text"><p>Check readme.plugins in the doc folder to see what files need to be changed to build a plugin.</p></div><div id="comment-23746-info" class="comment-info"><span class="comment-age">(13 Aug '13, 06:07)</span> Anders ♦</div></div></div><div id="comment-tools-23743" class="comment-tools"></div><div class="clear"></div><div id="comment-23743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24309"></span>

<div id="answer-container-24309" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24309-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>After spending further time on my problem I finally linked my dissector to a shared library (in my case the OpenSSL lib). However I'm not very happy with my solution :-/. First I briefly describe how it acutally worked.</p><p>Instead of adding -lssl and -lcrypto to Makefile.am, I searched the Makefile of my plugin itself for linking possibilities for the SSL lib. There I realized a weird thing:</p><pre><code>...
LD = /usr/bin/ld
LDFLAGS =  -Wl,--as-needed -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib
LDFLAGS_SHAREDLIB =
...</code></pre><p>Strangely the library path is added four times to the shell variable $(LDFLAGS). According to this i guessed it might be a libtool issue that I'm not able to link against any shared library. Further investigation on the Makefile reveal $(LDFLAGS) is indeed related to libtool linking process. (If this is trivial for you, I'm sry for explaining it, because I have never dealed with Makefiles or libtool before, but used tools like Eclipse for my purposes.) When I add -lssl and -lcrypto to $(LDFLAGS) my plugin works with openSSL support like a charme :-):</p><pre><code>...
LD = /usr/bin/ld
LDFLAGS =  -Wl,--as-needed -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -lssl -lcrypto
LDFLAGS_SHAREDLIB =
...</code></pre><p>but my question is now, what is the "official way" to link against a shared library? In readme.plugins the files which have to be adapted are: AUTHORS, COPYING, ChangeLog, CMakeLists.txt, Makefile.am, Makefile.common, Makefile.nmake, moduleinfo.h, moduleinfo.nmake, plugin.rc.in. But unfortunattely none of these files has an influence on the $(LDFLAGS) variable in the final Makefile of the plugin. Variable &amp;(LIBS) in Makefile.am which is supposed to add additional libraries has absolutely no effect because I can write garbage in that variable with no effect on the building process of my plugin? Maybe it's a wireshark bug? Searching the forum I discovered that other users have similar problems too. E.g.: <a href="http://ask.wireshark.org/questions/5152/link-shared-library-for-decoder-with-wireshark-on-linux">http://ask.wireshark.org/questions/5152/link-shared-library-for-decoder-with-wireshark-on-linux</a></p><p>Thanks for any comments, answers.</p><p>Arthur</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '13, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/4d0f1f7eeb5c80f659413b34da3dd344?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arthur%20Giss&#39;s gravatar image" /><p>Arthur Giss<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arthur Giss has no accepted answers">0%</span></p></div></div><div id="comments-container-24309" class="comments-container"></div><div id="comment-tools-24309" class="comment-tools"></div><div class="clear"></div><div id="comment-24309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

