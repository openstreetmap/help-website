+++
type = "question"
title = "Remote interface linux"
description = '''Hi, I am wanting to setup a remote interface as I am using an Aerohive Remote Sniffer http://boundless.aerohive.com/blog/innovative-wi-fi-how-to-do-packet-captures.html I have spent a while looking online and my understanding is that this feature is only implemented in Windows. I have been looking f...'''
date = "2016-09-22T23:40:00Z"
lastmod = "2016-09-24T02:29:00Z"
weight = 55768
keywords = [ "remote-monitoring", "remote-capture", "linux" ]
aliases = [ "/questions/55768" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Remote interface linux](/questions/55768/remote-interface-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55768-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am wanting to setup a remote interface as I am using an Aerohive Remote Sniffer <a href="http://boundless.aerohive.com/blog/innovative-wi-fi-how-to-do-packet-captures.html">http://boundless.aerohive.com/blog/innovative-wi-fi-how-to-do-packet-captures.html</a></p><p>I have spent a while looking online and my understanding is that this feature is only implemented in Windows. I have been looking for a linux alternative but everything I find seems to be about piping the network traffic from another unix machine to a local machine over ssh.</p><p>I was just wondering if there are any linux alternatives to the wireshark remote interface feature.</p><p>Thanks for your time</p></div><div id="question-tags" class="tags-container tags">remote-monitoring remote-capture linux</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '16, 23:40</strong></p><img src="https://secure.gravatar.com/avatar/767a49a3a781eff351fdbc3f38900dd2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roy_muzz&#39;s gravatar image" /><p>roy_muzz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roy_muzz has no accepted answers">0%</span></p></div></div><div id="comments-container-55768" class="comments-container"></div><div id="comment-tools-55768" class="comment-tools"></div><div class="clear"></div><div id="comment-55768-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55779"></span>

<div id="answer-container-55779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55779-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark on Linux does not support the rpcap method. Capturing over an encrypted SSH session is the way to go for Linux.</p><p>On older versions of Wireshark, your only method for remote live captures is a pipe from stdin (with the limitation that you have to restart Wireshark every time you want to restart your capture). Quite inconvenient, but here are two examples (see manual pages for explanation of options: <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a>, <a href="https://www.wireshark.org/docs/man-pages/wireshark.html">wireshark</a>, <a href="http://www.tcpdump.org/manpages/tcpdump.1.html">tcpdump</a>):</p><pre><code>ssh [email protected] dumpcap -i eth0 -P -w - -f &#39;tcp port 80&#39; | wireshark -i - -k -p
ssh [email protected] sudo tcpdump -Z user -i eth0 -p -U -w - &#39;tcp port 80&#39; | wireshark -i - -k -p</code></pre><p>Typically dumpcap is installed with extra capabilities (see <a href="https://wiki.wireshark.org/CaptureSetup/CapturePrivileges#Most_UNIXes">CaptureSetup/CapturePrivileges</a>), so no root is needed. For tcpdump you might have to configure a password-less sudo (edit with <code>visudo -f /etc/sudoers/wireshark-tcpdump</code>, add <code>%wireshark ALL = NOPASSWD: /usr/sbin/tcpdump</code> to allow everyone from the "wireshark" group use password-less sudo for just tcpdump).</p><p>Newer versions of Wireshark (since 2.2) however have the "Extcap" mechanism. If you have dumpcap installed on the remote server, you can configure the "sshdump" interface in the interfaces list (set a user and host). Then you can capture from it as if it was a local one (behind the scenes it uses ssh + dumpcap). This mechanism can also be used for tcpdump, but <code>sshdump</code> currently does not support it (see <a href="https://git.lekensteyn.nl/peter/wireshark-notes/tree/extcap/ssh-tcpdump">https://git.lekensteyn.nl/peter/wireshark-notes/tree/extcap/ssh-tcpdump</a> for an alternative script).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '16, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-55779" class="comments-container"><span id="55795"></span><div id="comment-55795" class="comment"><div id="post-55795-score" class="comment-score"></div><div class="comment-text"><p>Not that currently sshdump doesn't work that well on Windows, see bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12884">12884</a>.</p></div><div id="comment-55795-info" class="comment-info"><span class="comment-age">(24 Sep '16, 05:01)</span> grahamb ♦</div></div></div><div id="comment-tools-55779" class="comment-tools"></div><div class="clear"></div><div id="comment-55779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

