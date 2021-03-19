+++
type = "question"
title = "LTE RRC dissector linker issue"
description = '''Hi I was trying to create a dll for my own dissector, compilation went through, in dll creation I am facing the issue as below. kindly provide views for the issue. Thanks in advance. link -dll /out:rrc-fsm.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x64 /DYNAMICBASE /FIXED:no packet-lte-rrc-fsm.obj ...'''
date = "2015-12-01T11:10:00Z"
lastmod = "2015-12-02T14:26:00Z"
weight = 48152
keywords = [ "lterrc", "dissector", "link" ]
aliases = [ "/questions/48152" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [LTE RRC dissector linker issue](/questions/48152/lte-rrc-dissector-linker-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48152-score" class="post-score" title="current number of votes">0</div><span id="post-48152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I was trying to create a dll for my own dissector, compilation went through, in dll creation I am facing the issue as below. kindly provide views for the issue. Thanks in advance.</p><pre><code>link -dll /out:rrc-fsm.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x64 /DYNAMICBASE /FIXED:no  packet-lte-rrc-fsm.obj  plugin.obj ..\..\libwireshark.lib ..\dissectors.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\glib-2.0.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\gmodule-2.0.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\gobject-2.0.lib rrc-fsm.res
dissectors.lib(packet-gsm_a_common.obj) : error LNK2005: de_ms_cm_2 already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-gsm_a_common.obj) : error LNK2005: de_ms_cm_3 already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-gsm_a_gm.obj) : error LNK2005: de_gmm_ms_radio_acc_cap already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_null already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_constrained_sequence_of already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_boolean already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_constrained_integer already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_enumerated already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_choice already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_sequence already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_sequence_eag already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_bit_string already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_octet_string already defined in libwireshark.lib(libwireshark.dll)
dissectors.lib(packet-per.obj) : error LNK2005: dissect_per_octet_string_containing_pdu_new already defined in libwireshark.lib(libwireshark.dll)
   Creating library rrc-fsm.lib and object rrc-fsm.exp
dissectors.lib(packet-gsm_a_common.obj) : error LNK2001: unresolved external symbol tfs_supported_not_supported
dissectors.lib(packet-gsm_a_gm.obj) : error LNK2001: unresolved external symbol tfs_supported_not_supported
dissectors.lib(packet-bssgp.obj) : error LNK2001: unresolved external symbol tfs_supported_not_supported
dissectors.lib(packet-gsm_a_bssmap.obj) : error LNK2001: unresolved external symbol tfs_supported_not_supported
dissectors.lib(packet-nas_eps.obj) : error LNK2019: unresolved external symbol match_strval_idx_ext referenced in function get_nas_esm_msg_params
dissectors.lib(packet-bssgp.obj) : error LNK2001: unresolved external symbol match_strval_idx_ext
dissectors.lib(packet-sgsap.obj) : error LNK2001: unresolved external symbol match_strval_idx_ext
dissectors.lib(packet-gsm_a_bssmap.obj) : error LNK2001: unresolved external symbol match_strval_idx_ext
dissectors.lib(packet-gsm_a_gm.obj) : error LNK2001: unresolved external symbol tfs_present_not_present
dissectors.lib(packet-gsm_a_gm.obj) : error LNK2001: unresolved external symbol tfs_implemented_not_implemented
dissectors.lib(packet-gsm_a_gm.obj) : error LNK2001: unresolved external symbol ipproto_val_ext
dissectors.lib(packet-ip.obj) : error LNK2001: unresolved external symbol ipproto_val_ext
dissectors.lib(packet-gsm_a_dtap.obj) : error LNK2019: unresolved external symbol tvb_get_ephemeral_unicode_string referenced in function de_network_name
dissectors.lib(packet-per.obj) : error LNK2001: unresolved external symbol tvb_get_ephemeral_unicode_string
dissectors.lib(packet-gsm_sms.obj) : error LNK2001: unresolved external symbol tvb_get_ephemeral_unicode_string
dissectors.lib(packet-gsm_a_dtap.obj) : error LNK2019: unresolved external symbol IA5_7BIT_decode referenced in function de_sub_addr
dissectors.lib(packet-gmr1_rr.obj) : error LNK2019: unresolved external symbol proto_tree_add_split_bits_item_ret_val referenced in function gmr1_ie_rr_pkt_imm_ass_3_prm
dissectors.lib(packet-gsm_a_rr.obj) : error LNK2001: unresolved external symbol proto_tree_add_split_bits_item_ret_val
dissectors.lib(packet-bssgp.obj) : error LNK2001: unresolved external symbol tfs_reliable_not_reliable
dissectors.lib(packet-bssgp.obj) : error LNK2001: unresolved external symbol tfs_requested_not_requested
dissectors.lib(packet-gsm_bssmap_le.obj) : error LNK2001: unresolved external symbol tfs_requested_not_requested</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lterrc" rel="tag" title="see questions tagged &#39;lterrc&#39;">lterrc</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-link" rel="tag" title="see questions tagged &#39;link&#39;">link</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '15, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/aac777599ea2adb09230dc27672c4f6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viswanathan%20Jagadeesan&#39;s gravatar image" /><p><span>Viswanathan ...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viswanathan Jagadeesan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Dec '15, 13:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48152" class="comments-container"></div><div id="comment-tools-48152" class="comment-tools"></div><div class="clear"></div><div id="comment-48152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48155"></span>

