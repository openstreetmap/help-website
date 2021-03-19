+++
type = "question"
title = "make error Solaris 10 x86"
description = '''I&#x27;m trying to compile wireshark 1.8.11 on a solaris 10 x86 system. I have successfully run the ./configure command but when I run make the following errors occur. I do not have a lot of experience with compiling from source code so any help would be great. libtool: compile: gcc -DHAVE_CONFIG_H -I. -...'''
date = "2013-11-20T08:00:00Z"
lastmod = "2013-11-20T08:15:00Z"
weight = 27165
keywords = [ "make", "1.8.11", "solaris", "error" ]
aliases = [ "/questions/27165" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [make error Solaris 10 x86](/questions/27165/make-error-solaris-10-x86)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27165-score" class="post-score" title="current number of votes">0</div><span id="post-27165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to compile wireshark 1.8.11 on a solaris 10 x86 system. I have successfully run the ./configure command but when I run make the following errors occur. I do not have a lot of experience with compiling from source code so any help would be great.</p><pre><code>libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I../.. -I./../.. -I./.. -DINET6 -DG_
DISABLE_DEPRECATED -DG_DISABLE_SINGLE_INCLUDES -DGTK_DISABLE_DEPRECATED -DGTK_DI
SABLE_SINGLE_INCLUDES -D_FORTIFY_SOURCE=2 &quot;-D_U_=attribute((unused))&quot; -DFUNC
PROTO=15 -I/usr/local/include -I/usr/local/include -I/usr/include/kerberosv5 -DP
LUGIN_DIR=\&quot;/usr/local/lib/wireshark/plugins/1.8.11\&quot; -g -O2 -Wall -W -Wextra -W
declaration-after-statement -Wendif-labels -Wpointer-arith -Wcast-align -Wformat
-security -Wold-style-definition -Wno-return-type -D_REENTRANT -D_PTHREADS -D_RE
ENTRANT -D_PTHREADS -I/usr/local/include/gtk-2.0 -I/usr/local/lib/gtk-2.0/includ
e -I/usr/local/include/gtk-2.0 -I/usr/local/include/pango-1.0 -I/usr/local/inclu
de/atk-1.0 -I/usr/local/include/glib-2.0 -I/usr/local/lib/glib-2.0/include -I/us
r/local/include/cairo -I/usr/local/include/freetype2 -I/usr/local/include -I/usr
/local/include/libpng12 -I/usr/local/include -MT ftype-double.lo -MD -MP -MF .de
ps/ftype-double.Tpo -c ftype-double.c  -fPIC -DPIC -o .libs/ftype-double.o
In file included from ftype-double.c:29:
/usr/local/lib/gcc/i386-pc-solaris2.10/3.4.6/include/math.h:26:26: iso/math_iso.
h: No such file or directory
In file included from /usr/local/lib/gcc/i386-pc-solaris2.10/3.4.6/include/math.
h:336,
                 from ftype-double.c:29:
/usr/local/lib/gcc/i386-pc-solaris2.10/3.4.6/include/floatingpoint.h:30:24: sys/
ieeefp.h: No such file or directory
In file included from /usr/local/lib/gcc/i386-pc-solaris2.10/3.4.6/include/math.
h:336,
                 from ftype-double.c:29:
/usr/local/lib/gcc/i386-pc-solaris2.10/3.4.6/include/floatingpoint.h:104: error:
 field fpclass&#39; has incomplete type
/usr/local/lib/gcc/i386-pc-solaris2.10/3.4.6/include/floatingpoint.h:128: error:
 fieldrd&#39; has incomplete type
ftype-double.c: In function val_from_unparsed&#39;:
ftype-double.c:69: error:HUGE_VAL&#39; undeclared (first use in this function)
ftype-double.c:69: error: (Each undeclared identifier is reported only once
ftype-double.c:69: error: for each function it appears in.)
make[3]:  [ftype-double.lo] Error 1
make[3]: Leaving directory /usr01/wireshark-1.8.11/epan/ftypes&#39;
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory/usr01/wireshark-1.8.11/epan&#39;
make[1]:  [all-recursive] Error 1
make[1]: Leaving directory `/usr01/wireshark-1.8.11&#39;
make: *** [all] Error 2</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-1.8.11" rel="tag" title="see questions tagged &#39;1.8.11&#39;">1.8.11</span> <span class="post-tag tag-link-solaris" rel="tag" title="see questions tagged &#39;solaris&#39;">solaris</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/b8a53b1e3902596ccb0734c4eec78b97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tengood&#39;s gravatar image" /><p><span>tengood</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tengood has no accepted answers">0%</span></p></div></div><div id="comments-container-27165" class="comments-container"></div><div id="comment-tools-27165" class="comment-tools"></div><div class="clear"></div><div id="comment-27165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27168"></span>

<div id="answer-container-27168" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27168-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27168-score" class="post-score" title="current number of votes">0</div><span id="post-27168-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That seems to be a GCC problem that has been fixed some time ago (2005).</p><blockquote><p><a href="http://gcc.gnu.org/bugzilla/show_bug.cgi?id=19933">http://gcc.gnu.org/bugzilla/show_bug.cgi?id=19933</a></p></blockquote><p>I guess, your gcc is simply too old (version 3.4.6) !?!. Please try to install a more recent version of gcc. If you don't know how to do that, please ask you local Solaris 10 x86 guru.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Nov '13, 17:57</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-27168" class="comments-container"></div><div id="comment-tools-27168" class="comment-tools"></div><div class="clear"></div><div id="comment-27168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

