+++
type = "question"
title = "How to build tshark as a shared library, like libtshark.so?"
description = '''I want to use methods in tshark in my program. So I want to build tshark as a library. How can I do this? Thank you for anyone&#x27;s help in advance. more detalis: 1.I&#x27;m making a test result analysis tool to deal with *.pcap files. This tool will first get the data chunk above TCP layer from pcap files ...'''
date = "2015-06-24T02:46:00Z"
lastmod = "2015-07-07T06:23:00Z"
weight = 43495
keywords = [ "tshark", "library" ]
aliases = [ "/questions/43495" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to build tshark as a shared library, like libtshark.so?](/questions/43495/how-to-build-tshark-as-a-shared-library-like-libtsharkso)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43495-score" class="post-score" title="current number of votes">0</div><span id="post-43495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to use methods in tshark in my program. So I want to build tshark as a library. How can I do this?</p><p>Thank you for anyone's help in advance.</p><p>more detalis:<br />
1.I'm making a test result analysis tool to deal with *.pcap files. This tool will first get the data chunk above TCP layer from pcap files and then do some analysis. So I need to use tshark function to peel the data by different layers.<br />
2.I'm using GNU autotools building the whole wireshark source project.<br />
3.I've tried to make some changes in Makefile.am and automake and configure and make. And I got libtshark.a. The problem is some of the functions in tshark can not be seen from "nm libtshark.a| grep XXX", which means my tool cannot use it. There must be something wrong when I made the libtshark.a. I did it like this:<br />
</p><pre><code>a.I changed main() in tshark.c to tshark()
b.I removed &quot;tshark&quot; from bin_PROGRAMS and EXTRA_PROGRAMS in Makefile.am
c.I added &quot;lib_LIBRARIES = libtshark.a&quot; in Makefile.am
d.I added &quot;libtshark_a_SOURCES = $(tshark_SOURCES)&quot; in Makefile.common
e.I added &quot;libtshark_a_LIBADD = &quot; in Makefile.am
f.automake
g../configure
h.make</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-library" rel="tag" title="see questions tagged &#39;library&#39;">library</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '15, 02:46</strong></p><img src="https://secure.gravatar.com/avatar/b42192f79bcad791f5c1e4593116f934?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Zhou&#39;s gravatar image" /><p><span>David Zhou</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Zhou has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jun '15, 19:58</strong> </span></p></div></div><div id="comments-container-43495" class="comments-container"><span id="43503"></span><div id="comment-43503" class="comment"><div id="post-43503-score" class="comment-score"></div><div class="comment-text"><p>Do you actually mean tshark, or the wireshark dissection engine in libwireshark or the capture file reading\writing tools in libwiretap?</p><p>The tshark executable basically parses command line options and then calls into libwireshark\libwiretap as required.</p></div><div id="comment-43503-info" class="comment-info"><span class="comment-age">(24 Jun '15, 08:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43534"></span><div id="comment-43534" class="comment"><div id="post-43534-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>, Thank you for your reply. yes, I mean tshark. I know tshark implement some methods like "process_packet()" to deal with *.pcap files, spliting ethernet layer/IP layer/TCP layer, etc. And I know these methods in tshark are based on some interfaces from libwireshark and libwiretap.</p><p>So I need to use the functions in tshark in my program and I'm trying to make tshark as a shared library. Could you please help me on this? Thank you.</p></div><div id="comment-43534-info" class="comment-info"><span class="comment-age">(24 Jun '15, 19:18)</span> <span class="comment-user userinfo">David Zhou</span></div></div></div><div id="comment-tools-43495" class="comment-tools"></div><div class="clear"></div><div id="comment-43495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43551"></span>

