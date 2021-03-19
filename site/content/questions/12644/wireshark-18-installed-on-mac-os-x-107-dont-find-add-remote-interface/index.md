+++
type = "question"
title = "wireshark 1.8 installed on mac os x 10.7 don&#x27;t find &quot;add remote interface&quot;"
description = ''''''
date = "2012-07-11T23:23:00Z"
lastmod = "2012-07-12T08:15:00Z"
weight = 12644
keywords = [ "lion" ]
aliases = [ "/questions/12644" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark 1.8 installed on mac os x 10.7 don't find "add remote interface"](/questions/12644/wireshark-18-installed-on-mac-os-x-107-dont-find-add-remote-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12644-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">lion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '12, 23:23</strong></p><img src="https://secure.gravatar.com/avatar/d72264a2147217e31ec4d77f5692faa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bigkun&#39;s gravatar image" /><p>bigkun<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bigkun has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jul '12, 06:36</p></div></div><div id="comments-container-12644" class="comments-container"></div><div id="comment-tools-12644" class="comment-tools"></div><div class="clear"></div><div id="comment-12644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12661"></span>

<div id="answer-container-12661" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12661-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe some libpcap functions, needed for remote capturing, are not available on Mac OS X.</p><p>See here <code>http://anonsvn.wireshark.org/wireshark/trunk/acinclude.m4</code><br />
</p><pre><code>    if test $ac_cv_func_pcap_open = &quot;yes&quot; -a \
            $ac_cv_func_pcap_findalldevs_ex = &quot;yes&quot; -a \
            $ac_cv_func_pcap_createsrcstr = &quot;yes&quot; ; then
        AC_DEFINE(HAVE_PCAP_REMOTE, 1,
            [Define to 1 if you have WinPcap remote capturing support and prefer to use these new API features.])
    fi</code></pre><p>Looks like <strong><a href="http://www.winpcap.org/docs/docs_41b5/html/group__wpcapfunc.html#ga3111e10f930a9772a32a922b26948b0">pcap_createsrcstr()</a></strong> is not available on Mac OS X. Thus <strong>HAVE_PCAP_REMOTE</strong> is not set and that's the reason why that feature is not built into the Mac OS X binary.</p><p>UPDATE: You can implement another "remote capturing" method, by using pipes and ssh on Mac OS X.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/Pipes</code><br />
</p></blockquote><p>Search for "Remote Capture".</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '12, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jul '12, 08:35</p></div></div><div id="comments-container-12661" class="comments-container"><span id="12692"></span><div id="comment-12692" class="comment"><div id="post-12692-score" class="comment-score"></div><div class="comment-text"><p>@Kurt I typed</p><pre><code>$ mkfifo /tmp/sharkfin
$ wireshark -k -i /tmp/sharkfin &amp;
$ ssh [email protected] &quot;dumpcap -w - not port 22&quot; &gt; /tmp/sharkfin</code></pre><p>(192.168.0.142 is my remote host)</p><p>it not work!</p><p>and tip that: <img src="https://osqa-ask.wireshark.org/upfiles/wireshark_pipe.png" alt="alt text" /></p></div><div id="comment-12692-info" class="comment-info"><span class="comment-age">(13 Jul '12, 00:07)</span> bigkun</div></div><span id="12713"></span><div id="comment-12713" class="comment"><div id="post-12713-score" class="comment-score">1</div><div class="comment-text"><p>please run the following command and check if everything works fine:</p><blockquote><p><code>ssh [email protected] "dumpcap -w - not port 22" \&gt; /tmp/output.cap</code><br />
</p></blockquote><p>output.cap is just a regular file, not a pipe!</p><p>After a 30 seconds stop the ssh command (CTRL-C) and then open that file with 'more'. If it contains error messages, that's the reason why it does not work. If it looks like binary data, try to open it in Wireshark.</p><p>Report back the results.</p><p>If the capture file containes pcap data, you can modify the command and use this instead of a file system based pipe.</p><blockquote><p><code>ssh [email protected] 'dumpcap -w - -f "not port 22"' | wireshark -k -i -</code></p></blockquote><p><strong>UPDATE/SOLUTION:</strong> The problem is your dumpcap command. You need to specify the capture filter with -f (as done above), otherwise the last - (after -w) will terminate the CLI parameters in bash and dumpcap prints an error message.</p><p>dumpcap: Invalid argument: port</p></div><div id="comment-12713-info" class="comment-info"><span class="comment-age">(13 Jul '12, 17:19)</span> Kurt Knochner ♦</div></div><span id="12730"></span><div id="comment-12730" class="comment"><div id="post-12730-score" class="comment-score"></div><div class="comment-text"><p>it works well, thanks!</p></div><div id="comment-12730-info" class="comment-info"><span class="comment-age">(15 Jul '12, 18:43)</span> bigkun</div></div></div><div id="comment-tools-12661" class="comment-tools"></div><div class="clear"></div><div id="comment-12661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

