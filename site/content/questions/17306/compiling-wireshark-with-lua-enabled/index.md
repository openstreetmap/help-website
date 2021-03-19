+++
type = "question"
title = "compiling wireshark with lua enabled"
description = '''Hi, I want to compile wireshark 1.8.0 version with lua enabled on centos 6.2.  Here are the steps that I tried, 1) downloaded and extracted the wireshark source. 2) ./configure --with-lua=/usr/  3) make 4) created and rpm and installed it in the same system when i launch wireshark in about me sectio...'''
date = "2012-12-28T08:51:00Z"
lastmod = "2013-01-02T08:21:00Z"
weight = 17306
keywords = [ "compile", "lua", "luainterface", "wireshark" ]
aliases = [ "/questions/17306" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [compiling wireshark with lua enabled](/questions/17306/compiling-wireshark-with-lua-enabled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17306-score" class="post-score" title="current number of votes">0</div><span id="post-17306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to compile wireshark 1.8.0 version with lua enabled on centos 6.2.</p><p>Here are the steps that I tried, 1) downloaded and extracted the wireshark source.</p><p>2) ./configure --with-lua=/usr/</p><p>3) make</p><p>4) created and rpm and installed it in the same system</p><p>when i launch wireshark in about me section it says compiled without lua, although the .configure command output did say configured with lua library = yes. I have properly installed lua-devel 5.1 package installed in system.</p><p>Any suggestions or documentation that i can follow to compile lua on wireshark and how do I test it properly?</p><p>Thx</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-luainterface" rel="tag" title="see questions tagged &#39;luainterface&#39;">luainterface</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Dec '12, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/4539bd8a993e934fff1bce2e159f7e15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kerolkarper&#39;s gravatar image" /><p><span>kerolkarper</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kerolkarper has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Dec '12, 14:57</strong> </span></p></div></div><div id="comments-container-17306" class="comments-container"></div><div id="comment-tools-17306" class="comment-tools"></div><div class="clear"></div><div id="comment-17306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17309"></span>

<div id="answer-container-17309" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17309-score" class="post-score" title="current number of votes">1</div><span id="post-17309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>2) ./configure --with-lua=/usr/</p></blockquote><p>That looks strange. You better leave the path and let the build system find the correct path for lua.</p><blockquote><p><code>./configure --with-lua</code><br />
</p></blockquote><p>Can you show the output of your compiled wireshark?</p><blockquote><p><code>./wireshark -v</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Dec '12, 13:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-17309" class="comments-container"><span id="17310"></span><div id="comment-17310" class="comment"><div id="post-17310-score" class="comment-score"></div><div class="comment-text"><p>Now i configured it with command ./configure --with-lua</p><p>and here is the -v output</p><p>[<span class="__cf_email__" data-cfemail="7f0d10100b3f0b1a0c0b4e">[email protected]</span> wireshark-1.8.0rc2]# ./wireshark -v wireshark 1.8.0rc2 (SVN Rev Unknown from unknown)</p><p>Copyright 1998-2012 Gerald Combs <span><span class="__cf_email__" data-cfemail="5433312635383014233d2631273c35263f7a3b2633">[email protected]</span></span> and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (64-bit) with GTK+ 2.18.9, with Cairo 1.8.8, with Pango 1.28.1, with GLib 2.22.5, with libpcap, with libz 1.2.3, without POSIX capabilities, without SMI, without c-ares, without ADNS, without Lua, without Python, without GnuTLS, without Gcrypt, with MIT Kerberos, without GeoIP, without PortAudio, with AirPcap.</p><p>Running on Linux 2.6.32-220.el6.x86_64, with locale en_US.UTF-8, with libpcap version 1.3.0, with libz 1.2.3, without AirPcap.</p><p>Built using gcc 4.4.6 20120305 (Red Hat 4.4.6-4). [<span class="__cf_email__" data-cfemail="c7b5a8a8b387b3a2b4b3f6">[email protected]</span> wireshark-1.8.0rc2]#</p></div><div id="comment-17310-info" class="comment-info"><span class="comment-age">(28 Dec '12, 14:43)</span> <span class="comment-user userinfo">kerolkarper</span></div></div><span id="17311"></span><div id="comment-17311" class="comment"><div id="post-17311-score" class="comment-score"></div><div class="comment-text"><p>Why 1.8.0rc2? That's a release candidate leading up to 1.8.0. the lates bug fix release is 1.8.4</p></div><div id="comment-17311-info" class="comment-info"><span class="comment-age">(28 Dec '12, 16:59)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="17312"></span><div id="comment-17312" class="comment"><div id="post-17312-score" class="comment-score"></div><div class="comment-text"><p>can you please post the output of the following commands.</p><blockquote><p><code>grep LUA config.status</code><br />
<code>yum list | grep -i lua | grep -i installed</code><br />
</p></blockquote><p>And yes: why 1.8.0RC2?</p></div><div id="comment-17312-info" class="comment-info"><span class="comment-age">(28 Dec '12, 17:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17351"></span><div id="comment-17351" class="comment"><div id="post-17351-score" class="comment-score"></div><div class="comment-text"><p>[<span class="__cf_email__" data-cfemail="9ceef3f3e8dce8f9efe8ad">[email protected]</span> wireshark-1.8.0rc2]# grep LUA config.status</p><p>S["HAVE_LIBLUA_FALSE"]="#"</p><p>S["HAVE_LIBLUA_TRUE"]=""</p><p>S["LUA_INCLUDES"]=""</p><p>S["LUA_LIBS"]="-llua -lm"</p><p>D["HAVE_LUA_H"]=" 1"</p><p>D["HAVE_LUALIB_H"]=" 1"</p><p>D["HAVE_LUA_5_1"]=" 1"</p><p>[<span class="__cf_email__" data-cfemail="81f3eeeef5c1f5e4f2f5b0">[email protected]</span> wireshark-1.8.0rc2]#</p><p>i just randomly picked up source code, let me try on 1.8.4 version if that makes any difference.</p></div><div id="comment-17351-info" class="comment-info"><span class="comment-age">(31 Dec '12, 07:51)</span> <span class="comment-user userinfo">kerolkarper</span></div></div><span id="17352"></span><div id="comment-17352" class="comment"><div id="post-17352-score" class="comment-score"></div><div class="comment-text"><p>[<span class="__cf_email__" data-cfemail="dcaeb3b3a89ca8b9afa8ed">[email protected]</span> wireshark-1.8.0rc2]# yum install lua lua-devel Loaded plugins: fastestmirror, refresh-packagekit, rhnplugin, security Loading mirror speeds from cached hostfile Setting up Install Process Package lua-5.1.4-4.1.el6.x86_64 already installed and latest version Package lua-devel-5.1.4-4.1.el6.x86_64 already installed and latest version Nothing to do [<span class="__cf_email__" data-cfemail="25574a4a51655140565114">[email protected]</span> wireshark-1.8.0rc2]#</p></div><div id="comment-17352-info" class="comment-info"><span class="comment-age">(31 Dec '12, 07:52)</span> <span class="comment-user userinfo">kerolkarper</span></div></div><span id="17353"></span><div id="comment-17353" class="comment not_top_scorer"><div id="post-17353-score" class="comment-score"></div><div class="comment-text"><blockquote><p>i just randomly picked up source code, let me try on 1.8.4 version if that makes any difference.</p></blockquote><p>so, does it make any difference?</p></div><div id="comment-17353-info" class="comment-info"><span class="comment-age">(31 Dec '12, 08:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17357"></span><div id="comment-17357" class="comment not_top_scorer"><div id="post-17357-score" class="comment-score"></div><div class="comment-text"><p>It works 'out of the box' on CentOS 6.2 with the sources of Wireshark 1.8.0. The only packages I had to install: lua-devel and libpcap-devel.</p><pre><code>[[email protected] wireshark-1.8.0]# ./wireshark -v
wireshark 1.8.0 (SVN Rev Unknown from unknown)

