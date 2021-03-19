+++
type = "question"
title = "&quot;ld: crt1.o: No such file: No such file or directory&quot; Error while using powerpc-85xx-wrs-linux-gnu"
description = '''Hi, I am using the powerpc-85xx-wrs-linux-gnu cross compiler to build the wireshark binary. The Configuration flags that I used are, ./configure CC=&quot;powerpc-85xx-wrs-linux-gnu-gcc --sysroot=/auto/andpkg/rep_cache//wr-85xx/3.0.1/sysroot&quot; CFLAGS=&quot;-pipe -g -O2 -fno-strict-aliasing -D__ppc__ -D__BIG_END...'''
date = "2014-04-10T03:16:00Z"
lastmod = "2014-04-15T00:49:00Z"
weight = 31707
keywords = [ "build_error", "cross-compile", "wireshark1.2.9" ]
aliases = [ "/questions/31707" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["ld: crt1.o: No such file: No such file or directory" Error while using powerpc-85xx-wrs-linux-gnu](/questions/31707/ld-crt1o-no-such-file-no-such-file-or-directory-error-while-using-powerpc-85xx-wrs-linux-gnu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31707-score" class="post-score" title="current number of votes">0</div><span id="post-31707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am using the powerpc-85xx-wrs-linux-gnu cross compiler to build the wireshark binary.</p><p>The Configuration flags that I used are,</p><pre><code>./configure CC=&quot;powerpc-85xx-wrs-linux-gnu-gcc --sysroot=/auto/andpkg/rep_cache//wr-85xx/3.0.1/sysroot&quot; CFLAGS=&quot;-pipe -g -O2 -fno-strict-aliasing -D__ppc__ -D__BIG_ENDIAN__ -DB_ENDIAN -DP8572 -te500v2 -std=gnu99 -fgnu89-inline -Wno-pointer-sign --sysroot=/auto/andpkg/rep_cache//wr-85xx/3.0.1/sysroot&quot; CC_FOR_BUILD=$CC BUILD_CC=$CC  LD=&quot;powerpc-85xx-wrs-linux-gnu-ld  --sysroot=/auto/andpkg/rep_cache//wr-85xx/3.0.1/sysroot&quot; LDFLAGS=&quot;-L/auto/andpkg/rep_cache//wr-85xx/3.0.1/sysroot/te500v2/usr/lib -te500v2&quot; AR=&quot;powerpc-85xx-wrs-linux-gnu-ar&quot; RANLIB=&quot;powerpc-85xx-wrs-linux-gnu-ranlib&quot; --prefix=/isan --target=powerpc --disable-tests --host=powerpc-wrs-linux-gnu  --prefix=/isan --enable-ipv6=yes --enable-usr-local=no --disable-wireshark --disable-editcap --disable-reordercap --enable-dumpcap --disable-rawshark --disable-capinfos --disable-mergecap --disable-text2pcap --disable-dftest --disable-randpkt --disable-gtktest --disable-glibtest --with-pcap=/ws/aparnaga-sjc/libpcap/isan --with-pcap-remote --with-adns=no --with-plugins --with-libsmi=no --with-portaudio=no --with-krb5=no --with-lua=no --with-gcrypt=no</code></pre><p>The configuration is going through. When I run "make" I get the following error,</p><pre><code>LANG=C /auto/andatcd/perl/5.6.1/bin/perl ./make-version.pl .
Version configuration file version.conf not found.  Using defaults.
This is not a SVN build.
svnversion.h is up-to-date.
make  all-recursive
make[1]: Entering directory `/ws/aparnaga-sjc/REL_6_2_9_FM_0_37/third-party/src/tshark/wireshark-1.2.9&#39;
Making all in tools
make[2]: Entering directory `/ws/aparnaga-sjc/REL_6_2_9_FM_0_37/third-party/src/tshark/wireshark-1.2.9/tools&#39;
Making all in lemon
make[3]: Entering directory `/ws/aparnaga-sjc/REL_6_2_9_FM_0_37/third-party/src/tshark/wireshark-1.2.9/tools/lemon&#39;
powerpc-85xx-wrs-linux-gnu-gcc --sysroot=/auto/andpkg/rep_cache//wr-85xx/3.0.1/sysroot -D_U_=&quot;&quot;   -o lemon lemon.c
/auto/andpkg/rep_cache/wr-85xx/3.0.1/toolchain/bin/../lib/gcc/powerpc-wrs-linux-gnu/4.3.2/../../../../powerpc-wrs-linux-gnu/bin/ld: crt1.o: No such file: No such file or directory
collect2: ld returned 1 exit status
make[3]: *** [lemon] Error 1
make[3]: Leaving directory `/ws/aparnaga-sjc/REL_6_2_9_FM_0_37/third-party/src/tshark/wireshark-1.2.9/tools/lemon&#39;
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/ws/aparnaga-sjc/REL_6_2_9_FM_0_37/third-party/src/tshark/wireshark-1.2.9/tools&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/ws/aparnaga-sjc/REL_6_2_9_FM_0_37/third-party/src/tshark/wireshark-1.2.9&#39;
make: *** [all] Error 2</code></pre><p>I have tried to set the LD_LIBRARY_PATH and LIBRARY_PATH variable but, it does not seem to help. Can you please help me out as to what mistake I am doing?</p><p>Thanks, Aparna N.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-cross-compile" rel="tag" title="see questions tagged &#39;cross-compile&#39;">cross-compile</span> <span class="post-tag tag-link-wireshark1.2.9" rel="tag" title="see questions tagged &#39;wireshark1.2.9&#39;">wireshark1.2.9</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '14, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/b605d47d2e423a49d4a281eb597b9fba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aparna&#39;s gravatar image" /><p><span>Aparna</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aparna has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Apr '14, 10:38</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-31707" class="comments-container"><span id="31722"></span><div id="comment-31722" class="comment"><div id="post-31722-score" class="comment-score"></div><div class="comment-text"><p>What happens if you create a small <code>hello.c</code> file in <code>/tmp</code>:</p><pre><code>#include &lt;stdio.h&gt;

int
main(void)
{
    printf(&quot;Hello, world!\n&quot;);
    return 0;
}</code></pre><p>and then run</p><pre><code>cd /tmp
powerpc-85xx-wrs-linux-gnu-gcc --sysroot=/auto/andpkg/rep_cache//wr-85xx/3.0.1/sysroot -o hello hello.c</code></pre></div><div id="comment-31722-info" class="comment-info"><span class="comment-age">(10 Apr '14, 10:40)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="31815"></span><div id="comment-31815" class="comment"><div id="post-31815-score" class="comment-score"></div><div class="comment-text"><p>It gives the same error,</p><p><span class="__cf_email__" data-cfemail="492839283b27282e280928272d643a3e642b3c20252d7b7b">[email protected]</span>:/tmp$ powerpc-85xx-wrs-linux-gnu-gcc --sysroot=/auto/andpkg/rep_cache//wr-85xx/3.0.1/sysroot -o hello helloworld.c</p><p>/auto/andpkg/rep_cache/wr-85xx/3.0.1/toolchain/bin/../lib/gcc/powerpc-wrs-linux-gnu/4.3.2/../../../../powerpc-wrs-linux-gnu/bin/ld: crt1.o: No such file: No such file or directory collect2: ld returned 1 exit status</p></div><div id="comment-31815-info" class="comment-info"><span class="comment-age">(14 Apr '14, 23:03)</span> <span class="comment-user userinfo">Aparna</span></div></div></div><div id="comment-tools-31707" class="comment-tools"></div><div class="clear"></div><div id="comment-31707-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31820"></span>

<div id="answer-container-31820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31820-score" class="post-score" title="current number of votes">2</div><span id="post-31820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your cross-development environment doesn't work. You need to get that fixed (which is the responsibility of whoever supplied the cross-development environment, <em>not</em> the resposibility of the Wireshark developers).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-31820" class="comments-container"><span id="31822"></span><div id="comment-31822" class="comment"><div id="post-31822-score" class="comment-score"></div><div class="comment-text"><p>Thank you Guy Harris. I will contact the concerned :)</p></div><div id="comment-31822-info" class="comment-info"><span class="comment-age">(15 Apr '14, 00:49)</span> <span class="comment-user userinfo">Aparna</span></div></div></div><div id="comment-tools-31820" class="comment-tools"></div><div class="clear"></div><div id="comment-31820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