<div id="answer-container-48155" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48155-score" class="post-score" title="current number of votes">0</div><span id="post-48155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should not link with both libwireshark.lib and dissectors.lib. Remove the latter and keep only libwireshark.lib.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '15, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-48155" class="comments-container"><span id="48156"></span><div id="comment-48156" class="comment"><div id="post-48156-score" class="comment-score"></div><div class="comment-text"><p>Thanks many for response, after removing dissector.lib output as</p><pre><code>link -dll /out:rrc-fsm.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x64 /DYNAMICBASE /FIXED:no  packet-lte-rrc-fsm.obj  plugin.obj ..\..\libwireshark.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\glib-2.0.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\gmodule-2.0.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\gobject-2.0.lib rrc-fsm.res
   Creating library rrc-fsm.lib and object rrc-fsm.exp
packet-lte-rrc-fsm.obj : error LNK2001: unresolved external symbol gsm_a_rr_rxlev_vals_ext
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol de_emm_sec_par_from_eutra referenced in function dissect_lte_rrc_T_nas_SecurityParamFromEUTRA
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol de_emm_sec_par_to_eutra referenced in function dissect_lte_rrc_T_nas_SecurityParamToEUTRA
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol dissect_lpp_Ellipsoid_Point_PDU referenced in function dissect_lte_rrc_T_ellipsoid_Point_r10
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol dissect_lpp_EllipsoidPointWithAltitude_PDU referenced in function dissect_lte_rrc_T_ellipsoidPointWithAltitude_r10
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol dissect_lpp_HorizontalVelocity_PDU referenced in function dissect_lte_rrc_T_horizontalVelocity_r10
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol dissect_rrc_InterRATHandoverInfo_PDU referenced in function dissect_lte_rrc_T_ueCapabilityRAT_Container
rrc-fsm.dll : fatal error LNK1120: 7 unresolved externals</code></pre><hr /><p>after removing libwireshark.lib output as</p><pre><code>link -dll /out:rrc-fsm.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x64 /DYNAMICBASE /FIXED:no  packet-lte-rrc-fsm.obj  plugin.obj ..\dissectors.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\glib-2.0.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\gmodule-2.0.lib  C:\wireshark-win64-libs-1.8\gtk2\lib\gobject-2.0.lib rrc-fsm.res
   Creating library rrc-fsm.lib and object rrc-fsm.exp
dissectors.lib(packet-q708.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-ranap.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-rtp.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-ipx.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-ip.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-gsm_sms.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-q931.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-ber.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-s1ap.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-e212.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-gsm_map.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-ppp.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-isup.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-bssgp.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-sgsap.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-gsm_a_rr.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-gsm_a_bssmap.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
packet-lte-rrc-fsm.obj : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-gsm_a_common.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-nas_eps.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-gsm_a_gm.obj) : error LNK2001: unresolved external symbol _match_strval_ext_init
dissectors.lib(packet-s1ap.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-tcap.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-frame.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-sccp.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-gsm_a_bssmap.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-gsm_map.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-isup.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-gsm_sms.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-gsm_bssmap_le.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-gsm_bsslap.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-gsm_a_rr.obj) : error LNK2001: unresolved external symbol col_append_str
dissectors.lib(packet-gsm_a_rp.obj) : error LNK2001: unresolved external symbol col_append_str</code></pre></div><div id="comment-48156-info" class="comment-info"><span class="comment-age">(01 Dec '15, 12:36)</span> <span class="comment-user userinfo">Viswanathan ...</span></div></div><span id="48157"></span><div id="comment-48157" class="comment"><div id="post-48157-score" class="comment-score"></div><div class="comment-text"><p>The function you are calling (gsm_a_rr_rxlev_vals_ext, ...) are not exported, so you cannot call them from your external dll. They should either be declared as WS_DLL_PUBLIC in Wireshark source code (not likely to happen) or you should redefine them locally. Looks like you copy pasted the lte-rrc dissector code in your DLL. This does not seem to make a lot of sense to me. Again you should not link against dissectors.lib.</p></div><div id="comment-48157-info" class="comment-info"><span class="comment-age">(01 Dec '15, 12:50)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="48163"></span><div id="comment-48163" class="comment"><div id="post-48163-score" class="comment-score"></div><div class="comment-text"><p>the compilation is fine as it went through, the issue is with linking, i.e it is not allowing to call any function from epan\dissectors.</p><pre><code>cl /DHAVE_WIN32_LIBWIRESHARK_LIB /D_NEED_VAR_IMPORT_ /WX /DHAVE_CONFIG_H /I../../.. /I../../../wiretap 
/IC:\wireshark-win64-libs-1.8\gtk2\include\glib-2.0  /IC:\wireshark-win64-libs-1.8\gtk2\lib\glib-2.0\include 
-DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES  
/IC:\wireshark-win64-libs-1.8\WPdpack\include -D_U_=&quot;&quot; /Zi /W3 /MD /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  
/D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE /MP /GS -Fd.\ -c packet-lte-rrc-fsm.c plugin.c packet-lte-rrc-fsm.c plugin.c
link -dll /out:rrc-fsm.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x64 /DYNAMICBASE /FIXED:no
packet-lte-rrc-fsm.obj  plugin.obj ..\..\libwireshark.lib 
C:\wireshark-win64-libs-1.8\gtk2\lib\glib-2.0.lib  
C:\wireshark-win64-libs-1.8\gtk2\lib\gmodule-2.0.lib  
C:\wireshark-win64-libs-1.8\gtk2\lib\gobject-2.0.lib rrc-fsm.res
   Creating library rrc-fsm.lib and object rrc-fsm.exp
