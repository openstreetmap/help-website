+++
type = "question"
title = "How do I fix &quot;_version already defined in packet-gtpcdr.obj&quot; error?"
description = '''Thanks for you support. Could someone hep me for the following complile error? link -dll /out:gtpcdr.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x86 /SafeSEH /DYNAMICBASE /FIXED:no packet-gtpcdr.obj plugin.obj ..&#92;..&#92;epan&#92;libwireshark.lib C:&#92;wireshark-win32-libs-1.8&#92;gtk2&#92;lib&#92;glib-2.0.lib C:&#92;wireshark...'''
date = "2013-03-28T07:24:00Z"
lastmod = "2013-03-28T11:32:00Z"
weight = 19905
keywords = [ "msvc" ]
aliases = [ "/questions/19905" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I fix "\_version already defined in packet-gtpcdr.obj" error?](/questions/19905/how-do-i-fix-_version-already-defined-in-packet-gtpcdrobj-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19905-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thanks for you support. Could someone hep me for the following complile error?</p><pre><code>link -dll /out:gtpcdr.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x86 /SafeSEH /DYNAMICBASE /FIXED:no  packet-gtpcdr.obj  plugin.obj ..\..\epan\libwireshark.lib  C:\wireshark-win32-libs-1.8\gtk2\lib\glib-2.0.lib  C:\wireshark-win32-libs-1.8\gtk2\lib\gmodule-2.0.lib  C:\wireshark-win32-libs-1.8\gtk2\lib\gobject-2.0.lib gtpcdr.res
plugin.obj : error LNK2005: _version already defined in packet-gtpcdr.obj
   Creating library gtpcdr.lib and object gtpcdr.exp
gtpcdr.dll : fatal error LNK1169: one or more multiply defined symbols found
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\link.EXE&quot;&#39; : return code &#39;0x491&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags">msvc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '13, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/5318038b31cc44ad026905167c9b1824?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve21&#39;s gravatar image" /><p>steve21<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve21 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 28 Mar '13, 11:29</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19905" class="comments-container"></div><div id="comment-tools-19905" class="comment-tools"></div><div class="clear"></div><div id="comment-19905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19909"></span>

<div id="answer-container-19909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19909-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the variable named <code>version</code> in packet-gtpcdr.c is a plugin version number, get rid of it - that's already taken care of in plugin.c.</p><p>If the variable named <code>version</code> in packet-gtpcdr.c is not a plugin version number, but is a variable used in the process of dissecting packets, either rename it or make it a local variable rather than a global variable (global variables are discouraged in dissectors).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '13, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19909" class="comments-container"><span id="19914"></span><div id="comment-19914" class="comment"><div id="post-19914-score" class="comment-score"></div><div class="comment-text"><p>Below is the code for variable named version. What do you suggest to modify?</p><pre><code>#ifndef ENABLE_STATIC
G_MODULE_EXPORT const guint8 version[] = VERSION;
#endif

#ifndef ENABLE_STATIC
G_MODULE_EXPORT void
plugin_reg_handoff(void){
    proto_reg_handoff_gtpcdr();
}
G_MODULE_EXPORT void
plugin_register (void) {
    if (proto_gtpcdr == -1)
        proto_register_gtpcdr();
}
#endif</code></pre></div><div id="comment-19914-info" class="comment-info"><span class="comment-age">(28 Mar '13, 14:54)</span> steve21</div></div><span id="19915"></span><div id="comment-19915" class="comment"><div id="post-19915-score" class="comment-score"></div><div class="comment-text"><p>If that code is in packet-gtpcdr.c, I suggest you remove all of it. That code should be in plugin.c, and probably already <em>is</em> in plugin.c.</p></div><div id="comment-19915-info" class="comment-info"><span class="comment-age">(28 Mar '13, 14:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-19909" class="comment-tools"></div><div class="clear"></div><div id="comment-19909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

