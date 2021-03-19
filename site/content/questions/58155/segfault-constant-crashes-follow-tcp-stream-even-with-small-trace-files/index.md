+++
type = "question"
title = "Segfault - Constant crashes &quot;Follow TCP Stream&#x27;  - Even with small trace files"
description = '''Wireshark crashes constantly when I try to assemble TCP streams. It happens with small traces. when a filter a trace with &#x27;TCP&#x27;. Here is what a gathered: -- Wireshark Version 2.2.1  --System: Linux 4.6.0-amd64 #1 SMP Debian 4.6.4-(2016-07-21) x86_64 GNU/Linux --- dpkg -s libc6 | grep ^Version Versio...'''
date = "2016-12-15T16:16:00Z"
lastmod = "2016-12-17T10:00:00Z"
weight = 58155
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/58155" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Segfault - Constant crashes "Follow TCP Stream' - Even with small trace files](/questions/58155/segfault-constant-crashes-follow-tcp-stream-even-with-small-trace-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58155-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark crashes constantly when I try to assemble TCP streams. It happens with small traces. when a filter a trace with 'TCP'. Here is what a gathered:</p><p>-- Wireshark Version 2.2.1</p><p>--System:</p><p>Linux 4.6.0-amd64 #1 SMP Debian 4.6.4-(2016-07-21) x86_64 GNU/Linux</p><p>--- dpkg -s libc6 | grep ^Version Version: 2.24-7</p><p>dmesg:</p><p><code>[ 2421.293635] wireshark[1617]: segfault at 7fc4ea662d08 ip 00007fc4ea662d08 sp 00007ffc4252cc78 error 15 in libc-2.24.so[7fc4ea662000+2000] [ 2656.401863] wireshark[2133]: segfault at 561838529390 ip 0000561838529390 sp 00007ffe71b508a8 error 15 [ 3815.183482] wireshark[2222]: segfault at 557727157fa0 ip 0000557727157fa0 sp 00007fff6fc6e428 error 15 [ 4170.894616] wireshark[4775]: segfault at 7fed00000040 ip 00007fed00000040 sp 00007fff0f4099e8 error 14 in libkrb5.so.3.3[7fecffe6a000+200000</code></p><p>----System log</p><p><code>Dec 15 15:35:08 kalia kernel: [ 4170.894616] wireshark[4775]: segfault at 7fed00000040 ip 00007fed00000040 sp 00007fff0f4099e8 error 14 in libkrb5.so.3.3[7fecffe6a000+200000] Dec 15 15:35:16 kalia gnome-system-lo[4955]: Failed to get the GNOME session proxy: The name org.gnome.SessionManager is not owned Dec 15 15:35:16 kalia gnome-system-lo[4955]: Failed to get the Xfce session proxy: The name org.xfce.SessionManager is not owned Dec 15 15:35:16 kalia gnome-system-lo[4955]: Failed to get an inhibit portal proxy: The name org.freedesktop.portal.Desktop is not owned Dec 15 15:35:16 kalia gnome-system-lo[4955]: g_action_print_detailed_name: assertion 'g_action_name_is_valid (action_name)' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: gtk_application_set_accels_for_action: assertion 'detailed_action_name != NULL' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: g_action_print_detailed_name: assertion 'g_action_name_is_valid (action_name)' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: gtk_application_set_accels_for_action: assertion 'detailed_action_name != NULL' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: g_action_print_detailed_name: assertion 'g_action_name_is_valid (action_name)' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: gtk_application_set_accels_for_action: assertion 'detailed_action_name != NULL' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: g_action_print_detailed_name: assertion 'g_action_name_is_valid (action_name)' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: gtk_application_set_accels_for_action: assertion 'detailed_action_name != NULL' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: g_action_print_detailed_name: assertion 'g_action_name_is_valid (action_name)' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: gtk_application_set_accels_for_action: assertion 'detailed_action_name != NULL' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: g_action_print_detailed_name: assertion 'g_action_name_is_valid (action_name)' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: gtk_application_set_accels_for_action: assertion 'detailed_action_name != NULL' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: g_action_print_detailed_name: assertion 'g_action_name_is_valid (action_name)' failed Dec 15 15:35:16 kalia gnome-system-lo[4955]: gtk_application_set_accels_for_action: assertion 'detailed_action_name != NULL' failed Dec 15 15:35:17 kalia gnome-system-lo[4955]: Allocating size to GtkScrolledWindow 0x27643c0 without calling gtk_widget_get_preferred_width/height(). How does the code know the size to allocate?</code></p><p>Thanks for your help!</p><p>Christian</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '16, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/0a6d6884dbf91da2683ed6f0ec54ec33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toloop&#39;s gravatar image" /><p>toloop<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toloop has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '16, 10:54</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58155" class="comments-container"><span id="58193"></span><div id="comment-58193" class="comment"><div id="post-58193-score" class="comment-score"></div><div class="comment-text"><p>Is this installed from a distribution package or self-compiled?</p></div><div id="comment-58193-info" class="comment-info"><span class="comment-age">(17 Dec '16, 10:55)</span> grahamb ♦</div></div><span id="58213"></span><div id="comment-58213" class="comment"><div id="post-58213-score" class="comment-score"></div><div class="comment-text"><p>Wireshark v. 2.2.0 is bundled with Debian Kali Linux.</p><p>Thank you,</p><p>Christian</p></div><div id="comment-58213-info" class="comment-info"><span class="comment-age">(18 Dec '16, 08:35)</span> toloop</div></div></div><div id="comment-tools-58155" class="comment-tools"></div><div class="clear"></div><div id="comment-58155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58192"></span>

<div id="answer-container-58192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58192-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may have better luck reporting this in Wireshark's bugzilla site: <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '16, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-58192" class="comments-container"></div><div id="comment-tools-58192" class="comment-tools"></div><div class="clear"></div><div id="comment-58192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

