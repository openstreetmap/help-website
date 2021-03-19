+++
type = "question"
title = "tshark error - invalid -z argument"
description = '''Hello Gurus, I am executing the following command in a RH Linux environment (Wireshark 1.6.13 and Red Hat Linux version is 2.6.18-348.12.1.el5.): tshark -T fields -r ../P8Stress/WS1-WF-FL&#92;@2014-02-21_08-00_8-05.pcap -q -z &quot;follow,tcp,ascii,0&quot; I am getting the error message I have pasted below. The c...'''
date = "2014-04-30T14:44:00Z"
lastmod = "2014-05-01T10:09:00Z"
weight = 32322
keywords = [ "windows", "arguments", "linux", "tshark", "-z" ]
aliases = [ "/questions/32322" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark error - invalid -z argument](/questions/32322/tshark-error-invalid-z-argument)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32322-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Gurus,</p><p>I am executing the following command in a RH Linux environment (Wireshark 1.6.13 and Red Hat Linux version is 2.6.18-348.12.1.el5.):</p><p><code>tshark -T fields -r ../P8Stress/WS1-WF-FL\@2014-02-21_08-00_8-05.pcap -q -z "follow,tcp,ascii,0"</code></p><p>I am getting the error message I have pasted below. The command works when I run it on the Windows environment. However since our target environment is Linux, we need it to be working there as well. Is there a different way I need to use the -z switch in a Linux environment?</p><pre><code>tshark: invalid -z argument.
  -z argument must be one of :
     afp,srt
     ancp,tree
     ansi_a,
     bacapp_instanceid,tree
     bacapp_ip,tree
     bacapp_objectid,tree
     bacapp_service,tree
     bootp,stat,
     camel,counter
     camel,srt
     collectd,tree
     compare,
     conv,
     dcerpc,srt,
     dests,tree
     diameter,avp
     gsm_a,
     h225,counter
     h225,srt
     hosts
     http,stat,
     http,tree
     http_req,tree
     http_srv,tree
     icmp,srt
     icmpv6,srt
     io,phs
     io,stat,
     ip_hosts,tree
     isup_msg,tree
     megaco,rtd
     mgcp,rtd
     plen,tree
     proto,colinfo,
     ptype,tree
     radius,rtd
     rpc,programs
     rpc,srt,
     rtp,streams
     sametime,tree
     scsi,srt,
     sctp,stat
     sip,stat
     smb,sids
     smb,srt
     smpp_commands,tree
     sv
     ucp_messages,tree
     wsp,stat,</code></pre><p>Please help.</p></div><div id="question-tags" class="tags-container tags">windows arguments linux tshark -z</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '14, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/a4b274fac69275b61fbac559688c0ddb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssh_aix&#39;s gravatar image" /><p>ssh_aix<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssh_aix has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 May '14, 12:59</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-32322" class="comments-container"><span id="32324"></span><div id="comment-32324" class="comment"><div id="post-32324-score" class="comment-score"></div><div class="comment-text"><p>What version of tshark do you have on Windows, and what version do you have on AIX? I think the "-z follow" command was added in or around tshark 1.8. Run <code>tshark -v</code> to get the version information.</p></div><div id="comment-32324-info" class="comment-info"><span class="comment-age">(30 Apr '14, 14:47)</span> zachad</div></div><span id="32325"></span><div id="comment-32325" class="comment"><div id="post-32325-score" class="comment-score"></div><div class="comment-text"><p>1.10 in Windows. I am at a client place waiting for him to get the tshark version info. I already asked him that.</p><p>Is there any workaround for earlier versions?</p></div><div id="comment-32325-info" class="comment-info"><span class="comment-age">(30 Apr '14, 14:49)</span> ssh_aix</div></div><span id="32350"></span><div id="comment-32350" class="comment"><div id="post-32350-score" class="comment-score"></div><div class="comment-text"><p>Well, then -z follow,<strong>tcp</strong> is not available on that system.</p></div><div id="comment-32350-info" class="comment-info"><span class="comment-age">(01 May '14, 07:20)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-32322" class="comment-tools"></div><div class="clear"></div><div id="comment-32322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32356"></span>

<div id="answer-container-32356" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32356-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just to put an Answer to this question: as Kurt said, that option is not available on that older version of Wireshark/tshark. If you need the "follow" functionality you'll need to use the Wireshark GUI (you could cut-n-paste the "follow TCP stream" output into a text file if needed) or do the tshark work on a different system.</p><p>Unfortunately you can't (easily) get a more modern Wireshark on RHEL5 because the Gtk+ version in RHEL5 is too old to support even Wireshark 1.8.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '14, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-32356" class="comments-container"><span id="32360"></span><div id="comment-32360" class="comment"><div id="post-32360-score" class="comment-score"></div><div class="comment-text"><p>What version of wireshark is this? We found this on one other RHEL system within the Organization network. It looks to be some VERY old version of wireshark?</p><p><code>[[email protected] ~]# rpm -qa |grep wireshark</code></p><p><code>wireshark-1.0.15-5.el5.x86_64</code></p></div><div id="comment-32360-info" class="comment-info"><span class="comment-age">(01 May '14, 11:45)</span> ssh_aix</div></div><span id="32362"></span><div id="comment-32362" class="comment"><div id="post-32362-score" class="comment-score"></div><div class="comment-text"><p>Yeah, RHEL ships with Wireshark 1.0. Redhat EL's are all about stability so they generally don't change versions within a RHEL version (e.g., RHEL 5.0 shipped with Wireshark 1.0 so it will forever be stuck with Wireshark 1.0).</p><p>If you compile your own you could get up to Wireshark 1.6 on these systems (without massive effort) but Kurt thinks that won't help you get the tshark option you want.</p></div><div id="comment-32362-info" class="comment-info"><span class="comment-age">(01 May '14, 12:58)</span> JeffMorriss ♦</div></div><span id="32365"></span><div id="comment-32365" class="comment"><div id="post-32365-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but Kurt thinks that won't help you get the tshark option you want.</p></blockquote><p>it won't help, because <strong>-z follow</strong> does not exist in 1.6.x. Actually @zachad mentioned first, that this particular option was added in 1.8.x</p><p>@ssh_aix: it's probably easier to only record the data on RHEL (with tcpdump or dumpcap) and later analyze it on a system that provides at least wireshark 1.8.x (Windows, Linux, *BSD).</p></div><div id="comment-32365-info" class="comment-info"><span class="comment-age">(01 May '14, 16:05)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-32356" class="comment-tools"></div><div class="clear"></div><div id="comment-32356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

