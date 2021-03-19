+++
type = "question"
title = "Problem decrypting ssl packets"
description = '''Installed wireshark 1.4.4 from Sunfreeware on Solaris 10 update 9 sparc platform. I have enabled ssl decoding by setting in the preferences file the correct key files that I would need to decrypt the packets with using the ssl.key_list parameter. Wireshark starts up fine but when I open my saved fil...'''
date = "2011-03-21T08:33:00Z"
lastmod = "2011-03-22T07:03:00Z"
weight = 2969
keywords = [ "ssl" ]
aliases = [ "/questions/2969" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem decrypting ssl packets](/questions/2969/problem-decrypting-ssl-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2969-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Installed wireshark 1.4.4 from Sunfreeware on Solaris 10 update 9 sparc platform. I have enabled ssl decoding by setting in the preferences file the correct key files that I would need to decrypt the packets with using the ssl.key_list parameter.</p><p>Wireshark starts up fine but when I open my saved file I get the following error reported and the application is killed:</p><p>ld.so.1: wireshark: fatal: relocation error: file /usr/local/lib/libwireshark.so.0: symbol gcry_cipher_setkey: referenced symbol not found</p><p>Any help would be appreciated.</p><p>ldd /usr/bin/wireshark gives me the following output</p><pre><code>    libwiretap.so.0 =&gt;       /usr/local/lib/libwiretap.so.0
    libwireshark.so.0 =&gt;     /usr/local/lib/libwireshark.so.0
    libwsutil.so.0 =&gt;        /usr/local/lib/libwsutil.so.0
    libpcap.so.1 =&gt;  /usr/local/lib/libpcap.so.1
    libgtk-x11-2.0.so.0 =&gt;   /usr/local/lib/libgtk-x11-2.0.so.0
    libgdk-x11-2.0.so.0 =&gt;   /usr/local/lib/libgdk-x11-2.0.so.0
    libgdk_pixbuf-2.0.so.0 =&gt;        /usr/local/lib/libgdk_pixbuf-2.0.so.0
    libpango-1.0.so.0 =&gt;     /usr/local/lib/libpango-1.0.so.0
    libgobject-2.0.so.0 =&gt;   /usr/local/lib/libgobject-2.0.so.0
    libpthread.so.1 =&gt;       /usr/lib/libpthread.so.1
    libthread.so.1 =&gt;        /usr/lib/libthread.so.1
    libglib-2.0.so.0 =&gt;      /usr/local/lib/libglib-2.0.so.0
    libc.so.1 =&gt;     /usr/lib/libc.so.1
    libm.so.2 =&gt;     /usr/lib/libm.so.2
    libnsl.so.1 =&gt;   /usr/lib/libnsl.so.1
    libz.so =&gt;       /usr/lib/libz.so
    libgcc_s.so.1 =&gt;         /usr/sfw/lib/libgcc_s.so.1
    libgmodule-2.0.so.0 =&gt;   /usr/local/lib/libgmodule-2.0.so.0
    librt.so.1 =&gt;    /usr/lib/librt.so.1
    libintl.so.8 =&gt;  /usr/local/lib/libintl.so.8
    libiconv.so.2 =&gt;         /usr/local/lib/libiconv.so.2
    libsec.so.1 =&gt;   /usr/lib/libsec.so.1
    libsocket.so.1 =&gt;        /usr/lib/libsocket.so.1
    libadns.so =&gt;    /usr/local/lib/libadns.so
    libgcrypt.so.11 =&gt;       /usr/local/lib/libgcrypt.so.11
    libgpg-error.so.0 =&gt;     /usr/local/lib/libgpg-error.so.0
    libgnutls.so.13 =&gt;       /usr/local/lib/libgnutls.so.13
    libcrypto.so.1.0.0 =&gt;    /usr/local/ssl/lib/libcrypto.so.1.0.0
    libGeoIP.so.1 =&gt;         /usr/local/lib/libGeoIP.so.1
    libXrender.so.1 =&gt;       /usr/openwin/sfw/lib/libXrender.so.1
    libX11.so.4 =&gt;   /usr/lib/libX11.so.4
    libpangocairo-1.0.so.0 =&gt;        /usr/local/lib/libpangocairo-1.0.so.0
    libatk-1.0.so.0 =&gt;       /usr/lib/libatk-1.0.so.0
    libcairo.so.2 =&gt;         /usr/local/lib/libcairo.so.2
    libmlib.so.2 =&gt;  /usr/lib/libmlib.so.2
    libXrandr.so.2 =&gt;        /usr/lib/libXrandr.so.2
    libXext.so.0 =&gt;  /usr/lib/libXext.so.0
    libfontconfig.so.1 =&gt;    /usr/lib/libfontconfig.so.1
    libgthread-2.0.so.0 =&gt;   /usr/local/lib/libgthread-2.0.so.0
    libmp.so.2 =&gt;    /usr/lib/libmp.so.2
    libmd.so.1 =&gt;    /usr/lib/libmd.so.1
    libscf.so.1 =&gt;   /usr/lib/libscf.so.1
    libaio.so.1 =&gt;   /usr/lib/libaio.so.1
    libavl.so.1 =&gt;   /usr/lib/libavl.so.1
    libdl.so.1 =&gt;    /usr/lib/libdl.so.1
    libpangoft2-1.0.so.0 =&gt;  /usr/local/lib/libpangoft2-1.0.so.0
    libfreetype.so.6 =&gt;      /usr/local/lib/libfreetype.so.6
    libpng12.so.0 =&gt;         /usr/local/lib/libpng12.so.0
    libSM.so.6 =&gt;    /usr/lib/libSM.so.6
    libICE.so.6 =&gt;   /usr/lib/libICE.so.6
    libexpat.so.0 =&gt;         /usr/sfw/lib/libexpat.so.0
    libdoor.so.1 =&gt;  /usr/lib/libdoor.so.1
    libuutil.so.1 =&gt;         /usr/lib/libuutil.so.1
    libgen.so.1 =&gt;   /usr/lib/libgen.so.1
    /platform/SUNW,A70/lib/libc_psr.so.1
    /usr/lib/cpu/sparcv9+vis2/libmlib.so.2
    /platform/SUNW,A70/lib/libmd_psr.so.1</code></pre></div><div id="question-tags" class="tags-container tags">ssl</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '11, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/ef1e02accbf1c13236d6a60a4ac57fa9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="draslpd&#39;s gravatar image" /><p>draslpd<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="draslpd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Mar '11, 09:50</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-2969" class="comments-container"></div><div id="comment-tools-2969" class="comment-tools"></div><div class="clear"></div><div id="comment-2969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3019"></span>

<div id="answer-container-3019" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3019-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to <a href="https://bugzilla.redhat.com/show_bug.cgi?id=472631#c5">this comment</a> (on a Redhat bug), <code>gcry_cipher_setkey()</code> was changed from macro to function in libgcrypt-1.4.2.</p><p>I'm guessing that sunfreeware is compiling against a newer libgcrypt than you have installed. I'd suggest installing sunfreeware's libgcrypt package.</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '11, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '12, 07:07</p></div></div><div id="comments-container-3019" class="comments-container"></div><div id="comment-tools-3019" class="comment-tools"></div><div class="clear"></div><div id="comment-3019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

