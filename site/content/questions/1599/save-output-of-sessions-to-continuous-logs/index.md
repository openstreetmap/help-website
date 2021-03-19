+++
type = "question"
title = "Save output of sessions to continuous logs"
description = '''I want to capture everything from a mirrored port to my router. I want to be able to get captures in one hour increments continuously for four days then start wrapping these captures so the hard drive does not fill up. Is there a way to leave Wireshark running, then “cut pcap’s” every hour, then sta...'''
date = "2011-01-03T07:48:00Z"
lastmod = "2011-01-04T05:38:00Z"
weight = 1599
keywords = [ "save", "pcap", "file" ]
aliases = [ "/questions/1599" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Save output of sessions to continuous logs](/questions/1599/save-output-of-sessions-to-continuous-logs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture everything from a mirrored port to my router. I want to be able to get captures in one hour increments continuously for four days then start wrapping these captures so the hard drive does not fill up.</p><p>Is there a way to leave Wireshark running, then “cut pcap’s” every hour, then start wrapping these files after four days?</p></div><div id="question-tags" class="tags-container tags">save pcap file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '11, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/1ea09bab25129bf7cf8aa1272d48f02f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="georgeshark&#39;s gravatar image" /><p>georgeshark<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="georgeshark has no accepted answers">0%</span></p></div></div><div id="comments-container-1599" class="comments-container"></div><div id="comment-tools-1599" class="comment-tools"></div><div class="clear"></div><div id="comment-1599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="1602"></span>

<div id="answer-container-1602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1602-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A command I use very often is:</p><pre><code>dumpcap -i eth0 -w file.cap -b filesize:16384 -b files:1024</code></pre><p>This command will capture from interface <strong>eth0</strong> to a ring buffer of <strong>1024</strong> files of <strong>16MB</strong> size. The filenames will be <strong>file_NNNNN_YYYYMMDDHHMMSS.cap</strong>. After the 1024th file has been written, the 1st will be deleted and the 1025th will be created.</p><p>Of course you can change the parameters to your liking. If you do want one-hour files for 4 days, you can use:</p><pre><code>dumpcap -i eth0 -w file.cap -b duration:3600 -b files:96</code></pre><p>Of course you have no guarantee that your drive won't fill up, as you don't know how much data will be in each hour.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '11, 12:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1602" class="comments-container"><span id="1649"></span><div id="comment-1649" class="comment"><div id="post-1649-score" class="comment-score"></div><div class="comment-text"><p>I am using this: dumpcap -i 2 -w file.cap -b duration:3600 -b files:96 : and it works great. This is saving everything to the files.</p><p>Since I am using VoIP on the machine, is there a way to exclude RTP traffic from the file? I want to 'see' everything else, just not the RTP.</p><p>I tried using tshark with a !(RTP) but, with the -R you can't save it to and file AND exclude traffic. Can I do it using dumpcap?</p><p>Thanks again</p></div><div id="comment-1649-info" class="comment-info"><span class="comment-age">(06 Jan '11, 07:41)</span> georgeshark</div></div><span id="1651"></span><div id="comment-1651" class="comment"><div id="post-1651-score" class="comment-score"></div><div class="comment-text"><p>(I converted your answer to a comment to preserve the logical order of messages)</p><p>No, you can't use display filters with dumpcap as it does not do any dissection of packets. You can however use capture filters. So if you can make a capture filter that filters out RTP, then you're in business.</p><p>Does your voip traffic use speficic IP addresses to exclude? Or maybe it is in a separate vlan and you are capturen traffic on a tagged interface?</p></div><div id="comment-1651-info" class="comment-info"><span class="comment-age">(06 Jan '11, 09:17)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1602" class="comment-tools"></div><div class="clear"></div><div id="comment-1602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1612"></span>

<div id="answer-container-1612" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1612-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark, if you go to the Capture Options before starting your capture, you can do what you need Simply specify a folder and filename (which becomes the prefix for subsequent capture), check Use Multiple Files.Then check the box and fill-in Next File Every "1 hour" and check and fill-in Ring Buffer with "96" files. Note however that Wireshark will attempt to dissect the traffic it captures and consumes memory doing so.</p><p>So as has been pointed out by Sake and Bill, dumpcap is probably the best for continuous logging, as it does a raw capture and doesn't need to do any dissecting to build up state and consume memory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '11, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1612" class="comments-container"></div><div id="comment-tools-1612" class="comment-tools"></div><div class="clear"></div><div id="comment-1612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1601"></span>

<div id="answer-container-1601" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1601-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For continuous capturing, use dumpcap (the program used by wireshark and tshark to do the actual capture).</p><p>Also: see 'dumpcap -h' (or the dumpcap man page) for info on how to limit capture files to one hour and how to wrap the files after "n" files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '11, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-1601" class="comments-container"></div><div id="comment-tools-1601" class="comment-tools"></div><div class="clear"></div><div id="comment-1601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1616"></span>

<div id="answer-container-1616" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1616-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks all, these are great ways to do this..</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '11, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/1ea09bab25129bf7cf8aa1272d48f02f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="georgeshark&#39;s gravatar image" /><p>georgeshark<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="georgeshark has no accepted answers">0%</span></p></div></div><div id="comments-container-1616" class="comments-container"></div><div id="comment-tools-1616" class="comment-tools"></div><div class="clear"></div><div id="comment-1616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

