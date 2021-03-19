+++
type = "question"
title = "Wireshark build fails when trying to compile plugin"
description = '''Hi,  I&#x27;m trying to compile a plugin for Wireshark version 1.10.5 and am getting the following error: c:&#92;wireshark&#92;epan&#92;except.h(97) : error C2054: expected &#x27;(&#x27; to follow &#x27;WS_MSVC_NORETURN&#x27; c:&#92;wireshark&#92;epan&#92;except.h(97) : error C2085: &#x27;except_rethrow&#x27; : not in formal parameter list c:&#92;wireshark&#92;epan...'''
date = "2014-01-13T08:07:00Z"
lastmod = "2014-01-14T10:02:00Z"
weight = 28843
keywords = [ "windows", "failed", "build", "plugin" ]
aliases = [ "/questions/28843" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark build fails when trying to compile plugin](/questions/28843/wireshark-build-fails-when-trying-to-compile-plugin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28843-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to compile a plugin for Wireshark version 1.10.5 and am getting the following error:</p><pre><code>c:\wireshark\epan\except.h(97) : error C2054: expected &#39;(&#39; to follow &#39;WS_MSVC_NORETURN&#39;
c:\wireshark\epan\except.h(97) : error C2085: &#39;except_rethrow&#39; : not in formal parameter list
c:\wireshark\epan\except.h(98) : error C2082: redefinition of formal parameter &#39;WS_MSVC_NORETURN&#39;
c:\wireshark\epan\except.h(98) : error C2143: syntax error : missing &#39;;&#39; before &#39;type&#39;
c:\wireshark\epan\except.h(98) : error C2085: &#39;except_throw&#39; : not in formal parameter list
c:\wireshark\epan\except.h(99) : error C2082: redefinition of formal parameter &#39;WS_MSVC_NORETURN&#39;
c:\wireshark\epan\except.h(99) : error C2143: syntax error : missing &#39;;&#39; before &#39;type&#39;
c:\wireshark\epan\except.h(99) : error C2085: &#39;except_throwd&#39; : not in formal parameter list
c:\wireshark\epan\except.h(100) : error C2082: redefinition of formal parameter &#39;WS_MSVC_NORETURN&#39;
c:\wireshark\epan\except.h(100) : error C2143: syntax error : missing &#39;;&#39; before &#39;type&#39;
c:\wireshark\epan\except.h(100) : error C2085: &#39;except_throwf&#39; : not in formal parameter list
c:\wireshark\epan\except.h(101) : error C2085: &#39;except_unhandled_catcher&#39; : not in formal parameter list
c:\wireshark\epan\except.h(102) : error C2085: &#39;except_code&#39; : not in formal parameter list
c:\wireshark\epan\except.h(103) : error C2085: &#39;except_group&#39; : not in formal parameter list
c:\wireshark\epan\except.h(104) : error C2085: &#39;except_message&#39; : not in formal parameter list
c:\wireshark\epan\except.h(105) : error C2085: &#39;except_data&#39; : not in formal parameter list
c:\wireshark\epan\except.h(106) : error C2085: &#39;except_take_data&#39; : not in formal parameter list
c:\wireshark\epan\except.h(107) : error C2085: &#39;except_set_allocator&#39; : not in formal parameter list
c:\wireshark\epan\except.h(108) : error C2085: &#39;except_alloc&#39; : not in formal parameter list
c:\wireshark\epan\except.h(109) : error C2085: &#39;except_free&#39; : not in formal parameter list
C:\wireshark\epan/tvbuff.h(59) : error C2085: &#39;tvbuff_type&#39; : not in formal parameter list
C:\wireshark\epan/tvbuff.h(70) : error C2085: &#39;tvb_backing_t&#39; : not in formal parameter list
C:\wireshark\epan/tvbuff.h(81) : error C2085: &#39;tvb_comp_t&#39; : not in formal parameter list
C:\wireshark\epan/tvbuff.h(83) : error C2085: &#39;tvbuff_free_cb_t&#39; : not in formal parameter list
C:\wireshark\epan/tvbuff.h(87) : error C2016: C requires that a struct or union has at least one member
C:\wireshark\epan/tvbuff.h(87) : error C2061: syntax error : identifier &#39;tvbuff_type&#39;
C:\wireshark\epan/tvbuff.h(100) : error C2016: C requires that a struct or union has at least one member
C:\wireshark\epan/tvbuff.h(100) : error C2061: syntax error : identifier &#39;tvb_backing_t&#39;
C:\wireshark\epan/tvbuff.h(101) : error C2061: syntax error : identifier &#39;composite&#39;
C:\wireshark\epan/tvbuff.h(101) : error C2059: syntax error : &#39;;&#39;               
C:\wireshark\epan/tvbuff.h(102) : error C2059: syntax error : &#39;}&#39;
C:\wireshark\epan/tvbuff.h(122) : error C2061: syntax error : identifier &#39;free_cb&#39;
C:\wireshark\epan/tvbuff.h(122) : error C2059: syntax error : &#39;;&#39;
C:\wireshark\epan/tvbuff.h(123) : error C2059: syntax error : &#39;}&#39;
C:\wireshark\epan/tvbuff.h(158) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(179) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(179) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(179) : error C2059: syntax error : &#39;)&#39;               
C:\wireshark\epan/tvbuff.h(179) : error C2059: syntax error : &#39;;&#39;
C:\wireshark\epan/tvbuff.h(182) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(182) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(182) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(182) : error C2059: syntax error : &#39;;&#39;
C:\wireshark\epan/tvbuff.h(185) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(185) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(185) : error C2059: syntax error : &#39;,&#39;
C:\wireshark\epan/tvbuff.h(185) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(192) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(192) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(192) : error C2059: syntax error : &#39;,&#39;
C:\wireshark\epan/tvbuff.h(192) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(198) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(198) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(198) : error C2059: syntax error : &#39;,&#39;
C:\wireshark\epan/tvbuff.h(198) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(210) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(210) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(210) : error C2143: syntax error : missing &#39;;&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(210) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(212) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(212) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(212) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(212) : error C2371: &#39;guint8&#39; : redefinition; different basic types
        C:\wireshark-win32-libs-1.6\gtk2\lib\glib-2.0\include\glibconfig.h(36) : see declaration of &#39;guint8&#39;
C:\wireshark\epan/tvbuff.h(212) : warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored
C:\wireshark\epan/tvbuff.h(212) : error C2143: syntax error : missing &#39;;&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(212) : warning C4142: benign redefinition of type
C:\wireshark\epan/tvbuff.h(212) : error C2370: &#39;guint&#39; : redefinition; different storage class
        C:\wireshark-win32-libs-1.6\gtk2\include\glib-2.0\glib/gtypes.h(56) : see declaration of &#39;guint&#39;
C:\wireshark\epan/tvbuff.h(212) : warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored
C:\wireshark\epan/tvbuff.h(212) : error C2146: syntax error : missing &#39;;&#39; before identifier &#39;length&#39;
C:\wireshark\epan/tvbuff.h(212) : warning C4142: benign redefinition of type
C:\wireshark\epan/tvbuff.h(213) : error C2059: syntax error : &#39;type&#39;
C:\wireshark\epan/tvbuff.h(213) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(216) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(216) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(216) : error C2059: syntax error : &#39;,&#39;
C:\wireshark\epan/tvbuff.h(217) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(220) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(237) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(237) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(237) : error C2143: syntax error : missing &#39;;&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(238) : error C2370: &#39;gint&#39; : redefinition; different storage class
        C:\wireshark-win32-libs-1.6\gtk2\include\glib-2.0\glib/gtypes.h(50) : see declaration of &#39;gint&#39;
C:\wireshark\epan/tvbuff.h(238) : warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored
C:\wireshark\epan/tvbuff.h(238) : error C2146: syntax error : missing &#39;;&#39; before identifier &#39;backing_offset&#39;
C:\wireshark\epan/tvbuff.h(238) : error C2059: syntax error : &#39;type&#39;
C:\wireshark\epan/tvbuff.h(238) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(242) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(242) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(242) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(243) : error C2370: &#39;gint&#39; : redefinition; different storage class
        C:\wireshark-win32-libs-1.6\gtk2\include\glib-2.0\glib/gtypes.h(50) : see declaration of &#39;gint&#39;
C:\wireshark\epan/tvbuff.h(243) : warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored
C:\wireshark\epan/tvbuff.h(243) : error C2146: syntax error : missing &#39;;&#39; before identifier &#39;backing_offset&#39;
C:\wireshark\epan/tvbuff.h(243) : error C2059: syntax error : &#39;type&#39;
C:\wireshark\epan/tvbuff.h(243) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(247) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(247) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(247) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(248) : error C2370: &#39;gint&#39; : redefinition; different storage class
        C:\wireshark-win32-libs-1.6\gtk2\include\glib-2.0\glib/gtypes.h(50) : see declaration of &#39;gint&#39;
C:\wireshark\epan/tvbuff.h(248) : warning C4228: nonstandard extension used : qualifiers after comma in declarator list are ignored
C:\wireshark\epan/tvbuff.h(248) : error C2146: syntax error : missing &#39;;&#39; before identifier &#39;backing_offset&#39;
C:\wireshark\epan/tvbuff.h(248) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(255) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(255) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(255) : error C2143: syntax error : missing &#39;;&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(255) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(258) : error C2143: syntax error : missing &#39;)&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(258) : error C2143: syntax error : missing &#39;{&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(258) : error C2143: syntax error : missing &#39;;&#39; before &#39;*&#39;
C:\wireshark\epan/tvbuff.h(258) : error C2059: syntax error : &#39;)&#39;
C:\wireshark\epan/tvbuff.h(258) : fatal error C1003: error count exceeds 100; stopping compilation
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\cl.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>I know this question is similar to <a href="http://ask.wireshark.org/questions/15580/windows-build-suddenly-failed-after-svn-sync">http://ask.wireshark.org/questions/15580/windows-build-suddenly-failed-after-svn-sync</a> but the solution to this question didnt help me. I tried changing the include in my plugin file the way the solution to that question suggested and the build still failed. Also when i tried to build this plugin using version 1.11.3 it worked fine, however i need to use 1.10.5 so i dont know what to do.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">windows failed build plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '14, 08:07</strong></p><img src="https://secure.gravatar.com/avatar/5858984777c528900a115852219a1814?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hockeyfreak889&#39;s gravatar image" /><p>Hockeyfreak889<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hockeyfreak889 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Jan '14, 08:47</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-28843" class="comments-container"><span id="28856"></span><div id="comment-28856" class="comment"><div id="post-28856-score" class="comment-score"></div><div class="comment-text"><p>There are API and changes to #includes between 1.10.x and 1.11.x so I'd compare with the includes of the plugins that ship with 1.10.x. If you show us the include section of your plugin we might be able to figure out what the problem is.</p></div><div id="comment-28856-info" class="comment-info"><span class="comment-age">(14 Jan '14, 03:40)</span> Anders ♦</div></div><span id="28858"></span><div id="comment-28858" class="comment"><div id="post-28858-score" class="comment-score"></div><div class="comment-text"><p>the include section of the plugin consists of the following:</p><pre><code>#include &quot;config.h&quot;
#include &lt;glib.h&gt;
#include &lt;epan\packet.h&gt;
</code></pre><p>Note: The Q&amp;A markup doesn't play nicely with #includes.</p></div><div id="comment-28858-info" class="comment-info"><span class="comment-age">(14 Jan '14, 05:56)</span> Hockeyfreak889</div></div><span id="28871"></span><div id="comment-28871" class="comment"><div id="post-28871-score" class="comment-score"></div><div class="comment-text"><p>I don't have a 1.10 ref handy, how is "config.h" included in the "standard" plugins?</p></div><div id="comment-28871-info" class="comment-info"><span class="comment-age">(14 Jan '14, 09:24)</span> Anders ♦</div></div><span id="28872"></span><div id="comment-28872" class="comment"><div id="post-28872-score" class="comment-score"></div><div class="comment-text"><p>1.10 plugins that is.</p></div><div id="comment-28872-info" class="comment-info"><span class="comment-age">(14 Jan '14, 09:24)</span> Anders ♦</div></div><span id="28873"></span><div id="comment-28873" class="comment"><div id="post-28873-score" class="comment-score"></div><div class="comment-text"><p>Looking at <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.10/plugins/gryphon/packet-gryphon.c?revision=48968&amp;view=markup">packet-gryphon.c</a> as an example, it's just:</p><pre><code>#include &quot;config.h&quot;</code></pre></div><div id="comment-28873-info" class="comment-info"><span class="comment-age">(14 Jan '14, 09:34)</span> cmaynard ♦♦</div></div><span id="28875"></span><div id="comment-28875" class="comment not_top_scorer"><div id="post-28875-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Microsoft Visual Studio 9.0</p></blockquote><p>Is that a supported build platform?</p></div><div id="comment-28875-info" class="comment-info"><span class="comment-age">(14 Jan '14, 10:03)</span> Kurt Knochner ♦</div></div><span id="28877"></span><div id="comment-28877" class="comment not_top_scorer"><div id="post-28877-score" class="comment-score"></div><div class="comment-text"><p>The <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">Developer's Guide</a> mentions MSVC 2010 because that's what the official releases use, but MSVC 2008 is still supported, as indicated in section <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChToolsMSChain.html#idp352149148">4.4.1 Toolchain Package Alternatives</a>.</p></div><div id="comment-28877-info" class="comment-info"><span class="comment-age">(14 Jan '14, 10:13)</span> cmaynard ♦♦</div></div><span id="28879"></span><div id="comment-28879" class="comment not_top_scorer"><div id="post-28879-score" class="comment-score"></div><div class="comment-text"><p>O.K. thanks</p></div><div id="comment-28879-info" class="comment-info"><span class="comment-age">(14 Jan '14, 10:20)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28843" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-28843-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28874"></span>

<div id="answer-container-28874" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28874-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try carefully reviewing <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.10/doc/README.plugins?revision=48968&amp;view=markup">README.plugins</a> and comparing your plugin files to other plugins, such as <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.10/plugins/gryphon/">gryphon</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '14, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-28874" class="comments-container"><span id="28882"></span><div id="comment-28882" class="comment"><div id="post-28882-score" class="comment-score"></div><div class="comment-text"><p>Thanks that helped. Im not really sure what exactly i changed but when i redid all the files the way the README suggested it worked after.</p></div><div id="comment-28882-info" class="comment-info"><span class="comment-age">(14 Jan '14, 11:03)</span> Hockeyfreak889</div></div><span id="28884"></span><div id="comment-28884" class="comment"><div id="post-28884-score" class="comment-score">1</div><div class="comment-text"><p>What exactly did you change (before/after)? Might be interesting for others as well.</p></div><div id="comment-28884-info" class="comment-info"><span class="comment-age">(14 Jan '14, 11:07)</span> Kurt Knochner ♦</div></div><span id="28929"></span><div id="comment-28929" class="comment"><div id="post-28929-score" class="comment-score"></div><div class="comment-text"><p>Well what happened was that I had an automated process to generate the dissector code and makefiles and what not for Wireshark version 1.4, and then when i used the same process for 1.11 it still worked so i was confused when it didnt work for 1.10. So i ended up just deleting the makefile that my automated process made and following the process in the README you posted. It was pretty straight forward and i didnt run into any problems when i did that.</p></div><div id="comment-28929-info" class="comment-info"><span class="comment-age">(15 Jan '14, 10:35)</span> Hockeyfreak889</div></div><span id="28932"></span><div id="comment-28932" class="comment"><div id="post-28932-score" class="comment-score"></div><div class="comment-text"><p>Actually I've run into another problem: As this process is creating a lot of dissectors, I compiled 1 plugin and assumed it would work for the rest of them. However when i tried to apply the same process to plugins that include other C files it gives me:</p><p>LNK2019 error unresolved external symbol</p><p>I know this comes from me trying to use a function that is defined in an external source and apparently the linker isnt seeing it, but when i try to add this other file to the Makefiles (i tried to copy the process from the asn1 plugin since it appeared to have an external source as well called asn1.c) it gave me the same (or at least similar) errors to when I started.</p><p>Sorry if this is a basic question, i really dont know much about C or Makefiles, or wireshark for that matter.</p></div><div id="comment-28932-info" class="comment-info"><span class="comment-age">(15 Jan '14, 13:17)</span> Hockeyfreak889</div></div></div><div id="comment-tools-28874" class="comment-tools"></div><div class="clear"></div><div id="comment-28874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

