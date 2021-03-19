+++
type = "question"
title = "Unresolved externals LNK2001"
description = '''When I run nmake -g makefile.nmake all. this is what error I get in the end. Linking libwsutil.dll  link /INCREMENTAL:NO /NOLOGO -entry:_DllMainCRTStartup@12 -dll kernel32.lib ws2_32.lib mswsock.lib advapi32.lib shell32.lib /DEBUG /MACHINE:x86 /DYNAMICBASE /FIXED:no /OUT:libwsutil.dll /IMPLIB:libwsu...'''
date = "2014-06-04T12:15:00Z"
lastmod = "2014-06-04T14:25:00Z"
weight = 33402
keywords = [ "linker", "wireshark" ]
aliases = [ "/questions/33402" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unresolved externals LNK2001](/questions/33402/unresolved-externals-lnk2001)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33402-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33402-score" class="post-score" title="current number of votes">0</div><span id="post-33402-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I run nmake -g makefile.nmake all. this is what error I get in the end.</p><pre><code>Linking libwsutil.dll
        link  /INCREMENTAL:NO /NOLOGO -entry:[email protected] -dll kernel32.lib  ws2_32.lib mswsock.lib advapi32.lib shell32.lib  /DEBUG /MACHINE:x86 /DYNAMICBASE /FIXED:no   /OUT:libwsutil.dll  /IMPLIB:libwsutil.lib  ..\image\libwsutil.res  file_util.obj             inet_aton.obj           inet_ntop.obj    inet_pton.obj           adler32.obj     aes.obj                 airpdcap_wep.obj        base64.obj      bitswap.obj     crash_info.obj  crc6.obj     crc7.obj                crc8.obj                crc10.obj               crc11.obj               crc16.obj               crc16-plain.obj         crc32.obj           crcdrm.obj      des.obj                 eax.obj                 filesystem.obj  g711.obj                md4.obj                 md5.obj    mpeg-audio.obj  nstime.obj      plugins.obj     privileges.obj  sha1.obj  strnatcmp.obj   str_util.obj    rc4.obj                 report_err.obj  tempfile.obj    time_util.obj   type_util.obj   u3.obj          unicode-utils.obj  strptime.obj                 wsgetopt.obj C:\Wireshark-win64-libs\gtk2\lib\lib-2.0.lib  C:\Wireshark-win64-libs\gtk2\lib\gmodule-2.0.lib  C:\Wireshark-win64-libs\gtk2\lib\gobject-2.0.lib   C:\Wireshark-win64-libs\gnutls-2.12.18-1.2-win64ws\bin\libtasn1-3.lib  C:\Wireshark-win64-libs\gnutls-2.12.18-1.2-win64ws\bin\libgpg-error-0.lib       C:\Wireshark-win64-libs\gnutls-2.12.18-1.2-win64ws\bin\libgcrypt-11.lib  C:\Wireshark-win64-libs\gnutls-2.12.18-1.2-win64ws\bin\libgnutls-26.lib  nghttp2/nghttp2_buf.obj       nghttp2/nghttp2_hd.obj  nghttp2/nghttp2_hd_huffman.obj  nghttp2/nghttp2_hd_huffman_data.obj     nghttp2/nghttp2_helper.obj
   Creating library libwsutil.lib and object libwsutil.exp
