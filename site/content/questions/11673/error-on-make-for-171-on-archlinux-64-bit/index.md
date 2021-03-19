+++
type = "question"
title = "Error on &#x27;make&#x27; for 1.7.1 on Archlinux 64 bit"
description = '''I&#x27;m trying to install the 1.7.1 version on ArchLinux (3.3.7-1-ARCH #1 SMP PREEMPT Tue May 22 00:26:26 CEST 2012 x86_64 GNU/Linux)  In the past, I was able to get it installed but haven&#x27;t been able to for the last few months. I keep getting the following errors. My configure options are: $ ./configur...'''
date = "2012-06-05T10:39:00Z"
lastmod = "2012-06-05T10:39:00Z"
weight = 11673
keywords = [ "development", "build", "error" ]
aliases = [ "/questions/11673" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error on 'make' for 1.7.1 on Archlinux 64 bit](/questions/11673/error-on-make-for-171-on-archlinux-64-bit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11673-score" class="post-score" title="current number of votes">0</div><span id="post-11673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to install the 1.7.1 version on ArchLinux (3.3.7-1-ARCH #1 SMP PREEMPT Tue May 22 00:26:26 CEST 2012 x86_64 GNU/Linux)</p><p>In the past, I was able to get it installed but haven't been able to for the last few months. I keep getting the following errors. My configure options are:</p><pre><code>$ ./configure --prefix=/opt --with-dumpcap-group=wireshark --disable-warnings-as-errors</code></pre><p>I've googled and looked all over the place for a solution with no luck. Any ideas?</p><p>This is how my make statement ends:</p><pre><code>libtool: link: gcc -g -O2 -Wall -W -Wextra -Wdeclaration-after-statement -Wendif-labels -Wpointer-arith -Wno-pointer-sign -Warray-bounds -Wcast-align -Wformat-security -Wold-style-definition -Wno-error=unused-but-set-variable -fexcess-precision=fast -pthread -I/usr/include/gtk-2.0 -I/usr/lib/gtk-2.0/include -I/usr/include/atk-1.0 -I/usr/include/cairo -I/usr/include/gdk-pixbuf-2.0 -I/usr/include/pango-1.0 -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include -I/usr/include/pixman-1 -I/usr/include/freetype2 -I/usr/include/libpng15 -Wl,--as-needed -o .libs/wireshark wireshark-capture-pcap-util-unix.o wireshark-capture-pcap-util.o wireshark-cfile.o wireshark-clopts_common.o wireshark-disabled_protos.o wireshark-frame_data_sequence.o wireshark-packet-range.o wireshark-print.o wireshark-ps.o wireshark-sync_pipe_write.o wireshark-timestats.o wireshark-tap-megaco-common.o wireshark-tap-rtp-common.o wireshark-version_info.o wireshark-capture_ifinfo.o wireshark-capture_sync.o wireshark-capture_ui_utils.o wireshark-airpcap_loader.o wireshark-capture.o wireshark-capture_info.o wireshark-capture_opts.o wireshark-color_filters.o wireshark-file.o wireshark-fileset.o wireshark-filters.o wireshark-g711.o wireshark-merge.o wireshark-proto_hier_stats.o wireshark-recent.o wireshark-summary.o wireshark-tempfile.o wireshark-u3.o .libs/wiresharkS.o -Wl,-O1 -Wl,--sort-common -Wl,--as-needed -Wl,-z -Wl,relro -Wl,--hash-style=gnu -Wl,--export-dynamic  -L/usr/local/lib ui/gtk/libgtkui.a ui/gtk/libgtkui_dirty.a ui/libui.a codecs/libcodec.a wiretap/.libs/libwiretap.so epan/.libs/libwireshark.so wsutil/.libs/libwsutil.so -L/usr/lib -lpcap -lcares -lkrb5 -lk5crypto -lcom_err -lgcrypt -lgpg-error -lportaudio -lgtk-x11-2.0 -lgdk-x11-2.0 -latk-1.0 -lgio-2.0 -lpangoft2-1.0 -lpangocairo-1.0 -lgdk_pixbuf-2.0 -lcairo -lpango-1.0 -lfreetype -lfontconfig -lgobject-2.0 -lglib-2.0 -lm -lz -pthread -Wl,-rpath -Wl,/opt/lib
/usr/bin/ld: ui/gtk/libgtkui.a(libgtkui_a-plugins_dlg.o): undefined reference to symbol &#39;g_module_name&#39;
/usr/bin/ld: note: &#39;g_module_name&#39; is defined in DSO /usr/lib/libgmodule-2.0.so.0 so try adding it to the linker command line
/usr/lib/libgmodule-2.0.so.0: could not read symbols: Invalid operation
collect2: error: ld returned 1 exit status
make[2]: *** [wireshark] Error 1
make[2]: Leaving directory `/data/downloads/wireshark-1.7.1&#39;
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/data/downloads/wireshark-1.7.1&#39;
make: *** [all] Error 2</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jun '12, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/f503508305c5080605ee816bdf0fbde0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jholbrook&#39;s gravatar image" /><p><span>jholbrook</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jholbrook has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jun '12, 17:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11673" class="comments-container"></div><div id="comment-tools-11673" class="comment-tools"></div><div class="clear"></div><div id="comment-11673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

