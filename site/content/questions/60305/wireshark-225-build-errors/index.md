+++
type = "question"
title = "Wireshark 2.2.5 Build errors"
description = ''' qtui.dir&#92;RelWithDebInfo&#92;moc_protocol_hierarchy_dialog.obj  qtui.dir&#92;RelWithDebInfo&#92;moc_protocol_preferences_menu.obj  qtui.dir&#92;RelWithDebInfo&#92;moc_qcustomplot.obj  qtui.dir&#92;RelWithDebInfo&#92;moc_recent_file_status.obj  qtui.dir&#92;RelWithDebInfo&#92;moc_related_packet_delegate.obj  qtui.dir&#92;RelWithDebInfo&#92;moc...'''
date = "2017-03-24T03:08:00Z"
lastmod = "2017-04-06T01:43:00Z"
weight = 60305
keywords = [ "build_error", "build", "wireshark-2.2.5" ]
aliases = [ "/questions/60305" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark 2.2.5 Build errors](/questions/60305/wireshark-225-build-errors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60305-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60305-score" class="post-score" title="current number of votes">0</div><span id="post-60305-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>     qtui.dir\RelWithDebInfo\moc_protocol_hierarchy_dialog.obj
     qtui.dir\RelWithDebInfo\moc_protocol_preferences_menu.obj
     qtui.dir\RelWithDebInfo\moc_qcustomplot.obj
     qtui.dir\RelWithDebInfo\moc_recent_file_status.obj
     qtui.dir\RelWithDebInfo\moc_related_packet_delegate.obj
     qtui.dir\RelWithDebInfo\moc_resolved_addresses_dialog.obj
     qtui.dir\RelWithDebInfo\moc_response_time_delay_dialog.obj
     qtui.dir\RelWithDebInfo\moc_rpc_service_response_time_dialog.obj
     qtui.dir\RelWithDebInfo\moc_rtp_analysis_dialog.obj
     qtui.dir\RelWithDebInfo\moc_rtp_audio_stream.obj
     qtui.dir\RelWithDebInfo\moc_rtp_player_dialog.obj
     qtui.dir\RelWithDebInfo\moc_rtp_stream_dialog.obj
     qtui.dir\RelWithDebInfo\moc_sctp_all_assocs_dialog.obj
     qtui.dir\RelWithDebInfo\moc_sctp_assoc_analyse_dialog.obj
     qtui.dir\RelWithDebInfo\moc_sctp_chunk_statistics_dialog.obj
     qtui.dir\RelWithDebInfo\moc_sctp_graph_dialog.obj
     qtui.dir\RelWithDebInfo\moc_sctp_graph_arwnd_dialog.obj
     qtui.dir\RelWithDebInfo\moc_sctp_graph_byte_dialog.obj
     qtui.dir\RelWithDebInfo\moc_search_frame.obj
     qtui.dir\RelWithDebInfo\moc_sequence_diagram.obj
     qtui.dir\RelWithDebInfo\moc_sequence_dialog.obj
     qtui.dir\RelWithDebInfo\moc_show_packet_bytes_dialog.obj
     qtui.dir\RelWithDebInfo\moc_simple_dialog.obj
     qtui.dir\RelWithDebInfo\moc_splash_overlay.obj
     qtui.dir\RelWithDebInfo\moc_stats_tree_dialog.obj
     qtui.dir\RelWithDebInfo\moc_service_response_time_dialog.obj
     qtui.dir\RelWithDebInfo\moc_simple_statistics_dialog.obj
     qtui.dir\RelWithDebInfo\moc_stock_icon_tool_button.obj
     qtui.dir\RelWithDebInfo\moc_supported_protocols_dialog.obj
     qtui.dir\RelWithDebInfo\moc_syntax_line_edit.obj
     qtui.dir\RelWithDebInfo\moc_tap_parameter_dialog.obj
     qtui.dir\RelWithDebInfo\moc_tcp_stream_dialog.obj
     qtui.dir\RelWithDebInfo\moc_time_shift_dialog.obj
     qtui.dir\RelWithDebInfo\moc_timeline_delegate.obj
     qtui.dir\RelWithDebInfo\moc_traffic_table_dialog.obj
     qtui.dir\RelWithDebInfo\moc_uat_delegate.obj
     qtui.dir\RelWithDebInfo\moc_uat_dialog.obj
     qtui.dir\RelWithDebInfo\moc_uat_model.obj
     qtui.dir\RelWithDebInfo\moc_uat_tree_view.obj
     qtui.dir\RelWithDebInfo\moc_voip_calls_dialog.obj
     qtui.dir\RelWithDebInfo\moc_wireless_frame.obj
     qtui.dir\RelWithDebInfo\moc_wireshark_application.obj
     qtui.dir\RelWithDebInfo\moc_wireshark_dialog.obj
     qtui.dir\RelWithDebInfo\moc_wlan_statistics_dialog.obj
     qtui.dir\RelWithDebInfo\moc_remote_capture_dialog.obj
     qtui.dir\RelWithDebInfo\moc_remote_settings_dialog.obj
     qtui.dir\RelWithDebInfo\moc_extcap_argument.obj
     qtui.dir\RelWithDebInfo\moc_extcap_argument_file.obj
     qtui.dir\RelWithDebInfo\moc_extcap_argument_multiselect.obj
     qtui.dir\RelWithDebInfo\moc_extcap_options_dialog.obj
     qtui.dir\RelWithDebInfo\qrc_about.obj
     qtui.dir\RelWithDebInfo\qrc_languages.obj
     qtui.dir\RelWithDebInfo\qrc_layout.obj
     qtui.dir\RelWithDebInfo\qrc_toolbar.obj
     qtui.dir\RelWithDebInfo\qrc_wsicon.obj
     qtui.dir\RelWithDebInfo\qrc_i18n.obj
     &quot;qtui.dir\RelWithDebInfo\wireshark-tap-register.obj&quot;
     qtui.vcxproj -&gt; D:\Development\msbuild64\run\RelWithDebInfo\qtui.lib
   FinalizeBuildStatus:
     Deleting file &quot;qtui.dir\RelWithDebInfo\qtui.tlog\unsuccessfulbuild&quot;.
     Touching &quot;qtui.dir\RelWithDebInfo\qtui.tlog\qtui.lastbuildstate&quot;.</code></pre><p>106&gt;Done Building Project "D:\Development\msbuild64\ui\qt\qtui.vcxproj" (default targets). 40&gt;Done Building Project "D:\Development\msbuild64\ui\qt\qtui.vcxproj.metaproj" (default targets). 2&gt;Done Building Project "D:\Development\msbuild64\ALL_BUILD.vcxproj.metaproj" (default targets) -- FAILED. 1&gt;Done Building Project "D:\Development\msbuild64\Wireshark.sln" (default targets) -- FAILED.</p><p>Build FAILED.</p><pre><code>   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\docbook\release_notes_html.vcxproj.metaproj&quot; (default target) (46) -&gt;
   &quot;D:\Development\msbuild64\docbook\release_notes_html.vcxproj&quot; (default target) (101) -&gt;
   (CustomBuild target) -&gt;
     a2x : error : &quot;xmllint&quot; --nonet --noout --valid &quot;/cygdrive/d/Development/msbuild64/docbook/release-notes.xml&quot; returned non-zero exit status 4 [D:\Development\ms
   build64\docbook\release_notes_html.vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\wsutil\wsutil.vcxproj.metaproj&quot; (default target) (77) -&gt;
   &quot;D:\Development\msbuild64\wsutil\wsutil.vcxproj&quot; (default target) (97) -&gt;
   (Link target) -&gt;
     LINK : fatal error LNK1181: cannot open input file &#39;gmodule-2.0.lib&#39; [D:\Development\msbuild64\wsutil\wsutil.vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\epan\dissectors\dissectors.vcxproj.metaproj&quot; (default target) (19) -&gt;
   &quot;D:\Development\msbuild64\epan\dissectors\dissectors.vcxproj&quot; (default target) (89) -&gt;
   (ClCompile target) -&gt;
     D:\Development\WireShark\epan\dissectors\packet-ipv6.c(2093): error C2275: &#39;guint16&#39; : illegal use of this type as an expression [D:\Development\msbuild64\epan\
   dissectors\dissectors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-ipv6.c(2093): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;mapped_port&#39; [D:\Development\msbuild64\
   epan\dissectors\dissectors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-ipv6.c(2093): error C2065: &#39;mapped_port&#39; : undeclared identifier [D:\Development\msbuild64\epan\dissectors\disse
   ctors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-ipv6.c(2104): error C2065: &#39;mapped_port&#39; : undeclared identifier [D:\Development\msbuild64\epan\dissectors\disse
   ctors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-usb-i1d3.c(434): error C2275: &#39;guint32&#39; : illegal use of this type as an expression [D:\Development\msbuild64\ep
   an\dissectors\dissectors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-usb-i1d3.c(434): error C2146: syntax error : missing &#39;;&#39; before identifier &#39;response_code&#39; [D:\Development\msbui
   ld64\epan\dissectors\dissectors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-usb-i1d3.c(434): error C2065: &#39;response_code&#39; : undeclared identifier [D:\Development\msbuild64\epan\dissectors\
   dissectors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-usb-i1d3.c(436): error C2065: &#39;response_code&#39; : undeclared identifier [D:\Development\msbuild64\epan\dissectors\
   dissectors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-usb-i1d3.c(438): error C2065: &#39;response_code&#39; : undeclared identifier [D:\Development\msbuild64\epan\dissectors\
   dissectors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-usb-i1d3.c(439): error C2065: &#39;response_code&#39; : undeclared identifier [D:\Development\msbuild64\epan\dissectors\
   dissectors.vcxproj]
     D:\Development\WireShark\epan\dissectors\packet-usb-i1d3.c(442): error C2065: &#39;response_code&#39; : undeclared identifier [D:\Development\msbuild64\epan\dissectors\
   dissectors.vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (default target) (62) -&gt;
   &quot;D:\Development\msbuild64\docbook\user_guide_chm.vcxproj&quot; (default target) (105) -&gt;
   (CustomBuild target) -&gt;
     CUSTOMBUILD : I/O error : Attempt to load network entity http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd [D:\Development\msbuild64\docbook\user_guide_chm
   .vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (default target) (14) -&gt;
   &quot;D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj&quot; (default target) (111) -&gt;
     CUSTOMBUILD : I/O error : Attempt to load network entity http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd [D:\Development\msbuild64\docbook\developer_guid
   e_chm.vcxproj]

0 Warning(s)
15 Error(s)</code></pre><p>Time Elapsed 00:07:54.83</p><p>I just took the sources code and started building it. no idea wat is causing the build errors as i fallowed the procedure as mentioned in the developers guide.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-build_error" rel="tag" title="see questions tagged &#39;build_error&#39;">build_error</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-wireshark-2.2.5" rel="tag" title="see questions tagged &#39;wireshark-2.2.5&#39;">wireshark-2.2.5</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '17, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/600778689935688cd4eaaa966e880cae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DhanuShalz&#39;s gravatar image" /><p><span>DhanuShalz</span><br />
<span class="score" title="36 reputation points">36</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DhanuShalz has one accepted answer">100%</span></p></div></div><div id="comments-container-60305" class="comments-container"><span id="60313"></span><div id="comment-60313" class="comment"><div id="post-60313-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_8nZOmeX.JPG" width="640" /></p><p>The above was observed!</p></div><div id="comment-60313-info" class="comment-info"><span class="comment-age">(24 Mar '17, 07:29)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60316"></span><div id="comment-60316" class="comment"><div id="post-60316-score" class="comment-score"></div><div class="comment-text"><p>Does your build machine have internet access? Among other things it seems to be failing to download some xml files. You also have a problem with gmodule.</p><p>Please post the output (as text) of the CMake generation step, i.e.</p><pre><code>cmake -G ... &gt; cmake.txt</code></pre><p>I need to see what's in cmake.txt</p><p>To post msbuild output use the following redirection to capture the build info:</p><pre><code>msbuild ... 2&gt;&amp;1 &gt; msbuild.txt</code></pre></div><div id="comment-60316-info" class="comment-info"><span class="comment-age">(24 Mar '17, 08:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60337"></span><div id="comment-60337" class="comment"><div id="post-60337-score" class="comment-score"></div><div class="comment-text"><p><a href="https://drive.google.com/open?id=0B9dMRjnjjypGQlpoSjR1dUJadDg">cmake.txt</a></p><p><a href="https://drive.google.com/open?id=0B9dMRjnjjypGZ3pSN3lFUmoybmM">msbuid.txt</a></p><p><span>@grahamb</span> please find the attached log</p></div><div id="comment-60337-info" class="comment-info"><span class="comment-age">(27 Mar '17, 02:19)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div></div><div id="comment-tools-60305" class="comment-tools"></div><div class="clear"></div><div id="comment-60305-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60339"></span>

<div id="answer-container-60339" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60339-score" class="post-score" title="current number of votes">0</div><span id="post-60339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DhanuShalz has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The CMake output looks OK, the build errors were:</p><pre><code>   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\docbook\generate_user-guide.xml.vcxproj.metaproj&quot; (default target) (32) -&gt;
   &quot;D:\Development\msbuild64\docbook\generate_user-guide.xml.vcxproj&quot; (default target) (97) -&gt;
   (CustomBuild target) -&gt; 
     asciidoc : warning : user-guide.asciidoc: line 3: {include:/cygdrive/d/Development/WireShark/docbook/user-guide-docinfo.xml}: file does not exist [D:\Development\msbuild64\docbook\generate_user-guide.xml.vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\docbook\generate_developer-guide.xml.vcxproj.metaproj&quot; (default target) (31) -&gt;
   &quot;D:\Development\msbuild64\docbook\generate_developer-guide.xml.vcxproj&quot; (default target) (96) -&gt;
     asciidoc : warning : developer-guide.asciidoc: line 3: {include:/cygdrive/d/Development/WireShark/docbook/developer-guide-docinfo.xml}: file does not exist [D:\Development\msbuild64\docbook\generate_developer-guide.xml.vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\docbook\release_notes_html.vcxproj.metaproj&quot; (default target) (51) -&gt;
   &quot;D:\Development\msbuild64\docbook\release_notes_html.vcxproj&quot; (default target) (105) -&gt;
   (CustomBuild target) -&gt; 
     a2x : error : &quot;xmllint&quot; --nonet --noout --valid &quot;/cygdrive/d/Development/msbuild64/docbook/release-notes.xml&quot; returned non-zero exit status 4 [D:\Development\msbuild64\docbook\release_notes_html.vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\docbook\user_guide_chm.vcxproj.metaproj&quot; (default target) (64) -&gt;
   &quot;D:\Development\msbuild64\docbook\user_guide_chm.vcxproj&quot; (default target) (115) -&gt;
     CUSTOMBUILD : I/O error : Attempt to load network entity http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd [D:\Development\msbuild64\docbook\user_guide_chm.vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj.metaproj&quot; (default target) (15) -&gt;
   &quot;D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj&quot; (default target) (117) -&gt;
     CUSTOMBUILD : I/O error : Attempt to load network entity http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd [D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj]

   &quot;D:\Development\msbuild64\Wireshark.sln&quot; (default target) (1) -&gt;
   &quot;D:\Development\msbuild64\wsutil\wsutil.vcxproj.metaproj&quot; (default target) (80) -&gt;
   &quot;D:\Development\msbuild64\wsutil\wsutil.vcxproj&quot; (default target) (98) -&gt;
   (Link target) -&gt; 
     LINK : fatal error LNK1181: cannot open input file &#39;gmodule-2.0.lib&#39; [D:\Development\msbuild64\wsutil\wsutil.vcxproj]</code></pre><p>The first few errors are issues with building the documentation, some of which seem to be an inability to download required xml files from the internet. I repeat my question, does the build machine have direct internet access?</p><p>The link error is an inability to locate gmodule-2.0.lib, this is because CMake has picked up some other form of gmodule (and gthread2) as can be seen by the CMake output:</p><pre><code>-- Checking for one of the modules &#39;gmodule-2.0&#39;
-- GMODULE2 FOUND
-- GMODULE2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include
-- GMODULE2 libs: gmodule-2.0;glib-2.0;intl

-- Checking for one of the modules &#39;gthread-2.0&#39;
-- GTHREAD2 FOUND
-- GTHREAD2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include
-- GTHREAD2 libs: gthread-2.0;glib-2.0;intl</code></pre><p>To fix this you'll need to locate where these are coming from, possibly Cygwin or something else on your PATH and either remove the items or remove them from your PATH, delete CMakecache.txt and re-run the CMake generation step.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '17, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-60339" class="comments-container"><span id="60340"></span><div id="comment-60340" class="comment"><div id="post-60340-score" class="comment-score"></div><div class="comment-text"><p><strong>The first few errors are issues with building the documentation, some of which seem to be an inability to download required xml files from the internet. I repeat my question, does the build machine have direct internet access?</strong></p><p>the machine does have a direct internet connection</p></div><div id="comment-60340-info" class="comment-info"><span class="comment-age">(27 Mar '17, 02:59)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60343"></span><div id="comment-60343" class="comment"><div id="post-60343-score" class="comment-score"></div><div class="comment-text"><p>The download errors are:</p><pre><code>115&gt;CUSTOMBUILD : I/O error : Attempt to load network entity http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd [D:\Development\msbuild64\docbook\user_guide_chm.vcxproj]
     user-guide-plain-title.xml:2: warning: failed to load external entity &quot;http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd&quot;
     D DocBook XML V4.5//EN&quot; &quot;http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd&quot;
                                                                                    ^
117&gt;CUSTOMBUILD : I/O error : Attempt to load network entity http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd [D:\Development\msbuild64\docbook\developer_guide_chm.vcxproj]
     developer-guide-plain-title.xml:2: warning: failed to load external entity &quot;http://www.oasis-open.org/docbook/xml/4.5/docbookx.dtd&quot;</code></pre></div><div id="comment-60343-info" class="comment-info"><span class="comment-age">(27 Mar '17, 03:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60346"></span><div id="comment-60346" class="comment"><div id="post-60346-score" class="comment-score"></div><div class="comment-text"><p>You can modify the CMake command so that the documentation isn't built so those xml errors won't occur by deleting CMakeCache.txt and running the CMake generation step, but omitting the "-DENABLE_CHM_GUIDES=on" part, but note that if you try to build the installer that will fail.</p></div><div id="comment-60346-info" class="comment-info"><span class="comment-age">(27 Mar '17, 03:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60387"></span><div id="comment-60387" class="comment"><div id="post-60387-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@grahamb</span></p><p>-- Checking for one of the modules 'gmodule-2.0' -- GMODULE2 FOUND -- GMODULE2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include -- GMODULE2 libs: gmodule-2.0;glib-2.0;intl</p><p>-- Checking for one of the modules 'gthread-2.0' -- GTHREAD2 FOUND -- GTHREAD2 includes: /usr/include/glib-2.0;/usr/lib/glib-2.0/include -- GTHREAD2 libs: gthread-2.0;glib-2.0;intl</p><p>Can i get more insight on this, As i have tried removing the file from this location(/usr/include/glib-2.0), im facing the same error? and no such PATH is set.</p></div><div id="comment-60387-info" class="comment-info"><span class="comment-age">(28 Mar '17, 07:25)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60388"></span><div id="comment-60388" class="comment"><div id="post-60388-score" class="comment-score"></div><div class="comment-text"><p>Cmake uses "modules" to find libraries, for gmodule and gthread they are in the Wireshark source tree under cmake\modules\FINDGMODULE2.cmake and FINDGTHREAD2.cmake respectively.</p><p>Both modules try to use pkgconfig to locate the libraries first, normally that doesn't work on Windows as there is no pkgconfig, and then the modules take a hint which includes the Wireshark 3rd party libraries downloaded for the build (in your case Wireshark-win64-libs-2.2), and looks in there.</p><p>However from your CMake output it seems that the Cygwin pkgconfig was found:</p><pre><code>Found PkgConfig: C:/cygwin64/bin/pkg-config.exe (found version &quot;0.29.1&quot;)</code></pre><p>I suspect this is messing things up for you, probably because you have the Cygwin bin dir on your path (C:\cygwin64\bin). All my Wireshark build VM's do NOT have Cygwin on the path because of issues like this, even extending back to the nmake days.</p></div><div id="comment-60388-info" class="comment-info"><span class="comment-age">(28 Mar '17, 08:47)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="60452"></span><div id="comment-60452" class="comment not_top_scorer"><div id="post-60452-score" class="comment-score"></div><div class="comment-text"><p><span>@DhanuShalz</span> I'm seeing the same errors you're seeing related to glib...working with grahamb here:</p><p><a href="https://ask.wireshark.org/questions/59065/updating-custom-dissector-from-16-wireshark-to-22-wireshark">https://ask.wireshark.org/questions/59065/updating-custom-dissector-from-16-wireshark-to-22-wireshark</a></p><p>Just so you know. Working on finding a solution right now. I will post an answer here when I do.</p></div><div id="comment-60452-info" class="comment-info"><span class="comment-age">(30 Mar '17, 13:45)</span> <span class="comment-user userinfo">aawale15</span></div></div><span id="60599"></span><div id="comment-60599" class="comment not_top_scorer"><div id="post-60599-score" class="comment-score"></div><div class="comment-text"><p>"D:\Development\msbuild\Wireshark.sln" (default target) (1) -&gt; "D:\Development\msbuild\docbook\developer_guide_chm.vcxproj.metaproj" (default target) (16) -&gt; "D:\Development\msbuild\docbook\developer_guide_chm.vcxproj" (default target) (101) -&gt; (CustomBuild target) -&gt; HHC5003 : error : Compilation failed while compiling ws.css. [D:\Development\msbuild\docbook\developer_guide_chm.vcxproj]</p><p>"D:\Development\msbuild\Wireshark.sln" (default target) (1) -&gt; "D:\Development\msbuild\docbook\all_guides.vcxproj.metaproj" (default target) (3) -&gt; "D:\Development\msbuild\docbook\user_guides.vcxproj.metaproj" (default target) (30) -&gt; "D:\Development\msbuild\docbook\user_guide_chm.vcxproj.metaproj" (default target) (33) -&gt; "D:\Development\msbuild\docbook\user_guide_chm.vcxproj" (default target) (124) -&gt; (CustomBuild target) -&gt; HHC5003 : error : Compilation failed while compiling ws.css. [D:\Development\msbuild\docbook\user_guide_chm.vcxproj]</p><p>not sure what is causing it to fail! <span>@grahamb</span></p></div><div id="comment-60599-info" class="comment-info"><span class="comment-age">(05 Apr '17, 22:57)</span> <span class="comment-user userinfo">DhanuShalz</span></div></div><span id="60601"></span><div id="comment-60601" class="comment not_top_scorer"><div id="post-60601-score" class="comment-score"></div><div class="comment-text"><p>You seemed to have moved on a bit. In the past I had issues with ws.css being created by Cygwin with odd permissions. Deleting ws.css in your build directory docbook directory fixed that for me and then rebuilding.</p></div><div id="comment-60601-info" class="comment-info"><span class="comment-age">(06 Apr '17, 01:43)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-60339" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-60339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

