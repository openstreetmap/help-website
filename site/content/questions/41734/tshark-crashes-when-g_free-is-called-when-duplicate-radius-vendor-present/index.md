+++
type = "question"
title = "Tshark crashes when g_free is called when duplicate Radius vendor present"
description = '''In function add_vendor the below code gets executed if vendor info was already there. Why when a pointer is freed after a valid vendor info is found, g_free() crashing?  if (v-&amp;gt;name)  g_free((gpointer) v-&amp;gt;name);  v-&amp;gt;name = g_strdup(name);  We are seeing crash when g_free is called. (gdb) wh...'''
date = "2015-04-23T11:14:00Z"
lastmod = "2015-04-23T13:49:00Z"
weight = 41734
keywords = [ "g_free", "add_vendor", "tshark" ]
aliases = [ "/questions/41734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark crashes when g\_free is called when duplicate Radius vendor present](/questions/41734/tshark-crashes-when-g_free-is-called-when-duplicate-radius-vendor-present)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In function add_vendor the below code gets executed if vendor info was already there. Why when a pointer is freed after a valid vendor info is found, g_free() crashing?</p><pre><code>    if (v-&gt;name)
            g_free((gpointer) v-&gt;name);
    v-&gt;name = g_strdup(name);</code></pre><p>We are seeing crash when g_free is called.</p><pre><code>(gdb) where
#0  0xf77d1430 in __kernel_vsyscall ()
#1  0x41051daf in raise (sig=6) at ../nptl/sysdeps/unix/sysv/linux/raise.c:64
#2  0x41055305 in abort () at abort.c:91
#3  0x41095d2b in malloc_printerr (action=&lt;value optimized out&gt;, str=&lt;value optimized out&gt;, ptr=0xf4e48d00) at malloc.c:5012
#4  0x4109a05b in __libc_free (mem=0xf4e48d00) at malloc.c:2959
#5  0x4128344b in standard_free (mem=0xf4e48d00) at gmem.c:98
#6  0x41283670 in g_free (mem=0xf4e48d00) at gmem.c:252
#7  0xf5dc9580 in add_vendor (name=0x97f7c00 &quot;3GPP&quot;, vendor_id=10415, vendor_type_octets=1, vendor_length_octets=1, vendor_has_flags=0)
    at ../../../../tshark/wireshark-1.2.9/epan/radius_dict.l:318</code></pre></div><div id="question-tags" class="tags-container tags">g_free add_vendor tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '15, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/eb86fd9c4d4470a6593832d0c52ecc7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="universini&#39;s gravatar image" /><p>universini<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="universini has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '15, 15:41</p></div></div><div id="comments-container-41734" class="comments-container"></div><div id="comment-tools-41734" class="comment-tools"></div><div class="clear"></div><div id="comment-41734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41747"></span>

<div id="answer-container-41747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41747-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>[Updated after noticing this was Radius not Diameter--oops!]</strong></p><p>Well, looking at the code it appears that:</p><ol><li>The vendor has been found based on the vendor ID (not name).</li><li>The code wants to use whatever the latest vendor information it read was (so it overwrites the old one, this includes changing the name--note that the name may be different).</li><li>(But, because the name is g_ allocated, it has to be g_free'd or it would leak memory.)</li></ol><p>This code is different in the current development version--and it was changed to fix a crash (see <a href="https://code.wireshark.org/review/#/c/5265/">change 5265</a>).</p><p>You've got a couple options:</p><ol><li>Don't put duplicate vendor IDs in the XML</li><li>Upgrade to a modern version of Wireshark (1.2.9 is ancient). The current development version is likely your best bet.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '15, 13:49</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '15, 13:56</p></div></div><div id="comments-container-41747" class="comments-container"><span id="41752"></span><div id="comment-41752" class="comment"><div id="post-41752-score" class="comment-score"></div><div class="comment-text"><p>Ok, if it has already found vendor that means it has a valid vendor name right? Why g_free has to crash when freeing a valid pointer? Is it a good idea to replace char * with a static array?</p></div><div id="comment-41752-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:23)</span> universini</div></div><span id="41759"></span><div id="comment-41759" class="comment"><div id="post-41759-score" class="comment-score"></div><div class="comment-text"><p>It's not clear why it's crashing. Note that glib should actually be printing something (to stderr) to explain what's wrong with the free though that may not help explain too much.</p><p>The problem with a static char array is it's more restrictive: what happens if your vendor name is too long (Wireshark currently has a Diameter vendor whose name is "NokiaSolutionsAndNetworks").</p><p>As mentioned, the crash may be related to the fix described or it may not. But I don't think it's worth spending a lot of time investigating such an ancient version, especially when there's a simple solution: don't have a duplicated vendor.</p><p>If it crashes in the currently-supported versions and/or development version then it would be worth investigating (I tried it with a duplicated VENDOR line and it worked fine--Valgrind didn't complain either).</p></div><div id="comment-41759-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:50)</span> JeffMorriss ♦</div></div><span id="41764"></span><div id="comment-41764" class="comment"><div id="post-41764-score" class="comment-score"></div><div class="comment-text"><p>It says Abort with signal 6</p></div><div id="comment-41764-info" class="comment-info"><span class="comment-age">(23 Apr '15, 15:39)</span> universini</div></div><span id="41816"></span><div id="comment-41816" class="comment"><div id="post-41816-score" class="comment-score"></div><div class="comment-text"><p>By the way, I am confused with .l and .c versions of the same file. From my understanding it looks like changes should only be done in .l file and .c will be automatically generated when built. Is that right? or don't we care .c at all?</p></div><div id="comment-41816-info" class="comment-info"><span class="comment-age">(24 Apr '15, 22:30)</span> universini</div></div><span id="41889"></span><div id="comment-41889" class="comment"><div id="post-41889-score" class="comment-score"></div><div class="comment-text"><p>It's a (f)lex parser. So humans write the .l file which (f)lex turns into the .c file which the compiler turns into an object file.</p><p>We (humans) don't need to worry about the .c file--unless you're working on the build system (Makefiles).</p></div><div id="comment-41889-info" class="comment-info"><span class="comment-age">(27 Apr '15, 07:53)</span> JeffMorriss ♦</div></div><span id="41895"></span><div id="comment-41895" class="comment not_top_scorer"><div id="post-41895-score" class="comment-score"></div><div class="comment-text"><p>So always make changes in .l file and make sure new .c file is generated with latest changes, right? If .c file isn't recreated with new changes, then changes won't work. Is that the way it is?</p></div><div id="comment-41895-info" class="comment-info"><span class="comment-age">(27 Apr '15, 11:18)</span> universini</div></div><span id="41898"></span><div id="comment-41898" class="comment not_top_scorer"><div id="post-41898-score" class="comment-score"></div><div class="comment-text"><blockquote><p>So always make changes in .l file and make sure new .c file is generated with latest changes, right?</p></blockquote><p>Correct.</p><blockquote><p>If .c file isn't recreated with new changes, then changes won't work.</p></blockquote><p>Correct.</p><blockquote><p>Is that the way it is?</p></blockquote><p>Yes.</p></div><div id="comment-41898-info" class="comment-info"><span class="comment-age">(27 Apr '15, 12:20)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-41747" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-41747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

