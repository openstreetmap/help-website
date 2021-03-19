+++
type = "question"
title = "error when compiling wireshark1.2.9"
description = '''How can I compile Wireshark 1.2.9 successfully? In Windows XP, I executed nmake -f Makefile.nmake all, but I get the following errors: packet-ipmi-bridge.c packet-ipmi-chassis.c packet-ipmi-picmg.c packet-ipmi-se.c packet-ipmi-storage.c packet-ipmi-transport.c Generating Code... Compiling... packet-...'''
date = "2011-09-10T02:17:00Z"
lastmod = "2011-09-10T02:17:00Z"
weight = 6244
keywords = [ "development" ]
aliases = [ "/questions/6244" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error when compiling wireshark1.2.9](/questions/6244/error-when-compiling-wireshark129)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6244-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I compile Wireshark 1.2.9 successfully?</p><p>In Windows XP, I executed <strong><code>nmake -f Makefile.nmake all</code></strong>, but I get the following errors:</p><pre><code>packet-ipmi-bridge.c
packet-ipmi-chassis.c
packet-ipmi-picmg.c
packet-ipmi-se.c
packet-ipmi-storage.c
packet-ipmi-transport.c
Generating Code...
Compiling...
packet-ipmi-pps.c
packet-ipmi-update.c
packet-dcerpc-nt.c
Generating Code...
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio\VC98\bin\c
l.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio\VC98\bin\N
MAKE.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio\VC98\bin\N
MAKE.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="question-tags" class="tags-container tags">development</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '11, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/a5a3214300b3b17fc46c3b656b7bed01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ylda_ljm0620&#39;s gravatar image" /><p>ylda_ljm0620<br />
<span class="score" title="31 reputation points">31</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ylda_ljm0620 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Sep '11, 13:05</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6244" class="comments-container"><span id="6248"></span><div id="comment-6248" class="comment"><div id="post-6248-score" class="comment-score"></div><div class="comment-text"><p>You'll need to provide the output from prior to the above for us to provide any help..</p><p>At some point prior to the above messages there was a compile error which eventually caused a delayed exit with the messages shown above.</p><p>P.S. Why Wireshark 1.2.9 ? That version is old and not actuallysupported anymore.</p></div><div id="comment-6248-info" class="comment-info"><span class="comment-age">(10 Sep '11, 05:04)</span> Bill Meier ♦♦</div></div><span id="6253"></span><div id="comment-6253" class="comment"><div id="post-6253-score" class="comment-score"></div><div class="comment-text"><p>because wireshark1.2.9 just satisfy our needs, when tshark convert pcap to text, SMV remain original hex, we hope ourselves to dissect the SMV for higher efficiency. but wireshark1.2.9(as any vertion), it's tshark can not dissect mms when mms is not begining with initiate. so we try to develop wireshark1.2.9.</p><p>now, I compile wireshark1.2.9 in windows XP, My complier is Visual studio 6.0.</p><p>After nmake -f Makefile verify_tools, what appears as follows:</p><pre><code>Microsoft (R) Program Maintenance Utility   Version 6.00.8168.0
Copyright (C) Microsoft Corp 1988-1998. All rights reserved.

Checking for required applications:
        cl: /cygdrive/c/Program Files/Microsoft Visual Studio/VC98/Bin/cl
        link: /cygdrive/c/Program Files/Microsoft Visual Studio/VC98/Bin/link
        nmake: /cygdrive/c/Program Files/Microsoft Visual Studio/VC98/Bin/nmake

        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        perl: /usr/bin/perl
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget

then , nmake -f Makefile.nmake setup, it success!</code></pre><p><strong>finally, nmake -f Makefile.nmake all, errors as follws:</strong></p><pre><code>packet-sccpmg.c
packet-scsi.c
packet-scsi-mmc.c
packet-scsi-sbc.c
packet-scsi-smc.c
packet-scsi-ssc.c
packet-sdlc.c
packet-sdp.c
packet-sebek.c
packet-ses.c
packet-sflow.c
packet-simulcrypt.c
packet-sip.c
packet-sigcomp.c
packet-sipfrag.c
packet-sita.c
packet-skinny.c
packet-slimp3.c
packet-sll.c
Generating Code...
Compiling...
packet-slowprotocols.c
packet-slsk.c
packet-smb-browse.c
packet-smb-common.c
packet-smb-logon.c
packet-smb-mailslot.c
packet-smb-pipe.c
packet-smb-sidsnooping.c
packet-smb.c
packet-smb2.c
packet-smpp.c
packet-smtp.c
packet-sna.c
packet-snaeth.c
packet-sndcp.c
packet-sndcp-xid.c
packet-socks.c
packet-nasdaq-soup.c
packet-spp.c
packet-spray.c
Generating Code...
Compiling...
packet-srp.c
packet-sscf-nni.c
packet-srvloc.c
packet-sscop.c
packet-scriptingservice.c
packet-ssh.c
packet-ssl.c
packet-ssl-utils.c
packet-starteam.c
packet-stat-notify.c
packet-stat.c
packet-stun.c
packet-stun2.c
packet-sua.c
packet-symantec.c
packet-synergy.c
packet-synphasor.c
packet-syslog.c
packet-t30.c
packet-t38.c
Generating Code...
Compiling...
packet-tacacs.c
packet-tali.c
packet-tapa.c
packet-tcp.c
packet-tds.c
packet-teamspeak2.c
packet-teimanagement.c
packet-telnet.c
packet-teredo.c
packet-text-media.c
packet-telkonet.c
packet-tftp.c
packet-time.c
packet-tipc.c
packet-tivoconnect.c
packet-tnef.c
packet-tns.c
packet-tpkt.c
packet-tpncp.c
packet-tr.c
Generating Code...
Compiling...
packet-trmac.c
packet-tsp.c
packet-tte.c
packet-tte-pcf.c
packet-turbocell.c
packet-turnchannel.c
packet-tuxedo.c
packet-tzsp.c
packet-ucp.c
packet-udld.c
packet-uma.c
packet-udp.c
packet-usb.c
packet-usb-masstorage.c
packet-umts_fp.c
packet-uts.c
packet-v120.c
packet-v5ua.c
packet-vcdu.c
packet-vicp.c
Generating Code...
Compiling...
packet-vines.c
packet-vj.c
packet-vlan.c
packet-vnc.c
packet-vrrp.c
packet-vtp.c
packet-wap.c
packet-wassp.c
packet-wbxml.c
packet-wccp.c
packet-wcp.c
packet-wfleet-hdlc.c
packet-who.c
packet-windows-common.c
packet-winsrepl.c
packet-wlccp.c
packet-wol.c
packet-wow.c
packet-wps.c
packet-wsmp.c
Generating Code...
Compiling...
packet-wsp.c
packet-wtls.c
packet-wtp.c
packet-x11.c
packet-x25.c
packet-x29.c
packet-xcsl.c
packet-xdmcp.c
packet-xml.c
packet-xot.c
packet-xtp.c
packet-xyplex.c
packet-yhoo.c
packet-ymsg.c
packet-ypbind.c
packet-yppasswd.c
packet-ypserv.c
packet-ypxfr.c
packet-zbee-aps.c
packet-zbee-security.c
Generating Code...
Compiling...
packet-zbee-nwk.c
packet-zbee-zdp.c
packet-zbee-zdp-binding.c
packet-zbee-zdp-discovery.c
packet-zbee-zdp-management.c
packet-zebra.c
packet-zep.c
packet-ziop.c
packet-zrtp.c
packet-isakmp.c
packet-k12.c
packet-nbd.c
packet-sccp.c
packet-scsi-osd.c
packet-sctp.c
packet-user_encap.c
packet-dcerpc-atsvc.c
packet-dcerpc-budb.c
packet-dcerpc-butc.c
packet-dcerpc-dfs.c
Generating Code...
Compiling...
packet-dcerpc-drsuapi.c
packet-dcerpc-dssetup.c
packet-dcerpc-efs.c
packet-dcerpc-initshutdown.c
packet-dcerpc-nspi.c
packet-dcerpc-rfr.c
packet-dcerpc-wkssvc.c
packet-dcerpc-wzcsvc.c
packet-dcerpc-dnsserver.c
packet-dcerpc-eventlog.c
packet-dcerpc-lsa.c
packet-dcerpc-srvsvc.c
packet-dcerpc-winreg.c
packet-acp133.c
packet-acse.c
packet-ansi_tcap.c
packet-camel.c
packet-cdt.c
packet-cmip.c
packet-cmp.c
Generating Code...
Compiling...
packet-cms.c
packet-crmf.c
packet-dap.c
packet-disp.c
packet-dop.c
packet-dsp.c
packet-ess.c
packet-ftam.c
packet-goose.c
packet-h225.c
packet-h235.c
packet-h245.c
packet-h248.c
packet-h282.c
packet-h283.c
packet-h323.c
packet-h450.c
packet-h450-ros.c
packet-h460.c
packet-h501.c
Generating Code...
Compiling...
packet-logotypecertextn.c
packet-mms.c
packet-mpeg-audio.c
packet-mpeg-pes.c
packet-ns_cert_exts.c
packet-ocsp.c
packet-opsi.c
packet-p7.c
packet-pkcs1.c
packet-pkinit.c
packet-pkix1explicit.c
packet-pkix1implicit.c
packet-pkixproxy.c
packet-pkixqualified.c
packet-pkixtsp.c
packet-q932.c
packet-q932-ros.c
packet-qsig.c
packet-ranap.c
packet-ros.c
Generating Code...
Compiling...
packet-rtnet.c
packet-rtse.c
packet-s4406.c
packet-sabp.c
packet-smrse.c
packet-spnego.c
packet-ulp.c
packet-wlancertextn.c
packet-x224.c
packet-x509af.c
packet-x509ce.c
packet-x509if.c
packet-x509sat.c
packet-ansi_map.c
packet-charging_ase.c
packet-gnm.c
packet-gsm_map.c
packet-inap.c
packet-ldap.c
packet-lte-rrc.c
Generating Code...
Compiling...
packet-nbap.c
packet-pcap.c
packet-pkcs12.c
packet-pres.c
packet-rnsap.c
packet-rrlp.c
packet-s1ap.c
packet-snmp.c
packet-t125.c
packet-tcap.c
packet-x2ap.c
packet-x411.c
packet-x420.c
packet-ipmi-app.c
packet-ipmi-bridge.c
packet-ipmi-chassis.c
packet-ipmi-picmg.c
packet-ipmi-se.c
packet-ipmi-storage.c
packet-ipmi-transport.c
Generating Code...
Compiling...
packet-ipmi-pps.c
packet-ipmi-update.c
packet-dcerpc-nt.c
Generating Code...
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio\VC98\Bin\c
l.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio\VC98\Bin\N
MAKE.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio\VC98\Bin\N
MAKE.EXE&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="comment-6253-info" class="comment-info"><span class="comment-age">(10 Sep '11, 07:01)</span> ylda_ljm0620</div></div><span id="6257"></span><div id="comment-6257" class="comment"><div id="post-6257-score" class="comment-score"></div><div class="comment-text"><p>It seems the error must have occurred even before the text posted.</p><p>In any case, you're using VC6 to do the build.</p><p>VC6 certainly isn't supported for building Wireshark 1.2.9. (I suppose that it's possible to fix whatever is causing the problem when using VC6 but it isn't worth the effort). :)</p><p>I suggest downloading/installing Microsoft VC2008EE (free); that's the VC version used to build Windows Wireshark 1.2.9.</p><p>I'm not sure I understand your reason for using 1.2.9. Building with the the latest 1.4 or 1.6 source, will make it easier for us to help with any problems you may encounter,</p></div><div id="comment-6257-info" class="comment-info"><span class="comment-age">(10 Sep '11, 15:59)</span> Bill Meier ♦♦</div></div><span id="6261"></span><div id="comment-6261" class="comment"><div id="post-6261-score" class="comment-score"></div><div class="comment-text"><p>Tanks very much. I have downloaded VS2008EE and installed, but new errors happened.</p><pre><code>nmake -f Makefile.nmake verify_tools, it success.

Microsoft (R) Program Maintenance Utility Version 9.00.30729.01

Copyright (C) Microsoft Corporation.  All rights reserved.

Checking for required applications:
        cl: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/cl
        link: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/link

        nmake: /cygdrive/c/Program Files/Microsoft Visual Studio 9.0/VC/BIN/nmak
e
        mt: /cygdrive/c/Program Files/Microsoft SDKs/Windows/v6.0A/bin/mt
        bash: /usr/bin/bash
        bison: /usr/bin/bison
        flex: /usr/bin/flex
        env: /usr/bin/env
        grep: /usr/bin/grep
        /usr/bin/find: /usr/bin/find
        perl: /usr/bin/perl
        C:\Python27\python.exe: /cygdrive/c/Python27/python.exe
        sed: /usr/bin/sed
        unzip: /usr/bin/unzip
        wget: /usr/bin/wget</code></pre><p><strong>finally, nmake -f Makefile.nmake all, errors appears as follows:</strong></p><pre><code>Microsoft (R) Program Maintenance Utility Version 9.00.30729.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd tools
        &quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\bin\nmake.exe&quot; /
            -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.30729.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        cd lemon
        ..\native-nmake &quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\bin\nma
ke.exe&quot; /                   -f Makefile.nmake

Microsoft (R) Program Maintenance Utility Version 9.00.30729.01
Copyright (C) Microsoft Corporation.  All rights reserved.

        cl -WX -D_U_=&quot;&quot; /Zi /W3 /MD /D_CRT_SECURE_NO_DEPRECATE /D_CRT_NONSTDC_NO
_DEPRECATE /DWIN32_LEAN_AND_MEAN /DMSC_VER_REQUIRED=1500 /D_BIND_TO_CURRENT_CRT_
VERSION=1 lemon.c
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\bin
\cl.EXE&quot;&#39; : return code &#39;0xc0000135&#39;
Stop.
NMAKE : fatal error U1077: &#39;..\native-nmake.CMD&#39; : return code &#39;0x2&#39;
Stop.
NMAKE : fatal error U1077: &#39;&quot;C:\Program Files\Microsoft Visual Studio 9.0\VC\bin
\nmake.exe&quot;&#39; : return code &#39;0x2&#39;
Stop.</code></pre></div><div id="comment-6261-info" class="comment-info"><span class="comment-age">(10 Sep '11, 18:32)</span> ylda_ljm0620</div></div><span id="6262"></span><div id="comment-6262" class="comment not_top_scorer"><div id="post-6262-score" class="comment-score"></div><div class="comment-text"><p>in addition, I will tell you the reason to use wireshark1.2.9.</p><p>first, wireshark of any vertion can not dissect mms what is not begining with Initiate, so i try to develop the wireshark to solve the problem. not like mms-ethereal, even mms-ethereal start after Initiate(you known, just as Initiate-request, Initiate-response) ,It can dissect the mms. but the wireshark show "dissctor is not available" near by ASN1.type.</p><p>second, I think to dissect the 61850 SMV by myself for higher Efficiency. the tshark(covert pcap to text) of wireshark1.2.9 just remain 61850 SMV hex in text file. but the tshark(covert pcap to text) of wireshark 1.6 have dissected the 61850 SM.</p><p><strong>which vertion wireshark can solve the problem?</strong></p></div><div id="comment-6262-info" class="comment-info"><span class="comment-age">(10 Sep '11, 18:55)</span> ylda_ljm0620</div></div><span id="6263"></span><div id="comment-6263" class="comment not_top_scorer"><div id="post-6263-score" class="comment-score"></div><div class="comment-text"><p>in addition, i whill farther explain why i use wireshark1.2.9 to develop.</p><p>It is that we have used thark of wireshark1.2.9 to convert pcap to text, and we read the text and further dissect the text to other application.</p><p>different vertion of wireshark thark to text, the 61850SMV and 61850GOOSE int text have different format. so we had better not to change wireshark vertion.</p></div><div id="comment-6263-info" class="comment-info"><span class="comment-age">(10 Sep '11, 19:07)</span> ylda_ljm0620</div></div><span id="6265"></span><div id="comment-6265" class="comment not_top_scorer"><div id="post-6265-score" class="comment-score"></div><div class="comment-text"><pre><code>Thanks, Bill Meier.
I am very anxious and waiting on-net for your answer.
please help me, thank you very much.</code></pre></div><div id="comment-6265-info" class="comment-info"><span class="comment-age">(11 Sep '11, 00:02)</span> ylda_ljm0620</div></div><span id="6266"></span><div id="comment-6266" class="comment not_top_scorer"><div id="post-6266-score" class="comment-score"></div><div class="comment-text"><p>Bill Meier, Thanks.</p><p>I am very anxious and will waiting for your answer online. Please help me.</p></div><div id="comment-6266-info" class="comment-info"><span class="comment-age">(11 Sep '11, 04:19)</span> ylda_ljm0620</div></div><span id="6269"></span><div id="comment-6269" class="comment not_top_scorer"><div id="post-6269-score" class="comment-score"></div><div class="comment-text"><p>Re: cl.EXE"' : return code '0xc0000135'</p><p>A Google search suggests this is caused by some type of setup problem.</p><p>Are you following the instructions (exactly) in the Wireshark Developer's Guide section: Win32: Step-by-Step Guide? http://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html</p><p>What is your PATH ? Are you doing call "c:Program FilesMicrosoft Visual Studio 9.0VCbinvcvars32.bat" as described in the Guide ?</p></div><div id="comment-6269-info" class="comment-info"><span class="comment-age">(11 Sep '11, 08:05)</span> Bill Meier ♦♦</div></div><span id="6272"></span><div id="comment-6272" class="comment"><div id="post-6272-score" class="comment-score">1</div><div class="comment-text"><p>re: the questions about issues with dissecting mms and 61850 SMV and asking "which vertion wireshark can solve the problem?"</p><p>I've no knowledge of these protocols.</p><p>I suggest posting this question on the wireshark-dev mailing list: See: http://www.wireshark.org/lists/</p><p>ask.wireshark.org is not really intended for extended discussions so I also suggest posting (separately) on wireshark-dev any further issues about building Wireshark. (You can link to this ask.wireshark.org question if needed).</p><p>Thanks</p></div><div id="comment-6272-info" class="comment-info"><span class="comment-age">(11 Sep '11, 09:27)</span> Bill Meier ♦♦</div></div><span id="6349"></span><div id="comment-6349" class="comment not_top_scorer"><div id="post-6349-score" class="comment-score"></div><div class="comment-text"><p>Thanks. it compiled successfully.</p><p>the reason of compiling is that i called the vcvar32.bat and nmake in two different cmd-window.</p><p>if calling them in the same cmd-window, and firstly calling vcvar32.bat, then calling nmake, it will success.</p></div><div id="comment-6349-info" class="comment-info"><span class="comment-age">(14 Sep '11, 01:56)</span> ylda_ljm0620</div></div></div><div id="comment-tools-6244" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-6244-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

