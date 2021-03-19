+++
type = "question"
title = "Link error on Windows 7 32 bits"
description = '''Hi all, the link error happened on Win 7, 32 bits as following...  Linking libwireshark.dll  link /INCREMENTAL:NO /NOLOGO -entry:_DllMainCRTStartup@12 -dll kernel32.lib ws2_32.lib mswsock.lib advapi32.lib shell32.lib psapi.lib /DEBUG /MACHINE:x86 /SafeSEH /DYNAMICBASE /FIXED:no /OUT:libwireshark.dll...'''
date = "2014-01-22T01:54:00Z"
lastmod = "2014-01-22T02:31:00Z"
weight = 29085
keywords = [ "link", "error" ]
aliases = [ "/questions/29085" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Link error on Windows 7 32 bits](/questions/29085/link-error-on-windows-7-32-bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29085-score" class="post-score" title="current number of votes">0</div><span id="post-29085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, the link error happened on Win 7, 32 bits as following...</p><hr /><pre><code>Linking libwireshark.dll
        link  /INCREMENTAL:NO /NOLOGO -entry:[email protected] -dll kernel32.lib  ws2_32.lib mswsock.lib advapi32.lib shell32.lib psapi.lib  /DEBUG /MACHINE:x86 /SafeSEH /DYNAMICBASE /FIXED:no   /OUT:libwireshark.dll  /IMPLIB:libwireshark.lib addr_and_mask.obj addr_resolv.obj address_to_str.obj afn.obj aftypes.obj app_mem_usage.obj asn1.obj atalk-utils.obj charsets.obj circuit.obj column.obj column-utils.obj conversation.obj crc16-tvb.obj crc32-tvb.obj crc8-tvb.obj decode_as.obj disabled_protos.obj dissector_filters.obj dvb_chartbl.obj dwarf.obj emem.obj epan.obj ex-opt.obj except.obj expert.obj exported_pdu.obj filter_expressions.obj follow.obj frame_data.obj frame_data_sequence.obj frequency-utils.obj funnel.obj gcp.obj geoip_db.obj golay.obj guid-utils.obj h225-persistentdata.obj in_cksum.obj ipproto.obj ipv4.obj next_tvb.obj oids.obj osi-utils.obj packet-range.obj packet.obj prefs.obj print.obj proto.obj range.obj reassemble.obj reedsolomon.obj req_resp_hdrs.obj show_exception.obj sigcomp_state_hdlr.obj sigcomp-udvm.obj sminmpec.obj sna-utils.obj stat_cmd_args.obj stats_tree.obj strutil.obj stream.obj t35.obj tap.obj timestamp.obj timestats.obj tfs.obj to_str.obj tvbparse.obj tvbuff_base64.obj tvbuff_composite.obj tvbuff_real.obj tvbuff_subset.obj tvbuff_zlib.obj tvbuff.obj uat.obj value_string.obj xdlc.obj diam_dict.obj dtd_parse.obj dtd_preparse.obj radius_dict.obj uat_load.obj dtd_grammar.obj ps.obj  C:\Wireshark-win32-libs\gtk3\lib\glib-2.0.lib  C:\Wireshark-win32-libs\gtk3\lib\gmodule-2.0.lib  C:\Wireshark-win32-libs\gtk3\lib\gobject-2.0.lib C:\Wireshark-win32-libs\c-ares-1.9.1-1-win32ws\lib\libcares-2.lib    C:\Wireshark-win32-libs\kfw-3-2-2-i386-ws-vc6\lib\krb5_32.lib    C:\Wireshark-win32-libs\zlib125\lib\zdll.lib   C:\Wireshark-win32-libs\gnutls-2.12.18-1.2-win32ws\bin\libtasn1-3.lib      C:\Wireshark-win32-libs\gnutls-2.12.18-1.2-win32ws\bin\libgpg-error-0.lib       C:\Wireshark-win32-libs\gnutls-2.12.18-1.2-win32ws\bin\libgcrypt-11.lib  C:\Wireshark-win32-libs\gnutls-2.12.18-1.2-win32ws\bin\libgnutls-26.lib  C:\Wireshark-win32-libs\lua5.1.4\lua5.1.lib    C:\Wireshark-win32-libs\libsmi-svn-40773-win32ws\lib\libsmi-2.lib  C:\Wireshark-win32-libs\GeoIP-1.5.1-2-win32ws\lib\libGeoIP-1.lib  ..\wsutil\libwsutil.lib  ..\wiretap\wiretap-1.11.0.lib  crypt\airpdcap.lib  ftypes\ftypes.lib  dfilter\dfilter.lib  wmem\wmem.lib  wslua\wslua.lib    dissectors\dissectors.lib ..\image\libwireshark.res  dissectors\register.obj  asm_utils_win32_x86.obj
   libwireshark.lib ????? ? libwireshark.exp ??? ???? ????.

dissectors.lib(packet-ncp-sss.obj) : error LNK2001: _ett_nds ?? ??? ??? ? ????.
libwireshark.dll : fatal error LNK1120: 1?? ??? ? ?? ?? ?????.

NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 10.0\VC\Bi
n\link.EXE&quot;&#39; : &#39;0x460&#39; ?? ?????.
Stop.

NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 10.0\VC\Bi
n\nmake.exe&quot;&#39; : &#39;0x2&#39; ?? ?????.
Stop.</code></pre><hr /><p>can I find any solution? Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-link" rel="tag" title="see questions tagged &#39;link&#39;">link</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '14, 01:54</strong></p><img src="https://secure.gravatar.com/avatar/1093195e125343067453a8d21cec3f03?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssmage&#39;s gravatar image" /><p><span>ssmage</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssmage has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '14, 02:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-29085" class="comments-container"><span id="29086"></span><div id="comment-29086" class="comment"><div id="post-29086-score" class="comment-score"></div><div class="comment-text"><p>Python version is now 3.3.3 It could be problem?</p></div><div id="comment-29086-info" class="comment-info"><span class="comment-age">(22 Jan '14, 02:16)</span> <span class="comment-user userinfo">ssmage</span></div></div></div><div id="comment-tools-29085" class="comment-tools"></div><div class="clear"></div><div id="comment-29085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29087"></span>

<div id="answer-container-29087" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29087-score" class="post-score" title="current number of votes">0</div><span id="post-29087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunately the actual link error has been replaced with ???, probably due an alternate code page in use. The symbol ett_nds is exported from packet-ncp.c. Have you tried an <code>nmake -f Makefile.nmake clean</code>?</p><p>I think we still recommend Python2.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '14, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-29087" class="comments-container"></div><div id="comment-tools-29087" class="comment-tools"></div><div class="clear"></div><div id="comment-29087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