file_util.obj : error LNK2019: unresolved external symbol _g_path_is_absolute referenced in function _ws_stdio_stat64
file_util.obj : error LNK2019: unresolved external symbol _g_path_skip_root referenced in function _ws_stdio_stat64
file_util.obj : error LNK2019: unresolved external symbol _g_path_get_dirname referenced in function _init_dll_load_paths
filesystem.obj : error LNK2001: unresolved external symbol _g_path_get_dirname
tempfile.obj : error LNK2001: unresolved external symbol _g_free
u3.obj : error LNK2019: unresolved external symbol _g_free referenced in function _u3_contract_device_path
unicode-utils.obj : error LNK2001: unresolved external symbol _g_free
file_util.obj : error LNK2001: unresolved external symbol _g_free
eax.obj : error LNK2001: unresolved external symbol _g_free
filesystem.obj : error LNK2001: unresolved external symbol _g_free
plugins.obj : error LNK2001: unresolved external symbol _g_free
file_util.obj : error LNK2019: unresolved external symbol _g_malloc0_n referenced in function _create_app_running_mutex
file_util.obj : error LNK2019: unresolved external symbol _g_utf8_to_utf16 referenced in function _ws_stdio_open
file_util.obj : error LNK2019: unresolved external symbol _g_utf16_to_utf8 referenced in function _getenv_utf8
filesystem.obj : error LNK2001: unresolved external symbol _g_utf16_to_utf8
unicode-utils.obj : error LNK2001: unresolved external symbol _g_utf16_to_utf8
file_util.obj : error LNK2019: unresolved external symbol _g_module_build_path referenced in function _ws_load_library
file_util.obj : error LNK2019: unresolved external symbol _g_module_open_utf8 referenced in function _ws_module_open
plugins.obj : error LNK2001: unresolved external symbol _g_module_open_utf8
u3.obj : error LNK2019: unresolved external symbol _g_snprintf referenced in function _u3_runtime_info
inet_ntop.obj : error LNK2001: unresolved external symbol _g_snprintf
filesystem.obj : error LNK2001: unresolved external symbol _g_snprintf
plugins.obj : error LNK2001: unresolved external symbol _g_snprintf
tempfile.obj : error LNK2001: unresolved external symbol _g_snprintf
inet_ntop.obj : error LNK2019: unresolved external symbol _g_strlcpy referenced in function _inet_ntop4
tempfile.obj : error LNK2001: unresolved external symbol _g_strlcpy
eax.obj : error LNK2019: unresolved external symbol _gcry_cipher_open referenced in function _CTR
eax.obj : error LNK2019: unresolved external symbol _gcry_cipher_close referenced in function _CTR
eax.obj : error LNK2019: unresolved external symbol _gcry_cipher_encrypt referenced in function _CTR
eax.obj : error LNK2019: unresolved external symbol _gcry_cipher_setkey referenced in function _CTR
eax.obj : error LNK2019: unresolved external symbol _gcry_cipher_setiv referenced in function _dCMAC
eax.obj : error LNK2019: unresolved external symbol _gcry_cipher_setctr referenced in function _CTR
u3.obj : error LNK2019: unresolved external symbol _g_malloc referenced in function _u3_runtime_info
unicode-utils.obj : error LNK2001: unresolved external symbol _g_malloc
eax.obj : error LNK2001: unresolved external symbol _g_malloc
filesystem.obj : error LNK2001: unresolved external symbol _g_malloc
plugins.obj : error LNK2001: unresolved external symbol _g_malloc
tempfile.obj : error LNK2001: unresolved external symbol _g_malloc
filesystem.obj : error LNK2019: unresolved external symbol _g_dir_close referenced in function _has_global_profiles
plugins.obj : error LNK2001: unresolved external symbol _g_dir_close
filesystem.obj : error LNK2019: unresolved external symbol _g_dir_open_utf8 referenced in function _has_global_profiles
plugins.obj : error LNK2001: unresolved external symbol _g_dir_open_utf8
filesystem.obj : error LNK2019: unresolved external symbol _g_dir_read_name_utf referenced in function _has_global_profiles
plugins.obj : error LNK2001: unresolved external symbol _g_dir_read_name_utf8
filesystem.obj : error LNK2019: unresolved external symbol _g_list_free referenced in function _copy_persconffile_profile
filesystem.obj : error LNK2019: unresolved external symbol _g_list_first referenced in function _copy_persconffile_profile
filesystem.obj : error LNK2019: unresolved external symbol _g_hash_table_new referenced in function _profile_store_persconffiles
filesystem.obj : error LNK2019: unresolved external symbol _g_hash_table_insert referenced in function _get_persconffile_path
filesystem.obj : error LNK2019: unresolved external symbol _g_hash_table_lookup referenced in function _get_persconffile_path
filesystem.obj : error LNK2019: unresolved external symbol _g_hash_table_get_keys referenced in function _copy_persconffile_profile
filesystem.obj : error LNK2019: unresolved external symbol _g_str_equal referenced in function _profile_store_persconffiles
filesystem.obj : error LNK2019: unresolved external symbol _g_str_hash referenced in function _profile_store_persconffiles
filesystem.obj : error LNK2019: unresolved external symbol _g_strerror referenced in function _file_open_error_message
filesystem.obj : error LNK2019: unresolved external symbol _g_strdup referenced in function _set_profile_name
plugins.obj : error LNK2001: unresolved external symbol _g_strdup
privileges.obj : error LNK2001: unresolved external symbol _g_strdup
tempfile.obj : error LNK2001: unresolved external symbol _g_strdup
filesystem.obj : error LNK2019: unresolved external symbol _g_strdup_printf referenced in function _init_progfile_dir
plugins.obj : error LNK2001: unresolved external symbol _g_strdup_printf
tempfile.obj : error LNK2001: unresolved external symbol _g_strdup_printf
filesystem.obj : error LNK2019: unresolved external symbol _g_assertion_message_expr referenced in function _get_basename
str_util.obj : error LNK2001: unresolved external symbol _g_assertion_message_expr
plugins.obj : error LNK2019: unresolved external symbol _g_slist_append referenced in function _add_plugin_type
plugins.obj : error LNK2019: unresolved external symbol _g_slist_foreach referenced in function _plugins_get_descriptions
plugins.obj : error LNK2019: unresolved external symbol _g_string_new referenced in function _plugins_get_descriptions
str_util.obj : error LNK2001: unresolved external symbol _g_string_new
plugins.obj : error LNK2019: unresolved external symbol _g_string_free referenced in function _plugins_get_descriptions
str_util.obj : error LNK2001: unresolved external symbol _g_string_free
plugins.obj : error LNK2019: unresolved external symbol _g_string_append_printf referenced in function _add_plugin_type_description
plugins.obj : error LNK2019: unresolved external symbol _g_module_close referenced in function _plugins_scan_dir
plugins.obj : error LNK2019: unresolved external symbol _g_module_error referenced in function _plugins_scan_dir
plugins.obj : error LNK2019: unresolved external symbol _g_module_symbol referenced in function _plugins_scan_dir
plugins.obj : error LNK2019: unresolved external symbol _g_module_name_utf8 referenced in function _plugins_get_descriptions
str_util.obj : error LNK2019: unresolved external symbol _g_string_append referenced in function _format_size
u3.obj : error LNK2001: unresolved external symbol _g_string_append
str_util.obj : error LNK2019: unresolved external symbol _g_string_printf referenced in function _format_size
str_util.obj : error LNK2001: unresolved external symbol __imp__g_ascii_table
tempfile.obj : error LNK2019: unresolved external symbol _g_realloc referenced in function _create_tempfile
unicode-utils.obj : error LNK2001: unresolved external symbol _g_realloc
tempfile.obj : error LNK2019: unresolved external symbol _g_get_tmp_dir referened in function _get_tempfile_path
tempfile.obj : error LNK2019: unresolved external symbol _g_strdelimit referenced in function _create_tempfile
tempfile.obj : error LNK2019: unresolved external symbol _g_strconcat referenced in function _create_tempfile
u3.obj : error LNK2001: unresolved external symbol _g_strconcat
unicode-utils.obj : error LNK2019: unresolved external symbol _g_strdup_vprintf referenced in function _utf_8to16_snprintf

