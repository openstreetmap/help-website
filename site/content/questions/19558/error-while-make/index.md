+++
type = "question"
title = "Error while make"
description = '''Hello! I run ./configure and all seems ok. When run &quot;make&quot; i get the following error: In file included from airpcap_dlg.c:44:0: ../../pcap.h:276:7: error: conflicting types for ‘bpf_filter’ /usr/local/include/pcap/bpf.h:1274:14: note: previous declaration of ‘bpf_filter’ was here ../../pcap.h:277:5:...'''
date = "2013-03-16T09:51:00Z"
lastmod = "2013-03-16T10:48:00Z"
weight = 19558
keywords = [ "make", "error" ]
aliases = [ "/questions/19558" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error while make](/questions/19558/error-while-make)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19558-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I run ./configure and all seems ok. When run "make" i get the following error:</p><pre><code>In file included from airpcap_dlg.c:44:0:
../../pcap.h:276:7: error: conflicting types for ‘bpf_filter’
/usr/local/include/pcap/bpf.h:1274:14: note: previous declaration of ‘bpf_filter’ was here
../../pcap.h:277:5: error: conflicting types for ‘bpf_validate’
/usr/local/include/pcap/bpf.h:1273:12: note: previous declaration of ‘bpf_validate’ was here
airpcap_dlg.c: In function ‘on_merge_bt_clicked’:
airpcap_dlg.c:2406:11: warning: variable ‘n_curr_adapter_keys’ set but not used [-Wunused-but-set-variable]
airpcap_dlg.c:2405:11: warning: variable ‘n_driver_keys’ set but not used [-Wunused-but-set-variable]
airpcap_dlg.c:2404:11: warning: variable ‘n_wireshark_keys’ set but not used [-Wunused-but-set-variable]
airpcap_dlg.c: In function ‘on_import_bt_clicked’:
airpcap_dlg.c:2523:11: warning: variable ‘n_curr_adapter_keys’ set but not used [-Wunused-but-set-variable]
airpcap_dlg.c:2522:11: warning: variable ‘n_driver_keys’ set but not used [-Wunused-but-set-variable]
airpcap_dlg.c:2521:11: warning: variable ‘n_wireshark_keys’ set but not used [-Wunused-but-set-variable]
make[2]: *** [libgtkui_a-airpcap_dlg.o] Error 1
make[2]: Leaving directory `/home/juan/wireshark-1.8.6/ui/gtk&#39;
make[1]: *** [install-recursive] Error 1
make[1]: Leaving directory `/home/juan/wireshark-1.8.6&#39;
make: *** [install] Error 2</code></pre><p>Any help is welcome.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">make error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '13, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/933718eb91ca2140768b64eb0c277410?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrizzone&#39;s gravatar image" /><p>mrizzone<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrizzone has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Mar '14, 10:58</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-19558" class="comments-container"><span id="19560"></span><div id="comment-19560" class="comment"><div id="post-19560-score" class="comment-score"></div><div class="comment-text"><p>Please provide info as to the OS, OS version, Compiler version, libpcap version &amp; etc</p></div><div id="comment-19560-info" class="comment-info"><span class="comment-age">(16 Mar '13, 09:59)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-19558" class="comment-tools"></div><div class="clear"></div><div id="comment-19558-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19562"></span>

<div id="answer-container-19562" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19562-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>In file included from airpcap_dlg.c:44:0:
../../pcap.h:276:7: error: conflicting types for ‘bpf_filter’</code></pre><p>If there is a "pcap.h" file in the top-level Wireshark source directory, remove it, as it shouldn't be there (Wireshark does not include a "pcap.h" header file), and then try building again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19562" class="comments-container"></div><div id="comment-tools-19562" class="comment-tools"></div><div class="clear"></div><div id="comment-19562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

