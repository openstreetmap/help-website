+++
type = "question"
title = "Linker Error after removing a file"
description = '''I had added a new file in dissector folder. The file had two functions for registering few dissectors - proto_register_bacnetSBT and proto_reg_handoff_bacnetSBT. I add reference of this file in following to compile C:wiresharkepanCMakeLists.txt C:wiresharkepandissectorsMakefile.common Now I have rem...'''
date = "2011-04-20T09:07:00Z"
lastmod = "2011-04-20T09:12:00Z"
weight = 3633
keywords = [ "link", "libwireshark.lib", "for", "error" ]
aliases = [ "/questions/3633" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Linker Error after removing a file](/questions/3633/linker-error-after-removing-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3633-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I had added a new file in dissector folder. The file had two functions for registering few dissectors - proto_register_bacnetSBT and proto_reg_handoff_bacnetSBT.</p><p>I add reference of this file in following to compile</p><p>C:wiresharkepanCMakeLists.txt C:wiresharkepandissectorsMakefile.common</p><p>Now I have removed this file and its references from above 2 files. but i am still getting linker errors. I am using Visual C++ 2008 Express. I clean solution before compiling. I also tried distclean and compiling using command propmpt. (nmake -f Makefile.nmake disclean and all)</p><p>Creating library libwireshark.lib and object libwireshark.exp register.obj : error LNK2019: unresolved external symbol _proto_register_bacnetS BT referenced in function _register_all_protocols register.obj : error LNK2019: unresolved external symbol _proto_reg_handoff_bacn etSBT referenced in function _register_all_protocol_handoffs libwireshark.dll : fatal error LNK1120: 2 unresolved externals NMAKE : fatal error U1077: '"C:Program FilesMicrosoft Visual Studio 9.0VCBIN link.EXE"' : return code '0x460' Stop. NMAKE : fatal error U1077: '"C:Program FilesMicrosoft Visual Studio 9.0VCBIN nmake.exe"' : return code '0x2' Stop.</p><p>Can you please tell me what do we need to do to remove these linker errors?</p></div><div id="question-tags" class="tags-container tags">link libwireshark.lib for error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '11, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p>dsprabhu4<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span></p></div></div><div id="comments-container-3633" class="comments-container"></div><div id="comment-tools-3633" class="comment-tools"></div><div class="clear"></div><div id="comment-3633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3634"></span>

<div id="answer-container-3634" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3634-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The references come from register.c, found in epan/.</p><p>This file should be regenerated when you make changes to Makefile.common. I'm not sure why that doesn't happen, but you could remove it, regenerate it or modify by hand.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 09:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3634" class="comments-container"><span id="3636"></span><div id="comment-3636" class="comment"><div id="post-3636-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Deleted those function manually from Register.c. I can continue my work now but question remains why didn't register.c get generated again? Did i not execute something for cleaning solution so that register.c got deleted and created again?</p></div><div id="comment-3636-info" class="comment-info"><span class="comment-age">(20 Apr '11, 09:39)</span> dsprabhu4</div></div><span id="3637"></span><div id="comment-3637" class="comment"><div id="post-3637-score" class="comment-score"></div><div class="comment-text"><p>Get error in 2008 VSEE 11&gt; perl ws-manifest.pl nsis/wireshark.nsi &gt; wireshark.manifest 11&gt;ERROR 11&gt;The following directories have no known location on a U3 device: 11&gt; $INSTDIR $INSTDIR${GTK_WIMP_DLLDST_DIR} $INSTDIR${GTK_WIMP_RCDST_DIR} $INSTDIRdiameter $INSTDIRdtds $INSTDIRetcgtk-2.0 $INSTDIRetcpango $INSTDIRhelp $INSTDIRlibgtk-2.0${GTK_LIB_DIR}engines $INSTDIRlibgtk-2.0modules $INSTDIRradius $INSTDIRsnmpmibs $INSTDIRtpncp $INSTDIRwimaxasncp $PROFILE '$INSTDIRplugins${VERSION}' 11&gt;NMAKE : fatal error U1077: 'perl' : return code '0xff' 11&gt;Stop</p><p>Any idea?</p></div><div id="comment-3637-info" class="comment-info"><span class="comment-age">(20 Apr '11, 09:45)</span> dsprabhu4</div></div><span id="3638"></span><div id="comment-3638" class="comment"><div id="post-3638-score" class="comment-score"></div><div class="comment-text"><p>register.c depends the files listed in ALL_DISSECTORS_SRC in epan/dissectors/Makefile.common but it doesn't depend on Makefile.common itself. I'll check in a change to fix that.</p></div><div id="comment-3638-info" class="comment-info"><span class="comment-age">(20 Apr '11, 10:06)</span> Gerald Combs ♦♦</div></div><span id="3639"></span><div id="comment-3639" class="comment"><div id="post-3639-score" class="comment-score"></div><div class="comment-text"><p>Any idea about perl error?? Is any library missing??</p></div><div id="comment-3639-info" class="comment-info"><span class="comment-age">(20 Apr '11, 10:25)</span> dsprabhu4</div></div></div><div id="comment-tools-3634" class="comment-tools"></div><div class="clear"></div><div id="comment-3634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