packet-lte-rrc-fsm.obj : error LNK2001: unresolved external symbol gsm_a_rr_rxlev_vals_ext
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol de_emm_sec_par_from_eutra referenced in function dissect_lte_rrc_T_nas_SecurityParamFromEUTRA
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol de_emm_sec_par_to_eutra referenced in function dissect_lte_rrc_T_nas_SecurityParamToEUTRA
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol dissect_lpp_Ellipsoid_Point_PDU referenced in function dissect_lte_rrc_T_ellipsoid_Point_r10
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol dissect_lpp_EllipsoidPointWithAltitude_PDU referenced in function dissect_lte_rrc_T_ellipsoidPointWithAltitude_r10
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol dissect_lpp_HorizontalVelocity_PDU referenced in function dissect_lte_rrc_T_horizontalVelocity_r10
packet-lte-rrc-fsm.obj : error LNK2019: unresolved external symbol dissect_rrc_InterRATHandoverInfo_PDU referenced in function dissect_lte_rrc_T_ueCapabilityRAT_Container
rrc-fsm.dll : fatal error LNK1120: 7 unresolved externals</code></pre></div><div id="comment-48163-info" class="comment-info"><span class="comment-age">(01 Dec '15, 15:42)</span> <span class="comment-user userinfo">Viswanathan ...</span></div></div><span id="48164"></span><div id="comment-48164" class="comment"><div id="post-48164-score" class="comment-score"></div><div class="comment-text"><p>Note that <span></span><span>@Viswanathan</span> might be attempting to build an older version, maybe 1.8?</p><p>Can you clarify the source version you're working with?</p><p>The toolchain is VS2010.</p></div><div id="comment-48164-info" class="comment-info"><span class="comment-age">(01 Dec '15, 15:56)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48165"></span><div id="comment-48165" class="comment"><div id="post-48165-score" class="comment-score"></div><div class="comment-text"><p>I am using, 1.8.11</p></div><div id="comment-48165-info" class="comment-info"><span class="comment-age">(01 Dec '15, 16:02)</span> <span class="comment-user userinfo">Viswanathan ...</span></div></div><span id="48167"></span><div id="comment-48167" class="comment not_top_scorer"><div id="post-48167-score" class="comment-score"></div><div class="comment-text"><p>Juts a info :I could able to compile &amp; run the wireshark source code base 1.8.11 without any issue</p></div><div id="comment-48167-info" class="comment-info"><span class="comment-age">(01 Dec '15, 16:06)</span> <span class="comment-user userinfo">Viswanathan ...</span></div></div></div><div id="comment-tools-48155" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-48155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48169"></span>

<div id="answer-container-48169" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48169-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48169-score" class="post-score" title="current number of votes">0</div><span id="post-48169-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>the issue was resolved by - adding all export parameter libwireshark.def file &amp; re compile - modifying the Makefile.nmake for remove the library ..\dissectors.lib in LINK_PLUGIN_WITH macro</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '15, 17:41</strong></p><img src="https://secure.gravatar.com/avatar/aac777599ea2adb09230dc27672c4f6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Viswanathan%20Jagadeesan&#39;s gravatar image" /><p><span>Viswanathan ...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Viswanathan Jagadeesan has no accepted answers">0%</span></p></div></div><div id="comments-container-48169" class="comments-container"><span id="48216"></span><div id="comment-48216" class="comment"><div id="post-48216-score" class="comment-score"></div><div class="comment-text"><p>followup question, it does the creation of dissector dll for RRC successfully, when it loads on wireshark , it throws a error: "The procedure entry point dissect_lpp_Ellipsoid_Point_PDU could not be located in the dynamic link libwireshark.dll "</p><p>any suggestions.</p></div><div id="comment-48216-info" class="comment-info"><span class="comment-age">(02 Dec '15, 14:26)</span> <span class="comment-user userinfo">Viswanathan ...</span></div></div></div><div id="comment-tools-48169" class="comment-tools"></div><div class="clear"></div><div id="comment-48169-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

