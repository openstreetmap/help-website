+++
type = "question"
title = "How do you cross compile wireshark on Linux for Windows?"
description = '''Someone else recently asked this question, and the answer was to file a bug. Unfortunately, no link to the bug was posted, so here I am with the same question. Here is the basic info: ./configure --build=x86-pc-linux-gnu --host=i586-mingw32msvc  [...]  checking for connect in -lsocket... no  configu...'''
date = "2014-01-21T17:56:00Z"
lastmod = "2014-01-21T19:56:00Z"
weight = 29077
keywords = [ "compile", "dissector", "socket", "pthreads" ]
aliases = [ "/questions/29077" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do you cross compile wireshark on Linux for Windows?](/questions/29077/how-do-you-cross-compile-wireshark-on-linux-for-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29077-score" class="post-score" title="current number of votes">0</div><span id="post-29077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Someone else recently asked this question, and the answer was to file a bug. Unfortunately, no link to the bug was posted, so here I am with the same question. Here is the basic info:</p><pre><code>./configure --build=x86-pc-linux-gnu --host=i586-mingw32msvc</code></pre><p>[...]</p><pre><code> checking for connect in -lsocket... no
 configure: error: Function &#39;socket&#39; not found.</code></pre><p>config.log:</p><pre><code> configure:24681: checking for connect in -lsocket
 configure:24706: i586-mingw32msvc-gcc -o conftest.exe -g -O2 -Wall -W -Wextra -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wno-pointer-sign -Wcast-align -Wformat-security -Wold-style-definition -pthread -I/usr/include/gtk-2.0 -I/usr/lib/x86_64-linux-gnu/gtk-2.0/include -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/pango-1.0 -I/usr/include/gio-unix-2.0/ -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12   -DG_DISABLE_DEPRECATED -DG_DISABLE_SINGLE_INCLUDES -DGSEAL_ENABLE -DGTK_DISABLE_DEPRECATED -DGTK_DISABLE_SINGLE_INCLUDES -D_FORTIFY_SOURCE=2 -D_U_=&quot;__attribute__((unused))&quot;  -I/usr/local/include  -Wl,--as-needed -L/usr/local/lib conftest.c -lsocket   &gt;&amp;5
 i586-mingw32msvc-gcc: unrecognized option &#39;-pthread&#39;
 conftest.c: In function &#39;main&#39;:
 conftest.c:37: warning: old-style function definition
/usr/lib/gcc/i586-mingw32msvc/4.2.1-sjlj/../../../../i586-mingw32msvc/bin/ld: cannot find -lsocket
 collect2: ld returned 1 exit status</code></pre><p>Actually I'm only doing this because I'm trying to cross compile a dissector and I'm getting pthread errors there. It looks like glib is trying to use pthreads when it shouldn't:</p><pre><code> make  all-recursive
 make[1]: Entering directory `/Workspaces/andrew.knutsen_ubuntu1204_SDE/tools/ADN/WiresharkPlugin&#39;
 Making all in routing
 make[2]: Entering directory `/Workspaces/andrew.knutsen_ubuntu1204_SDE/tools/ADN/WiresharkPlugin/routing&#39;
 depbase=`echo add-peer.lo | sed &#39;s|[^/]*$|.deps/&amp;|;s|\.lo$||&#39;`;\
    /bin/bash ../libtool --tag=CXX   --mode=compile i586-mingw32msvc-g++ -DHAVE_CONFIG_H -I. -I..    -DENABLE_BINDIST -O2 -Wuninitialized  -g2 -ggdb -Wparentheses -Wswitch-enum -Wimplicit -Wformat -Wundef -Wshadow -Wall -W -Wreturn-type -Wunused -Wcast-qual -Wwrite-strings -Wconversion -Wsign-compare -Wredundant-decls -Wsign-promo -isystem &quot;/home/CF-CAL/andrew.knutsen/src/wireshark-1.8.11&quot;  -isystem /usr/include/glib-2.0 -isystem /usr/lib/x86_64-linux-gnu/glib-2.0/include -iquote &quot;/Workspaces/andrew.knutsen_ubuntu1204_SDE/tools/ADN/WiresharkPlugin&quot; -fvisibility=hidden -g -O2 -MT add-peer.lo -MD -MP -MF $depbase.Tpo -c -o add-peer.lo add-peer.cpp &amp;&amp;\
    mv -f $depbase.Tpo $depbase.Plo
 libtool: compile:  i586-mingw32msvc-g++ -DHAVE_CONFIG_H -I. -I.. -DENABLE_BINDIST -O2 -Wuninitialized -g2 -ggdb -Wparentheses -Wswitch-enum -Wimplicit -Wformat -Wundef -Wshadow -Wall -W -Wreturn-type -Wunused -Wcast-qual -Wwrite-strings -Wconversion -Wsign-compare -Wredundant-decls -Wsign-promo -isystem /home/CF-CAL/andrew.knutsen/src/wireshark-1.8.11 -isystem /usr/include/glib-2.0 -isystem /usr/lib/x86_64-linux-gnu/glib-2.0/include -iquote /Workspaces/andrew.knutsen_ubuntu1204_SDE/tools/ADN/WiresharkPlugin -fvisibility=hidden -g -O2 -MT add-peer.lo -MD -MP -MF .deps/add-peer.Tpo -c add-peer.cpp  -DDLL_EXPORT -DPIC -o .libs/add-peer.o
 In file included from /usr/include/glib-2.0/glib.h:108,
                 from /home/CF-CAL/andrew.knutsen/src/wireshark-1.8.11/wiretap/wtap.h:30,
                 from /home/CF-CAL/andrew.knutsen/src/wireshark-1.8.11/epan/packet.h:28,
                 from /Workspaces/andrew.knutsen_ubuntu1204_SDE/tools/ADN/WiresharkPlugin/util/base-registration.hpp:9,
                 from registration-block.hpp:6,
                 from add-peer.cpp:1:
/usr/include/glib-2.0/glib/deprecated/gthread.h:123:21: error: pthread.h: No such file or directory
 In file included from /usr/include/glib-2.0/glib.h:108,
                 from /home/CF-CAL/andrew.knutsen/src/wireshark-1.8.11/wiretap/wtap.h:30,
                 from /home/CF-CAL/andrew.knutsen/src/wireshark-1.8.11/epan/packet.h:28,
                 from /Workspaces/andrew.knutsen_ubuntu1204_SDE/tools/ADN/WiresharkPlugin/util/base-registration.hpp:9,
                 from registration-block.hpp:6,
                 from add-peer.cpp:1:
/usr/include/glib-2.0/glib/deprecated/gthread.h:133: error: &#39;pthread_mutex_t&#39; does not name a type
/usr/include/glib-2.0/glib/deprecated/gthread.h:162: error: &#39;pthread_t&#39; does not name a type
 make[2]: *** [add-peer.lo] Error 1
 make[2]: Leaving directory `/Workspaces/andrew.knutsen_ubuntu1204_SDE/tools/ADN/WiresharkPlugin/routing&#39;
 make[1]: *** [all-recursive] Error 1
 make[1]: Leaving directory `/Workspaces/andrew.knutsen_ubuntu1204_SDE/tools/ADN/WiresharkPlugin&#39;
 make: *** [all] Error 2</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-socket" rel="tag" title="see questions tagged &#39;socket&#39;">socket</span> <span class="post-tag tag-link-pthreads" rel="tag" title="see questions tagged &#39;pthreads&#39;">pthreads</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '14, 17:56</strong></p><img src="https://secure.gravatar.com/avatar/6669f689024758a37c3a68b80b7eaa0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrew%20Knutsen&#39;s gravatar image" /><p><span>Andrew Knutsen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrew Knutsen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jan '14, 18:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-29077" class="comments-container"></div><div id="comment-tools-29077" class="comment-tools"></div><div class="clear"></div><div id="comment-29077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29079"></span>

<div id="answer-container-29079" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29079-score" class="post-score" title="current number of votes">1</div><span id="post-29079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>We don't support cross-compiling for Windows on any flavor of UN*X.</p><p>You could file an enhancement request at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, but supporting cross-compiling for Windows would probably be a <em>lot</em> more work than supporting cross-compiling for some other UN*X (which is what the other person was trying to do), and I don't know whether any Wireshark developer has a setup to do that sort of cross-compiling, so the enhancement probably won't be implemented soon unless somebody (core developer or not) who is familiar with that sort of cross-development, and has an environment on which to try to make it work, does so.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '14, 19:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29079" class="comments-container"></div><div id="comment-tools-29079" class="comment-tools"></div><div class="clear"></div><div id="comment-29079-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

