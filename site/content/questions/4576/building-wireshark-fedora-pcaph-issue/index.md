+++
type = "question"
title = "Building Wireshark Fedora pcap.h issue"
description = '''I am trying to build Wireshark 1.6 on Fedora 14 x64. When I run the ./configure script I get the following error: configure: error: Header file pcap.h not found; if you installed libpcap from source, did you also do &quot;make install-incl&quot;, and if you installed a binary package of libpcap, is there also...'''
date = "2011-06-15T10:43:00Z"
lastmod = "2011-06-15T12:19:00Z"
weight = 4576
keywords = [ "pcap.h", "fedora" ]
aliases = [ "/questions/4576" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Building Wireshark Fedora pcap.h issue](/questions/4576/building-wireshark-fedora-pcaph-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4576-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to build Wireshark 1.6 on Fedora 14 x64. When I run the ./configure script I get the following error:</p><p>configure: error: Header file pcap.h not found; if you installed libpcap from source, did you also do "make install-incl", and if you installed a binary package of libpcap, is there also a developer's package of libpcap, and did you also install that package?</p><p>I found the following in the FAQ:</p><p>Q 4.1: I have libpcap installed; why did the configure script not find pcap.h or bpf.h?</p><p>A: Are you sure pcap.h and bpf.h are installed? The official distribution of libpcap only installs the libpcap.a library file when "make install" is run. To install pcap.h and bpf.h, you must run "make install-incl". If you're running Debian or Redhat, make sure you have the "libpcap-dev" or "libpcap-devel" packages installed. It's also possible that pcap.h and bpf.h have been installed in a strange location. If this is the case, you may have to tweak aclocal.m4.</p><p>I have downloaded libpcap-1.1.1 but the Makefile does not seem to have a "install-incl" target. Also, libpcap.x86_64 is installed from the fedora repository. There is no package named "libpcap-dev in the Fedora repository. What should I do next?</p></div><div id="question-tags" class="tags-container tags">pcap.h fedora</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '11, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/590ae8f6bc8d883d28059988ad52e19b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="irarcher&#39;s gravatar image" /><p>irarcher<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="irarcher has no accepted answers">0%</span></p></div></div><div id="comments-container-4576" class="comments-container"></div><div id="comment-tools-4576" class="comment-tools"></div><div class="clear"></div><div id="comment-4576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4579"></span>

<div id="answer-container-4579" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4579-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Redhat generally has a package named "libpcap-devel" (but not one called "libpcap-dev"). Did you try with that name?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '11, 12:19</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-4579" class="comments-container"><span id="4593"></span><div id="comment-4593" class="comment"><div id="post-4593-score" class="comment-score"></div><div class="comment-text"><p>Yes, I tried both names.</p></div><div id="comment-4593-info" class="comment-info"><span class="comment-age">(16 Jun '11, 08:07)</span> irarcher</div></div><span id="4595"></span><div id="comment-4595" class="comment"><div id="post-4595-score" class="comment-score"></div><div class="comment-text"><p>Argh, that's annoying. It looks like they forgot libpcap-devel. The package is in <a href="http://download.fedora.redhat.com/pub/fedora/linux/updates/testing/14/x86_64/">updates/testing</a>, though, so I guess they realized their mistake(?). Fedora 15 appears to have the same problem, but libpcap-devel has not yet made even to updates/testing.</p><p>For now, it looks like you can pick up the not-done-testing-yet update. Or find the right target to install the header files from the libpcap source. It might be worth opening a bug with Redhat too (I can't find one about it).</p></div><div id="comment-4595-info" class="comment-info"><span class="comment-age">(16 Jun '11, 08:40)</span> JeffMorriss ♦</div></div><span id="4596"></span><div id="comment-4596" class="comment"><div id="post-4596-score" class="comment-score"></div><div class="comment-text"><p>OK, I filed a Redhat <a href="https://bugzilla.redhat.com/show_bug.cgi?id=713872">bug</a> on the topic.</p></div><div id="comment-4596-info" class="comment-info"><span class="comment-age">(16 Jun '11, 09:15)</span> JeffMorriss ♦</div></div><span id="4600"></span><div id="comment-4600" class="comment"><div id="post-4600-score" class="comment-score"></div><div class="comment-text"><p>The Redhat bug is closed--looks like the problem <em>I</em> found was a bad mirror which was missing the libpcap-devel package. I don't know if your system is being unfortunate and picking the same mirror or if multiple mirrors have the problem or what, but libpcap-devel is part of the base OS for both Fedora 14 and 15 (see the URL to the master mirror in the bug report).</p></div><div id="comment-4600-info" class="comment-info"><span class="comment-age">(16 Jun '11, 11:10)</span> JeffMorriss ♦</div></div><span id="4607"></span><div id="comment-4607" class="comment"><div id="post-4607-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff. I'm actually working on an isolated network, and I was using the packages on the Fedora 14 DVD (which does not contain libpcap-devel). Also I realized that I needed to select the "Everything" directory instead of the "Fedora" directory to find this package (from http://dl.fedoraproject.org/pub/fedora/linux/releases/14/).</p></div><div id="comment-4607-info" class="comment-info"><span class="comment-age">(16 Jun '11, 15:19)</span> irarcher</div></div></div><div id="comment-tools-4579" class="comment-tools"></div><div class="clear"></div><div id="comment-4579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

