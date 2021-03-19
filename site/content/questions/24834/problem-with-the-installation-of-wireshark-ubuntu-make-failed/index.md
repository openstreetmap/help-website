+++
type = "question"
title = "problem with the installation of wireshark ubuntu “make” failed"
description = '''I am new to wireshark and ubuntu. I need to install wireshark but it seems to have some problems when I type &quot;sudo make&quot; command. here is what I get: dell@ubuntu:~$ cd wireshark/ dell@ubuntu:~/wireshark$ make LANG=C /usr/bin/perl ./make-version.pl . Version configuration file version.conf not found....'''
date = "2013-09-17T08:23:00Z"
lastmod = "2013-09-18T03:44:00Z"
weight = 24834
keywords = [ "failed", "make", "ubuntu", "wireshark" ]
aliases = [ "/questions/24834" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [problem with the installation of wireshark ubuntu “make” failed](/questions/24834/problem-with-the-installation-of-wireshark-ubuntu-make-failed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24834-score" class="post-score" title="current number of votes">0</div><span id="post-24834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark and ubuntu. I need to install wireshark but it seems to have some problems when I type "sudo make" command. here is what I get:</p><pre><code>[email protected]:~$ cd wireshark/
[email protected]:~/wireshark$ make
LANG=C /usr/bin/perl ./make-version.pl .
Version configuration file version.conf not found.  Using defaults.
This is not a SVN build.
svnversion.h is up-to-date.
make  all-recursive
make[1]: Entering directory `/home/dell/wireshark&#39;
Making all in tools
make[2]: Entering directory `/home/dell/wireshark/tools&#39;
Making all in lemon
make[3]: Entering directory `/home/dell/wireshark/tools/lemon&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/tools/lemon&#39;
make[3]: Entering directory `/home/dell/wireshark/tools&#39;
make[3]: Nothing to be done for `all-am&#39;.
make[3]: Leaving directory `/home/dell/wireshark/tools&#39;
make[2]: Leaving directory `/home/dell/wireshark/tools&#39;
Making all in wsutil
make[2]: Entering directory `/home/dell/wireshark/wsutil&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/wsutil&#39;
Making all in wiretap
make[2]: Entering directory `/home/dell/wireshark/wiretap&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/wiretap&#39;
Making all in doc
make[2]: Entering directory `/home/dell/wireshark/doc&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/doc&#39;
Making all in epan
make[2]: Entering directory `/home/dell/wireshark/epan&#39;
Making all in crc
make[3]: Entering directory `/home/dell/wireshark/epan/crc&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan/crc&#39;
Making all in crypt
make[3]: Entering directory `/home/dell/wireshark/epan/crypt&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan/crypt&#39;
Making all in ftypes
make[3]: Entering directory `/home/dell/wireshark/epan/ftypes&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan/ftypes&#39;
Making all in dfilter
make[3]: Entering directory `/home/dell/wireshark/epan/dfilter&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan/dfilter&#39;
Making all in dissectors
make[3]: Entering directory `/home/dell/wireshark/epan/dissectors&#39;
make  all-am
make[4]: Entering directory `/home/dell/wireshark/epan/dissectors&#39;
make[4]: Nothing to be done for `all-am&#39;.
make[4]: Leaving directory `/home/dell/wireshark/epan/dissectors&#39;
make[3]: Leaving directory `/home/dell/wireshark/epan/dissectors&#39;
make[3]: Entering directory `/home/dell/wireshark/epan&#39;
make[3]: Nothing to be done for `all-am&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan&#39;
make[2]: Leaving directory `/home/dell/wireshark/epan&#39;
Making all in plugins
make[2]: Entering directory `/home/dell/wireshark/plugins&#39;
Making all in asn1
make[3]: Entering directory `/home/dell/wireshark/plugins/asn1&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/asn1&#39;
Making all in docsis
make[3]: Entering directory `/home/dell/wireshark/plugins/docsis&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/docsis&#39;
Making all in ethercat
make[3]: Entering directory `/home/dell/wireshark/plugins/ethercat&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/ethercat&#39;
Making all in giop
make[3]: Entering directory `/home/dell/wireshark/plugins/giop&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/giop&#39;
Making all in gryphon
make[3]: Entering directory `/home/dell/wireshark/plugins/gryphon&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/gryphon&#39;
Making all in irda
make[3]: Entering directory `/home/dell/wireshark/plugins/irda&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/irda&#39;
Making all in m2m
make[3]: Entering directory `/home/dell/wireshark/plugins/m2m&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/m2m&#39;
Making all in mate
make[3]: Entering directory `/home/dell/wireshark/plugins/mate&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/mate&#39;
Making all in opcua
make[3]: Entering directory `/home/dell/wireshark/plugins/opcua&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/opcua&#39;
Making all in profinet
make[3]: Entering directory `/home/dell/wireshark/plugins/profinet&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/profinet&#39;
Making all in sercosiii
make[3]: Entering directory `/home/dell/wireshark/plugins/sercosiii&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/sercosiii&#39;
Making all in stats_tree
make[3]: Entering directory `/home/dell/wireshark/plugins/stats_tree&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/stats_tree&#39;
Making all in unistim
make[3]: Entering directory `/home/dell/wireshark/plugins/unistim&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/unistim&#39;
Making all in wimax
make[3]: Entering directory `/home/dell/wireshark/plugins/wimax&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/wimax&#39;
Making all in mux
make[3]: Entering directory `/home/dell/wireshark/plugins/mux&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/mux&#39;
Making all in wimaxasncp
make[3]: Entering directory `/home/dell/wireshark/plugins/wimaxasncp&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/wimaxasncp&#39;
make[3]: Entering directory `/home/dell/wireshark/plugins&#39;
make[3]: Nothing to be done for `all-am&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins&#39;
make[2]: Leaving directory `/home/dell/wireshark/plugins&#39;
Making all in packaging
make[2]: Entering directory `/home/dell/wireshark/packaging&#39;
Making all in macosx
make[3]: Entering directory `/home/dell/wireshark/packaging/macosx&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/packaging/macosx&#39;
Making all in rpm
make[3]: Entering directory `/home/dell/wireshark/packaging/rpm&#39;
Making all in SPECS
make[4]: Entering directory `/home/dell/wireshark/packaging/rpm/SPECS&#39;
make[4]: Nothing to be done for `all&#39;.
make[4]: Leaving directory `/home/dell/wireshark/packaging/rpm/SPECS&#39;
make[4]: Entering directory `/home/dell/wireshark/packaging/rpm&#39;
make[4]: Nothing to be done for `all-am&#39;.
make[4]: Leaving directory `/home/dell/wireshark/packaging/rpm&#39;
make[3]: Leaving directory `/home/dell/wireshark/packaging/rpm&#39;
Making all in svr4
make[3]: Entering directory `/home/dell/wireshark/packaging/svr4&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/packaging/svr4&#39;
Making all in nsis
make[3]: Entering directory `/home/dell/wireshark/packaging/nsis&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/packaging/nsis&#39;
make[3]: Entering directory `/home/dell/wireshark/packaging&#39;
make[3]: Nothing to be done for `all-am&#39;.
make[3]: Leaving directory `/home/dell/wireshark/packaging&#39;
make[2]: Leaving directory `/home/dell/wireshark/packaging&#39;
Making all in help
make[2]: Entering directory `/home/dell/wireshark/help&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/help&#39;
Making all in codecs
make[2]: Entering directory `/home/dell/wireshark/codecs&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/codecs&#39;
Making all in gtk
make[2]: Entering directory `/home/dell/wireshark/gtk&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/gtk&#39;
make[2]: Entering directory `/home/dell/wireshark&#39;
LANG=C /usr/bin/perl ./make-version.pl .
Version configuration file version.conf not found.  Using defaults.
This is not a SVN build.
svnversion.h is up-to-date.
/bin/bash ./libtool --tag=CC   --mode=link gcc  -DINET6 -D_U_=&quot;__attribute__((unused))&quot; -g -O2 -Wall -W -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wno-pointer-sign -Warray-bounds -Wcast-align -Wformat-security -I/usr/local/include -pthread -I/usr/include/gtk-2.0 -I/usr/lib/x86_64-linux-gnu/gtk-2.0/include -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/pango-1.0 -I/usr/include/gio-unix-2.0/ -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12   -I/usr/include   -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -o dftest dftest-dftest.o dftest-util.o  wiretap/libwiretap.la wsutil/libwsutil.la epan/libwireshark.la  -dlopen plugins/asn1/asn1.la -dlopen plugins/docsis/docsis.la -dlopen plugins/ethercat/ethercat.la -dlopen plugins/giop/cosnaming.la -dlopen plugins/giop/coseventcomm.la -dlopen plugins/gryphon/gryphon.la -dlopen plugins/irda/irda.la -dlopen plugins/m2m/m2m.la -dlopen plugins/mate/mate.la -dlopen plugins/mux/mux.la -dlopen plugins/opcua/opcua.la -dlopen plugins/profinet/profinet.la -dlopen plugins/sercosiii/sercosiii.la -dlopen plugins/stats_tree/stats_tree.la -dlopen plugins/unistim/unistim.la -dlopen plugins/wimax/wimax.la -lpcre -Wl,--export-dynamic -pthread -lgmodule-2.0 -lrt -lglib-2.0   -lm -L/usr/lib/x86_64-linux-gnu  -lpcap -lcares -L/usr/lib/x86_64-linux-gnu -Wl,-Bsymbolic-functions -Wl,-z,relro -lkrb5 -lk5crypto -lcom_err -L/lib/x86_64-linux-gnu -lgcrypt -lgnutls -L/usr/lib -lsmi -lz 
libtool: link: rm -f .libs/dftest.nm .libs/dftest.nmS .libs/dftest.nmT
./libtool: line 3687: .libs/dftestS.c: Permission denied
./libtool: line 3823: .libs/dftest.nm: Permission denied
make[2]: *** [dftest] Error 1
make[2]: Leaving directory `/home/dell/wireshark&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/dell/wireshark&#39;
make: *** [all] Error 2</code></pre><p>can anyone help me please. It's urgent. thanks a lot</p><p>Fadou</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span> <span class="post-tag tag-link-make" rel="tag" title="see questions tagged &#39;make&#39;">make</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '13, 08:23</strong></p><img src="https://secure.gravatar.com/avatar/7604586a6362ae1ae819bcec6ee0edaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fadou&#39;s gravatar image" /><p><span>fadou</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fadou has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '13, 08:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-24834" class="comments-container"></div><div id="comment-tools-24834" class="comment-tools"></div><div class="clear"></div><div id="comment-24834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="24845"></span>

<div id="answer-container-24845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24845-score" class="post-score" title="current number of votes">1</div><span id="post-24845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe start with the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcBuildFirstTime.html#idp4003536">Wireshark Developer's Guide</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '13, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24845" class="comments-container"><span id="24848"></span><div id="comment-24848" class="comment"><div id="post-24848-score" class="comment-score"></div><div class="comment-text"><p>I did follow all steps in order but I cannot understand what is the exact pb</p></div><div id="comment-24848-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:50)</span> <span class="comment-user userinfo">fadou</span></div></div><span id="24849"></span><div id="comment-24849" class="comment"><div id="post-24849-score" class="comment-score">1</div><div class="comment-text"><p>I suggest you start over with a fresh directory downloaded/extracted from original Wireshark source files as a normal user that will be used to compile the sources and not as root. Then follow the steps again as described in the developer's guide.</p></div><div id="comment-24849-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:55)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-24845" class="comment-tools"></div><div class="clear"></div><div id="comment-24845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24837"></span>

<div id="answer-container-24837" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24837-score" class="post-score" title="current number of votes">0</div><span id="post-24837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>"<strong>sudo make</strong>"<br />
./libtool: line 3687: .libs/dftestS.c: <strong>Permission denied</strong></p></blockquote><p>Why do you run <strong>make</strong> as root? Only <strong>make install</strong> would need root privileges. Please just try <strong>make</strong> and check if the <strong>permission denied</strong> error goes away.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '13, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Sep '13, 08:29</strong> </span></p></div></div><div id="comments-container-24837" class="comments-container"><span id="24839"></span><div id="comment-24839" class="comment"><div id="post-24839-score" class="comment-score"></div><div class="comment-text"><p>Hi kurt,</p><p>I still have the same errors even when I type make</p><pre><code>[email protected]:~/wireshark$ make
LANG=C /usr/bin/perl ./make-version.pl .
Version configuration file version.conf not found.  Using defaults.
This is not a SVN build.
svnversion.h is up-to-date.
make  all-recursive
make[1]: Entering directory `/home/dell/wireshark&#39;
Making all in tools
make[2]: Entering directory `/home/dell/wireshark/tools&#39;
Making all in lemon
make[3]: Entering directory `/home/dell/wireshark/tools/lemon&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/tools/lemon&#39;
make[3]: Entering directory `/home/dell/wireshark/tools&#39;
make[3]: Nothing to be done for `all-am&#39;.
make[3]: Leaving directory `/home/dell/wireshark/tools&#39;
make[2]: Leaving directory `/home/dell/wireshark/tools&#39;
Making all in wsutil
make[2]: Entering directory `/home/dell/wireshark/wsutil&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/wsutil&#39;
Making all in wiretap
make[2]: Entering directory `/home/dell/wireshark/wiretap&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/wiretap&#39;
Making all in doc
make[2]: Entering directory `/home/dell/wireshark/doc&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/doc&#39;
Making all in epan
make[2]: Entering directory `/home/dell/wireshark/epan&#39;
Making all in crc
make[3]: Entering directory `/home/dell/wireshark/epan/crc&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan/crc&#39;
Making all in crypt
make[3]: Entering directory `/home/dell/wireshark/epan/crypt&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan/crypt&#39;
Making all in ftypes
make[3]: Entering directory `/home/dell/wireshark/epan/ftypes&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan/ftypes&#39;
Making all in dfilter
make[3]: Entering directory `/home/dell/wireshark/epan/dfilter&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan/dfilter&#39;
Making all in dissectors
make[3]: Entering directory `/home/dell/wireshark/epan/dissectors&#39;
make  all-am
make[4]: Entering directory `/home/dell/wireshark/epan/dissectors&#39;
make[4]: Nothing to be done for `all-am&#39;.
make[4]: Leaving directory `/home/dell/wireshark/epan/dissectors&#39;
make[3]: Leaving directory `/home/dell/wireshark/epan/dissectors&#39;
make[3]: Entering directory `/home/dell/wireshark/epan&#39;
make[3]: Nothing to be done for `all-am&#39;.
make[3]: Leaving directory `/home/dell/wireshark/epan&#39;
make[2]: Leaving directory `/home/dell/wireshark/epan&#39;
Making all in plugins
make[2]: Entering directory `/home/dell/wireshark/plugins&#39;
Making all in asn1
make[3]: Entering directory `/home/dell/wireshark/plugins/asn1&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/asn1&#39;
Making all in docsis
make[3]: Entering directory `/home/dell/wireshark/plugins/docsis&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/docsis&#39;
Making all in ethercat
make[3]: Entering directory `/home/dell/wireshark/plugins/ethercat&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/ethercat&#39;
Making all in giop
make[3]: Entering directory `/home/dell/wireshark/plugins/giop&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/giop&#39;
Making all in gryphon
make[3]: Entering directory `/home/dell/wireshark/plugins/gryphon&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/gryphon&#39;
Making all in irda
make[3]: Entering directory `/home/dell/wireshark/plugins/irda&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/irda&#39;
Making all in m2m
make[3]: Entering directory `/home/dell/wireshark/plugins/m2m&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/m2m&#39;
Making all in mate
make[3]: Entering directory `/home/dell/wireshark/plugins/mate&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/mate&#39;
Making all in opcua
make[3]: Entering directory `/home/dell/wireshark/plugins/opcua&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/opcua&#39;
Making all in profinet
make[3]: Entering directory `/home/dell/wireshark/plugins/profinet&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/profinet&#39;
Making all in sercosiii
make[3]: Entering directory `/home/dell/wireshark/plugins/sercosiii&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/sercosiii&#39;
Making all in stats_tree
make[3]: Entering directory `/home/dell/wireshark/plugins/stats_tree&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/stats_tree&#39;
Making all in unistim
make[3]: Entering directory `/home/dell/wireshark/plugins/unistim&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/unistim&#39;
Making all in wimax
make[3]: Entering directory `/home/dell/wireshark/plugins/wimax&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/wimax&#39;
Making all in mux
make[3]: Entering directory `/home/dell/wireshark/plugins/mux&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/mux&#39;
Making all in wimaxasncp
make[3]: Entering directory `/home/dell/wireshark/plugins/wimaxasncp&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins/wimaxasncp&#39;
make[3]: Entering directory `/home/dell/wireshark/plugins&#39;
make[3]: Nothing to be done for `all-am&#39;.
make[3]: Leaving directory `/home/dell/wireshark/plugins&#39;
make[2]: Leaving directory `/home/dell/wireshark/plugins&#39;
Making all in packaging
make[2]: Entering directory `/home/dell/wireshark/packaging&#39;
Making all in macosx
make[3]: Entering directory `/home/dell/wireshark/packaging/macosx&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/packaging/macosx&#39;
Making all in rpm
make[3]: Entering directory `/home/dell/wireshark/packaging/rpm&#39;
Making all in SPECS
make[4]: Entering directory `/home/dell/wireshark/packaging/rpm/SPECS&#39;
make[4]: Nothing to be done for `all&#39;.
make[4]: Leaving directory `/home/dell/wireshark/packaging/rpm/SPECS&#39;
make[4]: Entering directory `/home/dell/wireshark/packaging/rpm&#39;
make[4]: Nothing to be done for `all-am&#39;.
make[4]: Leaving directory `/home/dell/wireshark/packaging/rpm&#39;
make[3]: Leaving directory `/home/dell/wireshark/packaging/rpm&#39;
Making all in svr4
make[3]: Entering directory `/home/dell/wireshark/packaging/svr4&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/packaging/svr4&#39;
Making all in nsis
make[3]: Entering directory `/home/dell/wireshark/packaging/nsis&#39;
make[3]: Nothing to be done for `all&#39;.
make[3]: Leaving directory `/home/dell/wireshark/packaging/nsis&#39;
make[3]: Entering directory `/home/dell/wireshark/packaging&#39;
make[3]: Nothing to be done for `all-am&#39;.
make[3]: Leaving directory `/home/dell/wireshark/packaging&#39;
make[2]: Leaving directory `/home/dell/wireshark/packaging&#39;
Making all in help
make[2]: Entering directory `/home/dell/wireshark/help&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/help&#39;
Making all in codecs
make[2]: Entering directory `/home/dell/wireshark/codecs&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/codecs&#39;
Making all in gtk
make[2]: Entering directory `/home/dell/wireshark/gtk&#39;
make[2]: Nothing to be done for `all&#39;.
make[2]: Leaving directory `/home/dell/wireshark/gtk&#39;
make[2]: Entering directory `/home/dell/wireshark&#39;
LANG=C /usr/bin/perl ./make-version.pl .
Version configuration file version.conf not found.  Using defaults.
This is not a SVN build.
svnversion.h is up-to-date.
/bin/bash ./libtool --tag=CC   --mode=link gcc  -DINET6 -D_U_=&quot;__attribute__((unused))&quot; -g -O2 -Wall -W -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wno-pointer-sign -Warray-bounds -Wcast-align -Wformat-security -I/usr/local/include -pthread -I/usr/include/gtk-2.0 -I/usr/lib/x86_64-linux-gnu/gtk-2.0/include -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/pango-1.0 -I/usr/include/gio-unix-2.0/ -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng12   -I/usr/include   -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -L/usr/local/lib -o dftest dftest-dftest.o dftest-util.o  wiretap/libwiretap.la wsutil/libwsutil.la epan/libwireshark.la  -dlopen plugins/asn1/asn1.la -dlopen plugins/docsis/docsis.la -dlopen plugins/ethercat/ethercat.la -dlopen plugins/giop/cosnaming.la -dlopen plugins/giop/coseventcomm.la -dlopen plugins/gryphon/gryphon.la -dlopen plugins/irda/irda.la -dlopen plugins/m2m/m2m.la -dlopen plugins/mate/mate.la -dlopen plugins/mux/mux.la -dlopen plugins/opcua/opcua.la -dlopen plugins/profinet/profinet.la -dlopen plugins/sercosiii/sercosiii.la -dlopen plugins/stats_tree/stats_tree.la -dlopen plugins/unistim/unistim.la -dlopen plugins/wimax/wimax.la -lpcre -Wl,--export-dynamic -pthread -lgmodule-2.0 -lrt -lglib-2.0   -lm -L/usr/lib/x86_64-linux-gnu  -lpcap -lcares -L/usr/lib/x86_64-linux-gnu -Wl,-Bsymbolic-functions -Wl,-z,relro -lkrb5 -lk5crypto -lcom_err -L/lib/x86_64-linux-gnu -lgcrypt -lgnutls -L/usr/lib -lsmi -lz 
libtool: link: rm -f .libs/dftest.nm .libs/dftest.nmS .libs/dftest.nmT
./libtool: line 3687: .libs/dftestS.c: Permission denied
./libtool: line 3823: .libs/dftest.nm: Permission denied
make[2]: *** [dftest] Error 1
make[2]: Leaving directory `/home/dell/wireshark&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/dell/wireshark&#39;
make: *** [all] Error 2
[email protected]:~/wireshark$</code></pre></div><div id="comment-24839-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:32)</span> <span class="comment-user userinfo">fadou</span></div></div><span id="24840"></span><div id="comment-24840" class="comment"><div id="post-24840-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I still have the same errors even when I type make</p></blockquote><p>O.K. where did you get the source code from and how did you extract it?</p><p>What is the output of the following commands?</p><blockquote><p>ls -al /home/dell/wireshark/.libs<br />
df -k /home/dell/wireshark</p></blockquote><p>BTW: Did you run <strong>./configure</strong> before typing <strong>make</strong>?</p></div><div id="comment-24840-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="24844"></span><div id="comment-24844" class="comment"><div id="post-24844-score" class="comment-score"></div><div class="comment-text"><p>I downloaded from the official website and extracted it here are outputs of respectively:</p><p><code> ls -al /home/dell/wireshark/.libs  [email protected]:~/wireshark$ ls -al /home/dell/wireshark/.libs  total 7598 drwxr-xr-x  2 root root    1024 sept. 17 13:52 . drwxrwxr-x 27 dell dell   13312 sept. 17 13:52 .. -rwxr-xr-x  1 root root   83257 sept. 17 13:52 capinfos -rw-r--r--  1 root root    2624 sept. 17 13:52 dftestS.o -rwxr-xr-x  1 root root  131157 sept. 17 13:52 editcap -rwxr-xr-x  1 root root   44242 sept. 17 13:52 mergecap -rwxr-xr-x  1 root root   30738 sept. 17 13:52 randpkt -rwxr-xr-x  1 root root   80733 sept. 17 13:51 text2pcap -rwxr-xr-x  1 root root  877381 sept. 17 13:51 tshark -rw-r--r--  1 root root    2624 sept. 17 13:51 tsharkS.o -rwxr-xr-x  1 root root 6475798 sept. 17 13:51 wireshark -rw-r--r--  1 root root    2640 sept. 17 13:51 wiresharkS.o</code></p><p><code></code></p><p><code>and for df -k /home/dell/wireshark: </code></p><code></code><p><code>[email protected]:~/wireshark$ df -k /home/dell/wireshark Filesystem     1K-blocks    Used Available Use% Mounted on /dev/loop0      29496487 7446096  22050391  26% /</code></p><p>Fadou</p></div><div id="comment-24844-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:45)</span> <span class="comment-user userinfo">fadou</span></div></div><span id="24846"></span><div id="comment-24846" class="comment"><div id="post-24846-score" class="comment-score"></div><div class="comment-text"><p>yes i did run ./configure before make but still have the same pb</p></div><div id="comment-24846-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:49)</span> <span class="comment-user userinfo">fadou</span></div></div><span id="24847"></span><div id="comment-24847" class="comment not_top_scorer"><div id="post-24847-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@fadou</span>,</p><p>Please wrap your voluminous "terminal output" in <code>&lt;code&gt;&lt;/code&gt;</code> markup so it's readable.</p><p>And please stop posting comments as "answers", use the "add a comment" button. This is not a forum, it's a Q&amp;A site, have a look at the FAQ for more info.</p></div><div id="comment-24847-info" class="comment-info"><span class="comment-age">(17 Sep '13, 08:50)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="24851"></span><div id="comment-24851" class="comment"><div id="post-24851-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>I downloaded from the official website <strong>and extracted it</strong> here are outputs of respectively:</p></blockquote><p>O.K. please repeat that as a regular user. Some files now belong to root (see ls -al).</p><blockquote><p>Mounted on <strong>/dev/loop0</strong> 29496487 7446096 22050391 26% /</p></blockquote><p>Why is your root filesystem mounted on /dev/loop0?? Maybe that's causing problems. Are you running your Ubuntu from a boot only CDROM? That would certainly cause problems!</p><p>Regards<br />
Kurt</p></div><div id="comment-24851-info" class="comment-info"><span class="comment-age">(17 Sep '13, 09:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24837" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-24837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24902"></span>

<div id="answer-container-24902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24902-score" class="post-score" title="current number of votes">0</div><span id="post-24902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I had the similars problem with permission when building Wireshark, but I realised that after installing Ubuntu, you should mount your drives by using: <strong><code>sudo blkid</code></strong> to get UID, then <strong><code>sudo gedit /etc/fstab</code></strong> to edit the file. Add your drive with corresponding UID and Save. Restart computer, and check if the problem stil happens. In my case, most of problem related to permission disappear. So, i think you can try it, Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '13, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-24902" class="comments-container"></div><div id="comment-tools-24902" class="comment-tools"></div><div class="clear"></div><div id="comment-24902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