<div id="answer-container-43551" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43551-score" class="post-score" title="current number of votes">0</div><span id="post-43551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To make tshark a library you'll have to hack whatever build system you're using, e.g. autotools, CMake or nmake.</p><p>However I still question the usefulness of this. A library is a collection of functions that allows library users to achieve some result. tshark doesn't have any of this, its a command line parser that then calls the real libraries, libwireshark and libwiretap to do some work.</p><p>I think you should reconsider either using tshark as a spawned process, providing it the required command line options to do what you want and parsing the output, or use libwireshark and libwiretap directly, which isn't very easy at all as they're not designed to be general purpose libraries.</p><p>You also haven't indicated exactly what you wish to achieve, if you do that we may be able to suggest a better approach.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '15, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-43551" class="comments-container"><span id="43567"></span><div id="comment-43567" class="comment"><div id="post-43567-score" class="comment-score"></div><div class="comment-text"><blockquote><p>To make tshark a library you'll have to hack whatever build system you're using, e.g. autotools, CMake or nmake.</p></blockquote><p>...and hack the <em>code</em> as well. It was written to be a <em>program</em>, not a <em>library</em>.</p></div><div id="comment-43567-info" class="comment-info"><span class="comment-age">(25 Jun '15, 13:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="43578"></span><div id="comment-43578" class="comment"><div id="post-43578-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>, Thank you for the information. I've provided more details, appending to my question. Please check that. I appreciate your help. Thank you.</p></div><div id="comment-43578-info" class="comment-info"><span class="comment-age">(25 Jun '15, 19:46)</span> <span class="comment-user userinfo">David Zhou</span></div></div><span id="43580"></span><div id="comment-43580" class="comment"><div id="post-43580-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@David Zhou</span></p><blockquote><p>a.I changed main() in tshark.c to tshark()</p></blockquote><p>Are you aware that tshark is a console application printing to STDOUT? It's by far not enough to rename main() to get a library. Large parts of the code structure would have to be changed for that.</p><p>Why don't you call the tshark binary from your code (execve) and parse the output. Way less trouble for you. Plus, you would have to do the parsing part anyway, even if you (somehow) manage to press the tshark functionality into a library, because tshark would then still do the same as the console application, <strong>outputting a text representation of the dissected frames</strong>.</p></div><div id="comment-43580-info" class="comment-info"><span class="comment-age">(26 Jun '15, 00:04)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="43581"></span><div id="comment-43581" class="comment"><div id="post-43581-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt Knochner</span>, Thank you for your attention.<br />
</p><p>To execute tshark from my program as a spawn process is an option that I've already considered and abandoned. In this case, If the pcap file is extremely large(big chance), the spawn process will last a long time without output in STDOUT and my father program has no idea what's going on. This will lead to chaos.<br />
</p><p>I've also hacked tshark. I made some changes based on tshark code and now, when I run command "tshark -r xxx.pcap", nothing will be output on STDOUT but it will do some test analysis on dissected frames.<br />
At this point, If I made this tshark a library, my program could get the layers' data directly from functions, not STDOUT, and do stuffs.<br />
</p><p>So if you have more information on how to generate libtshark.so/libtshark.a, I appreciate it you could share with me. Thank you.</p></div><div id="comment-43581-info" class="comment-info"><span class="comment-age">(26 Jun '15, 01:57)</span> <span class="comment-user userinfo">David Zhou</span></div></div></div><div id="comment-tools-43551" class="comment-tools"></div><div class="clear"></div><div id="comment-43551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43932"></span>

<div id="answer-container-43932" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43932-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43932-score" class="post-score" title="current number of votes">0</div><span id="post-43932-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>After weeks of torture, I've made libtshark.so for my tool and they work well together. Here I share the process for people wanting tshark library.<br />
</p><h3 id="summary">summary</h3><pre><code> 1. this is based on wireshark-1.7 source code
 2. I used autotools system(automake, autoconf...)
 3. I did it by making necessary changes in existing wireshark source autotool files.
 4. there are still some redundancy functionality that could be excluded from the build. I just made it with the minimum modifications.</code></pre><h3 id="details">details</h3><h4 id="tshark.c">tshark.c</h4><h4><pre><code>1.modify: main() =&gt; tshark()</code></pre></h4><h4 id="makefile.am">./Makefile.am</h4><pre><code>1.add &quot;lib_LTLIBRARIES = libtshark.la&quot;
2.remove &quot;@[email protected]&quot; from bin_PROGRAMS
3.remove &quot;tshark&quot; from EXTRA_PROGRAMS
4.modify wireshark_LDADDui/gtk/libgtkui.a =&gt; ui/gtk/libgtkui.la
ui/gtk/libgtkui_dirty.a =&gt; ui/gtk/libgtkui_dirty.la
ui/libui.a =&gt; ui/libui.la</code></pre>5.modify "if ENABLE_STATIC" macro<pre><code>after:
if ENABLE_STATIC
libtshark_LDFLAGS = -Wl, -static -all-static
else
libtshark_LDFLAGS = -export-dynamic
endif</code></pre>6.add libtshark.a and libtshark.la to CLEANFILES 7.add libtshark_la_LIBADD like this<pre><code>libtshark_la_LIBADD =   \
    ui/libui.la         \
    ui/cli/libcliui.la          \
    ui/gtk/libgtkui.la          \
    wiretap/libwiretap.la       \
    epan/libwireshark.la        \
    wsutil/libwsutil.la     \
    @[email protected]          \
    $(plugin_ldadd)         \
    @[email protected] -lm         \
    @[email protected]         \
    @[email protected]           \
    @[email protected]          \
    @[email protected]           \
    @[email protected]         \
    @[email protected]         \
    @[email protected]   \
    @[email protected]           \
    @[email protected]        \
    @[email protected]        \
    @[email protected]        \</code></pre></pre><h4 id="makefile.common">./Makefile.common</h4><pre><code>1.add libtshark_la_SOURCES like thislibtshark_la_SOURCES =  \
    $(WIRESHARK_COMMON_SRC) \
    $(SHARK_COMMON_CAPTURE_SRC) \
    airpcap_loader.c \
    capture_info.c  \
    color_filters.c \
    fileset.c   \
    filters.c   \
    g711.c \
    merge.c \
    proto_hier_stats.c  \
    recent.c    \
    summary.c   \
    u3.c        \
    capture_opts.c      \
    tempfile.c      \
    tshark.c</code></pre></pre><h4 id="uimakefile.am">./ui/Makefile.am</h4><pre><code>1.modify: noinst_LIBRARIES = libui.a =&gt; lib_LTLIBRARIES = libui.la
2.add libui.la to CLEANFILES
3.modify: libui_a_SOURCES =&gt; libui_la_SOURCES
4.modify: libui_a_CFLAGS =&gt; libui_la_CFLAGS
5.modify: libui_a_DEPENDENCIES =&gt; libui_la_DEPENDENCIES</code></pre><h4 id="uiclimakefile.am">./ui/cli/Makefile.am</h4><pre><code>1.modify: noinst_LIBRARIES = libcliui.a =&gt; lib_LTLIBRARIES = libcliui.la
2.add libcliui.la to CLEANFILES
3.modify: libcliui_a_SOURCES =&gt; libcliui_la_SOURCES
4.modify: libcliui_a_CFLAGS =&gt; libcliui_la_CFLAGS
5.modify: libcliui_a_DEPENCENCIES =&gt; libcliui_la_DEPENCENCIES</code></pre><h4 id="uigtkmakefile.am">./ui/gtk/Makefile.am</h4><pre><code>1.modify: noinst_LIBRARIES = libgtkui.a libgtkui_dirty.a =&gt; lib_LTLIBRARIES = libgtkui.la libgtkui_dirty.la
2.add libgtkui.la and libgtkui_dirty.la to CLEANFILES
3.modify: libgtkui_a_SOURCES =&gt; libgtkui_la_SOURCES
4.modify: libgtkui_a_CFLAS =&gt; libgtkui_la_CFLAGS
5.add libgtkui_la_LIBADD = -lglib-2.0 -lgobject-2.0 -lgtk-x11-2.0
6.modify: libgtkui_a_DEPENDENCIES =&gt; libgtkui_la_DEPENCENCIES
7.modify: libgtkui_dirty_a_SOURCES =&gt; libgtkui_dirty_la_SOURCES
8.modify: libgtkui_dirty_a_DEPENCENCIES =&gt; libgtkui_dirty_la_DEPENCENCIES</code></pre><h4 id="uigtkmakefile.common">./ui/gtk/Makefile.common</h4><pre><code>1.add ../../file.c and ../../capture.c to WIRESHARK_GTK_SRC</code></pre><h4 id="automake-under-.">automake under ./</h4><h4 id="configure---disable-dftest---disable-rawshark">#./configure --disable-dftest --disable-rawshark</h4><h4 id="make-after-thisyou-have-your-libtshark.so">#make (after this,you have your libtshark.so)</h4><h4 id="to-use-it-up-you-need-to-do-more.">to use it up, you need to do more.</h4><pre><code>1.declare tshark() function in your program, as a entry to use libtshark.so. You may create a header file called tshark.h in your project and declare like this:&#39;#ifdef __cplusplus
extern &quot;C&quot; {
&#39;#endif
int tshark(int argc, char *argv[]);
&#39;#ifdef __cplusplus
}
&#39;#endif</code></pre>remember to copy this header file under your libtshark directory before you build it.<p>2.link libtshark.so to your program 3.call tshark function like this, for example:</p><pre><code>char arg_self = &quot;/data/home/davidcyzhou/workspace/test/Debug/test&quot;;
char r_symbol = &quot;-r&quot;;
char r_option = &quot;/data/home/davidcyzhou/xxxx.pcap&quot;;
char V_symbol = &quot;-V&quot;;
char* args[4] = { arg_self, V_symbol, r_symbol, r_option };
tshark(4, args);</code></pre>4.when you build your program with libtshark.so, there might be some undefined reference err when it went with link command. Just comment related lines in your libtshark codes and rebuild. 5.before you execute your program, make sure your LD_LIBRARY_PATH have the path to the libtshark.so. 6.Now you should see your program can output like tshark does.</pre><h3 id="after-all-above-you-can-do-your-business-with-libtshark.so-like-if-you-want-to-get-the-contents-above-tcp-layer-in-each-packets-and-replay-them-just-save-the-contents-in-a-linked-list-where-it-prints-the-protocol-tree-in-tshark-and-return-the-list-back-to-your-program.-then-you-can-do-your-replay-logic-in-your-program.">After all above, you can do your business with libtshark.so, like if you want to get the contents above TCP layer in each packets and replay them, just save the contents in a linked-list where it prints the protocol tree in tshark and return the list back to your program. Then you can do your replay logic in your program.</h3><h4 id="i-will-be-happy-if-this-help-anyone-else.-if-you-have-trouble-with-the-process-please-send-me-emailemail-protected">I will be happy if this help anyone else. If you have trouble with the process, please send me email:<span class="__cf_email__" data-cfemail="c2b8aaadb7a6a3b4aba69db7acabb4a7b0b1a782aaadb6afa3abaeeca1adaf">[email protected]</span></h4></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '15, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/b42192f79bcad791f5c1e4593116f934?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="David%20Zhou&#39;s gravatar image" /><p><span>David Zhou</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="David Zhou has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jul '15, 06:27</strong> </span></p></div></div><div id="comments-container-43932" class="comments-container"></div><div id="comment-tools-43932" class="comment-tools"></div><div class="clear"></div><div id="comment-43932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

