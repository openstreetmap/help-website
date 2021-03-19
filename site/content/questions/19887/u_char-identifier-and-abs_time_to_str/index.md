+++
type = "question"
title = "u_char identifier and abs_time_to_str"
description = '''I am trying to adapt an old code packet-gtpcdr.c into new version of wireshark but failed during compilation.    If I rename the u_char to gchar the complilation continue. I am not sure if this is correct. /* TAG undefined */ int decode_tlv_undefined (tvbuff_t *tvb, proto_tree *tree, int offset) {  ...'''
date = "2013-03-27T14:59:00Z"
lastmod = "2013-03-27T15:55:00Z"
weight = 19887
keywords = [ "u_char", "abs_time_to_str" ]
aliases = [ "/questions/19887" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [u\_char identifier and abs\_time\_to\_str](/questions/19887/u_char-identifier-and-abs_time_to_str)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19887-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to adapt an old code packet-gtpcdr.c into new version of wireshark but failed during compilation.</p><ol><li><p>If I rename the u_char to gchar the complilation continue. I am not sure if this is correct.</p><pre><code>/* TAG undefined */
int decode_tlv_undefined (tvbuff_t *tvb, proto_tree *tree, int offset) {
    proto_tree  *tlv_tree;
    proto_item  *te;
    u_char  length, tag;
    tag = tvb_get_guint8 (tvb, offset);
    length = tvb_get_guint8 (tvb, offset + 1);
    te = proto_tree_add_text (tree, tvb, offset, length + 2, &quot;TAG %d (undefined)&quot;, tag);
    tlv_tree = proto_item_add_subtree (te, ett_gtp_cdr_undefined);
    proto_tree_add_text (tlv_tree, tvb, offset, 1, &quot;Type: %d&quot;, tag);
    proto_tree_add_text (tlv_tree, tvb, offset + 1, 1, &quot;Length: %d&quot;, length);
    proto_tree_add_text (tlv_tree, tvb, offset + 2, length, &quot;Value&quot;);</code></pre></li><li><p>Which additional value should I add for <code>abs_time_to_str</code>?</p><pre><code>static gchar *
time_int_to_str (guint32 time)
{
    static nstime_t nstime;
    nstime.secs = time;
    nstime.nsecs = 0;
    return abs_time_to_str (&amp;nstime);</code></pre></li></ol><p>See the compile error</p><pre><code>packet-gtpcdr.c
plugin.c
packet-gtpcdr.c(2573) : error C2198: &#39;abs_time_to_str&#39; : too few arguments for call
packet-gtpcdr.c(3901) : error C2065: &#39;uchar&#39; : undeclared identifier
packet-gtpcdr.c(3901) : error C2146: syntax error : missing &#39;;&#39; before identifier &#39;length&#39;
packet-gtpcdr.c(3901) : error C2065: &#39;length&#39; : undeclared identifier
packet-gtpcdr.c(3901) : error C2065: &#39;tag&#39; : undeclared identifier
packet-gtpcdr.c(3903) : error C2065: &#39;tag&#39; : undeclared identifier
packet-gtpcdr.c(3904) : error C2065: &#39;length&#39; : undeclared identifier
packet-gtpcdr.c(3906) : error C2065: &#39;length&#39; : undeclared identifier
packet-gtpcdr.c(3906) : error C2065: &#39;tag&#39; : undeclared identifier
packet-gtpcdr.c(3909) : error C2065: &#39;tag&#39; : undeclared identifier
packet-gtpcdr.c(3910) : error C2065: &#39;length&#39; : undeclared identifier
packet-gtpcdr.c(3911) : error C2065: &#39;length&#39; : undeclared identifier
packet-gtpcdr.c(3913) : error C2065: &#39;length&#39; : undeclared identifier
packet-gtpcdr.c(3921) : error C2065: &#39;uchar&#39; : undeclared identifier
packet-gtpcdr.c(3921) : error C2146: syntax error : missing &#39;;&#39; before identifier &#39;length&#39;</code></pre><p>Thanks</p></div><div id="question-tags" class="tags-container tags">u_char abs_time_to_str</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '13, 14:59</strong></p><img src="https://secure.gravatar.com/avatar/5318038b31cc44ad026905167c9b1824?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve21&#39;s gravatar image" /><p>steve21<br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve21 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Mar '13, 15:42</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19887" class="comments-container"><span id="19896"></span><div id="comment-19896" class="comment"><div id="post-19896-score" class="comment-score"></div><div class="comment-text"><p>First of all thanks for your support. Now compile failed because version already defined in packet in packet-gtpcdr.obj Can you help me?</p><pre><code>    link -dll /out:gtpcdr.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x86 /SafeSEH /DYNAMICBASE /FIXED:no  packet-gtpcdr.obj  plugin.obj ..\..\epan\libwireshark.lib  C:\wireshark-win32-libs-1.8\gtk2\lib\glib-2.0.lib  C:\wireshark-win32-libs-1.8\gtk2\lib\gmodule-2.0.lib  C:\wireshark-win32-libs-1.8\gtk2\lib\gobject-2.0.lib gtpcdr.res plugin.obj : error LNK2005: _version already defined in packet-gtpcdr.obj
   Creating library gtpcdr.lib and object gtpcdr.exp
gtpcdr.dll : fatal error LNK1169: one or more multiply defined symbols found
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\link.EXE&quot;&#39; : return code &#39;0x491&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="comment-19896-info" class="comment-info"><span class="comment-age">(28 Mar '13, 04:44)</span> steve21</div></div></div><div id="comment-tools-19887" class="comment-tools"></div><div class="clear"></div><div id="comment-19887-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19889"></span>

<div id="answer-container-19889" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19889-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should replace your u_char by guint8. Moreover the prototype of abs_time_to_str is now:</p><pre><code>gchar* abs_time_to_str(const nstime_t*, const absolute_time_display_e fmt, gboolean show_zone);</code></pre><p>so your code should be:</p><pre><code>static gchar *
time_int_to_str (guint32 time)
{
    static nstime_t nstime;
    nstime.secs = time;
    nstime.nsecs = 0;
    return abs_time_to_str (&amp;nstime, ABSOLUTE_TIME_UTC, FALSE);
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '13, 15:51</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-19889" class="comments-container"></div><div id="comment-tools-19889" class="comment-tools"></div><div class="clear"></div><div id="comment-19889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19890"></span>

<div id="answer-container-19890" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19890-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If I rename the u_char to gchar the complilation continue. I am not sure if this is correct.</p></blockquote><p><code>uchar</code>, <code>u_char</code>, etc. are types defined by the operating system on which you're compiling; they should be avoided, so that the code can compile on several operating systems (including Windows, which is what you're compiling on).</p><p>Instead, the GLib types should be used; for example, for an 8-bit unsigned integral quantity, use <code>guint8</code>. (Oh, and since it's unsigned, format it with <code>%u</code>, not <code>%d</code>.)</p><blockquote><p>Which additional value should I add for <code>abs_time_to_str</code>?</p></blockquote><p>You should add, as the second argument:</p><ul><li><code>ABSOLUTE_TIME_LOCAL</code>, if you want the time stamp displayed as local date and time, with the date shown as a month, day, and year;</li><li><code>ABSOLUTE_TIME_UTC</code>, if you want the time stamp displayed as UTC date and time, with the date shown as a month, day, and year;</li><li><code>ABSOLUTE_TIME_DOY_UTC</code>, if you want the time stamp displayed as UTC date and time, with the date shown as day-of-year and year, with January 1 being day-of-year 1.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '13, 15:55</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Mar '13, 15:56</p></div></div><div id="comments-container-19890" class="comments-container"><span id="19907"></span><div id="comment-19907" class="comment"><div id="post-19907-score" class="comment-score"></div><div class="comment-text"><p>@steve21, I'd already converted your "answer" to a comment under your original question as it wasn't clear which actual answer your "answer" was referring to, and in addition, it was really an extension of your original question.</p></div><div id="comment-19907-info" class="comment-info"><span class="comment-age">(28 Mar '13, 07:43)</span> grahamb ♦</div></div><span id="19910"></span><div id="comment-19910" class="comment"><div id="post-19910-score" class="comment-score"></div><div class="comment-text"><p>It's an extension only in that it's presumably an issue with the same dissector, but it's a completely different issue, so I made it into a separate question. This is a Q&amp;A site, not a forum, so each item in the site should cover a separate question, so that people searching the site to see whether somebody else already asked the same question and got an answer can more easily find the question.</p></div><div id="comment-19910-info" class="comment-info"><span class="comment-age">(28 Mar '13, 11:33)</span> Guy Harris ♦♦</div></div><span id="19913"></span><div id="comment-19913" class="comment"><div id="post-19913-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Sorry I did not know it.</p></div><div id="comment-19913-info" class="comment-info"><span class="comment-age">(28 Mar '13, 14:23)</span> steve21</div></div></div><div id="comment-tools-19890" class="comment-tools"></div><div class="clear"></div><div id="comment-19890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

