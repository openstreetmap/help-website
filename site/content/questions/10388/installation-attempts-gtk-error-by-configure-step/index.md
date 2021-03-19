+++
type = "question"
title = "Installation attempts GTK+ error by configure step"
description = '''I know, the solution should be &quot;upgrade my Solaris 10 to latest version&quot;, but I still want to solve this issue but not just upgrade. wireshark source: wireshark-1.6.4.tar.gz os:  bash-3.00# cat /etc/release   Solaris 10 11/06 s10x_u3wos_10 X86  Copyright 2006 Sun Microsystems, Inc. All Rights Reserv...'''
date = "2012-04-23T00:22:00Z"
lastmod = "2012-04-23T00:22:00Z"
weight = 10388
keywords = [ "wireshark" ]
aliases = [ "/questions/10388" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Installation attempts GTK+ error by configure step](/questions/10388/installation-attempts-gtk-error-by-configure-step)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10388-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I know, the solution should be "upgrade my Solaris 10 to latest version", but I still want to solve this issue but not just upgrade.</p><p>wireshark source: wireshark-1.6.4.tar.gz</p><p>os:</p><pre><code>bash-3.00# cat /etc/release

                    Solaris 10 11/06 s10x_u3wos_10 X86
       Copyright 2006 Sun Microsystems, Inc.  All Rights Reserved.
                    Use is subject to license terms.
                       Assembled 14 November 2006
bash-3.00# uname -a
SunOS solx86lab2 5.10 Generic_118855-33 i86pc i386 i86pc</code></pre><p>By running configure script, attempt an error</p><pre><code>checking for GTK+ - version &gt;= 2.4.0... no
*** Could not run GTK+ test program, checking why...
*** The test program failed to compile or link. See the file config.log for the
*** exact error that occured. This usually means GTK+ is incorrectly installed.
configure: error: GTK+ 2.4 or later isn&#39;t available, so Wireshark can&#39;t be compiled</code></pre><p>I have searched F&amp;Q and get the following answer:</p><p><a href="http://ask.wireshark.org/questions/5426/configure-gives-error-gtk-version-issue-solaris">http://ask.wireshark.org/questions/5426/configure-gives-error-gtk-version-issue-solaris</a></p><p><a href="http://www.wireshark.org/lists/wireshark-users/200802/msg00050.html">http://www.wireshark.org/lists/wireshark-users/200802/msg00050.html</a></p><p>I tried</p><pre><code>bash-3.00# cat /usr/lib/pkgconfig/gthread-2.0.pc
prefix=/usr
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: GThread
Description: Thread support for GLib
Requires: glib-2.0
Version: 2.4.1
Libs: -L${libdir} -lgthread-2.0 -mt
Cflags: -mt</code></pre><p>After configure, in configure.log</p><pre><code>configure:19371: gcc -o conftest -D_U_=&quot;__attribute__((unused))&quot; -g -O2 -Wall -W -Wextra -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wcast-align -Wformat-security -Wno-return-type -DFUNCPROTO=15 -I/usr/local/include -mt -I/usr/include/gtk-2.0 -I/usr/lib/gtk-2.0/include -I/usr/include/atk-1.0 -I/usr/include/pango-1.0 -I/usr/openwin/include -I/usr/sfw/include -I/usr/sfw/include/freetype2 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include    -I/usr/local/include  -L/usr/local/lib -R/usr/local/lib conftest.c -mt -lgtk-x11-2.0 -lgdk-x11-2.0 -latk-1.0 -lgdk_pixbuf-2.0 -lm -lmlib -lpangoxft-1.0 -lpangox-1.0 -lpango-1.0 -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0    -R/opt/csw/lib:/usr/sfw/lib &gt;&amp;5
cc1: error: invalid option `t&#39;
cc1: error: invalid option `t&#39;
configure:19371: $? = 1</code></pre><p>It is true, gcc don't know -mt, but even how I modified file gthread-2.0.pc with -pthread or -D_REENTRANT still doesn't work.</p><p>Does anyone has idea??</p><p>Thanks at first.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '12, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/cbec934b26f5436e93778fac3726551e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob&#39;s gravatar image" /><p>Bob<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '12, 00:58</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-10388" class="comments-container"><span id="10485"></span><div id="comment-10485" class="comment"><div id="post-10485-score" class="comment-score"></div><div class="comment-text"><p>Well, what does the configure.log say after you modified ghtread-2.0.pc? The quoted output indicates the "-mt" is still there, so I suppose this is the "before" output.</p></div><div id="comment-10485-info" class="comment-info"><span class="comment-age">(27 Apr '12, 07:48)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-10388" class="comment-tools"></div><div class="clear"></div><div id="comment-10388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

