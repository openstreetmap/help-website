+++
type = "question"
title = "Shell32.lib file extension error in Wireshark-2.0.2 Build"
description = '''Hi Wireshark Version: 2.0.2, I tried building latest wireshark code on my Windows 7, MSVC2013 Compiler Please find the below error asking for shell32.lib extension.  I tried in changing extension(.lib) to MSVC, Notepad .... But no use stucked up with different error, [Error: Could not make libwersha...'''
date = "2016-04-25T04:28:00Z"
lastmod = "2016-04-25T07:01:00Z"
weight = 51920
keywords = [ "windows", "shell32", "wireshark" ]
aliases = [ "/questions/51920" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Shell32.lib file extension error in Wireshark-2.0.2 Build](/questions/51920/shell32lib-file-extension-error-in-wireshark-202-build)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51920-score" class="post-score" title="current number of votes">0</div><span id="post-51920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Wireshark Version: 2.0.2, I tried building latest wireshark code on my Windows 7, MSVC2013 Compiler Please find the below error asking for shell32.lib extension. <img src="https://osqa-ask.wireshark.org/upfiles/shell32_lib_error.JPG" alt="alt text" /></p><p>I tried in changing extension(.lib) to MSVC, Notepad .... But no use stucked up with different error, [Error: Could not make libwershark.lib] Please suggets me. If anyone came out of these error.</p><h2 id="text-form-for-the-above-error">Text Form for the above Error</h2><pre><code>cd dissectors
        &quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\nmake.exe&quot; /
                   -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 12.00.21005.1
Copyright (C) Microsoft Corporation.  All rights reserved.

&#39;dissectors.lib&#39; is up-to-date
        cd ..
Linking libwireshark.dll
           shell32.lib psapi.lib  /DEBUG /MACHINE:x86 /RELEASE /SafeSEH /DYNAMICBASE /FIXED:no   /OUT:libwireshark.dll  /IMPLIB:libwireshark.lib addr_and_mask.o
bj               addr_resolv.obj                 address_types.obj       afn.obj                         aftypes.obj             app_mem_usage.obj
asn1.obj                        charsets.obj            circuit.obj
column.obj              column-utils.obj                conversation.obj
         conversation_table.obj  crc10-tvb.obj           crc16-tvb.obj
         crc32-tvb.obj           crc6-tvb.obj            crc8-tvb.obj            decode_
as.obj           disabled_protos.obj     dissector_filters.obj   dvb_chartbl.obj                 dwarf.obj                       epan.obj
ex-opt.obj              except.obj              expert.obj              exported_pdu.obj                plugin_if.obj           filter_expressions.obj  follow.
obj              frame_data.obj          frame_data_sequence.obj         funnel.obj              g_int64_hash_routines.obj       gcp.obj
geoip_db.obj            golay.obj                       guid-utils.obj
in_cksum.obj            ipproto.obj             ipv4.obj
next_tvb.obj            oids.obj                        osi-utils.obj
oui.obj                         packet-range.obj                packet.obj
         prefs.obj                       print.obj                       print_stream.obj                proto.obj                       range.obj
         reassemble.obj          reedsolomon.obj                 req_resp_hdrs.obj               rtd_table.obj   show_exception.obj      sminmpec.obj
srt_table.obj   stat_tap_ui.obj                 stats_tree.obj          strutil.obj             stream.obj              t35.obj                         tap.obj
                         timestamp.obj           timestats.obj           tfs.obj                         to_str.obj              tvbparse.obj            tvbuff_base64.obj               tvbuff_composite.obj    tvbuff_real.obj
                         tvbuff_subset.obj               tvbuff_zlib.obj                 tvbuff.obj         uat.obj                         value_string.obj                xdlc.obj        diam_dict.obj           dtd_parse.obj           dtd_preparse.obj         radius_dict.obj                 uat_load.obj  dtd_grammar.obj
         ps.obj  C:\Wireshark-win32-libs-2.0\gtk2\lib\glib-2.0.lib  C:\Wireshark-win32-libs-2.0\gtk2\lib\gmodule-2.0.lib  C:\Wireshark-win32-libs-2.0\gtk2\lib\gobject-2.0.lib   C:\Wireshark-win32-libs-2.0\c-ares-1.9.1-1-win32ws\lib\libcares-2.lib    C:\Wireshark-win32-libs-2.0\kfw-3-2-2-i386-ws-vc6\lib\krb5_32.lib  C:\Wireshark-win32-libs-2.0\zlib-1.2.8-ws\lib\zdll.lib   C:\Wireshark-win32-libs-2.0\gnutls-3.2.15-2.7-win32ws\bin\libtasn1-6.lib   C:\Wireshark-win32-libs-2.0\gnutls-3.2.15-2.7-win32ws\bin\libgpg-error-0.lib    C:\Wireshark-win32-libs-2.0\gnutls-3.2.15-2.7-win32ws\bin\libgcrypt-20.lib  C:\Wireshark-win32-libs-2.0\gnutls-3.2.15-2.7-win32ws\bin\libgnutls-28.lib  C:\Wireshark-win32-libs-2.0\lua5.2.3\lua52.lib  C:\Wireshark-win32-libs-2.0\libsmi-svn-40773-win32ws\lib\libsmi-2.lib
