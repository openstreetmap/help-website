+++
type = "question"
title = "need help reading pcapng file"
description = '''EDIT 2 i can open.pcapng with notepad. some stuff is in plain english. i see it connecting to another website&#x27;s iis server. huh :( some weird charectors so i would guess thats the code. gonna try and see what else i can get from this stream capture. any thoughts appreciated.   EDIT: how can i view u...'''
date = "2012-12-03T16:00:00Z"
lastmod = "2012-12-10T01:43:00Z"
weight = 16516
keywords = [ "sort" ]
aliases = [ "/questions/16516" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [need help reading pcapng file](/questions/16516/need-help-reading-pcapng-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16516-score" class="post-score" title="current number of votes">0</div><span id="post-16516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>EDIT 2 i can open.pcapng with notepad. some stuff is in plain english. i see it connecting to another website's iis server. huh :( some weird charectors so i would guess thats the code. gonna try and see what else i can get from this stream capture. any thoughts appreciated.<br />
</p><p>EDIT: how can i view udp packets? i need to look at what commands are being run in java with a udp field i belive. looking to see what files are being transfered or what commands are being sent to my pc... i isolated the traffic, now i just want to read/translate the code inside.</p><p>i go to (what appears to be ) a regular company website with a link off <a href="http://google.com">google.com</a> and i see my ms sec essntials open up and clean up/quarantine a virus. its a java exploit:</p><p>trojan:JS/<a href="http://Redirector.LB">Redirector.LB</a></p><p>i captured 349 packets. all i did was start the capture, clicked the link, saw the ms security essential quarantine the exploit (Again) and stopped the capture</p><p>now i would like to find whats tripping the av software.</p><p>if i follow a tcp stream of the packets i got froom the server answering the pings, would that cause the exploit to be run again? as soon as i followed the stream, my ms security essentials opened again quarantining that exploit again. ever time i follow the stream i get the virus.</p><p>its showing an error on the tcp stream: could not open temp file C:\users\x\appdata\local\temp\follow_20121203192017_a04336: access is denied</p><p>is this normal when you foolow a tcp stream? is that file above the virus or the temp file of the wireshark capture? how can i find the file/virus from the wireshark capture?</p><p>thanks for the time. any help appreciated... Im sick of getting viruses.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sort" rel="tag" title="see questions tagged &#39;sort&#39;">sort</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '12, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/9fc3a6d60d019040bf0a2a71362ed36c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="networktec&#39;s gravatar image" /><p><span>networktec</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="networktec has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Dec '12, 01:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-16516" class="comments-container"></div><div id="comment-tools-16516" class="comment-tools"></div><div class="clear"></div><div id="comment-16516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16517"></span>

<div id="answer-container-16517" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16517-score" class="post-score" title="current number of votes">0</div><span id="post-16517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is this normal when you foolow a tcp stream? is that file above the virus or the temp file of the wireshark capture?</p></blockquote><p>That's a temp file, written by Wireshark, when you follow a TCP stream. It contains the payload data of the TCP connection. As the virus/trojan code is downloaded via the HTTP connection, wireshark writes the virus/trojan code into that temp file. Your AV scanner detects that write attempt and blocks the action, as it finds the virus/trojan code.</p><p>You could add an exception in your AV scanner for the path where Wireshark writes the temp file, <strong>if you really know what you are doing</strong> ;-). However, just writing the virus/trojan code in the temp file, does not pose any risk, as the virus/trojan code will not be executed.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '12, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-16517" class="comments-container"><span id="16738"></span><div id="comment-16738" class="comment"><div id="post-16738-score" class="comment-score"></div><div class="comment-text"><p>thanks.</p><p>1.) i see the stream opening up a connection to a different iis server so im guessing thats where its coming in from. wheres the temp file go? %temp%? i could add exception, but wouldnt the code self execute? if i have enough to trip the av software, that might let it install and delete file if thats in the programing. i was reading about using a debugger to slow down the program and see whats going on.any thoughts appreciated.</p><p>2.) i opened the pcapng with notepad. dont understand how to read stuff like: &lt;/script&gt; &lt;/body&gt; &lt;/html&gt;&lt;script&gt;try{n&amp;=window[\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\...NUL NUL ACK NUL NUL etc.</p><p>hTML code? just not sure what \\\ is?</p><p>its full of stuff like this. im guessing im looking for java code, just not sure what it looks like, etc.</p><p>then at end i see:</p><p>&lt;msgfmtrev&gt;3&lt;/msgfmtrev&gt; &lt;msgcontrev&gt;6&lt;/msgcontrev&gt; &lt;netstatus&gt;0&lt;/netstatus&gt; &lt;hmadevice&gt; &lt;devstatus&gt;0&lt;/devstatus&gt; &lt;macaddr&gt;xxxxxxxxxxxx&lt;/macaddr&gt; &lt;ipaddr&gt;xxx.xxx.1.xxx&lt;/ipaddr&gt; &lt;unitaddr&gt;00029583A9&lt;/unitaddr&gt; &lt;networkmaster&gt;Master&lt;/networkmaster&gt; &lt;devicetype&gt;2&lt;/devicetype&gt; &lt;settopnodeid&gt;1&lt;/settopnodeid&gt; &lt;netconnecttype&gt;1&lt;/netconnecttype&gt; &lt;mocanodeid&gt;0&lt;/mocanodeid&gt; &lt;mocaversion&gt;01.73&lt;/mocaversion&gt; &lt;hmaauth&gt;Yes&lt;/hmaauth&gt; &lt;hmacontsupport&gt;SDorHD&lt;/hmacontsupport&gt; &lt;numcontses&gt;0&lt;/numcontses&gt; &lt;hmastreamtypesupport&gt;MPEG2orMPEG4&lt;/hmastreamtypesupport&gt; &lt;/hmadevice&gt; &lt;/hmanetconfig&gt;</p><p>java code? weird. any thoughts appreciated.</p></div><div id="comment-16738-info" class="comment-info"><span class="comment-age">(09 Dec '12, 14:51)</span> <span class="comment-user userinfo">networktec</span></div></div></div><div id="comment-tools-16517" class="comment-tools"></div><div class="clear"></div><div id="comment-16517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16744"></span>

<div id="answer-container-16744" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16744-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16744-score" class="post-score" title="current number of votes">0</div><span id="post-16744-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://wiki.wireshark.org/Development/PcapNg">.pcapng</a> file is the file that Wireshark stores the network traffic captured from the interface, but it is not an executable file, nor is it (generally) human readable. One piece of software that can generate or display the contents of a pcapng file is called Wireshark.</p><p>If the capture file contains the download of some malware, it is possible that av software may trigger on the write (or read) of the file due to the av "recognising" a pattern of bytes that match an entry in the av database of malware.</p><p>I don't know of a way to encode data in a pcapng file that would cause a normal program that read it to misbehave (apart from crash), but I would think it possible that a malware program <strong>could</strong> use a pcapng file to hold data (or code) for it in the same way any other file could be used for the same purpose.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '12, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-16744" class="comments-container"></div><div id="comment-tools-16744" class="comment-tools"></div><div class="clear"></div><div id="comment-16744-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

