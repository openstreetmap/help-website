+++
type = "question"
title = "Wireshark relocation error : symbol g_int64_equal in solaris 10"
description = '''Hi, I have installed wireshark for Solaris 10 and it dependency packages. Got all the packages from sunfreeware.com But I am not able to run the application. It is throwing below error.  could any one help us to resolve this issue  ./wireshark ld.so.1: wireshark: fatal: relocation error: file /usr/l...'''
date = "2011-07-11T01:03:00Z"
lastmod = "2011-07-11T08:48:00Z"
weight = 4975
keywords = [ "wireshark" ]
aliases = [ "/questions/4975" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark relocation error : symbol g\_int64\_equal in solaris 10](/questions/4975/wireshark-relocation-error-symbol-g_int64_equal-in-solaris-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4975-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have installed wireshark for Solaris 10 and it dependency packages. Got all the packages from sunfreeware.com</p><p>But I am not able to run the application. It is throwing below error. could any one help us to resolve this issue</p><h1 id="wireshark">./wireshark</h1><p>ld.so.1: wireshark: fatal: relocation error: file /usr/local/lib/libwireshark.so.1: symbol g_int64_equal: referenced symbol not found Killed</p><h1 id="ldd-wireshark">ldd wireshark</h1><pre><code>    libwiretap.so.1 =&gt;       /usr/local/lib/libwiretap.so.1
    libwireshark.so.1 =&gt;     /usr/local/lib/libwireshark.so.1
    libwsutil.so.1 =&gt;        /usr/local/lib/libwsutil.so.1
    libpcap.so.1 =&gt;  /usr/local/lib/libpcap.so.1
    libgtk-x11-2.0.so.0 =&gt;   /usr/lib/libgtk-x11-2.0.so.0
    libgdk-x11-2.0.so.0 =&gt;   /usr/lib/libgdk-x11-2.0.so.0
    libgdk_pixbuf-2.0.so.0 =&gt;        /usr/lib/libgdk_pixbuf-2.0.so.0
    libpango-1.0.so.0 =&gt;     /usr/lib/libpango-1.0.so.0
    libgobject-2.0.so.0 =&gt;   /usr/lib/libgobject-2.0.so.0
    libpthread.so.1 =&gt;       /usr/lib/libpthread.so.1
    libthread.so.1 =&gt;        /usr/lib/libthread.so.1
    libglib-2.0.so.0 =&gt;      /usr/lib/libglib-2.0.so.0
    libc.so.1 =&gt;     /usr/lib/libc.so.1
    libm.so.2 =&gt;     /usr/lib/libm.so.2
    libnsl.so.1 =&gt;   /usr/lib/libnsl.so.1
    libz.so =&gt;       /usr/lib/libz.so
    libgcc_s.so.1 =&gt;         /usr/local/lib/libgcc_s.so.1
    libgthread-2.0.so.0 =&gt;   /usr/lib/libgthread-2.0.so.0
    libgmodule-2.0.so.0 =&gt;   /usr/lib/libgmodule-2.0.so.0
    librt.so.1 =&gt;    /usr/lib/librt.so.1
    libintl.so.8 =&gt;  /usr/local/lib/libintl.so.8
    libiconv.so.2 =&gt;         /usr/local/lib/libiconv.so.2
    libsec.so.1 =&gt;   /usr/lib/libsec.so.1
    libsocket.so.1 =&gt;        /usr/lib/libsocket.so.1
    libadns.so =&gt;    /usr/local/lib/libadns.so
    libgcrypt.so.11 =&gt;       /usr/local/lib/libgcrypt.so.11
    libgpg-error.so.0 =&gt;     /usr/lib/libgpg-error.so.0
    libgnutls.so.13 =&gt;       /usr/local/lib/libgnutls.so.13
    libcrypto.so.1.0.0 =&gt;    /usr/local/ssl/lib/libcrypto.so.1.0.0
    libGeoIP.so.1 =&gt;         /usr/local/lib/libGeoIP.so.1
    libatk-1.0.so.0 =&gt;       /usr/lib/libatk-1.0.so.0
    libpangoxft-1.0.so.0 =&gt;  /usr/lib/libpangoxft-1.0.so.0
    libpangox-1.0.so.0 =&gt;    /usr/lib/libpangox-1.0.so.0
    libXft.so.2 =&gt;   /usr/openwin/lib/libXft.so.2
    libfreetype.so.6 =&gt;      /usr/sfw/lib/libfreetype.so.6
    libXrender.so.1 =&gt;       /usr/sfw/lib/libXrender.so.1
    libfontconfig.so.1 =&gt;    /usr/lib/libfontconfig.so.1
    libX11.so.4 =&gt;   /usr/openwin/lib/libX11.so.4
    libmlib.so.2 =&gt;  /usr/lib/libmlib.so.2
    libXrandr.so.2 =&gt;        /usr/X11/lib/libXrandr.so.2
    libXi.so.5 =&gt;    /usr/openwin/lib/libXi.so.5
    libXext.so.0 =&gt;  /usr/openwin/lib/libXext.so.0
    libmp.so.2 =&gt;    /lib/libmp.so.2
    libmd.so.1 =&gt;    /lib/libmd.so.1
    libscf.so.1 =&gt;   /lib/libscf.so.1
    libaio.so.1 =&gt;   /lib/libaio.so.1
    libavl.so.1 =&gt;   /lib/libavl.so.1
    libdl.so.1 =&gt;    /lib/libdl.so.1
    libpangoft2-1.0.so.0 =&gt;  /usr/lib/libpangoft2-1.0.so.0
    libexpat.so.0 =&gt;         /usr/sfw/lib/libexpat.so.0
    libdoor.so.1 =&gt;  /lib/libdoor.so.1
    libuutil.so.1 =&gt;         /lib/libuutil.so.1
    libgen.so.1 =&gt;   /lib/libgen.so.1
    /platform/SUNW,Sun-Blade-T6340/lib/libc_psr.so.1
    /usr/lib/cpu/sparcv9+vis2/libmlib.so.2
    /platform/SUNW,Sun-Blade-T6340/lib/libmd_psr.so.1</code></pre></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '11, 01:03</strong></p><img src="https://secure.gravatar.com/avatar/415685ffb42cdbdfd2ef424e7497a844?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muthu&#39;s gravatar image" /><p>Muthu<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muthu has no accepted answers">0%</span></p></div></div><div id="comments-container-4975" class="comments-container"><span id="4980"></span><div id="comment-4980" class="comment"><div id="post-4980-score" class="comment-score"></div><div class="comment-text"><p>I have the same problem. Moreover I had installed glib before. Does Wireshark require specify version of glib?</p></div><div id="comment-4980-info" class="comment-info"><span class="comment-age">(11 Jul '11, 06:18)</span> p4w3k</div></div><span id="5865"></span><div id="comment-5865" class="comment"><div id="post-5865-score" class="comment-score"></div><div class="comment-text"><p>I have the same problem.</p><p>My wireshark version is wireshark-1.6.1 and My glib version is glib-2.25.13 . The fatal is still like this.</p><p>Can any one help me?</p></div><div id="comment-5865-info" class="comment-info"><span class="comment-age">(25 Aug '11, 02:05)</span> firobaccano</div></div></div><div id="comment-tools-4975" class="comment-tools"></div><div class="clear"></div><div id="comment-4975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="4977"></span>

<div id="answer-container-4977" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4977-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>g_int64_equal</code> is from <a href="http://www.opencsw.org/package/glib/">glib</a>. It looks like you're missing that dependency.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '11, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-4977" class="comments-container"></div><div id="comment-tools-4977" class="comment-tools"></div><div class="clear"></div><div id="comment-4977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4981"></span>

<div id="answer-container-4981" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4981-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ok, the thing is that you need to install current glib. I have installed glib-2.25.13 and it solved whole problem.</p><p>Regards</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '11, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/5869b529d5289248cfb53dd9ce2c4acb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="p4w3k&#39;s gravatar image" /><p>p4w3k<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="p4w3k has no accepted answers">0%</span></p></div></div><div id="comments-container-4981" class="comments-container"><span id="6693"></span><div id="comment-6693" class="comment"><div id="post-6693-score" class="comment-score"></div><div class="comment-text"><p>I have installed all the packages dependencies for the wireshark and also installed glib with version 2.25.13 still I am getting same error : ld.so.1: wireshark: fatal: relocation error: file /usr/local/lib/libwireshark.so.1: symbol g_int64_equal: referenced symbol not found Killed</p><p>So could you pleaople tell me what went wrong in my case.</p><p>Thanks in advacnce ......... Ranjeet</p></div><div id="comment-6693-info" class="comment-info"><span class="comment-age">(04 Oct '11, 04:21)</span> Ranjeet</div></div></div><div id="comment-tools-4981" class="comment-tools"></div><div class="clear"></div><div id="comment-4981-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4982"></span>

<div id="answer-container-4982" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4982-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://developer.gnome.org/glib/2.28/glib-Hash-Tables.html#g-int64-equal">g_int64_equal</a> was introduced in glib 2.22, so you'll need at least that version or later to use the package from <a href="ftp://ftp.sunfreeware.com/pub/freeware/sparc/10/wireshark-1.6.0-sol10-sparc-local.gz">sunfreeware</a>. Alternatively, if you don't want to upgrade your glib version, you can compile Wireshark yourself from <a href="http://wiresharkdownloads.riverbed.com/wireshark/src/wireshark-1.6.0.tar.bz2">source</a>. Wireshark currently still only requires glib 2.4 as the minimum version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '11, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Jul '11, 08:48</p></div></div><div id="comments-container-4982" class="comments-container"><span id="5089"></span><div id="comment-5089" class="comment"><div id="post-5089-score" class="comment-score"></div><div class="comment-text"><p>Issue was resolved after i installed glib2.22. Thanks a lot for the help.</p></div><div id="comment-5089-info" class="comment-info"><span class="comment-age">(18 Jul '11, 01:11)</span> Muthu</div></div></div><div id="comment-tools-4982" class="comment-tools"></div><div class="clear"></div><div id="comment-4982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