C:\Wireshark-win32-libs-2.0\GeoIP-1.6.6-win32ws\lib\libGeoIP-1.lib  ..\wsutil\libwsutil.lib  ..\wiretap\wiretap-2.0.0.lib  compress\lzxpress.lib  crypt\airpdcap.lib  ftypes\ftypes.lib  dfilter\dfilter.lib  wmem\wmem.lib  wslua\wslua.lib  nghttp2\nghttp2.lib  dissectors\dissectors.lib ..\image\libwireshark.res  dissectors\register.obj  asm_utils_win32_x86.obj
The system cannot execute the specified program.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Lib\shell32.lib&quot;&#39; : return code &#39;0x1&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>Thanks Dinesh Sadu</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-shell32" rel="tag" title="see questions tagged &#39;shell32&#39;">shell32</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '16, 04:28</strong></p><img src="https://secure.gravatar.com/avatar/04334c27cb629065a13d61a61b611038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinesh%20Babu%20Sadu&#39;s gravatar image" /><p><span>Dinesh Babu ...</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinesh Babu Sadu has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Apr '16, 06:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-51920" class="comments-container"></div><div id="comment-tools-51920" class="comment-tools"></div><div class="clear"></div><div id="comment-51920-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51921"></span>

<div id="answer-container-51921" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51921-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51921-score" class="post-score" title="current number of votes">1</div><span id="post-51921-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You obscured screenshot looks as though you're building with nmake. Note that support for nmake will be dropped in 2.2.x, so you should switch to using CMake as per the Developer's Guide as soon as you can.</p><p>Please post the output from nmake (as text not a screenshot) to allow inspection of the actual output causing the error. Note that renaming "things" is unlikely to fix the issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '16, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51921" class="comments-container"><span id="51923"></span><div id="comment-51923" class="comment"><div id="post-51923-score" class="comment-score"></div><div class="comment-text"><p>Hi Grahamb</p><p>Updated the question with the output text form for the shell32.lib error</p><p>Thanks Dinesh Sadu</p></div><div id="comment-51923-info" class="comment-info"><span class="comment-age">(25 Apr '16, 05:35)</span> <span class="comment-user userinfo">Dinesh Babu ...</span></div></div><span id="51925"></span><div id="comment-51925" class="comment"><div id="post-51925-score" class="comment-score"></div><div class="comment-text"><p>Something has gone wrong with your build environment. If you look at the buildbots for 1.12.x (as neither 2.0 or master build with nmake anymore), then you can see the link command line should start:</p><pre><code>Linking libwireshark.dll
link  /INCREMENTAL:NO /NOLOGO -entry:_DllMainCRTStartup -dll kernel32.lib  ws2_32.lib mswsock.lib advapi32.lib shell32.lib psapi.lib  /DEBUG</code></pre><p>The bits between the link command and shell32.lib are provided by the nmake variables <code>dlllflags</code> and <code>conlibsdll</code>, which are in turn sourced from win32.mak. This file isn't provided by more recent installations of Visual Studio and has to be copied from an earlier version. I vaguely remember nmake objecting if it couldn't find this file. You might want to modify epan\Makefile.nmake to print out the contents of those variables.</p></div><div id="comment-51925-info" class="comment-info"><span class="comment-age">(25 Apr '16, 07:01)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-51921" class="comment-tools"></div><div class="clear"></div><div id="comment-51921-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

