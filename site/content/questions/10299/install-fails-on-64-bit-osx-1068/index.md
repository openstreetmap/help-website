+++
type = "question"
title = "Install fails on 64 bit OSX 10.6.8"
description = '''I just downloaded the latest stable OS X 10.6 and later Intel 64-bit .dmg from wireshark.org, and installed it on a MacBook Pro running OS X 10.6.8. The same error occurs when attempting to start wireshark. Seems as though the wireshark installation is broken not this user&#x27;s mac.  Would someone on t...'''
date = "2012-04-19T12:08:00Z"
lastmod = "2012-04-19T12:08:00Z"
weight = 10299
keywords = [ "osx", "install" ]
aliases = [ "/questions/10299" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Install fails on 64 bit OSX 10.6.8](/questions/10299/install-fails-on-64-bit-osx-1068)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10299-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just downloaded the latest stable OS X 10.6 and later Intel 64-bit .dmg from <a href="http://wireshark.org">wireshark.org</a>, and installed it on a MacBook Pro running OS X 10.6.8. The same error occurs when attempting to start wireshark. Seems as though the wireshark installation is broken not this user's mac.<br />
</p><p>Would someone on the wireshark team please look in to fixing this? Why do you need to link to such new libraries anyhow? Mac no longer supports X11 seems to me you should be using native Mac Graphics if you are only going to distribute Mac and Windows installs.</p><p>Building the code on linux is problematic due to all of the dependencies being so new in wireshark that YUM and other distro tools haven't caught up. This translates into much pain trying to get the blasted thing to run.</p></div><div id="question-tags" class="tags-container tags">osx install</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '12, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/36c739aedf31baf750724dfcb263fe8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WantaKnow&#39;s gravatar image" /><p>WantaKnow<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WantaKnow has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 19 Apr '12, 12:20</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10299" class="comments-container"><span id="10302"></span><div id="comment-10302" class="comment"><div id="post-10302-score" class="comment-score"></div><div class="comment-text"><p>I converted your answer to a question as that is how this site works, please read the FAQ.</p><p>I'm sure the issue will be resolved once a Mac owning volunteer finds enough of their own personal time available to work on a solution.</p></div><div id="comment-10302-info" class="comment-info"><span class="comment-age">(19 Apr '12, 12:22)</span> grahamb ♦</div></div><span id="10311"></span><div id="comment-10311" class="comment"><div id="post-10311-score" class="comment-score"></div><div class="comment-text"><p>What is the error that occurs? My machine is running 10.6.8 with all the security updates, and has libfreetype with a compatibility version of 14.0.0:</p><pre><code>$ otool -L /usr/X11/lib/libfreetype.6.dylib
/usr/X11/lib/libfreetype.6.dylib:
/usr/X11/lib/libfreetype.6.dylib (compatibility version 14.0.0, current version 14.2.0)</code></pre><p>and that appears to be what the current Snow Leopard dmgs require.</p></div><div id="comment-10311-info" class="comment-info"><span class="comment-age">(19 Apr '12, 14:41)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-10299" class="comment-tools"></div><div class="clear"></div><div id="comment-10299-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

