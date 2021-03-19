+++
type = "question"
title = "Custom Stop Recording Trigger"
description = '''hello i want a custom trigger set on a value changes from one value to another in same position in data to stop recording.. is it possible and if so how? thank you'''
date = "2015-03-26T06:00:00Z"
lastmod = "2015-03-26T07:37:00Z"
weight = 40888
keywords = [ "trigger" ]
aliases = [ "/questions/40888" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Stop Recording Trigger](/questions/40888/custom-stop-recording-trigger)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40888-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello</p><p>i want a custom trigger set on a value changes from one value to another in same position in data to stop recording.. is it possible and if so how?</p><p>thank you</p></div><div id="question-tags" class="tags-container tags">trigger</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '15, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/b16481f6bdf27742efdda0c16f177b8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YaronS&#39;s gravatar image" /><p>YaronS<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YaronS has no accepted answers">0%</span></p></div></div><div id="comments-container-40888" class="comments-container"><span id="40893"></span><div id="comment-40893" class="comment"><div id="post-40893-score" class="comment-score"></div><div class="comment-text"><p>Can you be a bit more specific about what you're trying to do? Also, what platform is this for, and what version of Wireshark are you using?</p></div><div id="comment-40893-info" class="comment-info"><span class="comment-age">(26 Mar '15, 07:12)</span> cmaynard ♦♦</div></div><span id="40894"></span><div id="comment-40894" class="comment"><div id="post-40894-score" class="comment-score"></div><div class="comment-text"><p>hello.. i wish to analyze a frame of data that being sent in a protocol (Profinet) and i want to catch the moment i have an error (that i can see when data changes to a certain value). Wireshark version 1.12.3, windows 7. i hope that is specified enough.. thanks</p></div><div id="comment-40894-info" class="comment-info"><span class="comment-age">(26 Mar '15, 07:15)</span> YaronS</div></div></div><div id="comment-tools-40888" class="comment-tools"></div><div class="clear"></div><div id="comment-40888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="40895"></span>

<div id="answer-container-40895" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40895-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong><em>If</em></strong> you are able to construct a capture filter for the value at the applicable field/offset location you are interested in, since you are using Windows and a new enough version of Wireshark, you <em>may</em> be able to make use of the <a href="https://wiki.wireshark.org/Tools?action=AttachFile&amp;do=view&amp;target=dumpcap.bat"><code>dumpcap.bat</code></a> file I wrote. It is available for download on the Wireshark wiki's <a href="https://wiki.wireshark.org/Tools">Tools</a> page.</p><p>In its simplest configuration to meet your needs, you would run it in <em>"Dumcpap+Event"</em> mode, specifying a general capture filter of packets you wish to capture along with an <em>"Event"</em> capture filter, which would be your very specific filter for the value at the offset you're looking for. Upon matching that specific filter, capturing would be terminated, optionally after some additional delay so that you could, if you wanted to, continue to capture some traffic for a specified time duration following the event of interest.</p><p>The batch file can also configure <code>dumpcap.exe</code> for autostop and/or ringbuffer settings, and with the help of the <a href="https://code.google.com/p/mailsend/downloads/detail?name=mailsend1.17b14.exe"><code>mailsend.exe</code></a> utility, you can even get an e-mail notification of the event when it occurs, which can be handy, especially if the event in question is quite rare.</p><p>For help with writing capture filters, refer to the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">pcap-filter man page</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '15, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-40895" class="comments-container"><span id="40896"></span><div id="comment-40896" class="comment"><div id="post-40896-score" class="comment-score"></div><div class="comment-text"><p>Hello cmaynard thanks for the answer i will try to do that.. however when i run the dumpcap file i will choose option 5 to set the filter however i do not see any option for stopping the recording when i get wanted value with the filter.. as i never used the dumpcap file i appreciate some help.. thank you yaron</p></div><div id="comment-40896-info" class="comment-info"><span class="comment-age">(26 Mar '15, 08:06)</span> YaronS</div></div><span id="40897"></span><div id="comment-40897" class="comment"><div id="post-40897-score" class="comment-score"></div><div class="comment-text"><p>As I explained, you will need to set the Dumpcap Mode to <em>"Dumpcap+Event"</em>. This is option #2. Once you do that, you will see the <code>CAPTURE EVENT OPTIONS</code> section.</p></div><div id="comment-40897-info" class="comment-info"><span class="comment-age">(26 Mar '15, 08:11)</span> cmaynard ♦♦</div></div><span id="40901"></span><div id="comment-40901" class="comment"><div id="post-40901-score" class="comment-score"></div><div class="comment-text"><p>thank you now i see it.. i see there is also an option for trigger there.. maybe that will be good as well.. will try.. by the way where the file recorded being saved? thanks again Yaron</p></div><div id="comment-40901-info" class="comment-info"><span class="comment-age">(26 Mar '15, 08:24)</span> YaronS</div></div><span id="40903"></span><div id="comment-40903" class="comment"><div id="post-40903-score" class="comment-score">1</div><div class="comment-text"><p>Trigger Mode is probably not what you want. In Trigger Mode, capturing isn't started UNTIL the event of interest occurs. Unfortunately, this means that the resulting capture file won't actually contain the packets leading up to the event, nor the event itself. <em>Maybe</em> this mode has some useful application, but none for me personally.</p></div><div id="comment-40903-info" class="comment-info"><span class="comment-age">(26 Mar '15, 08:28)</span> cmaynard ♦♦</div></div><span id="40905"></span><div id="comment-40905" class="comment"><div id="post-40905-score" class="comment-score"></div><div class="comment-text"><p><em>where the file recorded being saved?</em></p><p>You specify the capture file and path in option #4, e.g.:</p><pre><code>C:\path\to\captures\file</code></pre><p>No need to add the .pcap or .pcapng extension as the batch file will auto-append the correct extension based on the format selected (option #9).</p><p>If you don't specify a capture file, then <code>dumpcap</code> will write to a temporary file located in your <code>Temp</code> directory. You can run "<code>echo %TEMP%</code>" to find the location. You will also be able to see the location and temporary file name when you start capturing, as it will be displayed by the batch file, i.e.:</p><pre><code>Capturing on &#39;Some Interface&#39;
File: C:\Users\YaronS\AppData\Local\Temp\wireshark_pcapng_Some_Interface_20150326120000_123456</code></pre></div><div id="comment-40905-info" class="comment-info"><span class="comment-age">(26 Mar '15, 08:51)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-40895" class="comment-tools"></div><div class="clear"></div><div id="comment-40895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40889"></span>

<div id="answer-container-40889" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40889-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's nothing available really apart from parsing the output of tshark and then killing the capture process.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '15, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40889" class="comments-container"><span id="40891"></span><div id="comment-40891" class="comment"><div id="post-40891-score" class="comment-score"></div><div class="comment-text"><p>hello grahamb thank you for the quick reply do you mean that i need to edit what the tshark is following on and when he sees it to kill the process? how do i edit the tshark output? with lua? or somthing else? Yaron</p></div><div id="comment-40891-info" class="comment-info"><span class="comment-age">(26 Mar '15, 07:05)</span> YaronS</div></div></div><div id="comment-tools-40889" class="comment-tools"></div><div class="clear"></div><div id="comment-40889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

