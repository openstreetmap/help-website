+++
type = "question"
title = "Wireshark reading some tcpdump files but not others."
description = '''I have a Linux box running a cron job of tcpdump constantly with: tcpdump -i eth0 -nnv &amp;gt; blahblahlog.log and I am trying to look at the last few days to research a problem I was seeing. When I change the extension of the capture of today (still ongoing) I just get a little message that it was cut...'''
date = "2015-10-28T14:04:00Z"
lastmod = "2015-10-28T14:53:00Z"
weight = 47035
keywords = [ "file-format", "tcpdump" ]
aliases = [ "/questions/47035" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark reading some tcpdump files but not others.](/questions/47035/wireshark-reading-some-tcpdump-files-but-not-others)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47035-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Linux box running a cron job of tcpdump constantly with: <em>tcpdump -i eth0 -nnv &gt; blahblahlog.log</em> and I am trying to look at the last few days to research a problem I was seeing. When I change the extension of the capture of today (still ongoing) I just get a little message that it was cut off in the middle of a capture, which I know since I did it. However if I try to do one of the previous days captures I get "The file "blahblahlog.pcap" isn't a capture file in a format Wireshark understands." I saw in looking on here and StackOverflow that I should use the -w flag but what I'm confused by is if that is the case why is it able to open the incomplete capture from today and not these other ones?</p></div><div id="question-tags" class="tags-container tags">file-format tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '15, 14:04</strong></p><img src="https://secure.gravatar.com/avatar/f4ba30b7c46ee3911ab992280c905829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WetStoneTech&#39;s gravatar image" /><p>WetStoneTech<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WetStoneTech has no accepted answers">0%</span></p></div></div><div id="comments-container-47035" class="comments-container"></div><div id="comment-tools-47035" class="comment-tools"></div><div class="clear"></div><div id="comment-47035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47039"></span>

<div id="answer-container-47039" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47039-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>the &gt; does not work here. You must use "-i eth0 -nnv -w blagblahlog.log" instead of your example.</p><p>Next, you should also add "-s 0" to your command line if you want the complete contents of the packets to be stored and not just the first 60 (?) bytes.</p><p>But it is also not clear to me how is it possible that the "today's" capture can be open.</p><p>Regards</p><p>Pavel</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '15, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Oct '15, 14:54</p></div></div><div id="comments-container-47039" class="comments-container"><span id="47040"></span><div id="comment-47040" class="comment"><div id="post-47040-score" class="comment-score"></div><div class="comment-text"><p>I've just tried it - as expected, "&gt; filename" saves the text output of tcpdump into the "filename", so I don't get how you could open the result with Wireshark. Has Wireshark first complained about the file being cut in the middle of a packet and then has shown some packets making sense or it has shown the complaint and that was all?</p><p>To double check, you may simply "cat" or "less" the "today's" file; if it is human-readable, it is not a pcap nor pcapng file. But it may be so short that Wireshark's heuristics false-detects it as some of the other formats which Wireshark supports.</p></div><div id="comment-47040-info" class="comment-info"><span class="comment-age">(28 Oct '15, 15:17)</span> sindy</div></div><span id="47061"></span><div id="comment-47061" class="comment"><div id="post-47061-score" class="comment-score"></div><div class="comment-text"><p>I've already added the -w to my command string and I'll go back and add the -s for tomorrow's log and going forward, thanks for the suggestions.</p><p>As for the "today's" file it actually stopped opening in Wireshark now and is giving me the same format error as the other ones. With the way some of my equipment has been operating lately I'm chalking the fact that it worked up to the computer gods at this point.</p></div><div id="comment-47061-info" class="comment-info"><span class="comment-age">(29 Oct '15, 05:37)</span> WetStoneTech</div></div></div><div id="comment-tools-47039" class="comment-tools"></div><div class="clear"></div><div id="comment-47039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

