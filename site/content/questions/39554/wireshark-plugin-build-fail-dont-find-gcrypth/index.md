+++
type = "question"
title = "Wireshark plugin build fail (don&#x27;t find gcrypt.h)"
description = '''Hello, I recently pulled last Wireshark update from git repo and merged with my branch. After resovling some conflict I had, I realized there was some changes in plugin dir so I added CMakelists.txt en modified my Makefile.nmake/plugin.rc.in/Makefile.common/Makefile.am file in my plugin dir.  But no...'''
date = "2015-02-02T07:18:00Z"
lastmod = "2015-02-03T02:15:00Z"
weight = 39554
keywords = [ "fail", "plugin", "build", "gcrypt.h", "wireshark" ]
aliases = [ "/questions/39554" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark plugin build fail (don't find gcrypt.h)](/questions/39554/wireshark-plugin-build-fail-dont-find-gcrypth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39554-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I recently pulled last Wireshark update from git repo and merged with my branch. After resovling some conflict I had, I realized there was some changes in plugin dir so I added CMakelists.txt en modified my Makefile.nmake/plugin.rc.in/Makefile.common/Makefile.am file in my plugin dir.</p><p>But now I'm having an issue with the gcrypt.h, "wireshark\wsutil/wsgcrypt.h(36) : fatal error C1083: Cannot open include file 'gcrypt.h' : No such file or directory"</p><p>I tried to link the lib by adding ....\wsutil\libwsutil.lib without any good result.</p><p>When I try to add GCRYPT_LIBS or GNUTLS_DIR I got command line warnings and unresolved external symbol error.</p><p>Does something else has changed ? Or maybe I'm doing something wrong ?</p></div><div id="question-tags" class="tags-container tags">fail plugin build gcrypt.h wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '15, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p>Afrim<br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-39554" class="comments-container"><span id="39555"></span><div id="comment-39555" class="comment"><div id="post-39555-score" class="comment-score"></div><div class="comment-text"><p>What is your OS and how are you configuring and running the build, i.e. autotools\Make or CMake?</p></div><div id="comment-39555-info" class="comment-info"><span class="comment-age">(02 Feb '15, 07:24)</span> grahamb ♦</div></div><span id="39558"></span><div id="comment-39558" class="comment"><div id="post-39558-score" class="comment-score"></div><div class="comment-text"><p>Well I'm using running nmake (so OS is windows), don't know if that's what you asked for</p></div><div id="comment-39558-info" class="comment-info"><span class="comment-age">(02 Feb '15, 07:44)</span> Afrim</div></div><span id="39559"></span><div id="comment-39559" class="comment"><div id="post-39559-score" class="comment-score"></div><div class="comment-text"><p>Can you build the sources without your changes? This is to determine if the error is in your environment, or your changes.</p><p>The reported error is in a core library (wsutil), so it looks like an environment issue.</p></div><div id="comment-39559-info" class="comment-info"><span class="comment-age">(02 Feb '15, 08:02)</span> grahamb ♦</div></div><span id="39560"></span><div id="comment-39560" class="comment"><div id="post-39560-score" class="comment-score"></div><div class="comment-text"><p>You mean without my plugin ? Or without all things i've tried to resolve my problem (in Makefile.nmake) ?</p></div><div id="comment-39560-info" class="comment-info"><span class="comment-age">(02 Feb '15, 08:07)</span> Afrim</div></div><span id="39565"></span><div id="comment-39565" class="comment"><div id="post-39565-score" class="comment-score"></div><div class="comment-text"><p>Assuming you have copies of all your changes, revert everything back to plain unmodified sources, then <code>nmake -f Makefile.nmake distclean</code> and then build again.</p></div><div id="comment-39565-info" class="comment-info"><span class="comment-age">(02 Feb '15, 08:29)</span> grahamb ♦</div></div><span id="39591"></span><div id="comment-39591" class="comment not_top_scorer"><div id="post-39591-score" class="comment-score"></div><div class="comment-text"><p>The build is successfull without any changes. It's weird because before the merge all was OK in my build even with my plugin</p></div><div id="comment-39591-info" class="comment-info"><span class="comment-age">(03 Feb '15, 01:03)</span> Afrim</div></div></div><div id="comment-tools-39554" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-39554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39593"></span>

<div id="answer-container-39593" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39593-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just because something merges doesn't mean it will build.</p><p>Without changing anything else, merge your changes, cd into your plugins directory and <code>nmake -f Makefile.nmake &gt; tmp.txt</code> there. Post the output of tmp.txt back here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '15, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39593" class="comments-container"><span id="39598"></span><div id="comment-39598" class="comment"><div id="post-39598-score" class="comment-score"></div><div class="comment-text"><pre><code>    &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /                   -f Makefile.nmake PLUGIN_TARGET= process-plugins
    cd docsis
    &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /                   -f Makefile.nmake 
Making plugin.c
Updating plugin.c
    sed -e s/@[email protected]/docsis/  -e s/@[email protected]/0,0,5,0/  -e s/@[email protected]/1,99,2,0/  -e s/@[email protected]/0.0.5.0/  -e s/@[email protected]/docsis/  -e s/@[email protected]/1.99.2/  -e s/@[email protected]/MSVC2010/  &lt; plugin.rc.in &gt; docsis.rc
    rc  /r docsis.rc
Microsoft (R) Windows (R) Resource Compiler Version 6.1.7600.16385

Copyright (C) Microsoft Corporation.  All rights reserved.

    cl -WX /DWINPCAP_VERSION=4_1_3 /Zi /WX /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /w34295 /w34189  /I../.. /IC:\Wireshark-win32-libs\gtk2\include\glib-2.0  /IC:\Wireshark-win32-libs\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES  /IC:\Wireshark-win32-libs\WPdpack\include -Fd.\ -c packet-bintrngreq.c packet-bpkmattr.c packet-bpkmreq.c packet-bpkmrsp.c packet-cmctrlreq.c packet-cmctrlrsp.c packet-cmstatus.c packet-intrngreq.c packet-dbcreq.c packet-dbcrsp.c packet-dbcack.c packet-dccack.c packet-dccreq.c packet-dccrsp.c packet-dcd.c packet-dpvreq.c packet-dpvrsp.c packet-docsis.c packet-dsaack.c packet-dsareq.c packet-dsarsp.c packet-dscack.c packet-dscreq.c packet-dscrsp.c packet-dsdreq.c packet-dsdrsp.c packet-macmgmt.c packet-map.c packet-mdd.c packet-regack.c packet-regreq.c packet-regreqmp.c packet-regrsp.c packet-regrspmp.c packet-rngreq.c packet-rngrsp.c packet-sync.c packet-tlv.c packet-tlv-cmctrl.c packet-type29ucd.c packet-uccreq.c packet-uccrsp.c packet-ucd.c packet-vendor.c plugin.c 
packet-bintrngreq.c
packet-bpkmattr.c
packet-bpkmreq.c
packet-bpkmrsp.c
packet-cmctrlreq.c
packet-cmctrlrsp.c
packet-cmstatus.c
packet-intrngreq.c
packet-dbcreq.c
packet-dbcrsp.c
packet-dbcack.c
packet-dccack.c
packet-dccreq.c
packet-dccrsp.c
packet-dcd.c
packet-dpvreq.c
packet-dpvrsp.c
packet-docsis.c
packet-dsaack.c
packet-dsareq.c
packet-dsarsp.c
packet-dscack.c
packet-dscreq.c
packet-dscrsp.c
packet-dsdreq.c
packet-dsdrsp.c
packet-macmgmt.c
packet-map.c
packet-mdd.c
packet-regack.c
packet-regreq.c
packet-regreqmp.c
packet-regrsp.c
packet-regrspmp.c
packet-rngreq.c
packet-rngrsp.c
packet-sync.c
packet-tlv.c
packet-tlv-cmctrl.c
packet-type29ucd.c
packet-uccreq.c
packet-uccrsp.c
packet-ucd.c
packet-vendor.c
plugin.c
    link -dll /out:docsis.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x86 /RELEASE /SafeSEH /DYNAMICBASE /FIXED:no      packet-bintrngreq.obj  packet-bpkmattr.obj  packet-bpkmreq.obj  packet-bpkmrsp.obj  packet-cmctrlreq.obj  packet-cmctrlrsp.obj  packet-cmstatus.obj  packet-intrngreq.obj  packet-dbcreq.obj  packet-dbcrsp.obj  packet-dbcack.obj  packet-dccack.obj  packet-dccreq.obj  packet-dccrsp.obj  packet-dcd.obj  packet-dpvreq.obj  packet-dpvrsp.obj  packet-docsis.obj  packet-dsaack.obj  packet-dsareq.obj  packet-dsarsp.obj  packet-dscack.obj  packet-dscreq.obj  packet-dscrsp.obj  packet-dsdreq.obj  packet-dsdrsp.obj  packet-macmgmt.obj  packet-map.obj  packet-mdd.obj  packet-regack.obj  packet-regreq.obj  packet-regreqmp.obj  packet-regrsp.obj  packet-regrspmp.obj  packet-rngreq.obj  packet-rngrsp.obj  packet-sync.obj  packet-tlv.obj  packet-tlv-cmctrl.obj  packet-type29ucd.obj  packet-uccreq.obj  packet-uccrsp.obj  packet-ucd.obj  packet-vendor.obj      plugin.obj ..\..\epan\libwireshark.lib  C:\Wireshark-win32-libs\gtk2\lib\glib-2.0.lib  C:\Wireshark-win32-libs\gtk2\lib\gmodule-2.0.lib  C:\Wireshark-win32-libs\gtk2\lib\gobject-2.0.lib docsis.res
   Creating library docsis.lib and object docsis.exp
    cd ..
    cd ethercat
    &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /                   -f Makefile.nmake 
Making plugin.c
Updating plugin.c
    sed -e s/@[email protected]/ethercat/  -e s/@[email protected]/0,1,0,0/  -e s/@[email protected]/1,99,2,0/  -e s/@[email protected]/0.1.0.0/  -e s/@[email protected]/ethercat/  -e s/@[email protected]/1.99.2/  -e s/@[email protected]/MSVC2010/  &lt; plugin.rc.in &gt; ethercat.rc
    rc  /r ethercat.rc
Microsoft (R) Windows (R) Resource Compiler Version 6.1.7600.16385

Copyright (C) Microsoft Corporation.  All rights reserved.

    cl -WX /DWINPCAP_VERSION=4_1_3 /Zi /WX /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /w34295 /w34189  /I../.. /IC:\Wireshark-win32-libs\gtk2\include\glib-2.0  /IC:\Wireshark-win32-libs\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES  /IC:\Wireshark-win32-libs\WPdpack\include -Fd.\ -c packet-ams.c packet-ecatmb.c packet-esl.c packet-ethercat-datagram.c packet-ethercat-frame.c packet-ioraw.c packet-nv.c plugin.c 
packet-ams.c
packet-ecatmb.c
packet-esl.c
packet-ethercat-datagram.c
packet-ethercat-frame.c
packet-ioraw.c
packet-nv.c
plugin.c
    link -dll /out:ethercat.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x86 /RELEASE /SafeSEH /DYNAMICBASE /FIXED:no      packet-ams.obj  packet-ecatmb.obj  packet-esl.obj  packet-ethercat-datagram.obj  packet-ethercat-frame.obj  packet-ioraw.obj  packet-nv.obj      plugin.obj ..\..\epan\libwireshark.lib ..\..\wsutil\libwsutil.lib  C:\Wireshark-win32-libs\gtk2\lib\glib-2.0.lib  C:\Wireshark-win32-libs\gtk2\lib\gmodule-2.0.lib  C:\Wireshark-win32-libs\gtk2\lib\gobject-2.0.lib ethercat.res
   Creating library ethercat.lib and object ethercat.exp
    cd ..
    cd gryphon
    &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /                   -f Makefile.nmake 
Making plugin.c
Updating plugin.c
    sed -e s/@[email protected]/gryphon/  -e s/@[email protected]/0,0,4,0/  -e s/@[email protected]/1,99,2,0/  -e s/@[email protected]/0.0.4.0/  -e s/@[email protected]/gryphon/  -e s/@[email protected]/1.99.2/  -e s/@[email protected]/MSVC2010/  &lt; plugin.rc.in &gt; gryphon.rc
    rc  /r gryphon.rc
Microsoft (R) Windows (R) Resource Compiler Version 6.1.7600.16385

Copyright (C) Microsoft Corporation.  All rights reserved.

    cl -WX /DWINPCAP_VERSION=4_1_3 /Zi /WX /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /w34295 /w34189  /I../.. /IC:\Wireshark-win32-libs\gtk2\include\glib-2.0  /IC:\Wireshark-win32-libs\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES  /IC:\Wireshark-win32-libs\WPdpack\include -Fd.\ -c packet-gryphon.c plugin.c 
plugin.c
packet-gryphon.c
    link -dll /out:gryphon.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x86 /RELEASE /SafeSEH /DYNAMICBASE /FIXED:no      packet-gryphon.obj      plugin.obj ..\..\epan\libwireshark.lib  C:\Wireshark-win32-libs\gtk2\lib\glib-2.0.lib  C:\Wireshark-win32-libs\gtk2\lib\gmodule-2.0.lib  C:\Wireshark-win32-libs\gtk2\lib\gobject-2.0.lib gryphon.res
   Creating library gryphon.lib and object gryphon.exp
    cd ..
    cd irda
    &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /                   -f Makefile.nmake 
Making plugin.c
Updating plugin.c
    sed -e s/@[email protected]/irda/  -e s/@[email protected]/0,0,6,0/  -e s/@[email protected]/1,99,2,0/  -e s/@[email protected]/0.0.6.0/  -e s/@[email protected]/irda/  -e s/@[email protected]/1.99.2/  -e s/@[email protected]/MSVC2010/  &lt; plugin.rc.in &gt; irda.rc
    rc  /r irda.rc
Microsoft (R) Windows (R) Resource Compiler Version 6.1.7600.16385

Copyright (C) Microsoft Corporation.  All rights reserved.

    cl -WX /DWINPCAP_VERSION=4_1_3 /Zi /WX /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /w34295 /w34189  /I../.. /IC:\Wireshark-win32-libs\gtk2\include\glib-2.0  /IC:\Wireshark-win32-libs\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES  /IC:\Wireshark-win32-libs\WPdpack\include -Fd.\ -c packet-ircomm.c packet-irda.c packet-sir.c plugin.c 
packet-ircomm.c
packet-irda.c
packet-sir.c
plugin.c
    link -dll /out:irda.dll /NOLOGO /INCREMENTAL:no /DEBUG /MACHINE:x86 /RELEASE /SafeSEH /DYNAMICBASE /FIXED:no      packet-ircomm.obj  packet-irda.obj  packet-sir.obj      plugin.obj ..\..\epan\libwireshark.lib  C:\Wireshark-win32-libs\gtk2\lib\glib-2.0.lib  C:\Wireshark-win32-libs\gtk2\lib\gmodule-2.0.lib  C:\Wireshark-win32-libs\gtk2\lib\gobject-2.0.lib irda.res
   Creating library irda.lib and object irda.exp
    cd ..
    cd myPLugin
    &quot;c:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\Bin\nmake.exe&quot; /                   -f Makefile.nmake</code></pre><p>Here is the output without any changes, the error says he don't know how to make '../../tools/make-dissector-reg', this is because my makefile.nmake (in my plugin) is old. In fact the directory of myPlugin is old (it's been awhile since I didn't merge with the official wireshark repo). So basically I took an exemple in another plugin to update my files. I got 5 plugin but 2 of these need encryption so I need to include wsutil/wsgcrypt.h, but it seems like my plugins didn't have access to Wireshark lib (The 3 other plugin are building correctly).</p></div><div id="comment-39598-info" class="comment-info"><span class="comment-age">(03 Feb '15, 03:08)</span> Afrim</div></div><span id="39603"></span><div id="comment-39603" class="comment"><div id="post-39603-score" class="comment-score"></div><div class="comment-text"><p>All that's normal output for building the standard plugins and doesn't give us any clue what's up with your plugin.</p><p>Yes, the plugins build has undergone some changes, you'll have to adapt the standard plugin build files to compile your plugin and probably modify your plugin as well if the interfaces it uses to Wireshark have changed.</p><p>Can you try again, this time <code>cd</code> into your actual plugin directory <code>nmake .. clean</code> and then nmake again, posting the output.</p></div><div id="comment-39603-info" class="comment-info"><span class="comment-age">(03 Feb '15, 04:35)</span> grahamb ♦</div></div><span id="39604"></span><div id="comment-39604" class="comment"><div id="post-39604-score" class="comment-score"></div><div class="comment-text"><p>The build doesn't even start and there is nothing in tmp.txt. It tells that he don't know how to make '../../tools/make-dissector-reg' but that's obvious because there is no more make-dissector-reg.</p><p>Now if make some changes on my plugin files (makefile.*, plugin.rc.in, etc) to fit with the "new way" i got this output.</p><p><code>     sed -e s/@[email protected]/myPlugin/  -e s/@[email protected]/0,0,1,0/  -e s/@[email protected]/1,99,2,0/  -e s/@[email protected]/0.0.1.0/  -e s/@[email protected]/myPlugin/  -e s/@[email protected]/1.99.2/  -e s/@[email protected]/MSVC2010/  &lt; plugin.rc.in &gt; myPlugin.rc     rc  /r myPlugin.rc Microsoft (R) Windows (R) Resource Compiler Version 6.1.7600.16385</code></p><p><code></code></p><p><code>Copyright (C) Microsoft Corporation.  All rights reserved.</code></p><code></code><pre><code>cl -WX /DWINPCAP_VERSION=4_1_3 /Zi /WX /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /w34295 /w34189  /I../.. /IC:\Wireshark-win32-libs\gtk2\include\glib-2.0  /IC:\Wireshark-win32-libs\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES  /IC:\Wireshark-win32-libs\WPdpack\include -Fd.\ -c packet-myPlugin.c plugin.c</code></pre></code><p><code>packet-myPlugin.c plugin.c C:\WiresharkLastVersion\wsutil/wsgcrypt.h(36) : fatal error C1083: Cannot open include file: 'gcrypt.h': No such file or directory</code></p></div><div id="comment-39604-info" class="comment-info"><span class="comment-age">(03 Feb '15, 05:10)</span> Afrim</div></div><span id="39606"></span><div id="comment-39606" class="comment"><div id="post-39606-score" class="comment-score">1</div><div class="comment-text"><p>OK, so it appears that your plugin includes wsgcrypt.h, possibly via other includes, and that file includes the third party gcrypt.h.</p><p>To allow the compiler to find that include you will need to modify <code>CFLAGS</code> in your plugins Makefile.nmake to include <code>$(GNUTLS_FLAGS)</code> and to link with the libraries modify <code>LINK_PLUGIN_WITH</code> to include <code>..\..\wsutil\libwsutil.lib</code> and possibly <code>$(GNUTLS_LIBS)</code> as well.</p></div><div id="comment-39606-info" class="comment-info"><span class="comment-age">(03 Feb '15, 05:40)</span> grahamb ♦</div></div><span id="39607"></span><div id="comment-39607" class="comment"><div id="post-39607-score" class="comment-score"></div><div class="comment-text"><p>I already did the 2 first steps and it tells me some unresolved external symbol. I'll try with also the <code>$(GNUTLS_LIBS)</code> in <code>LINK_PLUGIN_WITH </code>.</p><p>EDIT : in my plugin dir i added <code>$(GNUTLS_FLAGS)</code> to <code>CFLAGS</code> so i got <code> CFLAGS=$(WARNINGS_ARE_ERRORS) $(STANDARD_CFLAGS) \     /I../.. $(GLIB_CFLAGS) $(GNUTLS_FLAGS)\     /I$(PCAP_DIR)\include</code> then i added ....\wsutil\libwsutil.lib and <code>$(GNUTLS_LIBS)</code> to <code>LINK_PLUGIN_WITH</code></p><p>then I ran <code>nmake....clean</code> and nmake and I got this output : <code> cl -WX /DWINPCAP_VERSION=4_1_3 /Zi /WX /MD /O2 /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1600  /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO_DEPRECATE -DPSAPI_VERSION=1 /D_BIND_TO_CURRENT_CRT_VERSION=1 /MP /w34295 /w34189  /I../.. /IC:\Wireshark-win32-libs\gtk2\include\glib-2.0  /IC:\Wireshark-win32-libs\gtk2\lib\glib-2.0\include  -DG_DISABLE_DEPRECATED  -DG_DISABLE_SINGLE_INCLUDES  /IC:\Wireshark-win32-libs\WPdpack\include -Fd.\ -c packet-myPlugin.c  packet-myPlugin.c C:\WiresharkLastVersion\wsutil/wsgcrypt.h(36) : fatal error C1083: Cannot open include file: 'gcrypt.h': No such file or directory</code></p><p>In my opinion there is something wrong because I should see something like <code>C:\Wireshark-win32-libs\gnutls-3.2.15-2.7-win32ws\include</code></p></div><div id="comment-39607-info" class="comment-info"><span class="comment-age">(03 Feb '15, 05:52)</span> Afrim</div></div><span id="39608"></span><div id="comment-39608" class="comment not_top_scorer"><div id="post-39608-score" class="comment-score"></div><div class="comment-text"><p>Ok I resolved my problem It's <code>$(GNUTLS_CFLAGS)</code> which was what I did but I also need <code>$(GNUTLS_LIBS)</code> in <code>LINK_PLUGIN_WITH</code> to avoid unresolved external symbol error.</p><p>Thank you grahamb :)</p></div><div id="comment-39608-info" class="comment-info"><span class="comment-age">(03 Feb '15, 06:16)</span> Afrim</div></div><span id="39609"></span><div id="comment-39609" class="comment not_top_scorer"><div id="post-39609-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the typo, got there in the end though.</p><p>FWIW, I just looked at what the makefile in epan did for including the GNUTLS stuff.</p></div><div id="comment-39609-info" class="comment-info"><span class="comment-age">(03 Feb '15, 06:34)</span> grahamb ♦</div></div></div><div id="comment-tools-39593" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-39593-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

