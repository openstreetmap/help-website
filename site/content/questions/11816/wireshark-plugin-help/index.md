+++
type = "question"
title = "Wireshark Plugin Help"
description = '''Hi All, Recently I began to work with Wireshark, so I have little experience with the &quot;plugin&quot; environment or setup. When I attempted to install the plugin by building Wireshark, I got the following errors. Could someone tell me what I&#x27;m doing wrong and/or what I can do to fix it? Thanks! Ian packet...'''
date = "2012-06-11T10:47:00Z"
lastmod = "2012-06-12T07:35:00Z"
weight = 11816
keywords = [ "u1077", "plugin", "wireshark", "error" ]
aliases = [ "/questions/11816" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Plugin Help](/questions/11816/wireshark-plugin-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11816-score" class="post-score" title="current number of votes">0</div><span id="post-11816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>Recently I began to work with Wireshark, so I have little experience with the "plugin" environment or setup. When I attempted to install the plugin by building Wireshark, I got the following errors. Could someone tell me what I'm doing wrong and/or what I can do to fix it?</p><p>Thanks!</p><p>Ian</p><pre><code>packet-ipa.c
c:\Program Files (x86)\wireshark\epan/reassemble.h(69) : error C2061: syntax error : identifier &#39;guint32&#39;

c:\Program Files (x86)\wireshark\epan/reassemble.h(70) : error C2061: syntax error : identifier &#39;offset&#39;

c:\Program Files (x86)\wireshark\epan/reassemble.h(70) : error C2059: syntax error : &#39;;&#39;</code></pre><p>[non-relevant errors snipped for brevity]</p><pre><code>NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\cl.EXE&quot;&#39; : return code &#39;0x2&#39;

Stop.

NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\
VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;

Stop.

NMAKE : fatal error U1077: &#39;if&#39; : return code &#39;0x2&#39;

Stop.

NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\
VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;

Stop.

NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\
VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;

Stop.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-u1077" rel="tag" title="see questions tagged &#39;u1077&#39;">u1077</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '12, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/40b1f396144af1f57dd3b8a211387e6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ian&#39;s gravatar image" /><p><span>Ian</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ian has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '12, 14:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-11816" class="comments-container"></div><div id="comment-tools-11816" class="comment-tools"></div><div class="clear"></div><div id="comment-11816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11820"></span>

<div id="answer-container-11820" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11820-score" class="post-score" title="current number of votes">1</div><span id="post-11820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ian has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>From the first error line you seem to be missing the path to glibconfig.h that has the definition of guint32. I suspect that your build environment is't set up correctly. Have you followed all the steps in the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Developers Guide</a> for Win32 builds exactly as laid out?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '12, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-11820" class="comments-container"><span id="11822"></span><div id="comment-11822" class="comment"><div id="post-11822-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>,</p><p>Thanks for that note, corrected that and half of the errors disappeared.</p></div><div id="comment-11822-info" class="comment-info"><span class="comment-age">(11 Jun '12, 12:12)</span> <span class="comment-user userinfo">Ian</span></div></div><span id="11824"></span><div id="comment-11824" class="comment"><div id="post-11824-score" class="comment-score"></div><div class="comment-text"><p>Okay, however, ...</p><pre><code>guint8 flags = tvb_get_guint8(tvb, offset);</code></pre><p>is still coming back as an improper use of the guint8 variable, why would this be? A previous use of guint8...</p><pre><code>guint8 packet_type = tvb_get_guint8(tvb,0);</code></pre><p>did indeed work, but why wouldn't the former line?</p></div><div id="comment-11824-info" class="comment-info"><span class="comment-age">(11 Jun '12, 12:30)</span> <span class="comment-user userinfo">Ian</span></div></div><span id="11828"></span><div id="comment-11828" class="comment"><div id="post-11828-score" class="comment-score"></div><div class="comment-text"><p>What's the exact error message for the error?</p><p>It's always best to ensure you can compile a standard copy of Wireshark before you try to add anything new. Have you managed that?</p></div><div id="comment-11828-info" class="comment-info"><span class="comment-age">(11 Jun '12, 13:10)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="11830"></span><div id="comment-11830" class="comment"><div id="post-11830-score" class="comment-score"></div><div class="comment-text"><p>I have indeed, and everything works fine, but this is the first plugin from scratch for me.</p><hr /><p><code> packet-ipa.c(284) : error C2275: 'guint8' : illegal use of this type as an expression C:\wireshark-win32-libs-1.6\gtk2\lib\glib2.0\include\glibconfig.h(36) : see declaration of 'guint8' packet-ipa.c(284) : error C2146: syntax error : missing ';' before identifier 'flags' packet-ipa.c(284) : error C2065: 'flags' : undeclared identifier</code></p></div><div id="comment-11830-info" class="comment-info"><span class="comment-age">(11 Jun '12, 13:22)</span> <span class="comment-user userinfo">Ian</span></div></div><span id="11832"></span><div id="comment-11832" class="comment"><div id="post-11832-score" class="comment-score"></div><div class="comment-text"><p>Possibly missing a statement terminator on the previous line?</p><p>Can you post a bit of context for the erroring statement?</p></div><div id="comment-11832-info" class="comment-info"><span class="comment-age">(11 Jun '12, 13:28)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="11836"></span><div id="comment-11836" class="comment not_top_scorer"><div id="post-11836-score" class="comment-score"></div><div class="comment-text"><p>Can't see the issue :-( Is flags declared earlier in the function?</p><p>When stuck like this I just comment out bits until I find what the compiler is upset about.</p></div><div id="comment-11836-info" class="comment-info"><span class="comment-age">(11 Jun '12, 13:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="11837"></span><div id="comment-11837" class="comment not_top_scorer"><div id="post-11837-score" class="comment-score"></div><div class="comment-text"><p>Ya, I did mass chunks of commenting and it compiled for the first time :) I'll keep at it, thanks!</p></div><div id="comment-11837-info" class="comment-info"><span class="comment-age">(11 Jun '12, 14:03)</span> <span class="comment-user userinfo">Ian</span></div></div><span id="11842"></span><div id="comment-11842" class="comment not_top_scorer"><div id="post-11842-score" class="comment-score"></div><div class="comment-text"><p>I think Anders nailed it. You can't declare flags there.</p></div><div id="comment-11842-info" class="comment-info"><span class="comment-age">(11 Jun '12, 15:56)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="11845"></span><div id="comment-11845" class="comment not_top_scorer"><div id="post-11845-score" class="comment-score"></div><div class="comment-text"><p>While this is true for .c files (I think this is part of the C standard), the usual VS error for this is: <code>error C2143: syntax error : missing ';' before 'type'</code>.</p><p>Using this file:</p><p><code>void main(void) {   int dummy = 0;   dummy = 4*2;   int dummy2 = dummy; }</code></p><p>Gives the output:</p><p><code>c:\users\graham\Documents&gt;cl test.c Microsoft (R) C/C++ Optimizing Compiler Version 16.00.40219.01 for x64 Copyright (C) Microsoft Corporation.  All rights reserved.</code></p><p><code></code></p><p><code>test.c test.c(5) : error C2143: syntax error : missing ';' before 'type'</code></p><p>The error is the same for VS2005 &amp; VS2010</p></div><div id="comment-11845-info" class="comment-info"><span class="comment-age">(12 Jun '12, 02:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="11846"></span><div id="comment-11846" class="comment not_top_scorer"><div id="post-11846-score" class="comment-score"></div><div class="comment-text"><p>if you compile that with <code>gcc -pedantic</code> it tells the reason for the error:</p><blockquote><p><code>[email protected]:/soft$ gcc -pedantic test.c</code><br />
<code>test.c:1:6: warning: return type of ‘main’ is not ‘int’ [-Wmain]</code><br />
<code>test.c: In function ‘main’:</code><br />
<code>test.c:5:1: warning:</code> <strong><code>ISO C90 forbids mixed declarations and code</code></strong> <code>[-pedantic]</code><br />
</p></blockquote><p>Seems to be the C90 standard. gcc accepts the code and does only warn with -pedantic.</p></div><div id="comment-11846-info" class="comment-info"><span class="comment-age">(12 Jun '12, 02:44)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11847"></span><div id="comment-11847" class="comment not_top_scorer"><div id="post-11847-score" class="comment-score"></div><div class="comment-text"><p>And that's why we declare all vars in dissectors at the start of the function, for portability. From the Developers Guide (1.1.1 Portability):</p><p>Don't declare variables in the middle of executable code; not all C compilers support that. Variables should be declared outside a function, or at the beginning of a function or compound statement.</p><p>Still not sure why the OP is getting a different error though.</p></div><div id="comment-11847-info" class="comment-info"><span class="comment-age">(12 Jun '12, 03:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="11849"></span><div id="comment-11849" class="comment not_top_scorer"><div id="post-11849-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Still not sure why the OP is getting a different error though.</p></blockquote><p>hard to say without the code. I assume your previous statement ("Possibly missing a statement terminator") nails it down, as uncommenting large parts of the code "fixes" the problem.</p></div><div id="comment-11849-info" class="comment-info"><span class="comment-age">(12 Jun '12, 05:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11854"></span><div id="comment-11854" class="comment not_top_scorer"><div id="post-11854-score" class="comment-score"></div><div class="comment-text"><p>Got it to work, thanks guys :)</p></div><div id="comment-11854-info" class="comment-info"><span class="comment-age">(12 Jun '12, 07:16)</span> <span class="comment-user userinfo">Ian</span></div></div><span id="11855"></span><div id="comment-11855" class="comment not_top_scorer"><div id="post-11855-score" class="comment-score"></div><div class="comment-text"><p>what was the problem?</p></div><div id="comment-11855-info" class="comment-info"><span class="comment-age">(12 Jun '12, 07:29)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11856"></span><div id="comment-11856" class="comment not_top_scorer"><div id="post-11856-score" class="comment-score"></div><div class="comment-text"><blockquote><p>And that's why we declare all vars in dissectors at the start of the function, for portability. From the Developers Guide (1.1.1 Portability):</p><p>Don't declare variables in the middle of executable code; not all C compilers support that. Variables should be declared outside a function, or at the beginning of a function or compound statement.</p></blockquote><hr /><p>What Graham said basically summed it up: VS didn't like me putting declarations within functions themselves, so I declared all vars that were giving me errors at the beginning :)</p></div><div id="comment-11856-info" class="comment-info"><span class="comment-age">(12 Jun '12, 07:35)</span> <span class="comment-user userinfo">Ian</span></div></div></div><div id="comment-tools-11820" class="comment-tools"><span class="comments-showing"> showing 5 of 15 </span> <a href="#" class="show-all-comments-link">show 10 more comments</a></div><div class="clear"></div><div id="comment-11820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11818"></span>

<div id="answer-container-11818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11818-score" class="post-score" title="current number of votes">0</div><span id="post-11818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a syntax error in your code either before or with the include statement for</p><blockquote><p><code>#include &lt;epan/reassemble.h&gt;</code><br />
</p></blockquote><p>Please post 10-20 lines of your code in front of the include statement.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '12, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-11818" class="comments-container"><span id="11821"></span><div id="comment-11821" class="comment"><div id="post-11821-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for replying so quickly, here's the lines.</p><h1 id="ifdef-have_config_h">ifdef HAVE_CONFIG_H</h1><h1 id="include-config.h">include "config.h"</h1><h1 id="endif">endif</h1><p>/ <em>Include only as needed</em> /</p><h1 id="include-stdio.h">include &lt;stdio.h&gt;</h1><h1 id="include-gmodule.h">include &lt;gmodule.h&gt;</h1><h1 id="include-stdlib.h">include &lt;stdlib.h&gt;</h1><h1 id="include-string.h">include &lt;string.h&gt;</h1><h1 id="include-glib.h">include &lt;glib.h&gt;</h1><h1 id="include-epan-packet.h">include &lt;epan packet.h=""&gt;</h1><h1 id="include-epan-prefs.h">include &lt;epan prefs.h=""&gt;</h1><h1 id="include-epan-emem.h">include &lt;epan emem.h=""&gt;</h1><h1 id="include-epan-reassemble.h">include &lt;epan reassemble.h=""&gt;</h1></div><div id="comment-11821-info" class="comment-info"><span class="comment-age">(11 Jun '12, 12:09)</span> <span class="comment-user userinfo">Ian</span></div></div><span id="11827"></span><div id="comment-11827" class="comment"><div id="post-11827-score" class="comment-score"></div><div class="comment-text"><p>the last include statements look pretty strange, but I guess that's just a copy-paste error with the Q&amp;A site, right?</p></div><div id="comment-11827-info" class="comment-info"><span class="comment-age">(11 Jun '12, 12:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11831"></span><div id="comment-11831" class="comment"><div id="post-11831-score" class="comment-score"></div><div class="comment-text"><p>Ya, it should be:</p><p>include &lt;epan.reassemble.h&gt; with the # in front</p></div><div id="comment-11831-info" class="comment-info"><span class="comment-age">(11 Jun '12, 13:23)</span> <span class="comment-user userinfo">Ian</span></div></div><span id="11834"></span><div id="comment-11834" class="comment"><div id="post-11834-score" class="comment-score">1</div><div class="comment-text"><p>Windows does not like declarations in the middle of the code, is that what you are doing?</p></div><div id="comment-11834-info" class="comment-info"><span class="comment-age">(11 Jun '12, 13:45)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="11835"></span><div id="comment-11835" class="comment"><div id="post-11835-score" class="comment-score"></div><div class="comment-text"><p>These are declarations at the top of the plugin I'm trying to write, and I was showing Kurt that the include statements should be correct.</p><pre><code>#ifdef HAVE_CONFIG_H
# include &quot;config.h&quot;
#endif

/* Include only as needed */
#include &lt;stdio.h&gt;
#include &lt;gmodule.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;

#include &lt;glib.h&gt;

#include &lt;epan/packet.h&gt;
#include &lt;epan/prefs.h&gt;
#include &lt;epan/emem.h&gt;
#include &lt;epan/reassemble.h&gt;</code></pre></div><div id="comment-11835-info" class="comment-info"><span class="comment-age">(11 Jun '12, 13:54)</span> <span class="comment-user userinfo">Ian</span></div></div><span id="11852"></span><div id="comment-11852" class="comment not_top_scorer"><div id="post-11852-score" class="comment-score"></div><div class="comment-text"><p>Loose the gmodule.h include.</p></div><div id="comment-11852-info" class="comment-info"><span class="comment-age">(12 Jun '12, 05:45)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-11818" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-11818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

