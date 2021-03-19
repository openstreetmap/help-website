+++
type = "question"
title = "Wireshark GTK Compilation error"
description = '''I am working to port wireshark(1.6.4) to iOS, and a am getting a GTK compilation error when running the configure script. It seems that the GTK version is undetermined as justified by these lines in the config.log file configure:19423: gcc -o conftest -no-cpp-precomp -D_U_=&quot;__attribute__((unused))&quot; ...'''
date = "2011-12-19T08:19:00Z"
lastmod = "2011-12-19T14:17:00Z"
weight = 8042
keywords = [ "versions", "gtk", "ios", "port", "error" ]
aliases = [ "/questions/8042" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark GTK Compilation error](/questions/8042/wireshark-gtk-compilation-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8042-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8042-score" class="post-score" title="current number of votes">1</div><span id="post-8042-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working to port wireshark(1.6.4) to iOS, and a am getting a GTK compilation error when running the configure script. It seems that the GTK version is undetermined as justified by these lines in the config.log file</p><pre><code>configure:19423: gcc -o conftest -no-cpp-precomp -D_U_=&quot;__attribute__((unused))&quot; -g -O2 -Wall -W -Wextra -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wno-pointer-sign -Wcast-align -Wformat-security -I/usr/local/include   -I/usr/local/include -Wl,-search_paths_first  -L/usr/local/lib conftest.c   &gt;&amp;5
Undefined symbols:
  &quot;_gtk_micro_version&quot;, referenced from:
      _gtk_micro_version$non_lazy_ptr in ccxkEWm4.o
  &quot;_gtk_major_version&quot;, referenced from:
      _gtk_major_version$non_lazy_ptr in ccxkEWm4.o
  &quot;_gtk_minor_version&quot;, referenced from:
      _gtk_minor_version$non_lazy_ptr in ccxkEWm4.o
ld: symbol(s) not found
collect2: ld returned 1 exit status</code></pre><p>Full config.log can be found at: <a href="http://ininjas.com/trcx/config.log">http://ininjas.com/trcx/config.log</a></p><p>The GTK developers said this is because wireshark is not using "<em>PKG_CHECK_MODULES()</em>" but instead "<em>AM_PATH_GTK()</em>". My question is twofold:</p><p>1) How could I bypass this error? For some reason the configure script does not seem to recognize the --disable-gtktest flag. I do not think this is the way to go as wireshark it's self may reference these variables. What would be the best way to patch this?</p><p>2) What is the best way to get this updated for future releases to use PKG_CHECK_MODULES(). The GTK developers seemed to infer that this is the officially supported way to check the GTK version.<br />
</p><p>Any advice is appreciated.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-versions" rel="tag" title="see questions tagged &#39;versions&#39;">versions</span> <span class="post-tag tag-link-gtk" rel="tag" title="see questions tagged &#39;gtk&#39;">gtk</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span> <span class="post-tag tag-link-port" rel="tag" title="see questions tagged &#39;port&#39;">port</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '11, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/983a2a3cdc85c20e90972fdb108319e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trcx&#39;s gravatar image" /><p><span>Trcx</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trcx has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-8042" class="comments-container"></div><div id="comment-tools-8042" class="comment-tools"></div><div class="clear"></div><div id="comment-8042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8050"></span>

<div id="answer-container-8050" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8050-score" class="post-score" title="current number of votes">0</div><span id="post-8050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ol><li>If the GTK+ developers say <code>PKG_CHECK_MODULES</code> should be used, rather than <code>AM_PATH_GTK</code>, the best way to patch this would probably be to change <code>configure.in</code> to use <code>PKG_CHECK_MODULES</code>, run the <code>autogen.sh</code> script, and re-run the <code>configure</code> script.</li><li>The best way to get this updated for future releases would be to file a bug at the <a href="http://bugs.wireshark.org/">Wireshark Bugzilla</a>.</li><li>While I'm at it, you might want to work from SVN rather than a source tarball, if you're not already working from SVN, if you're doing that much development work. (Presumably this is for jailbroken iOS machines....)</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Dec '11, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Dec '11, 14:18</strong> </span></p></div></div><div id="comments-container-8050" class="comments-container"></div><div id="comment-tools-8050" class="comment-tools"></div><div class="clear"></div><div id="comment-8050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

