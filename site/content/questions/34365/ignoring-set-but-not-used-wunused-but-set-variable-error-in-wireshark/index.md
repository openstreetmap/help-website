+++
type = "question"
title = "Ignoring &quot;set but not used [-Wunused-but-set-variable]&quot; error in Wireshark"
description = '''I&#x27;m building an old version of wireshark (1.5.0) and I got in the compilation time 255 errors. Most if not all of them seem to be &quot;set but not used [-Wunused-but-set-variable]&quot;. I&#x27;m using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1). I want to just ignore them instead of working on fixing them for now...'''
date = "2014-07-02T15:35:00Z"
lastmod = "2014-07-02T15:59:00Z"
weight = 34365
keywords = [ "ignore", "compile", "gcc", "error" ]
aliases = [ "/questions/34365" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Ignoring "set but not used \[-Wunused-but-set-variable\]" error in Wireshark](/questions/34365/ignoring-set-but-not-used-wunused-but-set-variable-error-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34365-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm building an old version of wireshark (1.5.0) and I got in the compilation time 255 errors. Most if not all of them seem to be <strong>"set but not used [-Wunused-but-set-variable]"</strong>. I'm using <strong>gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1).</strong></p><p>I want to just ignore them instead of working on fixing them for now! One of the ways to accomplish this is descried in <a href="http://stackoverflow.com/questions/386220/how-can-i-hide-defined-but-not-used-warnings-in-gcc">here</a>. It uses <strong>Wno-unused-function</strong> which is one of the gcc flags. I want to try that solution but I'm not sure where can I implement it in my case (which files I need to modify and how?). There are more than one Makefile and when I searched the word gcc in my current build directory I found it occurs 18,643 times.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">ignore compile gcc error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '14, 15:35</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-34365" class="comments-container"></div><div id="comment-tools-34365" class="comment-tools"></div><div class="clear"></div><div id="comment-34365-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34367"></span>

<div id="answer-container-34367" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34367-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>(1.5.0 was a development release; you should probably be working on either 1.4.x or 1.6.x.)</p><p><code>-W</code> flags generate warnings; they're only errors if <code>-Werror</code> is being used. You should be able to specify <code>--disable-warnings-as-errors</code> to the configure script to cause <code>-Werror</code> not to be used. That will cause the build to succeed; <em>however</em>:</p><ul><li>you'll still get the warnings printed, so you'll still get a lot of noise from the build;</li><li><em>other</em> warnings won't be treated as errors;</li></ul><p>so if you <em>do</em> care about other warnings, removing <code>-Werror</code> won't help.</p><p>The SourceForge answer is, I suspect, wrong; the user complained about messages such as <code>'prefix_LineNumber' defined but not used</code> from code such as <code>CASSERT(isTrue) or CASSERT2(isTrue, prefix_)</code>, which sounds as if it's warning about unused <em>variables</em>, not unused <em>functions</em>. As the error message indicates, the <code>-W</code> flag causing the warnings you're seeing is <code>-Wunused-but-set-variable</code>, so you would either want to remove <code>-Wunused-but-set-variable</code> from the set of options or arrange that <code>-Wno-unused-but-set-variable</code> be in the set of options.</p><p>So, if you still want warnings to be treated as errors, but don't want <em>particular</em> warnings to be issued <em>at all</em>, then, <em>if</em> adding it to the options is sufficient, running the configure script as</p><pre><code>CFLAGS=-Wno-unused-but-set-variable ./configure</code></pre><p>would work. However, doing that might put <code>-Wno-unused-but-set-variable</code> into the options <em>before</em> <code>-Wunused-but-set-variable</code>, and the last of the options might rule. If that's the case, you might need to edit the configure script source file (probably called <code>configure.in</code> in that older release), remove the line that adds <code>-Wunused-but-set-variable</code>, re-run <code>./autogen.sh</code> to generate the configure script, and reconfigure. You would also remove whatever other warning options are causing issues.</p><p>But <code>--disable-warnings-as-errors</code> is the easiest way, so if you're willing to have a lot of warnings printed, but not have <em>any</em> warnings treated as errors, just do that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '14, 15:59</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-34367" class="comments-container"><span id="34479"></span><div id="comment-34479" class="comment"><div id="post-34479-score" class="comment-score"></div><div class="comment-text"><p>Thanks your answer! It helps a lot. Wireshark is working perfect now after using in the configuration part</p><p>CFLAGS="-Wno-unused-but-set-variable" ./configure --disable-warnings-as-errors</p></div><div id="comment-34479-info" class="comment-info"><span class="comment-age">(08 Jul '14, 14:36)</span> flora</div></div></div><div id="comment-tools-34367" class="comment-tools"></div><div class="clear"></div><div id="comment-34367-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

