+++
type = "question"
title = "Linking problem when add an extra lib to wireshark"
description = '''I&#x27;ve added libcstl to wireshark project.When I compile, problems occur: a lot of unresolved external symbols e.g. dissectors.lib(packet-http.obj) : error LNK2019: unresolved external symbol _set_init I think I should add libcstl.lib to the dependent library list, but I don&#x27;t know where to add it.Any...'''
date = "2013-11-20T01:28:00Z"
lastmod = "2013-11-20T19:11:00Z"
weight = 27139
keywords = [ "problem", "add", "lib", "linking" ]
aliases = [ "/questions/27139" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Linking problem when add an extra lib to wireshark](/questions/27139/linking-problem-when-add-an-extra-lib-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27139-score" class="post-score" title="current number of votes">0</div><span id="post-27139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've added libcstl to wireshark project.When I compile, problems occur: a lot of unresolved external symbols e.g. dissectors.lib(packet-http.obj) : error LNK2019: unresolved external symbol _set_init</p><p>I think I should add libcstl.lib to the dependent library list, but I don't know where to add it.Anybody knows?</p><p>Any reply will be appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-add" rel="tag" title="see questions tagged &#39;add&#39;">add</span> <span class="post-tag tag-link-lib" rel="tag" title="see questions tagged &#39;lib&#39;">lib</span> <span class="post-tag tag-link-linking" rel="tag" title="see questions tagged &#39;linking&#39;">linking</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '13, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p><span>metamatrix</span><br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Nov '13, 01:30</strong> </span></p></div></div><div id="comments-container-27139" class="comments-container"><span id="27142"></span><div id="comment-27142" class="comment"><div id="post-27142-score" class="comment-score"></div><div class="comment-text"><p>How did you add the library to the project? You seem to have broken existing dissectors, have you modified them as well? Are you able to compile an unmodified version? And what version of Wireshark are you modifying?</p></div><div id="comment-27142-info" class="comment-info"><span class="comment-age">(20 Nov '13, 02:18)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="27184"></span><div id="comment-27184" class="comment"><div id="post-27184-score" class="comment-score"></div><div class="comment-text"><blockquote><p>How did you add the library to the project? You seem to have broken existing dissectors, have you modified them as well? Are you able to compile an unmodified version? And what version of Wireshark are you modifying?</p></blockquote><p>I add the library in visual studio. I add the set_init function in libcstl to dissectors.Unmodified version is OK. Wireshark version is 1.10.2 stable.</p></div><div id="comment-27184-info" class="comment-info"><span class="comment-age">(20 Nov '13, 16:52)</span> <span class="comment-user userinfo">metamatrix</span></div></div><span id="27187"></span><div id="comment-27187" class="comment"><div id="post-27187-score" class="comment-score"></div><div class="comment-text"><p>I use nmake to make wireshark project on windows.I just want to know where to modify the dependent library for libwireshark(I want to add libcstl to below arg list, where to config it? In makefiles or config files?).</p><p>Linking libwireshark.dll link /INCREMENTAL:NO /NOLOGO -entry:<span class="__cf_email__" data-cfemail="b7e8f3dbdbfad6ded9f4e5e3e4c3d6c5c3c2c7f78685">[email protected]</span> -dll kernel32 .lib ws2_32.lib mswsock.lib advapi32.lib shell32.lib /DEBUG /MACHINE:x86 /Safe SEH /DYNAMICBASE /FIXED:no /OUT:libwireshark.dll /IMPLIB:libwireshark.lib add r_and_mask.obj addr_resolv.obj address_to_str.obj adler32.obj afn.obj asn1.obj atalk-utils.obj base64.obj bitswap.obj camel-persistentdata.obj charsets.obj circuit.obj codecs.obj column.obj column-utils.obj conversation.obj crc16-tvb.obj crc32-tvb.obj crc8-tvb.obj dissector_filters.obj emem.obj epan.obj ex-opt.obj except.obj expert.obj filesystem.obj filter_expressions.obj follow.obj frame_data.obj frequency-utils.obj funnel. obj gcp.obj geoip_db.obj golay.o bj guid-utils.obj h225-persistentdata.obj in_cksum.obj ipproto.obj ipv4.obj next_tvb.obj nstime.obj oids.obj osi-utils.obj packet.obj plugins.obj prefs.o bj proto.obj range.obj reassemble.obj reedsolomon.obj report_err.obj req_resp_hdrs.obj show_exception.obj sigcomp_state_h dlr.obj sigcomp-udvm.obj sminmpec.obj sna-utils.obj stat_cmd_args.obj stats_tree.obj strutil.obj stream.obj t35.obj tap.obj tcap-persistentdata.obj timestamp.obj tfs.obj to_str.obj tvbparse.obj tvbuff. obj uat.obj value_string.obj xdlc.obj diam_dict.obj dtd_parse.obj dtd_preparse.ob j radius_dict.obj uat_load.obj dtd_grammar.obj C:\Wireshark-win32-libs-1.10\gtk2\lib\glib-2.0.lib C:\Wireshark-win32-libs-1.10 \gtk2\lib\gmodule-2.0.lib C:\Wireshark-win32-libs-1.10\gtk2\lib\gobject-2.0.lib C:\Wireshark-win32-libs-1.10\c-ares-1.9.1-1-win32ws\lib\libcares-2.lib C:\Wireshark-win32-libs-1.10\kfw-3-2-2-i386-ws-vc6\lib\krb5_32.lib C:\Wire shark-win32-libs-1.10\zlib125\lib\zdll.lib C:\Wireshark-win32-libs-1.10\gnutls -2.12.18-1.2-win32ws\bin\libtasn1-3.lib C:\Wireshark-win32-libs-1.10\gnutls-2.1 2.18-1.2-win32ws\bin\libgpg-error-0.lib C:\Wireshark-win32-libs-1.10\gnutls-2.1 2.18-1.2-win32ws\bin\libgcrypt-11.lib C:\Wireshark-win32-libs-1.10\gnutls-2.12. 18-1.2-win32ws\bin\libgnutls-26.lib C:\Wireshark-win32-libs-1.10\lua5.1.4\lua5. 1.lib C:\Wireshark-win32-libs-1.10\libsmi-svn-40773-win32ws\lib\libsmi-2.lib C:\Wireshark-win32-libs-1.10\GeoIP-1.4.8-2-win32ws\lib\libGeoIP-1.lib ..\wsuti l\libwsutil.lib ..\wiretap\wiretap-1.10.0.lib crypt\airpdcap.lib ftypes\ftype s.lib dfilter\dfilter.lib wmem\wmem.lib wslua\wslua.lib wspython\wspython.li b dissectors\dissectors.lib ..\image\libwireshark.res dissectors\register.obj asm_utils_win32_x86.obj</p></div><div id="comment-27187-info" class="comment-info"><span class="comment-age">(20 Nov '13, 18:28)</span> <span class="comment-user userinfo">metamatrix</span></div></div></div><div id="comment-tools-27139" class="comment-tools"></div><div class="clear"></div><div id="comment-27139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27188"></span>

<div id="answer-container-27188" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27188-score" class="post-score" title="current number of votes">0</div><span id="post-27188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="metamatrix has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I solved the problem :-）</p><p>Edit makefile.nmake in epan directory. Add path of libcstl.lib to libwireshark_LIBS.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '13, 19:11</strong></p><img src="https://secure.gravatar.com/avatar/13679628c84abac93be65773340d2589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metamatrix&#39;s gravatar image" /><p><span>metamatrix</span><br />
<span class="score" title="56 reputation points">56</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metamatrix has one accepted answer">100%</span></p></div></div><div id="comments-container-27188" class="comments-container"></div><div id="comment-tools-27188" class="comment-tools"></div><div class="clear"></div><div id="comment-27188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

