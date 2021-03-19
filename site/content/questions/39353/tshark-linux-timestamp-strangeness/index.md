+++
type = "question"
title = "tshark linux timestamp strangeness"
description = '''I&#x27;ve run tshark on a linux VM, capturing packets between the linux server and a database server. I&#x27;ve told tshark to use the -t ad option for timestamps and to run for an hour and just redirect it&#x27;s output to a text file. The weirdness is that the timestamps in the output file start to drift from th...'''
date = "2015-01-22T05:00:00Z"
lastmod = "2015-01-22T05:51:00Z"
weight = 39353
keywords = [ "timestamp" ]
aliases = [ "/questions/39353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark linux timestamp strangeness](/questions/39353/tshark-linux-timestamp-strangeness)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've run tshark on a linux VM, capturing packets between the linux server and a database server. I've told tshark to use the -t ad option for timestamps and to run for an hour and just redirect it's output to a text file.</p><p>The weirdness is that the timestamps in the output file start to drift from the system time (checked by doing a tail on the output file) and tshark finally completes after 90 minutes (despite the log file only having 60 minutes of data logged).</p><p>in other words I kicked tshark off at 12.01, and at 13.25 I tailed the output file and the last timestamp in the log was 2015-01-22 13:00:45.715033. When tshark finally completes at 13.31 the last timestamp in the file is 2015-01-22 13:01:58.374895.</p><p>I've done exactly the same thing on a server in a different environment and it completes on time (ie after 60 minutes) having logged 60 minutes of data....</p><p>Help!</p></div><div id="question-tags" class="tags-container tags">timestamp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '15, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/ac6bf5ff595edbe87ecbcb82c2298ff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ecrowe&#39;s gravatar image" /><p>ecrowe<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ecrowe has no accepted answers">0%</span></p></div></div><div id="comments-container-39353" class="comments-container"></div><div id="comment-tools-39353" class="comment-tools"></div><div class="clear"></div><div id="comment-39353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39354"></span>

<div id="answer-container-39354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39354-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>How well do you keep time in your VM? Does it have a 'direct' link from the VM to the host (sometimes certain tools are required IIRC), or does it have a NTP daemon?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '15, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39354" class="comments-container"><span id="39357"></span><div id="comment-39357" class="comment"><div id="post-39357-score" class="comment-score"></div><div class="comment-text"><p>It has vmware tools installed, ntpd isn't running.</p><p>Just to be clear, the time on the VM itself stays accurate, the times recorded by tshark drift further and further out over time.</p></div><div id="comment-39357-info" class="comment-info"><span class="comment-age">(22 Jan '15, 07:03)</span> ecrowe</div></div><span id="39360"></span><div id="comment-39360" class="comment"><div id="post-39360-score" class="comment-score"></div><div class="comment-text"><p>The times recorded by tshark come from the capture file written by dumpcap, the times in the capture file written by dumpcap come from libpcap, and the time stamps from libpcap come from the Linux kernel's PF_PACKET code, and "the system time" also comes from the kernel, so the two clocks <em>shouldn't</em> drift - they shouldn't even be two clocks.</p></div><div id="comment-39360-info" class="comment-info"><span class="comment-age">(22 Jan '15, 16:09)</span> Guy Harris ♦♦</div></div><span id="39362"></span><div id="comment-39362" class="comment"><div id="post-39362-score" class="comment-score"></div><div class="comment-text"><p>so is it possibly that the time stamps aren't drifting, just that there is some weird delay in writing to standard out / the file?</p></div><div id="comment-39362-info" class="comment-info"><span class="comment-age">(23 Jan '15, 03:01)</span> ecrowe</div></div><span id="39369"></span><div id="comment-39369" class="comment"><div id="post-39369-score" class="comment-score"></div><div class="comment-text"><p>Well, there's a delay with <em>any</em> program writing lines with the C standard I/O library, as it buffers output and only writes to the file every 4096 or so bytes. You can force TShark (or tcpdump) to write the buffer out after every packet by specifying the <code>-l</code> flag.</p><p>When you say "tshark finally completes after 90 minutes", what does "completes" mean? Did you tell tshark to capture for 90 minutes, so that it stops on its own, or did you ^C it after 90 minutes, or did you tell it to stop after a certain number of packets were captured?</p><p>Were you capturing with a capture filter?</p><p>How many packets did it capture per unit of time - was it a high rate or a lwo rate?</p><p>When it stopped, did it report any packets being dropped?</p></div><div id="comment-39369-info" class="comment-info"><span class="comment-age">(23 Jan '15, 11:28)</span> Guy Harris ♦♦</div></div><span id="39396"></span><div id="comment-39396" class="comment"><div id="post-39396-score" class="comment-score"></div><div class="comment-text"><p>I told it to do -a duration 3600. despite this it took 90 minutes before it finished.</p></div><div id="comment-39396-info" class="comment-info"><span class="comment-age">(26 Jan '15, 02:26)</span> ecrowe</div></div></div><div id="comment-tools-39354" class="comment-tools"></div><div class="clear"></div><div id="comment-39354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

