+++
type = "question"
title = "How to specify path of libgcc during tshark compilation??"
description = '''Hi, I am compiling tshark 1.6.14 on Solaris 10. On Solaris 10 server, libgcc 3.4.3 version is installed. Tshark is not getting compiled with libgcc 3.4.3 due to tshark issue 7637. As mentioned in bug 7637, I am now compiling tshark with libgcc 4.2.4. I compiled libgcc 4.2.4 and installed it in /opt/...'''
date = "2013-04-22T19:47:00Z"
lastmod = "2014-01-06T03:51:00Z"
weight = 20724
keywords = [ "tshark" ]
aliases = [ "/questions/20724" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to specify path of libgcc during tshark compilation??](/questions/20724/how-to-specify-path-of-libgcc-during-tshark-compilation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20724-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am compiling tshark 1.6.14 on Solaris 10. On Solaris 10 server, libgcc 3.4.3 version is installed. Tshark is not getting compiled with libgcc 3.4.3 due to tshark <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7637">issue 7637</a>.</p><p>As mentioned in bug 7637, I am now compiling tshark with libgcc 4.2.4. I compiled libgcc 4.2.4 and installed it in /opt/libgcc-4.2.4 directory. I don't want to install libgcc in default directory (/usr) as this server is being used for compilation of many other software. Two version of libgcc may conflict with others.</p><p>Is there any way to specify the path of libgcc in "Configure" command (something like --with-libgcc=/opt/libgcc-4.2.4)??</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Apr '13, 19:47</strong></p><img src="https://secure.gravatar.com/avatar/a273217076451fb71206e452cf39243e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="friends&#39;s gravatar image" /><p>friends<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="friends has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Apr '13, 22:40</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-20724" class="comments-container"><span id="28551"></span><div id="comment-28551" class="comment"><div id="post-28551-score" class="comment-score"></div><div class="comment-text"><p>I am also very concerned about this problem！</p><p>(Converted to a comment as per the way ask.wireshark.org works. Please see the FAQ).</p></div><div id="comment-28551-info" class="comment-info"><span class="comment-age">(03 Jan '14, 08:13)</span> mathzzz</div></div></div><div id="comment-tools-20724" class="comment-tools"></div><div class="clear"></div><div id="comment-20724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28597"></span>

<div id="answer-container-28597" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28597-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess the config help output would give you hints here. For instance:</p><pre><code>  LDFLAGS     linker flags, e.g. -L&lt;lib dir&gt; if you have libraries in a
              nonstandard directory &lt;lib dir&gt;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '14, 03:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-28597" class="comments-container"></div><div id="comment-tools-28597" class="comment-tools"></div><div class="clear"></div><div id="comment-28597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