Copyright 1998-2012 Gerald Combs &lt;[email protected]&lt;a href=&quot;http://wireshark.org&quot;&gt;wireshark.org&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (32-bit) with GTK+ 2.18.9, with Cairo 1.8.8, with Pango 1.28.1, with
GLib 2.22.5, with libpcap, with libz 1.2.3, without POSIX capabilities, without
SMI, without c-ares, without ADNS, with Lua 5.1, without Python, with GnuTLS
2.8.5, with Gcrypt 1.4.5, with MIT Kerberos, without GeoIP, without PortAudio,
with AirPcap.

Running on Linux 2.6.32-220.el6.i686, with locale en_US.utf8, with libpcap
version 1.0.0, with libz 1.2.3, GnuTLS 2.8.5, Gcrypt 1.4.5, without AirPcap.

Built using gcc 4.4.6 20110731 (Red Hat 4.4.6-3).</code></pre></div><div id="comment-17357-info" class="comment-info"><span class="comment-age">(31 Dec '12, 09:06)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17388"></span><div id="comment-17388" class="comment not_top_scorer"><div id="post-17388-score" class="comment-score"></div><div class="comment-text"><p>worked with 1.8.0 version . Thanks Kurt and Anders. Appreciate it.</p></div><div id="comment-17388-info" class="comment-info"><span class="comment-age">(02 Jan '13, 07:25)</span> <span class="comment-user userinfo">kerolkarper</span></div></div></div><div id="comment-tools-17309" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-17309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17390"></span>

<div id="answer-container-17390" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17390-score" class="post-score" title="current number of votes">1</div><span id="post-17390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Any arguments you manually give 'configure' when building an RPM are not used when building the RPM. The RPM .spec file has its own 'configure' line which controls what actually goes into the RPM.</p><p>(Remember that RPMs are designed to build from un-modified source and a .spec file; the .spec file contains everything that controls the actual build.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '13, 08:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span> </br></br></p></div></div><div id="comments-container-17390" class="comments-container"></div><div id="comment-tools-17390" class="comment-tools"></div><div class="clear"></div><div id="comment-17390-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

