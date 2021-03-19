+++
type = "question"
title = "Wireshark fails to run on my SPARC server"
description = '''Hi,   I have installed the wireshark server on my sparc server. after installing when I am launching the wireshark it gets launched successfully.  But after I do do the tcsh to set the DISPLAY I gets the below error. what could be the reason: ld.so.1: wireshark: fatal: relocation error: file /usr/lo...'''
date = "2013-06-13T04:58:00Z"
lastmod = "2013-06-30T23:04:00Z"
weight = 22004
keywords = [ "launch", "wireshark" ]
aliases = [ "/questions/22004" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark fails to run on my SPARC server](/questions/22004/wireshark-fails-to-run-on-my-sparc-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22004-score" class="post-score" title="current number of votes">0</div><span id="post-22004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have installed the wireshark server on my sparc server. after installing when I am launching the wireshark it gets launched successfully.</p><p>But after I do do the tcsh to set the DISPLAY I gets the below error. what could be the reason:</p><p>ld.so.1: wireshark: fatal: relocation error: file /usr/local/lib/libwireshark.so.1: symbol g_int64_equal: referenced symbol not found Killed</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-launch" rel="tag" title="see questions tagged &#39;launch&#39;">launch</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '13, 04:58</strong></p><img src="https://secure.gravatar.com/avatar/c83ca22a760e356093e591f491b6744f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KumarM&#39;s gravatar image" /><p><span>KumarM</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KumarM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '13, 10:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-22004" class="comments-container"></div><div id="comment-tools-22004" class="comment-tools"></div><div class="clear"></div><div id="comment-22004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22018"></span>

<div id="answer-container-22018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22018-score" class="post-score" title="current number of votes">0</div><span id="post-22018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you configure and build Wireshark on a machine with the same version of the GLib library as the server on which you installed it?</p><p>If not, do so. g_int64_equal() is defined by GLib 2.22 and later; if Wireshark is built on a system with a pre-2.22 version of GLib, the Infiniband dissector will supply its own versions, but if it's built on a system with GLib 2.22 or later, it relies on GLib to supply it, so if you configure and build Wireshark on a system with GLib 2.22 or later, that version of Wireshark will not work on a system with a version of GLib earlier than GLib 2.22.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22018" class="comments-container"><span id="22361"></span><div id="comment-22361" class="comment"><div id="post-22361-score" class="comment-score"></div><div class="comment-text"><p>I have installed Glib 2.22. But now I am getting another error:</p><p>ld.so.1: wireshark: fatal: relocation error: file /usr/local/bin/wireshark: symbol gtk_window_set_icon_name: referenced symbol not found</p><p>I did not find any info related to above error. Anyone knows what could be the reason of this error.</p></div><div id="comment-22361-info" class="comment-info"><span class="comment-age">(26 Jun '13, 07:26)</span> <span class="comment-user userinfo">KumarM</span></div></div><span id="22368"></span><div id="comment-22368" class="comment"><div id="post-22368-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Anyone knows what could be the reason of this error.</p></blockquote><p>One reason could be that <a href="https://developer.gnome.org/gtk2/stable/GtkWindow.html#gtk-window-set-icon-name"><code>gtk_window_set_icon_name()</code> isn't present in GTK+ prior to 2.6</a>, so you'll need to install GTK+ 2.6 or later if you have an older version installed.</p></div><div id="comment-22368-info" class="comment-info"><span class="comment-age">(26 Jun '13, 10:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="22435"></span><div id="comment-22435" class="comment"><div id="post-22435-score" class="comment-score"></div><div class="comment-text"><p>I have installed the gtk+-2.12.0-sol10-x86-local, but still the same error.</p></div><div id="comment-22435-info" class="comment-info"><span class="comment-age">(27 Jun '13, 20:29)</span> <span class="comment-user userinfo">KumarM</span></div></div><span id="22441"></span><div id="comment-22441" class="comment"><div id="post-22441-score" class="comment-score"></div><div class="comment-text"><p>What gets printed by</p><pre><code>ldd /usr/local/bin/wireshark</code></pre></div><div id="comment-22441-info" class="comment-info"><span class="comment-age">(28 Jun '13, 00:06)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="22448"></span><div id="comment-22448" class="comment"><div id="post-22448-score" class="comment-score"></div><div class="comment-text"><p>Here is the output:</p><pre><code>atrcx1220{root} # ldd /usr/local/bin/wireshark
 libwiretap.so.2 =&gt;  /usr/local/lib/libwiretap.so.2
 libwireshark.so.2 =&gt; /usr/local/lib/libwireshark.so.2
 liblua.so =&gt;     /usr/local/lib/liblua.so
 libwsutil.so.2 =&gt;   /usr/local/lib/libwsutil.so.2
 libcrypto.so.0.9.8 =&gt;    /usr/local/ssl/lib/libcrypto.so.0.9.8
 libkrb5.so.3 =&gt;  /usr/local/lib/libkrb5.so.3
 libk5crypto.so.3 =&gt; /usr/local/lib/libk5crypto.so.3
 libcom_err.so.3 =&gt;  /usr/local/lib/libcom_err.so.3
 libgtk-x11-2.0.so.0 =&gt;   /usr/local/lib/libgtk-x11-2.0.so.0
 libgdk-x11-2.0.so.0 =&gt;  /usr/local/lib/libgdk-x11-2.0.so.0
 libatk-1.0.so.0 =&gt;  /usr/local/lib/libatk-1.0.so.0
 libgdk_pixbuf-2.0.so.0 =&gt;        /usr/local/lib/libgdk_pixbuf-2.0.so.0
 libmlib.so.2 =&gt;  /usr/lib/libmlib.so.2
 libpangocairo-1.0.so.0 =&gt; /usr/local/lib/libpangocairo-1.0.so.0
 libpangoft2-1.0.so.0 =&gt;  /usr/local/lib/libpangoft2-1.0.so.0
 libpango-1.0.so.0 =&gt;  /usr/local/lib/libpango-1.0.so.0
 libcairo.so.2 =&gt;  /usr/local/lib/libcairo.so.2
 libfontconfig.so.1 =&gt;  /usr/local/lib/libfontconfig.so.1
 libfreetype.so.6 =&gt;  /usr/local/lib/libfreetype.so.6
 libexpat.so.1 =&gt; /usr/local/lib/libexpat.so.1
 libresolv.so.2 =&gt; /usr/lib/libresolv.so.2
 libpng12.so.0 =&gt;  /usr/local/lib/libpng12.so.0
 libXrender.so.1 =&gt; /usr/local/lib/libXrender.so.1
 libSM.so.6 =&gt;    /usr/lib/libSM.so.6
 libICE.so.6 =&gt;   /usr/lib/libICE.so.6
 libX11.so.4 =&gt;   /usr/lib/libX11.so.4
 libsocket.so.1 =&gt; /usr/lib/libsocket.so.1
 libgobject-2.0.so.0 =&gt; /usr/local/lib/libgobject-2.0.so.0
 libgthread-2.0.so.0 =&gt; /usr/local/lib/libgthread-2.0.so.0
 libpthread.so.1 =&gt; /usr/lib/libpthread.so.1
 libthread.so.1 =&gt;  /usr/lib/libthread.so.1
 librt.so.1 =&gt;  /usr/lib/librt.so.1
 libgmodule-2.0.so.0 =&gt;  /usr/local/lib/libgmodule-2.0.so.0
 libdl.so.1 =&gt;    /usr/lib/libdl.so.1
 libglib-2.0.so.0 =&gt;      /usr/local/lib/libglib-2.0.so.0
 libintl.so.8 =&gt;  /usr/local/lib/libintl.so.8
 libiconv.so.2 =&gt; /usr/local/lib/libiconv.so.2
 libsec.so.1 =&gt; /usr/lib/libsec.so.1
 libc.so.1 =&gt; /usr/lib/libc.so.1
 libm.so.2 =&gt; /usr/lib/libm.so.2
 libnsl.so.1 =&gt;/usr/lib/libnsl.so.1
 libz.so =&gt;/usr/local/lib/libz.so
 libgcc_s.so.1 =&gt;  /usr/local/lib/libgcc_s.so.1
 libkrb5support.so.0 =&gt; /usr/local/lib/libkrb5support.so.0
 libXrandr.so.2 =&gt; /usr/lib/libXrandr.so.2
 libXext.so.0 =&gt;  /usr/lib/libXext.so.0
 libexpat.so.0 =&gt; /usr/local/lib/libexpat.so.0
 libaio.so.1 =&gt;   /lib/libaio.so.1
 libmd.so.1 =&gt;    /lib/libmd.so.1
 libavl.so.1 =&gt;   /lib/libavl.so.1
 libmp.so.2 =&gt;    /lib/libmp.so.2
 libscf.so.1 =&gt;   /lib/libscf.so.1
 libXrender.so.1 =&gt; /usr/openwin/sfw/lib/libXrender.so.1
 libdoor.so.1 =&gt;  /lib/libdoor.so.1
 libuutil.so.1 =&gt;/lib/libuutil.so.1
 libgen.so.1 =&gt; /lib/libgen.so.1
 /usr/lib/libmlib/libmlib_sse2.so.2</code></pre></div><div id="comment-22448-info" class="comment-info"><span class="comment-age">(28 Jun '13, 03:22)</span> <span class="comment-user userinfo">KumarM</span></div></div><span id="22455"></span><div id="comment-22455" class="comment not_top_scorer"><div id="post-22455-score" class="comment-score"></div><div class="comment-text"><p>OK, what does</p><pre><code>nm -p /usr/local/lib/libgtk-x11-2.0.so.0 | egrep gtk_window_set_icon_name</code></pre><p>print?</p></div><div id="comment-22455-info" class="comment-info"><span class="comment-age">(28 Jun '13, 09:22)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="22496"></span><div id="comment-22496" class="comment not_top_scorer"><div id="post-22496-score" class="comment-score"></div><div class="comment-text"><p>This:</p><pre><code>atrcx1220{root} # nm -p /usr/local/lib/libgtk-x11-2.0.so.0 | egrep gtk_window_set_icon_name
0002388232 T gtk_window_set_icon_name</code></pre></div><div id="comment-22496-info" class="comment-info"><span class="comment-age">(30 Jun '13, 20:15)</span> <span class="comment-user userinfo">KumarM</span></div></div><span id="22499"></span><div id="comment-22499" class="comment not_top_scorer"><div id="post-22499-score" class="comment-score"></div><div class="comment-text"><p>And if you type the command</p><pre><code>/usr/local/bin/wireshark</code></pre><p>what happens?</p></div><div id="comment-22499-info" class="comment-info"><span class="comment-age">(30 Jun '13, 23:04)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-22018" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-22018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

