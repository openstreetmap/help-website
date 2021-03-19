+++
type = "question"
title = "Wireshark from command line"
description = '''I&#x27;d like to programatically call wireshark to capture 100 packets, parse source mac address of each packet and close. How can I do this? This is what I have so far, but it&#x27;s not working:  wireshark -c 100 -k -Q -w -  This is supposed to stop capturing after 100 packets, start capturing immediately, ...'''
date = "2011-08-22T02:43:00Z"
lastmod = "2011-08-22T06:01:00Z"
weight = 5800
keywords = [ "mac", "command-line", "wireshark" ]
aliases = [ "/questions/5800" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark from command line](/questions/5800/wireshark-from-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5800-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'd like to programatically call wireshark to capture 100 packets, parse source mac address of each packet and close. How can I do this?</p><p>This is what I have so far, but it's not working:</p><pre><code>wireshark -c 100 -k -Q -w -</code></pre><p>This is supposed to stop capturing after 100 packets, start capturing immediately, shut down wireshark after done, and print the output to stdout, which is the command prompt. Any help? <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChCustCommandLine.html">http://www.wireshark.org/docs/wsug_html_chunked/ChCustCommandLine.html</a></p></div><div id="question-tags" class="tags-container tags">mac command-line wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '11, 02:43</strong></p><img src="https://secure.gravatar.com/avatar/d7c782bb984b130f22efa1bd122633da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonio09&#39;s gravatar image" /><p>tonio09<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonio09 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Aug '11, 17:43</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-5800" class="comments-container"><span id="5813"></span><div id="comment-5813" class="comment"><div id="post-5813-score" class="comment-score"></div><div class="comment-text"><p>The documentation you quote says that "-w -" sets the "savefile" to -, i.e. to the standard output". That's "savefile" in the tcpdump sense, i.e. it's a raw pcap or pcap-ng capture file, not some nice human-readable printed output.</p><p>You don't want Wireshark for this, you want TShark (which, unlike Wireshark, is intended to write dissected packets to the standard output), as the answers say.</p></div><div id="comment-5813-info" class="comment-info"><span class="comment-age">(22 Aug '11, 17:26)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5800" class="comment-tools"></div><div class="clear"></div><div id="comment-5800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5801"></span>

<div id="answer-container-5801" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5801-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can also use <a href="http://www.wireshark.org/docs/man-pages/tshark.html">TShark</a>. This command line tool is shipped together with Wireshark.<br />
<br />
Start with tshark -D to get an overview of the available interfaces.<br />
<br />
Capture 100 packets:<br />
tshark -i &lt;interface&gt; -c 100 -w 100packets.pcap<br />
<br />
Multiple files and switch to a new file every n seconds or every n kilobytes (there is no option to switch to a new file every 100 packets).<br />
Switch to a new file every 100 kilobytes:<br />
$ tshark -i 3 -b filesize:100 -w mf1.pcap<br />
<br />
Switch to new file every 60 seconds:<br />
$ tshark -i 3 -b duration:60 -w mf2.pcap<br />
<br />
Switch to a new file every 100 kilobytes and stop capturing after 20 files:<br />
$ tshark -i 3 -b filesize:100 -a files:20 -w mf3.pcap<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '11, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p>joke<br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-5801" class="comments-container"></div><div id="comment-tools-5801" class="comment-tools"></div><div class="clear"></div><div id="comment-5801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5803"></span>

<div id="answer-container-5803" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5803-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Actually, you <strong>should</strong> use tshark for this. Like so:</p><pre><code>tshark -i &lt;interface&gt; -c 100 -T fields -e eth.src</code></pre><p>which spits out the mac source list on standard out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '11, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></br></p></div></div><div id="comments-container-5803" class="comments-container"><span id="5811"></span><div id="comment-5811" class="comment"><div id="post-5811-score" class="comment-score"></div><div class="comment-text"><p>But specifying the "<code>wireshark -c 100 -k -Q -w -</code>" command shouldn't cause Wireshark to crash, right? When I tried it with SVN 38675 on Windows XP SP3, that's exactly what happened. Does Wireshark really support "-w -" on Windows? If so, then I guess there's a functional bug here; if not, then I guess there's a documentation bug.</p></div><div id="comment-5811-info" class="comment-info"><span class="comment-age">(22 Aug '11, 16:30)</span> cmaynard ♦♦</div></div><span id="5812"></span><div id="comment-5812" class="comment"><div id="post-5812-score" class="comment-score"></div><div class="comment-text"><p>If it truly crashes, that's a functional bug.</p><p>I tried it with SVN 38652 on OS X, and it popped up a complaint that "-" isn't a regular file (even though I'd redirected the standard output to a file), but spewed out a ton of "poll(2) failed due to: Bad file descriptor" complaints.</p><p>"-w -" should only work if the standard output is redirected to a file; it should fail otherwise. The person who asked the question apparently thought it'd write parsed output to the standard output; it will, of course, do no such thing.</p></div><div id="comment-5812-info" class="comment-info"><span class="comment-age">(22 Aug '11, 17:24)</span> Guy Harris ♦♦</div></div><span id="5814"></span><div id="comment-5814" class="comment"><div id="post-5814-score" class="comment-score"></div><div class="comment-text"><p>True. It's definitely a functional bug. I guess my question is whether there's also a documentation bug, but it wouldn't appear so. Anyway, I opened <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6256">bug 6256</a> for the crash.</p></div><div id="comment-5814-info" class="comment-info"><span class="comment-age">(22 Aug '11, 17:58)</span> cmaynard ♦♦</div></div><span id="5833"></span><div id="comment-5833" class="comment"><div id="post-5833-score" class="comment-score"></div><div class="comment-text"><p>We've fixed the crash.</p><p>However, it's not clear that -Q is a useful option, as per all the notes above that TShark is the right program to use here and that Wireshark won't do what you want. Unless somebody can come up with a case where -Q is useful - i.e., where it's useful to have the GUI running while the capture is in progress, but not when the capture stops - we're probably going to eliminate it.</p></div><div id="comment-5833-info" class="comment-info"><span class="comment-age">(23 Aug '11, 20:02)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5803" class="comment-tools"></div><div class="clear"></div><div id="comment-5803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