libwsutil.dll : fatal error LNK1120: 50 unresolved externals
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.
\VC\BIN\link.EXE&quot;&#39; : return code &#39;0x460&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files (x86)\Microsoft Visual Studio 12.
\VC\BIN\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre><p>How to solve this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-linker" rel="tag" title="see questions tagged &#39;linker&#39;">linker</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '14, 12:15</strong></p><img src="https://secure.gravatar.com/avatar/a9a254ac482208f766093c0f9c144364?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aman&#39;s gravatar image" /><p><span>aman</span><br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aman has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jun '14, 14:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33402" class="comments-container"></div><div id="comment-tools-33402" class="comment-tools"></div><div class="clear"></div><div id="comment-33402-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33408"></span>

<div id="answer-container-33408" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33408-score" class="post-score" title="current number of votes">0</div><span id="post-33408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please use the "Code" formatting button to correctly format code or terminal output so it can be easily viewed. In addition, when cutting code from the terminal please ensure you cut the whole of the text, your post above was missing a character either at the start, or more likely the end of the line. I've fixed that where I can.</p><p>You build environment seems to be messed up. You are performing a 32 bit link <code>/MACHINE:x86</code> but appear to be attempting to link to 64 bit libraries, e.g. <code>C:\Wireshark-win64-libs\gtk2\lib\lib-2.0.lib</code>, unless your'e confusing us all by having the 32 bit libraries in a path with win64 in the name.</p><p>The link errors indicate that the linker could't find the referenced functions in the supplied list of libraries. Maybe this is because the link is 32 bit and the libraries are 64 bit.</p><p>As suggested elsewhere in one of your other questions about build issues, I strongly suggest that you concentrate on building a 32 bit version first, and then move on to a 64 bit version if you really need to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '14, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33408" class="comments-container"></div><div id="comment-tools-33408" class="comment-tools"></div><div class="clear"></div><div id="comment-33408-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

