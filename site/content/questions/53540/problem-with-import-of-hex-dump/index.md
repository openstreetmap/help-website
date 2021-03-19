+++
type = "question"
title = "Problem with  import of Hex Dump!"
description = '''Hi, I hope there is someone, that can answer my question/ problem, and sorry if my English isn&#x27;t the best. First I would like to describe what I want to do: I want to capture packets/ protocols, but with the addition of an imported packet/ protocol that should show up in the captured packets. The pa...'''
date = "2016-06-17T11:34:00Z"
lastmod = "2016-06-18T10:32:00Z"
weight = 53540
keywords = [ "import", "hex", "dump", "packet" ]
aliases = [ "/questions/53540" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with import of Hex Dump!](/questions/53540/problem-with-import-of-hex-dump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53540-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53540-score" class="post-score" title="current number of votes">0</div><span id="post-53540-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I hope there is someone, that can answer my question/ problem, and sorry if my English isn't the best.</p><p>First I would like to describe what I want to do: I want to capture packets/ protocols, but with the addition of an imported packet/ protocol that should show up in the captured packets. The package I want to add is special: I want it to have a string for example "12345" in the payload or in the protocol headers [using ASCII to translate it] and to be able to find the packet under: String, "12345", Packet Bytes.</p><p>Now the problems: I don't get the import from Hex Dump right whatever I try, the program always complains about errors/ mistakes, or just doesn't find the string "12345" when I want to find the packet. When importing I never change anything in the import menu, should I maybe change something there, for example other headers, instead of "no dummy header"? Or am I doing the package/ packet itself wrong? I already tried many different combinations of numbers, maybe I miss something important? I would be really glad if someone could help me out about the packet itself (the numbers and stuff). Maybe someone could explain it for me/ give me an answer for an example: 991199</p><p>If I wanted this sting to show up in the payload/ headers as described before, how would the packet lock like? What is important?</p><p>I would appretiate help a lot!</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-hex" rel="tag" title="see questions tagged &#39;hex&#39;">hex</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '16, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/40b6eacb78f0e3377d6f3d4a8803da1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maximal99334&#39;s gravatar image" /><p><span>Maximal99334</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maximal99334 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '16, 10:49</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-53540" class="comments-container"></div><div id="comment-tools-53540" class="comment-tools"></div><div class="clear"></div><div id="comment-53540-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53544"></span>

<div id="answer-container-53544" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53544-score" class="post-score" title="current number of votes">1</div><span id="post-53544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First things first, your hex dump file must match the format as described in the <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html">text2pcap</a> manual page.</p><p>So lets test this, lets try an import.</p><p>Put this in a text file:</p><pre><code>0000 31 32 33 34 35 12345</code></pre><p>Go to Wireshark, select import from hex dump. Select this file you just saved, select UDP and fill in both ports, eg. '1000'. Then click import. Now you should see the packet you're looking for in Wireshark.</p><p>Export this packet dissection (via the file menu) to a plain text file and select as packet format only 'Bytes'.</p><p>This file you can import from the hex dump again, without the need to add a dummy header any more, it's a complete packet now. So this file can be inserted into your other file before you import that.</p><p>PS: This assumes you're talking about Ethernet packets, but I hope my guess is right.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '16, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53544" class="comments-container"><span id="53550"></span><div id="comment-53550" class="comment"><div id="post-53550-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Jaap, but it still doesn't work :(</p><p>Let me explain where I still have problems:</p><p>I did everything as described by you. I imported with UDP 1000 and below I filled 1000 as well. Before the packet dissection export this was my packet: 0000 31 32 33 34 35 12345</p><p>I did the packet dissection export with these steps: -file menu -packet dissection export -as plain text -then I just selected Packet Bytes in the Packet Format Box, but didn't change anything else -then I chose the original file and saved it on it (I did overwrite it)</p><p>Is that correct?</p><p>Then the text file looked like this:</p><pre><code>      1 0.000000       1.1.1.1               2.2.2.2               UDP      60     1000 → 1000  Len=5
Frame 1: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
Ethernet II, Src: Send_00 (20:53:45:4e:44:00), Dst: Receive_00 (20:52:45:43:56:00)
Internet Protocol Version 4, Src: 1.1.1.1, Dst: 2.2.2.2
User Datagram Protocol, Src Port: 1000 (1000), Dst Port: 1000 (1000)
Data (5 bytes)
0000  20 52 45 43 56 00 20 53 45 4e 44 00 08 00 45 00    RECV. SEND...E.
0010  00 21 12 34 00 00 ff 11 a3 92 01 01 01 01 02 02   .!.4............
0020  02 02 03 e8 03 e8 00 0d 58 98 31 32 33 34 35 00   ........X.12345.
0030  00 00 00 00 00 00 00 00 00 00 00 00               ............</code></pre><p>Then I imported that file from hex dump without choosing a dummy header this time, as you said.</p><p>But when I want to find the string 12345 in "find packet", with the search options (Packet Bytes, narrow and wide, string, 12345) it still doesn't work and wireshark says: "Search reached the end. Continuing from beginning".</p><p>What is the problem?</p><p>And when I click on "Start capture Packets", it still doesn't work and wireshark says, that it couln#t find that string in the core files/ packet files, bytes.</p><p>I hope you can help me (or someone else that is online).</p></div><div id="comment-53550-info" class="comment-info"><span class="comment-age">(18 Jun '16, 03:22)</span> <span class="comment-user userinfo">Maximal99334</span></div></div><span id="53551"></span><div id="comment-53551" class="comment"><div id="post-53551-score" class="comment-score"></div><div class="comment-text"><p>Oh and my text documents that I use are type .txt and are created by PSPad (if that matters).</p><p>And what exactly did you mean with: "So this file can be inserted into your other file before you import that."</p><p>Oh and what may be important as well, is that I want to use a string that consists of 6 numbers, like for example 991199.</p><p>I really hope that these infos in addition to the ones in my comment above help you, help me ;)</p></div><div id="comment-53551-info" class="comment-info"><span class="comment-age">(18 Jun '16, 03:52)</span> <span class="comment-user userinfo">Maximal99334</span></div></div><span id="53552"></span><div id="comment-53552" class="comment"><div id="post-53552-score" class="comment-score"></div><div class="comment-text"><p>One additional question:</p><p>How can I include the packet to show up in the capture of the communication protocols, if I start capturing protocols. Because right now I have the feeling that the packet doesn't show up in the caputured packets/ protocols.</p><p>I would be thankful for a fast answer, it is really important!</p></div><div id="comment-53552-info" class="comment-info"><span class="comment-age">(18 Jun '16, 06:20)</span> <span class="comment-user userinfo">Maximal99334</span></div></div><span id="53555"></span><div id="comment-53555" class="comment"><div id="post-53555-score" class="comment-score"></div><div class="comment-text"><p>Oh okay, I was under the impression what wanted to add your special packets <em>after</em> the capture was done. Now I understand you want to do that while the capture is happening?</p><p>If so have a look at the <a href="https://wiki.wireshark.org/Tools">Tools wiki page</a>, like <a href="http://packeth.sourceforge.net/packeth/Home.html">PackETH</a>, or <a href="http://ostinato.org">Ostinato</a></p></div><div id="comment-53555-info" class="comment-info"><span class="comment-age">(18 Jun '16, 10:32)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-53544" class="comment-tools"></div><div class="clear"></div><div id="comment-53544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

