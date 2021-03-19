+++
type = "question"
title = "Installing an old version of Wireshark"
description = '''Hi guys, I need to install from source the 1.0.2 version of wireshark. After running the make command I get the following error: /usr/bin/ld: gtk/libui.a(sctp_graph_dlg.o): undefined reference to symbol &#x27;floor@@GLIBC_2.2.5&#x27; /usr/bin/ld: note: &#x27;floor@@GLIBC_2.2.5&#x27; is defined in DSO /lib/x86_64-linux-...'''
date = "2013-08-16T16:17:00Z"
lastmod = "2013-08-16T16:17:00Z"
weight = 23834
keywords = [ "old", "installation", "wireshark" ]
aliases = [ "/questions/23834" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Installing an old version of Wireshark](/questions/23834/installing-an-old-version-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23834-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I need to install from source the 1.0.2 version of wireshark. After running the make command I get the following error:</p><pre><code>/usr/bin/ld: gtk/libui.a(sctp_graph_dlg.o): undefined reference to symbol &#39;[email protected]@GLIBC_2.2.5&#39;
/usr/bin/ld: note: &#39;[email protected]@GLIBC_2.2.5&#39; is defined in DSO /lib/x86_64-linux-gnu/libm.so.6 so try adding it to the linker command line
/lib/x86_64-linux-gnu/libm.so.6: could not read symbols: Invalid operation
collect2: error: ld returned 1 exit status
make[2]: *** [wireshark] Error 1
make[2]: Leaving directory `/home/andre/Documents/wireshark_source_3/wireshark-1.0.2&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/andre/Documents/wireshark_source_3/wireshark-1.0.2&#39;
make: *** [all] Error 2</code></pre><p>Any Ideas?</p></div><div id="question-tags" class="tags-container tags">old installation wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Aug '13, 16:17</strong></p><img src="https://secure.gravatar.com/avatar/fdbc91810fafdddfb7b893d55830e03d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andr%C3%A9%20de%20Melo&#39;s gravatar image" /><p>André de Melo<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="André de Melo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Aug '13, 18:19</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-23834" class="comments-container"><span id="23861"></span><div id="comment-23861" class="comment"><div id="post-23861-score" class="comment-score"></div><div class="comment-text"><p>what is your OS (brand and version)?</p><p>BTW: Why do you need 1.0.2?</p></div><div id="comment-23861-info" class="comment-info"><span class="comment-age">(20 Aug '13, 01:59)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-23834" class="comment-tools"></div><div class="clear"></div><div id="comment-23834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

