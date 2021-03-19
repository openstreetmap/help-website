+++
type = "question"
title = "wireshark segfaults gobject errors"
description = '''Hi, Since a few days ago wiresharks segfaults whenever its starts. dmesg gives wireshark[2320]: segfault at ffffffffa4004920 ip 00007fa5bc13d425 sp 00007ffcb149fbb8 error 5 in libgobject-2.0.so.0.4400.1[7fa5bc10a000+50000] OS is Ubuntu 15.04 64 bit, wireshark 1.12.6 compiled from source. Please help...'''
date = "2015-06-28T09:05:00Z"
lastmod = "2015-06-28T09:05:00Z"
weight = 43631
keywords = [ "wireshark" ]
aliases = [ "/questions/43631" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark segfaults gobject errors](/questions/43631/wireshark-segfaults-gobject-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43631-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Since a few days ago wiresharks segfaults whenever its starts. dmesg gives wireshark[2320]: segfault at ffffffffa4004920 ip 00007fa5bc13d425 sp 00007ffcb149fbb8 error 5 in libgobject-2.0.so.0.4400.1[7fa5bc10a000+50000]</p><p>OS is Ubuntu 15.04 64 bit, wireshark 1.12.6 compiled from source.</p><p>Please help. Thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '15, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/937b0a2f8973f575fa8ac5e253345787?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kmod&#39;s gravatar image" /><p>kmod<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kmod has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jun '15, 09:12</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43631" class="comments-container"><span id="43632"></span><div id="comment-43632" class="comment"><div id="post-43632-score" class="comment-score"></div><div class="comment-text"><p>I suspect you'll have to generate a backtrace to get any further with this. See the Ubuntu page on how to do this <a href="https://wiki.ubuntu.com/Backtrace">here</a>.</p></div><div id="comment-43632-info" class="comment-info"><span class="comment-age">(28 Jun '15, 09:14)</span> grahamb ♦</div></div><span id="43636"></span><div id="comment-43636" class="comment"><div id="post-43636-score" class="comment-score"></div><div class="comment-text"><p>Any changes the last few days, for instance software updates?</p></div><div id="comment-43636-info" class="comment-info"><span class="comment-age">(28 Jun '15, 11:54)</span> Jaap ♦</div></div><span id="43647"></span><div id="comment-43647" class="comment"><div id="post-43647-score" class="comment-score"></div><div class="comment-text"><p>Yes, there was a update of libglib a few days ago.</p><p>Upgraded the following packages: libglib2.0-0 (2.44.0-1ubuntu3) to 2.44.1-1ubuntu1 libglib2.0-0:i386 (2.44.0-1ubuntu3) to 2.44.1-1ubuntu1 libglib2.0-bin (2.44.0-1ubuntu3) to 2.44.1-1ubuntu1 libglib2.0-data (2.44.0-1ubuntu3) to 2.44.1-1ubuntu1 libglib2.0-dev (2.44.0-1ubuntu3) to 2.44.1-1ubuntu1</p></div><div id="comment-43647-info" class="comment-info"><span class="comment-age">(28 Jun '15, 22:23)</span> kmod</div></div><span id="43656"></span><div id="comment-43656" class="comment"><div id="post-43656-score" class="comment-score"></div><div class="comment-text"><p>Here is a backtrace</p><pre><code>Reading symbols from wireshark...(no debugging symbols found)...done.
(gdb) handle SIG33 pass nostop noprint
Signal        Stop  Print   Pass to program Description
SIG33         No    No  Yes     Real-time event 33
(gdb) set pagination 0
(gdb) run
Starting program: /usr/bin/wireshark 
[Thread debugging using libthread_db enabled]
Using host libthread_db library &quot;/lib/x86_64-linux-gnu/libthread_db.so.1&quot;.
[New Thread 0x7fffe51e8700 (LWP 2907)]
[New Thread 0x7fffe59e9700 (LWP 2906)]

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff113d425 in g_type_check_instance_is_fundamentally_a () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
(gdb) backtrace full
#0  0x00007ffff113d425 in g_type_check_instance_is_fundamentally_a () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
No symbol table info available.
#1  0x00007ffff111eeae in g_object_ref () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
No symbol table info available.
#2  0x00007ffff0e4107d in g_list_foreach () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
No symbol table info available.
#3  0x00007ffff22f1e01 in gtk_window_set_icon_list () from /usr/lib/x86_64-linux-gnu/libgtk-3.so.0
No symbol table info available.
#4  0x0000000000441e30 in ?? ()
No symbol table info available.
#5  0x00007ffff111a2d5 in g_closure_invoke () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
No symbol table info available.
#6  0x00007ffff112c03c in ?? () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
No symbol table info available.
#7  0x00007ffff1134698 in g_signal_emit_valist () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
No symbol table info available.
#8  0x00007ffff11348ff in g_signal_emit () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
No symbol table info available.
#9  0x00007ffff22e24ac in gtk_widget_realize () from /usr/lib/x86_64-linux-gnu/libgtk-3.so.0
No symbol table info available.
#10 0x00000000004ba61b in ?? ()
No symbol table info available.
#11 0x000000000042311a in ?? ()
No symbol table info available.
#12 0x00007fffefd8fa40 in __libc_start_main (main=0x422d10, argc=1, argv=0x7fffffffdfa8, init=&lt;optimized out&gt;, fini=&lt;optimized out&gt;, rtld_fini=&lt;optimized out&gt;, stack_end=0x7fffffffdf98) at libc-start.c:289
        result = &lt;optimized out&gt;
        unwind_buf = {cancel_jmp_buf = {{jmp_buf = {0, 5433218451502865264, 4342592, 140737488347040, 0, 0, -5433218848626238608, -5433183450742056080}, mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x5266f0 &lt;__libc_csu_init&gt;, 0x7fffffffdfa8}, data = {prev = 0x0, cleanup = 0x0, canceltype = 5400304}}}
        not_first_call = &lt;optimized out&gt;
#13 0x0000000000424369 in _start ()
No symbol table info available.
(gdb) info registers
rax            0x953580 9778560
rbx            0xffffffffd8004920   -671069920
rcx            0x2  2
rdx            0x1  1
rsi            0x50 80
rdi            0xffffffffd8004920   -671069920
rbp            0x0  0x0
rsp            0x7fffffffd828   0x7fffffffd828
r8             0x95a330 9806640
r9             0x95a2e0 9806560
r10            0x19a    410
r11            0x7ffff0e41060   140737234866272
r12            0x7ffff111eea0   140737237872288
r13            0x1  1
r14            0x7fffffffda60   140737488345696
r15            0x7fffffffda00   140737488345600
rip            0x7ffff113d425   0x7ffff113d425 &lt;g_type_check_instance_is_fundamentally_a+5&gt;
eflags         0x10282  [ SF IF RF ]
cs             0x33 51
ss             0x2b 43
ds             0x0  0
es             0x0  0
fs             0x0  0
gs             0x0  0
(gdb) x/16i $pc
=&gt; 0x7ffff113d425 &lt;g_type_check_instance_is_fundamentally_a+5&gt;: mov    (%rdi),%rax
   0x7ffff113d428 &lt;g_type_check_instance_is_fundamentally_a+8&gt;: test   %rax,%rax
   0x7ffff113d42b &lt;g_type_check_instance_is_fundamentally_a+11&gt;:    je     0x7ffff113d470 &lt;g_type_check_instance_is_fundamentally_a+80&gt;
   0x7ffff113d42d &lt;g_type_check_instance_is_fundamentally_a+13&gt;:    mov    (%rax),%rax
   0x7ffff113d430 &lt;g_type_check_instance_is_fundamentally_a+16&gt;:    cmp    $0x3fc,%rax
   0x7ffff113d436 &lt;g_type_check_instance_is_fundamentally_a+22&gt;:    ja     0x7ffff113d460 &lt;g_type_check_instance_is_fundamentally_a+64&gt;
   0x7ffff113d438 &lt;g_type_check_instance_is_fundamentally_a+24&gt;:    lea    0x21e301(%rip),%rdx        # 0x7ffff135b740
   0x7ffff113d43f &lt;g_type_check_instance_is_fundamentally_a+31&gt;:    shr    $0x2,%rax
   0x7ffff113d443 &lt;g_type_check_instance_is_fundamentally_a+35&gt;:    mov    (%rdx,%rax,8),%rax
   0x7ffff113d447 &lt;g_type_check_instance_is_fundamentally_a+39&gt;:    test   %rax,%rax
   0x7ffff113d44a &lt;g_type_check_instance_is_fundamentally_a+42&gt;:    je     0x7ffff113d470 &lt;g_type_check_instance_is_fundamentally_a+80&gt;
   0x7ffff113d44c &lt;g_type_check_instance_is_fundamentally_a+44&gt;:    movzbl 0x14(%rax),%edx
   0x7ffff113d450 &lt;g_type_check_instance_is_fundamentally_a+48&gt;:    cmp    %rsi,0x48(%rax,%rdx,8)
   0x7ffff113d455 &lt;g_type_check_instance_is_fundamentally_a+53&gt;:    sete   %al
   0x7ffff113d458 &lt;g_type_check_instance_is_fundamentally_a+56&gt;:    movzbl %al,%eax
   0x7ffff113d45b &lt;g_type_check_instance_is_fundamentally_a+59&gt;:    retq   
(gdb) thread apply all backtrace

Thread 3 (Thread 0x7fffe59e9700 (LWP 2906)):
#0  0x00007fffefe6a8dd in poll () at ../sysdeps/unix/syscall-template.S:81
#1  0x00007ffff0e44ebc in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff0e44fcc in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x00007fffe59f127d in ?? () from /usr/lib/x86_64-linux-gnu/gio/modules/libdconfsettings.so
#4  0x00007ffff0e6b955 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#5  0x00007ffff01406aa in start_thread (arg=0x7fffe59e9700) at pthread_create.c:333
#6  0x00007fffefe75eed in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 2 (Thread 0x7fffe51e8700 (LWP 2907)):
#0  0x00007fffefe6a8dd in poll () at ../sysdeps/unix/syscall-template.S:81
#1  0x00007ffff0e44ebc in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#2  0x00007ffff0e45242 in g_main_loop_run () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x00007fffed300af6 in ?? () from /usr/lib/x86_64-linux-gnu/libgio-2.0.so.0
#4  0x00007ffff0e6b955 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#5  0x00007ffff01406aa in start_thread (arg=0x7fffe51e8700) at pthread_create.c:333
#6  0x00007fffefe75eed in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:109

Thread 1 (Thread 0x7ffff7f899c0 (LWP 2902)):
#0  0x00007ffff113d425 in g_type_check_instance_is_fundamentally_a () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#1  0x00007ffff111eeae in g_object_ref () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#2  0x00007ffff0e4107d in g_list_foreach () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#3  0x00007ffff22f1e01 in gtk_window_set_icon_list () from /usr/lib/x86_64-linux-gnu/libgtk-3.so.0
#4  0x0000000000441e30 in ?? ()
#5  0x00007ffff111a2d5 in g_closure_invoke () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#6  0x00007ffff112c03c in ?? () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#7  0x00007ffff1134698 in g_signal_emit_valist () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#8  0x00007ffff11348ff in g_signal_emit () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
#9  0x00007ffff22e24ac in gtk_widget_realize () from /usr/lib/x86_64-linux-gnu/libgtk-3.so.0
#10 0x00000000004ba61b in ?? ()
#11 0x000000000042311a in ?? ()
#12 0x00007fffefd8fa40 in __libc_start_main (main=0x422d10, argc=1, argv=0x7fffffffdfa8, init=&lt;optimized out&gt;, fini=&lt;optimized out&gt;, rtld_fini=&lt;optimized out&gt;, stack_end=0x7fffffffdf98) at libc-start.c:289
#13 0x0000000000424369 in _start ()
(gdb) quit
A debugging session is active.

    Inferior 1 [process 2902] will be killed.

Quit anyway? (y or n) n[Ky</code></pre></div><div id="comment-43656-info" class="comment-info"><span class="comment-age">(29 Jun '15, 03:42)</span> kmod</div></div><span id="43657"></span><div id="comment-43657" class="comment"><div id="post-43657-score" class="comment-score"></div><div class="comment-text"><p>I should add that starting wireshark with sudo (yes, I know it is a bad idea) does not cause segfault. But there is a warning</p><blockquote><p>Gtk-Message: GtkDialog mapped without a transient parent. This is discouraged.</p></blockquote><p>So I think GtkDialog mapped with a transient parent might have caused segfault, though I have no idea what it means.</p></div><div id="comment-43657-info" class="comment-info"><span class="comment-age">(29 Jun '15, 03:50)</span> kmod</div></div></div><div id="comment-tools-43631" class="comment-tools"></div><div class="clear"></div><div id="comment-43631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

