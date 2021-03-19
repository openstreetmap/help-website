+++
type = "question"
title = "How capture in tshark, time of the visit url, who looks at a specific url ...."
description = ''' As in the main WINDOW set to display the time of the visit URL column? If the server with installed tshark, people connected on the vpn, then how to display the information in capture list of the program, who looks at a specific url? And how to display the user agent(what browser) url viewed in the...'''
date = "2017-01-07T19:08:00Z"
lastmod = "2017-01-09T23:53:00Z"
weight = 58586
keywords = [ "url", "column", "tshark" ]
aliases = [ "/questions/58586" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How capture in tshark, time of the visit url, who looks at a specific url ....](/questions/58586/how-capture-in-tshark-time-of-the-visit-url-who-looks-at-a-specific-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58586-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><ol><li>As in the main WINDOW set to display the time of the visit URL column?</li><li>If the server with installed tshark, people connected on the vpn, then how to display the information in capture list of the program, who looks at a specific url?</li><li>And how to display the user agent(what browser) url viewed in the log of the capture list of the program?</li><li>If possible, how to display URLs of images, videos, banners and so on in capture list. That is all that load a page of the website or application?</li></ol></div><div id="question-tags" class="tags-container tags">url column tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '17, 19:08</strong></p><img src="https://secure.gravatar.com/avatar/ebef6356dd73fc6e18fa2c3340d7fd31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Saldor&#39;s gravatar image" /><p>Saldor<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Saldor has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jan '17, 04:26</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-58586" class="comments-container"><span id="58619"></span><div id="comment-58619" class="comment"><div id="post-58619-score" class="comment-score"></div><div class="comment-text"><p>I would like to clarify that I use tshark on Ubuntu, after you enter the above commands, that is what appeared.</p><pre><code>tshark -2 -q -ta -T fields -E separator=, -E quote=d -E header=y -Y http.request.method -e frame.number -e _ws.col.Time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e http.user_agent -e _ws.col.Info -i _interface_number_ frame.number,_ws.col.Time,ip.src,ip.dst,tcp.srcport,tcp.dstport,http.user_agent,_ws.col.Info
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on &#39;_interface_number_&#39;
tshark: The capture session could not be initiated (No such device exists).
Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified.</code></pre></div><div id="comment-58619-info" class="comment-info"><span class="comment-age">(09 Jan '17, 20:16)</span> Saldor</div></div><span id="58621"></span><div id="comment-58621" class="comment"><div id="post-58621-score" class="comment-score"></div><div class="comment-text"><p>When i run list of commands, without -i _interface_number. i get this messeage:</p><pre><code> tshark -2 -q -ta -T fields -E separator=, -E quote=d -E header=y -Y http.request.method -e frame.number -e _ws.col.Time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e http.user_agent -e _ws.col.Info frame.number,_ws.col.Time,ip.src,ip.dst,tcp.srcport,tcp.dstport,http.user_agent, _ws.col.Info
Running as user &quot;root&quot; and group &quot;root&quot;. This could be dangerous.
Capturing on &#39;venet0&#39;</code></pre><p>And then nothing happens.</p></div><div id="comment-58621-info" class="comment-info"><span class="comment-age">(09 Jan '17, 22:24)</span> Saldor</div></div><span id="58622"></span><div id="comment-58622" class="comment"><div id="post-58622-score" class="comment-score"></div><div class="comment-text"><p>I adapted this from a command to extract the data from a pcap file. I've certainly made one mistake as I don't think you can specify the -2 parameter on a live capture. Let me have a think and I'll get back to you.</p><p>PS: The following should work for a captured file:</p><p><code>tshark -2 -q -ta -T fields -E separator=, -E quote=d -E header=y -Y http.request.method -e frame.number -e _ws.col.Time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e http.user_agent -e _ws.col.Info -r _file_name/file_path_</code></p></div><div id="comment-58622-info" class="comment-info"><span class="comment-age">(09 Jan '17, 23:30)</span> PaulOfford</div></div><span id="58624"></span><div id="comment-58624" class="comment"><div id="post-58624-score" class="comment-score"></div><div class="comment-text"><p>@Saldor: Your answers has been converted to a comments as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-58624-info" class="comment-info"><span class="comment-age">(09 Jan '17, 23:37)</span> Jaap ♦</div></div></div><div id="comment-tools-58586" class="comment-tools"></div><div class="clear"></div><div id="comment-58586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58611"></span>

<div id="answer-container-58611" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58611-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If I understand the question correctly, you need a command like this:</p><p><code>"c:\Program Files\Wireshark\tshark" -2 -q -ta -T fields -E separator=, -E quote=d -E header=y -Y http.request.method -e frame.number -e _ws.col.Time -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e http.user_agent -e _ws.col.Info -i _interface_number_</code></p><p>The interface number will be the one that shows the data flowing inside the VPN tunnel. This won't work for websites accessed using SSL.</p><p>Having said all of the above, it would be far easier to capture and analyse the activity using the web access log. If you are monitoring access to a Microsoft IIS web server you can read the log files into Wireshark using a free tool called TribeLab Workbench - see <a href="https://youtu.be/wHKocRR-reE">https://youtu.be/wHKocRR-reE</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '17, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '17, 05:11</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58611" class="comments-container"></div><div id="comment-tools-58611" class="comment-tools"></div><div class="clear"></div><div id="comment-58611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58625"></span>

<div id="answer-container-58625" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58625-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Saldor,</p><p>Sorry about the mistake. I don't have Ubuntu but the following works on my Centos 7 machine:</p><pre><code>tshark -q -ta -T fields -E separator=, -E quote=d -E header=y -Y http.request.method -e col.Time -e http.user_agent -e col.Info -i _interface_number_</code></pre><p>My Centos machine is running a rather old release of tshark (1.10.14) and at some point the names of the time and Info columns were changed I think. Try the above and we'll tweak the column labels if necessary.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '17, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '17, 23:54</p></div></div><div id="comments-container-58625" class="comments-container"></div><div id="comment-tools-58625" class="comment-tools"></div><div class="clear"></div><div id="comment-58625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

