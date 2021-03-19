+++
type = "question"
title = "qt5.9 fails to build on Solaris10"
description = '''Building Wireshark 2.4.2 on Solaris10 i386 VMware. build fails with QT missing. Building qt-everywhere-opensource-src-5.9.2 Tools: gmake-3.82, g++-5.3.0, ld/ar-2.29 Libs: libgcrypt-1.8.1, libgpg-error-1.27, binutils-2.29, mpfr-3.1.4, mpc-1.0.3, libiconv-1.14 ./configure –prefix $PWD/qtbase –opensour...'''
date = "2017-10-26T03:29:00Z"
lastmod = "2017-10-26T03:29:00Z"
weight = 64221
keywords = [ "qt5", "solaris", "build-error" ]
aliases = [ "/questions/64221" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [qt5.9 fails to build on Solaris10](/questions/64221/qt59-fails-to-build-on-solaris10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64221-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Building Wireshark 2.4.2 on Solaris10 i386 VMware. build fails with QT missing.</p><p>Building qt-everywhere-opensource-src-5.9.2<br />
Tools: gmake-3.82, g++-5.3.0, ld/ar-2.29<br />
Libs: libgcrypt-1.8.1, libgpg-error-1.27, binutils-2.29, mpfr-3.1.4, mpc-1.0.3, libiconv-1.14</p><p>./configure –prefix $PWD/qtbase –opensource –confirm-license –nomake tests –qt-xcb –platform solaris-g++<br />
gmake – error message<br />
ld: libQt5core.so.5.9.2: version node not found for symbol [email protected]_5.6<br />
ld: failed to set dynamic section sizes: Bad value</p><p>Looks like Qt sees a mismatch of 5.6 vs 5.9.2, but where?<br />
Any thoughts?</p></div><div id="question-tags" class="tags-container tags">qt5 solaris build-error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '17, 03:29</strong></p><img src="https://secure.gravatar.com/avatar/fff1fc9cdef54373801e6f3d0cfa3449?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kevin-gmail&#39;s gravatar image" /><p>kevin-gmail<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kevin-gmail has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-64221" class="comments-container"></div><div id="comment-tools-64221" class="comment-tools"></div><div class="clear"></div><div id="comment-64221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

