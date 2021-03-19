+++
type = "question"
title = "Plugin Dissector Compilation Error &quot;request for implicit conversion ..&quot;"
description = '''I&#x27;m trying to test a dissector plug in for wireshark in Linux by following these steps. When I use sudo make -C plugins, I get several similar compilation errors say that MySourceFileDissectorName.c: In function &#x27;X&#x27;: MySourceFileDissectorName.c:990:11: error: request for implicit conversion from &#x27;gp...'''
date = "2014-06-15T14:18:00Z"
lastmod = "2014-06-15T15:49:00Z"
weight = 33849
keywords = [ "make", "plugin", "error", "wireshark" ]
aliases = [ "/questions/33849" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Plugin Dissector Compilation Error "request for implicit conversion .."](/questions/33849/plugin-dissector-compilation-error-request-for-implicit-conversion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to test a dissector plug in for wireshark in Linux by following <a href="http://stackoverflow.com/questions/4905846/how-do-i-compile-this-plugin">these steps</a>. When I use <strong>sudo make -C plugins</strong>, I get several similar compilation errors say that MySourceFileDissectorName.c: In function 'X': MySourceFileDissectorName.c:990:11: error: request for implicit conversion from 'gpointer' to 'some struct data type *' not permitted in C++ [-Werror=c++-compat] .... etc.</p><p>I've no idea what the cause of the error or how can I resolve it. Any ideas or hints!</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">make plugin error wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '14, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-33849" class="comments-container"><span id="33859"></span><div id="comment-33859" class="comment"><div id="post-33859-score" class="comment-score"></div><div class="comment-text"><blockquote><p><strong>sudo make -C plugins</strong></p></blockquote><p>You should not run your compiler as root. Neither should you run Wireshark as root.</p></div><div id="comment-33859-info" class="comment-info"><span class="comment-age">(16 Jun '14, 02:28)</span> Jaap ♦</div></div><span id="33867"></span><div id="comment-33867" class="comment"><div id="post-33867-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your comment but Why not?!</p></div><div id="comment-33867-info" class="comment-info"><span class="comment-age">(16 Jun '14, 10:45)</span> flora</div></div><span id="33868"></span><div id="comment-33868" class="comment"><div id="post-33868-score" class="comment-score">1</div><div class="comment-text"><p>Because any program running as root has the ability to do many more harmful things to your system than a program running under your own user ID, so a bug (or misfeature!) in the compiler, or linker, or "make", or Wireshark, or... can cause more problems if you run the program as root than if you run it as yourself.</p></div><div id="comment-33868-info" class="comment-info"><span class="comment-age">(16 Jun '14, 10:52)</span> Guy Harris ♦♦</div></div><span id="33870"></span><div id="comment-33870" class="comment"><div id="post-33870-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much Guy! I've come across Jaap's comment several times in different contexts and just now I knew the reason behind that.</p></div><div id="comment-33870-info" class="comment-info"><span class="comment-age">(16 Jun '14, 11:22)</span> flora</div></div></div><div id="comment-tools-33849" class="comment-tools"></div><div class="clear"></div><div id="comment-33849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33855"></span>

<div id="answer-container-33855" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33855-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The cause of the error is that</p><ul><li>C++, unlike C, does not allow <code>void *</code> (<code>gpointer</code> is a GLib alias for <code>void *</code>) to be cast to another type value without a case;</li><li>we want to make sure our C code can be compiled by C++ compilers;</li></ul><p>so we build the code with "-Werror=c++-compat".</p><p>You resolve it by doing</p><pre><code>void *foo;
struct hello *bar;

    ...

bar = (struct hello *)foo;</code></pre><p>rather than</p><pre><code>void *foo;
struct hello *bar;

    ...

bar = foo;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '14, 15:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-33855" class="comments-container"><span id="33866"></span><div id="comment-33866" class="comment"><div id="post-33866-score" class="comment-score"></div><div class="comment-text"><p>Thank you. This solves the problem.</p></div><div id="comment-33866-info" class="comment-info"><span class="comment-age">(16 Jun '14, 09:24)</span> flora</div></div></div><div id="comment-tools-33855" class="comment-tools"></div><div class="clear"></div><div id="comment-33855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

