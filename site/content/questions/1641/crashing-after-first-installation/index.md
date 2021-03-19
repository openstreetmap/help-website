+++
type = "question"
title = "Crashing after first installation"
description = '''X11 is booting fine. Wireshark is crashing: Here&#x27;s the bug report: Process: wireshark-bin [4578] Path: /Applications/VideoNet&amp;amp;Decorder/Wireshark.app/Contents/Resources/bin/wireshark-bin Identifier: wireshark-bin Version: ??? (???) Code Type: PPC (Native) Parent Process: Wireshark [4577]  Interva...'''
date = "2011-01-05T15:35:00Z"
lastmod = "2011-01-05T15:35:00Z"
weight = 1641
keywords = [ "boot-process", "crash" ]
aliases = [ "/questions/1641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Crashing after first installation](/questions/1641/crashing-after-first-installation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1641-score" class="post-score" title="current number of votes">0</div><span id="post-1641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>X11 is booting fine. Wireshark is crashing: Here's the bug report:</p><pre><code>Process:         wireshark-bin [4578]
Path:            /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/bin/wireshark-bin
Identifier:      wireshark-bin
Version:         ??? (???)
Code Type:       PPC (Native)
Parent Process:  Wireshark [4577]

Interval Since Last Report:          429 sec
Crashes Since Last Report:           2
Per-App Interval Since Last Report:  0 sec
Per-App Crashes Since Last Report:   2

Date/Time:       2011-01-06 00:24:32.262 +0100
OS Version:      Mac OS X 10.5.8 (9L31a)
Report Version:  6
Anonymous UUID:  B8D7FBF7-6F29-4E5F-8DAA-234200F58426

Exception Type:  EXC_CRASH (SIGABRT)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Crashed Thread:  0

Thread 0 Crashed:
0   libSystem.B.dylib               0x92aa3b50 __kill + 12
1   libSystem.B.dylib               0x92b3ebfc abort + 84
2   libglib-2.0.0.dylib             0x00eae0d0 g_assertion_message + 320
3   libglib-2.0.0.dylib             0x00eae5e8 g_assertion_message_expr + 88
4   wireshark-bin                   0x0008918c stock_icons_init + 124
5   wireshark-bin                   0x0004c020 main + 3504
6   wireshark-bin                   0x00002c50 start + 64

Thread 0 crashed with PPC Thread State 32:
  srr0: 0x92aa3b50  srr1: 0x0200f030   dar: 0x00eec30c dsisr: 0x40000000
    r0: 0x00000025    r1: 0xbfffec60    r2: 0x00000000    r3: 0x00000000
    r4: 0x00000000    r5: 0x00000001    r6: 0x00000004    r7: 0x084fe005
    r8: 0x0000082c    r9: 0x00431700   r10: 0x92a6ca10   r11: 0xa042952c
   r12: 0x92aa3b3c   r13: 0x00000000   r14: 0x00000000   r15: 0x00000000
   r16: 0x00000000   r17: 0x00000000   r18: 0x0015b280   r19: 0xbfffee6c
   r20: 0xbfffee4c   r21: 0x0623b000   r22: 0x0015b280   r23: 0x0014b280
   r24: 0x04a6eed4   r25: 0x0015b280   r26: 0x00137d6c   r27: 0x001381b4
   r28: 0x00137d6c   r29: 0x08440040   r30: 0x0843e220   r31: 0x92b3ebb4
    cr: 0x42002402   xer: 0x00000000    lr: 0x92b3ec00   ctr: 0x92aa3b3c
vrsave: 0x00000000

Binary Images:
    0x1000 -   0x144ff3 +wireshark-bin ??? (???) &lt;db314bf140c2a233c10a6af141bddb13&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/bin/wireshark-bin
  0x1d7000 -   0x20fffb +libwiretap.0.dylib ??? (???) &lt;9b9bb079d37f33dca9f1d39e25fa4cac&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libwiretap.0.dylib
  0x237000 -   0x238fff +libwsutil.0.dylib ??? (???) &lt;a390e168f9a2e4cc1cf121036dd1f314&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libwsutil.0.dylib
  0x23c000 -   0x264fff  libpcap.A.dylib ??? (???) &lt;155cc10bed10c655dc4b603a6af02ff2&gt; /usr/lib/libpcap.A.dylib
  0x26e000 -   0x2e5ffb +libgdk-x11-2.0.0.dylib ??? (???) &lt;8c1c73da30d9d789098e2ee7f6e66600&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgdk-x11-2.0.0.dylib
  0x326000 -   0x33affb +libatk-1.0.0.dylib ??? (???) &lt;6901b5a69ef34af2637749340029c392&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libatk-1.0.0.dylib
  0x34f000 -   0x350fff +libgmodule-2.0.0.dylib ??? (???) &lt;2daef9d4311886bb072527204635fe4e&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgmodule-2.0.0.dylib
  0x4f9000 -   0x84bff7 +libgtk-x11-2.0.0.dylib ??? (???) &lt;6e5cde035b6047b80e32738562e957b1&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgtk-x11-2.0.0.dylib
  0x9f2000 -   0xa05fff +libgdk_pixbuf-2.0.0.dylib ??? (???) &lt;dc33eba36fa3a1817bd4268cd657108f&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgdk_pixbuf-2.0.0.dylib
  0xa11000 -   0xa17fff +libpangocairo-1.0.0.dylib ??? (???) &lt;c2be4f1c231c5335f6d7d3e6bda79b07&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libpangocairo-1.0.0.dylib
  0xa20000 -   0xa44ff3 +libpangoft2-1.0.0.dylib ??? (???) &lt;385c9bfbf5fc5a787d257bd3223e0e64&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libpangoft2-1.0.0.dylib
  0xa55000 -   0xa8bff7 +libpango-1.0.0.dylib ??? (???) &lt;8e3607b2878b8c7d7394eada15a40d8e&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libpango-1.0.0.dylib
  0xaac000 -   0xb0bfff +libcairo.2.dylib ??? (???) &lt;69953d6066b92bc1a502f3b0c6953835&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libcairo.2.dylib
  0xb43000 -   0xb7bfff +libfontconfig.1.dylib ??? (???) &lt;d532468bbb8a174dc5593bb5bee43cc1&gt; /usr/X11/lib/libfontconfig.1.dylib
  0xb86000 -   0xc33fff +libfreetype.6.dylib ??? (???) &lt;df91927cb8f9b9b414c7b61de20fe7de&gt; /usr/X11/lib/libfreetype.6.dylib
  0xc4a000 -   0xc6bfff  libexpat.1.dylib ??? (???) &lt;e955fbf7296287c4d40694cf7dffd64f&gt; /usr/lib/libexpat.1.dylib
  0xc72000 -   0xc91fff +libpng12.0.dylib ??? (???) &lt;f63bbc4db93549f37f0119b06d012921&gt; /usr/X11/lib/libpng12.0.dylib
  0xc99000 -   0xca1ff7 +libXrender.1.dylib ??? (???) &lt;4b371b93de232042fedd5a8f115517f4&gt; /usr/X11/lib/libXrender.1.dylib
  0xca6000 -   0xd95ff7 +libX11.6.dylib ??? (???) &lt;53e39115925032643c51b495b4872256&gt; /usr/X11/lib/libX11.6.dylib
  0xdb5000 -   0xdb6ff2 +libXau.6.dylib ??? (???) &lt;4c3545453b575fedbd570092cfab410d&gt; /usr/X11/lib/libXau.6.dylib
  0xdba000 -   0xdbdff7 +libXdmcp.6.dylib ??? (???) &lt;8cca6c224f522589e7be57720bcebb73&gt; /usr/X11/lib/libXdmcp.6.dylib
  0xdc1000 -   0xdeffff +libpixman-1.0.dylib ??? (???) &lt;ae72e8a882fcf73dc500526791eb7f34&gt; /usr/X11/lib/libpixman-1.0.dylib
  0xdf8000 -   0xe30ff7 +libgobject-2.0.0.dylib ??? (???) &lt;956c87b4d13abb232a0276c0e49a55e3&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgobject-2.0.0.dylib
  0xe52000 -   0xe54ff9 +libgthread-2.0.0.dylib ??? (???) &lt;0a13189479eef1266657b0ea2e30953b&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgthread-2.0.0.dylib
  0xe58000 -   0xf21fff +libglib-2.0.0.dylib ??? (???) &lt;fdfa1309ecb83644b5c7bbb5ec87c14e&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libglib-2.0.0.dylib
  0xf67000 -   0xff4ffb +libgnutls.26.dylib ??? (???) &lt;b7f0bf1ff38a5afa26b595e9f1bfbe57&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgnutls.26.dylib
 0x1032000 -  0x1034ff3 +libgpg-error.0.dylib ??? (???) &lt;b160d62dacc1a505a59ffe298a8a8451&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgpg-error.0.dylib
 0x1037000 -  0x103fff4 +libintl.8.dylib ??? (???) &lt;5222f6c46eb329a95b1631fb3dc1e202&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libintl.8.dylib
 0x1046000 -  0x1090ffb +libsmi.2.dylib ??? (???) &lt;8981c86689a333add96fc300817f6ff3&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libsmi.2.dylib
 0x2fdf000 -  0x407ffff +libwireshark.0.dylib ??? (???) &lt;57681c001d4b31cbbaba519b563d5a6b&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libwireshark.0.dylib
 0x5fbe000 -  0x602efff +libgcrypt.11.dylib ??? (???) &lt;fe51092403d39451ed2a0995f4dc7176&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libgcrypt.11.dylib
 0x605e000 -  0x606dfff +libportaudio.2.dylib ??? (???) &lt;2e6f977aa90aa13d42e7c7f0694e5a40&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/libportaudio.2.dylib
 0x6079000 -  0x607affc +libXinerama.1.dylib ??? (???) &lt;a8056d54d641780d04d0dd931c7036de&gt; /usr/X11/lib/libXinerama.1.dylib
 0x607e000 -  0x6083ff3 +libXrandr.2.dylib ??? (???) &lt;78910d74ba8674a1c22a942b5a9d3681&gt; /usr/X11/lib/libXrandr.2.dylib
 0x6088000 -  0x608fff3 +libXcursor.1.dylib ??? (???) &lt;03aa21f0d2d653d79119a78f2e36c4fc&gt; /usr/X11/lib/libXcursor.1.dylib
 0x6095000 -  0x60a3ffb +libXext.6.dylib ??? (???) &lt;4edc2a2e173ce7a6fa3095841e7b4460&gt; /usr/X11/lib/libXext.6.dylib
 0x60aa000 -  0x60acffd +libXcomposite.1.dylib ??? (???) &lt;37ff0ab28f4b24c781b04421157cd8b0&gt; /usr/X11/lib/libXcomposite.1.dylib
 0x60b0000 -  0x60b1ffa +libXdamage.1.dylib ??? (???) &lt;a7ea67102de4c75cb66caaf263cde41a&gt; /usr/X11/lib/libXdamage.1.dylib
 0x60b5000 -  0x60b8ff3 +libXfixes.3.dylib ??? (???) &lt;0a865ceb222ef4671bbeedc68f8f4610&gt; /usr/X11/lib/libXfixes.3.dylib
 0x60bd000 -  0x60deff1  libmx.A.dylib ??? (???) /usr/lib/libmx.A.dylib
 0x6240000 -  0x6246ff7 +libpixmap.so ??? (???) &lt;823f57d57d49d22c1c2072791f2f55da&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/gtk-2.0/2.10.0/engines/libpixmap.so
 0x7fb8000 -  0x7fc5fff +asn1.so ??? (???) &lt;1899cdc45e69e4a5455386910a00430e&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/asn1.so
 0x7fd0000 -  0x7fd0ffd +coseventcomm.so ??? (???) &lt;3110d0e02dc04840fa9fad8fe1ab108d&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/coseventcomm.so
 0x7fd3000 -  0x7fd4ffa +cosnaming.so ??? (???) &lt;21707d4cc324dd17d894ac7886099bb3&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/cosnaming.so
 0x7fd8000 -  0x7feefff +docsis.so ??? (???) &lt;1e309e1e49e77faaed5651ff2483b017&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/docsis.so
 0x800e000 -  0x801aff1 +ethercat.so ??? (???) &lt;25682ebfc649c199b00ea2a12e0de73e&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/ethercat.so
 0x802f000 -  0x8037ff7 +gryphon.so ??? (???) &lt;589e9113f580386bccf02d018581090a&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/gryphon.so
 0x803d000 -  0x803dff4 +interlink.so ??? (???) &lt;7fb1a2422d48b4fec572281be55344a0&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/interlink.so
 0x8040000 -  0x8045ff3 +irda.so ??? (???) &lt;a5b612fa4be86407ea6cc3b486edadd9&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/irda.so
 0x804e000 -  0x804fffa +m2m.so ??? (???) &lt;4b92de2bd33f0fe4675049fbc04ec601&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/m2m.so
 0x8053000 -  0x8064fff +mate.so ??? (???) &lt;a87abf620fa755ab55ac0913c4538393&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/mate.so
 0x807e000 -  0x8093ffb +opcua.so ??? (???) &lt;91c6ff4c355889b039469df8ba7586b1&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/opcua.so
 0x80b8000 -  0x8152ff7 +parlay.so ??? (???) &lt;4782f5718f01c4d7bf510dd6ab7c56bf&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/parlay.so
 0x8195000 -  0x81c3ff3 +profinet.so ??? (???) &lt;6bf037a287d49a22c6dbb3836161cec3&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/profinet.so
 0x81f4000 -  0x81f9ff4 +sercosiii.so ??? (???) &lt;aa2a9b6966cfe3634fdd332d5304c5fc&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/sercosiii.so
 0x8203000 -  0x8203ffd +stats_tree.so ??? (???) &lt;9af71e294c752932424a61b3e496b5dd&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/stats_tree.so
 0x8206000 -  0x820eff2 +tango.so ??? (???) &lt;3388b8a4e03627ff8294cc61a7c4dcdb&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/tango.so
 0x8213000 -  0x8221ff3 +unistim.so ??? (???) &lt;056412b0e5a7d3c0beaecd683eabe2bb&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/unistim.so
 0x8235000 -  0x828aff3 +wimax.so ??? (???) &lt;d470fa1e6c9900d93815d42e7a65aa00&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/wimax.so
 0x82ec000 -  0x82f6ff7 +wimaxasncp.so ??? (???) &lt;0e86d28806d6bd4a9990256d3d6d698a&gt; /Applications/VideoNet&amp;Decorder/Wireshark.app/Contents/Resources/lib/wireshark/plugins/wimaxasncp.so
0x8fe00000 - 0x8fe30c23  dyld 97.1 (???) &lt;89a0055b0e7ea2db881b73c6e63bc774&gt; /usr/lib/dyld
0x90046000 - 0x90087ffb  libTIFF.dylib ??? (???) &lt;a4fac1b78bf536e570841166630ff642&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/Resources/libTIFF.dylib
0x90088000 - 0x9008dff6  libmathCommon.A.dylib ??? (???) /usr/lib/system/libmathCommon.A.dylib
0x901a2000 - 0x901d3fff  com.apple.coreui 1.2 (62) /System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI
0x901d4000 - 0x9026dfc3  libvDSP.dylib ??? (???) /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libvDSP.dylib
0x9026f000 - 0x90304ff7  com.apple.framework.IOKit 1.5.2 (???) &lt;ced0a498252f76a2d2ba9f2a0ae02160&gt; /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
0x90454000 - 0x90507ffc  com.apple.CFNetwork 438.14 (438.14) &lt;6e213ab40eabfc276ca46a7c7cfad01a&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
0x90b23000 - 0x90bf3fff  com.apple.ColorSync 4.5.3 (4.5.3) /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ColorSync.framework/Versions/A/ColorSync
0x90c33000 - 0x911afff7  com.apple.CoreGraphics 1.409.5 (???) &lt;5055e3621c3a2239851bd7e829e94ea1&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
0x911b0000 - 0x914d9fe7  libLAPACK.dylib ??? (???) /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libLAPACK.dylib
0x914de000 - 0x91563fff  libsqlite3.0.dylib ??? (???) &lt;daf55b073488086ef5b9a3781be53f14&gt; /usr/lib/libsqlite3.0.dylib
0x91cdb000 - 0x91fddffb  com.apple.CoreServices.CarbonCore 786.11 (786.14) &lt;4da8e0984e333f8cea32a24ba4364e8c&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/CarbonCore.framework/Versions/A/CarbonCore
0x91fe4000 - 0x91fe7ffb  com.apple.securityhi 3.0 (30817) &lt;e50c0cac9048f8923b95797753d50b5c&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/SecurityHI.framework/Versions/A/SecurityHI
0x91fe8000 - 0x92037fff  libGLImage.dylib ??? (???) &lt;2e1f2a2625064149d209ec19e52d0384&gt; /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLImage.dylib
0x92038000 - 0x92054ffb  libPng.dylib ??? (???) &lt;036c49544cb7b1d09d5e0185a1e26f7d&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/Resources/libPng.dylib
0x92055000 - 0x92060ffb  libgcc_s.1.dylib ??? (???) &lt;ea47fd375407f162c76d14d64ba246cd&gt; /usr/lib/libgcc_s.1.dylib
0x92083000 - 0x920e5ffb  com.apple.htmlrendering 68 (1.1.3) &lt;e852db1c007de975fae2f0c2769c88ef&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HTMLRendering.framework/Versions/A/HTMLRendering
0x920e6000 - 0x92106ff7  libJPEG.dylib ??? (???) &lt;bcc63fc19e0a5fa3d4b411f0de1d5851&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/Resources/libJPEG.dylib
0x92107000 - 0x92109ffd  libRadiance.dylib ??? (???) &lt;304e574d5de8d26630c4c516cc6e47fb&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/Resources/libRadiance.dylib
0x9210a000 - 0x92199ffb  com.apple.DesktopServices 1.4.8 (1.4.8) &lt;efaf20fbcdf58c7da37ddbcf190bba75&gt; /System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/DesktopServicesPriv
0x9219a000 - 0x92224fff  libvMisc.dylib ??? (???) /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libvMisc.dylib
0x92225000 - 0x92229ffe  libGIF.dylib ??? (???) &lt;cc34b3a44618a0e1ccc1c5b1cf28b5bb&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/Resources/libGIF.dylib
0x9222a000 - 0x92263fff  com.apple.SystemConfiguration 1.9.2 (1.9.2) &lt;21dee7ffd93306032f911b5ef3fdbab3&gt; /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
0x92335000 - 0x923b0fff  com.apple.SearchKit 1.2.2 (1.2.2) &lt;a9d0033a5e1e55b5e382e52fe578d734&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/SearchKit.framework/Versions/A/SearchKit
0x92529000 - 0x92541ffb  com.apple.DictionaryServices 1.0.0 (1.0.0) &lt;fe37191e732eeb66189185cd000a210b&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/DictionaryServices.framework/Versions/A/DictionaryServices
0x92542000 - 0x92542fff  com.apple.Accelerate 1.4.2 (Accelerate 1.4.2) /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
0x92560000 - 0x9264afff  libxml2.2.dylib ??? (???) &lt;c16d0fbbf8fd6b30695cd3c930355066&gt; /usr/lib/libxml2.2.dylib
0x92661000 - 0x92689fff  libxslt.1.dylib ??? (???) &lt;bb985380f353bbc7ce694d56884ea156&gt; /usr/lib/libxslt.1.dylib
0x927d9000 - 0x927e0fff  com.apple.CommonPanels 1.2.4 (85) &lt;0d1256175c5512c911ede094d767acfe&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/CommonPanels.framework/Versions/A/CommonPanels
0x927e1000 - 0x92891fff  com.apple.QD 3.11.57 (???) &lt;e74b370c6f81fc00e8936f5cf7c8ebe0&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/QD.framework/Versions/A/QD
0x928c5000 - 0x928fafff  com.apple.AE 402.3 (402.3) &lt;75725936d014fd3ca2553d18b784b99b&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/AE.framework/Versions/A/AE
0x92a21000 - 0x92bc1fe3  libSystem.B.dylib ??? (???) &lt;45c5920425c80bf594b3f1bde2382e95&gt; /usr/lib/libSystem.B.dylib
0x92c92000 - 0x92fcbff7  com.apple.HIToolbox 1.5.6 (???) &lt;a3b713a77c16da495c886463985f1e39&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/HIToolbox
0x93186000 - 0x931edffb  libstdc++.6.dylib ??? (???) &lt;a4e9b10268b3ffac26d0296499b24e8e&gt; /usr/lib/libstdc++.6.dylib
0x93212000 - 0x9323ffff  libGL.dylib ??? (???) /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGL.dylib
0x93240000 - 0x93253ffb  com.apple.speech.synthesis.framework 3.7.1 (3.7.1) &lt;050180a659a3905ea38f2acddcdf7b40&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/SpeechSynthesis.framework/Versions/A/SpeechSynthesis
0x93255000 - 0x932b2ffb  com.apple.HIServices 1.7.1 (???) &lt;a6c5c0bf2d68aeb453dbc493b7d0c8d9&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/HIServices.framework/Versions/A/HIServices
0x932b3000 - 0x93363fff  edu.mit.Kerberos 6.0.13 (6.0.13) &lt;2ed20a450576465ee4f9c317b8ce8c44&gt; /System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos
0x933a2000 - 0x933b0fff  libz.1.dylib ??? (???) &lt;1a70dd3594a8c5ad39d785af5da23237&gt; /usr/lib/libz.1.dylib
0x933b1000 - 0x937dfffe  libGLProgrammability.dylib ??? (???) &lt;5d52750ec9e438b25d3a4db51361fa2b&gt; /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLProgrammability.dylib
0x937e0000 - 0x9380bff7  libauto.dylib ??? (???) &lt;a64d088b2d17e013b9ee5a08d3a20d33&gt; /usr/lib/libauto.dylib
0x93818000 - 0x93824ff3  com.apple.audio.SoundManager 3.9.2 (3.9.2) &lt;79588842bcaf6c747a95b2120304397a&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/CarbonSound.framework/Versions/A/CarbonSound
0x93825000 - 0x938f8fff  com.apple.CoreServices.OSServices 228.1 (228.1) &lt;2724e880900a223dfd47e08e1b52ed17&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/OSServices.framework/Versions/A/OSServices
0x938f9000 - 0x938f9ffb  com.apple.installserver.framework 1.0 (8) /System/Library/PrivateFrameworks/InstallServer.framework/Versions/A/InstallServer
0x938fa000 - 0x93994ff7  com.apple.ApplicationServices.ATS 3.8.1 (???) &lt;6b490d945417fa114cfa607608c6b58e&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ATS.framework/Versions/A/ATS
0x93995000 - 0x93b7efff  com.apple.security 5.0.6 (37592) &lt;e945bd5cce817d5a95e2671659e5107a&gt; /System/Library/Frameworks/Security.framework/Versions/A/Security
0x93b7f000 - 0x93b86ffb  com.apple.print.framework.Print 218.0.3 (220.2) &lt;021d2263007c538fd9e6b52e66a2623d&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Print.framework/Versions/A/Print
0x93b87000 - 0x93b92fff  com.apple.speech.recognition.framework 3.7.24 (3.7.24) &lt;ae3dc890a43a9269388301f6b59d3091&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/SpeechRecognition.framework/Versions/A/SpeechRecognition
0x93b99000 - 0x93b9afff  libffi.dylib ??? (???) &lt;11b77dbce4aa0f0b66d40014230abd1d&gt; /usr/lib/libffi.dylib
0x9473a000 - 0x94742fff  libbsm.dylib ??? (???) &lt;c1fca3cbe3b1c21e9b31bc89b920f34c&gt; /usr/lib/libbsm.dylib
0x94743000 - 0x9488ffff  com.apple.ImageIO.framework 2.0.7 (2.0.7) &lt;c466caa621b9fa7431877610c21e39a6&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/ImageIO.framework/Versions/A/ImageIO
0x9489e000 - 0x948c5fff  libcups.2.dylib ??? (???) &lt;3ec5cc45c49c9e3deef8f0bd18b8dc50&gt; /usr/lib/libcups.2.dylib
0x948c6000 - 0x9495dfff  com.apple.LaunchServices 292 (292) &lt;06cb373fd960fbc2b4a0201f55c7dd6d&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/LaunchServices
0x949de000 - 0x949dfff8  com.apple.ApplicationServices 34 (34) &lt;6aa5ee485bb2e656531b3505932b845f&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
0x949e6000 - 0x94a05ffb  com.apple.CoreVideo 1.6.1 (48.6) &lt;4a3dfc7082a48c4e3c99ed644f49b9ba&gt; /System/Library/Frameworks/CoreVideo.framework/Versions/A/CoreVideo
0x95422000 - 0x95505fff  libobjc.A.dylib ??? (???) &lt;a1d4be2eed463c6799b6a1447fde72ba&gt; /usr/lib/libobjc.A.dylib
0x95507000 - 0x955c1fff  libcrypto.0.9.7.dylib ??? (???) &lt;1d82e65c85d65367f3b6b06355c89c9b&gt; /usr/lib/libcrypto.0.9.7.dylib
0x95688000 - 0x956a7fff  libresolv.9.dylib ??? (???) &lt;c5c72e1cf61cb844163156956a1d8407&gt; /usr/lib/libresolv.9.dylib
0x956a8000 - 0x956b1fff  com.apple.DiskArbitration 2.2.1 (2.2.1) &lt;682f5c45591e8c4a89c79e384e2c49af&gt; /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
0x956dc000 - 0x956eaff3  com.apple.opengl 1.5.10 (1.5.10) &lt;54bae289e544387ce7997a4a05e70aa9&gt; /System/Library/Frameworks/OpenGL.framework/Versions/A/OpenGL
0x95736000 - 0x95749fff  com.apple.LangAnalysis 1.6.5 (1.6.5) &lt;2a661ad6e432dd62dd831e234904061f&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/LangAnalysis.framework/Versions/A/LangAnalysis
0x9574a000 - 0x9574afff  com.apple.audio.units.AudioUnit 1.5 (1.5) /System/Library/Frameworks/AudioUnit.framework/Versions/A/AudioUnit
0x9576a000 - 0x957cbfff  com.apple.CoreText 2.0.4 (???) &lt;ebcc2c7e9b0bc10016af530d82a11f03&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/CoreText.framework/Versions/A/CoreText
0x9580a000 - 0x95829fff  com.apple.vecLib 3.4.2 (vecLib 3.4.2) /System/Library/Frameworks/vecLib.framework/Versions/A/vecLib
0x9585c000 - 0x95e16fff  libBLAS.dylib ??? (???) /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib
0x95e5e000 - 0x95e75ffb  com.apple.ImageCapture 5.0.2 (5.0.2) /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/ImageCapture.framework/Versions/A/ImageCapture
0x95ee3000 - 0x95f65fff  com.apple.print.framework.PrintCore 5.5.4 (245.6) &lt;3cde2550ec10348b7162d2b6cb0dfc67&gt; /System/Library/Frameworks/ApplicationServices.framework/Versions/A/Frameworks/PrintCore.framework/Versions/A/PrintCore
0x95f66000 - 0x95feefff  com.apple.ink.framework 101.3 (86) &lt;66a99ad6bc695390a66dd24789e23dcc&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Ink.framework/Versions/A/Ink
0x96206000 - 0x9632bff3  com.apple.CoreFoundation 6.5.7 (476.19) &lt;dee0f0024f3bf976cfa0a0816e8aa338&gt; /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
0x9632c000 - 0x96348ffb  com.apple.openscripting 1.2.8 (???) &lt;01f86cdb8f7347d2f3f13066e954acb6&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/OpenScripting.framework/Versions/A/OpenScripting
0x96349000 - 0x9634cfff  com.apple.help 1.1 (36) &lt;7106d6e074a3b9835ebf1e6cc6c822ce&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/Help.framework/Versions/A/Help
0x9639c000 - 0x96424ffb  com.apple.audio.CoreAudio 3.1.2 (3.1.2) &lt;6fc8a8cb43506b57b951da899a55d3b9&gt; /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
0x964ee000 - 0x965e4ffc  libiconv.2.dylib ??? (???) &lt;05ae1fcc97404173b2f9caef8f8be797&gt; /usr/lib/libiconv.2.dylib
0x965e5000 - 0x96604fff  com.apple.Accelerate.vecLib 3.4.2 (vecLib 3.4.2) /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/vecLib
0x96616000 - 0x96665fff  com.apple.Metadata 10.5.8 (398.26) &lt;1a261534027b9d1518327d1fabe1182b&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/Metadata.framework/Versions/A/Metadata
0x96a25000 - 0x96a7bfff  libGLU.dylib ??? (???) &lt;3418ce7ca0863162847f553c15d08674&gt; /System/Library/Frameworks/OpenGL.framework/Versions/A/Libraries/libGLU.dylib
0x96ba9000 - 0x96f0effe  com.apple.QuartzCore 1.5.8 (1.5.8) &lt;60e54cfb861dc5e66bb4f263a192d558&gt; /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
0x96f40000 - 0x97088ff3  libicucore.A.dylib ??? (???) &lt;bdab570d90979c4f601131d442f84720&gt; /usr/lib/libicucore.A.dylib
0x97089000 - 0x971d0ffb  com.apple.audio.toolbox.AudioToolbox 1.5.3 (1.5.3) /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
0x971d1000 - 0x97417ffb  com.apple.Foundation 6.5.9 (677.26) &lt;c30e4aea51bbae480d4550cd53abb441&gt; /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
0x974ae000 - 0x974f5fff  com.apple.NavigationServices 3.5.2 (163) &lt;453fd79dd63debad4908dcc726f9aa04&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/NavigationServices.framework/Versions/A/NavigationServices
0x976b9000 - 0x976b9fff  com.apple.Carbon 136 (136) &lt;6a6a209ec9179368db7ead8382b8ee63&gt; /System/Library/Frameworks/Carbon.framework/Versions/A/Carbon
0x976ba000 - 0x976baffa  com.apple.CoreServices 32 (32) &lt;42b6dda539f7411606187335d9eae0c5&gt; /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
0x976fa000 - 0x9780effa  com.apple.vImage 3.0 (3.0) /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vImage.framework/Versions/A/vImage
0xfffec000 - 0xfffeffff  libobjc.A.dylib ??? (???) /usr/lib/libobjc.A.dylib
0xffff8000 - 0xffff9703  libSystem.B.dylib ??? (???) /usr/lib/libSystem.B.dylib

My system is:
Model: PowerMac7,3, BootROM 5.2.4f1, 2 processors, PowerPC G5  (3.0), 2 GHz, 3 GB
Graphics: kHW_ATIrv351leItem, ATY,RV351, spdisplays_agp_device, 128 MB
Memory Module: DIMM0/J11, 1 GB, DDR SDRAM, PC3200U-30330
Memory Module: DIMM1/J12, 1 GB, DDR SDRAM, PC3200U-30330
Memory Module: DIMM2/J13, 512 MB, DDR SDRAM, PC3200U-30330
Memory Module: DIMM3/J14, 512 MB, DDR SDRAM, PC3200U-30330
Network Service: Ethernet, Ethernet, en0
Serial ATA Device: Maxtor 6B160M0, 152,67 GB
Serial ATA Device: Maxtor 6L250S0, 233,76 GB
Parallel ATA Device: PIONEER DVD-RW  DVR-109
USB Device: Desktop USB Drive, (null) mA
USB Device: Hub in Apple Extended USB Keyboard, (null) mA
USB Device: composite_device, (null) mA
USB Device: composite_device, (null) mA
USB Device: Apple Extended USB Keyboard, (null) mA
FireWire Device: (1394 ATAPI,Rev 1.00), Formac Disk 2.5&quot; Combo Device, 400mbit_speed</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-boot-process" rel="tag" title="see questions tagged &#39;boot-process&#39;">boot-process</span> <span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '11, 15:35</strong></p><img src="https://secure.gravatar.com/avatar/290b8d0f2411673e722327f4a8f96ec8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vividword&#39;s gravatar image" /><p><span>vividword</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vividword has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '11, 15:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-1641" class="comments-container"></div><div id="comment-tools-1641" class="comment-tools"></div><div class="clear"></div><div id="comment-1641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

