+++
type = "question"
title = "(OSX) libcairo.2.dylib claims libfreetype.6.dylib provides an older package than it does"
description = '''Just updated from 1.5 to 1.6.5 on my Macbook Pro and now Wireshark will not launch. Checking the crash file, I see this: Dyld Error Message:  Library not loaded: /usr/X11/lib/libfreetype.6.dylib  Referenced from: /usr/X11/lib/libcairo.2.dylib  Reason: Incompatible library version: libcairo.2.dylib r...'''
date = "2012-03-22T13:58:00Z"
lastmod = "2012-03-22T14:09:00Z"
weight = 9711
keywords = [ "osx", "libfreetype", "libcairo" ]
aliases = [ "/questions/9711" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [(OSX) libcairo.2.dylib claims libfreetype.6.dylib provides an older package than it does](/questions/9711/osx-libcairo2dylib-claims-libfreetype6dylib-provides-an-older-package-than-it-does)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9711-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Just updated from 1.5 to 1.6.5 on my Macbook Pro and now Wireshark will not launch. Checking the crash file, I see this:</p><pre><code>Dyld Error Message:
  Library not loaded: /usr/X11/lib/libfreetype.6.dylib
  Referenced from: /usr/X11/lib/libcairo.2.dylib
  Reason: Incompatible library version: libcairo.2.dylib requires version 14.0.0 or later, but libfreetype.6.dylib provides version 13.0.0</code></pre><p>But if I check with otool, my libfreetype.6.dylib says it provides version 14.0.0. I also checked libcairo with otool and it says the libfreetype library provides version 14 as well. Any ideas as to a fix?</p><pre><code>  $ otool -L /usr/X11/lib/libfreetype.6.dylib
    /usr/X11/lib/libfreetype.6.dylib:
        /usr/X11/lib/libfreetype.6.dylib (compatibility version 14.0.0, current version 14.2.0)
        /usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.5)
        /usr/lib/libbz2.1.0.dylib (compatibility version 1.0.0, current version 1.0.5)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 159.1.0)

$ otool -L /usr/X11/lib/libcairo.2.dylib
    /usr/X11/lib/libcairo.2.dylib:
        /usr/X11/lib/libcairo.2.dylib (compatibility version 11003.0.0, current version 11003.2.0)
        /usr/X11/lib/libpixman-1.0.dylib (compatibility version 21.0.0, current version 21.2.0)
        /usr/X11/lib/libfontconfig.1.dylib (compatibility version 6.0.0, current version 6.4.0)
        /usr/X11/lib/libfreetype.6.dylib (compatibility version 14.0.0, current version 14.2.0)
        /usr/X11/lib/libpng15.15.dylib (compatibility version 20.0.0, current version 20.0.0)
        /usr/X11/lib/libxcb-shm.0.dylib (compatibility version 1.0.0, current version 1.0.0)
        /usr/X11/lib/libX11-xcb.1.dylib (compatibility version 2.0.0, current version 2.0.0)
        /usr/X11/lib/libxcb-render.0.dylib (compatibility version 1.0.0, current version 1.0.0)
        /usr/X11/lib/libxcb.1.dylib (compatibility version 3.0.0, current version 3.0.0)
        /usr/X11/lib/libXrender.1.dylib (compatibility version 5.0.0, current version 5.0.0)
        /usr/X11/lib/libX11.6.dylib (compatibility version 10.0.0, current version 10.0.0)
        /usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.5)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 159.1.0)</code></pre></div><div id="question-tags" class="tags-container tags">osx libfreetype libcairo</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '12, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/3f72c57f8a11b72028e39d8cfe61b6e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aubreyw&#39;s gravatar image" /><p>aubreyw<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aubreyw has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Mar '12, 13:58</p></div></div><div id="comments-container-9711" class="comments-container"></div><div id="comment-tools-9711" class="comment-tools"></div><div class="clear"></div><div id="comment-9711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9712"></span>

<div id="answer-container-9712" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9712-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Of course I figure it out right after I ask. Seems the dyld message was misleading. It was not trying to load /usr/X11/lib/libfreetype.6.dylib it was instead trying to use the one bundled with Wireshark.app - /Applications/Wireshark.app/Contents/Resources/lib/libfreetype.6.dylib or maybe its just an artifact from the 1.5 install that I upgraded from. Copied libfreetype.6.dylib from /usr/X11/lib into /Applications/Wireshark.app/Contents/Resources/lib and now it works fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '12, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/3f72c57f8a11b72028e39d8cfe61b6e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aubreyw&#39;s gravatar image" /><p>aubreyw<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aubreyw has one accepted answer">100%</span></p></div></div><div id="comments-container-9712" class="comments-container"><span id="19448"></span><div id="comment-19448" class="comment"><div id="post-19448-score" class="comment-score"></div><div class="comment-text"><p>I'm so glad you posted this solution. It wasn't so obvious to me. I just had the same error message after installing Maxima and trying to use its Gnuplot. Copying /usr/X11/lib/libfreetype.6.dylib into /Applications/Gnuplot.app/Contents/Resources/lib fixed it.</p></div><div id="comment-19448-info" class="comment-info"><span class="comment-age">(13 Mar '13, 07:03)</span> ferndoc</div></div></div><div id="comment-tools-9712" class="comment-tools"></div><div class="clear"></div><div id="comment-9712-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

