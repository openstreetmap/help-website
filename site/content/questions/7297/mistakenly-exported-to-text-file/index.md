+++
type = "question"
title = "Mistakenly exported to text file"
description = '''Hi guys, I was running a capture and instead of saving the pcap, I exported it to text, now I can&#x27;t open it in Wireshark. I tried using text2pcap and importing it back into Wireshark using various options (oct,dec,hex), but it doesn&#x27;t show properly. I am using windows.'''
date = "2011-11-08T15:25:00Z"
lastmod = "2011-11-08T21:51:00Z"
weight = 7297
keywords = [ "text2pcap", "text" ]
aliases = [ "/questions/7297" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mistakenly exported to text file](/questions/7297/mistakenly-exported-to-text-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7297-score" class="post-score" title="current number of votes">0</div><span id="post-7297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I was running a capture and instead of saving the pcap, I exported it to text, now I can't open it in Wireshark. I tried using text2pcap and importing it back into Wireshark using various options (oct,dec,hex), but it doesn't show properly.</p><p>I am using windows.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text2pcap" rel="tag" title="see questions tagged &#39;text2pcap&#39;">text2pcap</span> <span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '11, 15:25</strong></p><img src="https://secure.gravatar.com/avatar/58d8501fd270237dbbffbc19407f4090?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="WatchFan&#39;s gravatar image" /><p><span>WatchFan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="WatchFan has no accepted answers">0%</span></p></div></div><div id="comments-container-7297" class="comments-container"><span id="7304"></span><div id="comment-7304" class="comment"><div id="post-7304-score" class="comment-score"></div><div class="comment-text"><p>Can you post one or two packets from your text file into your original question or as a new comment? I'd like to see what the output looks like.</p></div><div id="comment-7304-info" class="comment-info"><span class="comment-age">(08 Nov '11, 18:27)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="7306"></span><div id="comment-7306" class="comment"><div id="post-7306-score" class="comment-score"></div><div class="comment-text"><p>Managed to open it with 010 editor. 5gb maxed out most other ones.</p><p>Seems to be a size limitation on the number of characters.</p><p>No. Time Source Destination Protocol Length Info 1 0.000000 192.168.x.x 192.168.x.x SIP 534 Request: SUBSCRIBE sip:<span class="__cf_email__" data-cfemail="ce9883e09ba0a7ba9697948efff7fce0fff8f6e0b6e0b6fbfef8fe">[email protected]</span>;transport=udp, in-dialog</p><p>Frame 1: 534 bytes on wire (4272 bits), 534 bytes captured (4272 bits) Arrival Time: Nov 4, 2011 22:23:34.993951000 AUS Eastern Daylight Time Epoch Time: 1320405814.993951000 seconds</p></div><div id="comment-7306-info" class="comment-info"><span class="comment-age">(08 Nov '11, 20:05)</span> <span class="comment-user userinfo">WatchFan</span></div></div></div><div id="comment-tools-7297" class="comment-tools"></div><div class="clear"></div><div id="comment-7297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7310"></span>

<div id="answer-container-7310" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7310-score" class="post-score" title="current number of votes">0</div><span id="post-7310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The conversion is possible only if you used File/Export/File ... menu with "Packet Bytes" checkbox marked. otherwise only few bytes of each packet would present in the text file, which makes them useless of course.</p><p>The text2pcap utility will only convert raw frames of data, but unfortunately your text file is full of dissected information. And what's more sad, it has reassembled frames (and, possibly some other conversions, like HTTP de-chunking, GZIP de-compression) mixed with the original bytes from the wire.</p><p>However if you'd manage to strip all this information, leaving only frame data, e.g.</p><pre><code>0000  00 11 22 33 44 55 00 11 22 33 44 55 08 00 45 00   ..^...........E.
0010  00 a1 37 22 00 00 01 11 d0 1b c0 a8 01 6c ef ff   ..7&quot;.........l..
0020  ff fa cb 1f 07 6c 00 8d d4 4f 4d 2d 53 45 41 52   .....l...OM-SEAR
0030  43 48 20 2a 20 48 54 54 50 2f 31 2e 31 0d 0a 48   CH * HTTP/1.1..H
0040  6f 73 74 3a 32 33 39 2e 32 35 35 2e 32 35 35 2e   ost:239.255.255.
0050  32 35 30 3a 31 39 30 30 0d 0a 53 54 3a 75 72 6e   250:1900..ST:urn
0060  3a 73 63 68 65 6d 61 73 2d 75 70 6e 70 2d 6f 72   :schemas-upnp-or
0070  67 3a 64 65 76 69 63 65 3a 49 6e 74 65 72 6e 65   g:device:Interne
0080  74 47 61 74 65 77 61 79 44 65 76 69 63 65 3a 31   tGatewayDevice:1
0090  0d 0a 4d 61 6e 3a 22 73 73 64 70 3a 64 69 73 63   ..Man:&quot;ssdp:disc
00a0  6f 76 65 72 22 0d 0a 4d 58 3a 33 0d 0a 0d 0a      over&quot;..MX:3....

0000  00 11 22 33 44 55 00 11 22 33 44 55 08 00 45 00   ........kS....E.
0010  00 2b d7 fa 40 00 33 06 ea bb 95 05 2d fd c0 a8   [email protected]
0020  01 6c a8 1b fa 29 85 b8 9a e7 f3 53 a8 10 50 18   .l...).....S..P.
0030  00 7e 41 ef 00 00 69 fb 20                        .~A...i.

...</code></pre><p>then result would be convertable and openable in wireshark as well any other .pcap reading program.</p><p>I'm not sure of handful tools to automate that process in Windows, you should try installing Cygwin - GNU awk + sed will do text transformations just fine. May be it is just simplier to install testbed and capture data once more.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 21:09</strong></p><img src="https://secure.gravatar.com/avatar/35d96b8e73e6deb4e332d076fd3269b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShomeaX&#39;s gravatar image" /><p><span>ShomeaX</span><br />
<span class="score" title="73 reputation points">73</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShomeaX has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '11, 21:11</strong> </span></p></div></div><div id="comments-container-7310" class="comments-container"><span id="7313"></span><div id="comment-7313" class="comment"><div id="post-7313-score" class="comment-score"></div><div class="comment-text"><p>I will give them a go. Any in Linux that would be better? I could copy the file across if need be.</p><p>Replicating this on a testbed is a difficult one, as this is to catch an error that occurs every two weeks that makes the SIP phones drop out. (an even we are trying to make sure doesn't happen again)</p></div><div id="comment-7313-info" class="comment-info"><span class="comment-age">(08 Nov '11, 21:20)</span> <span class="comment-user userinfo">WatchFan</span></div></div><span id="7316"></span><div id="comment-7316" class="comment"><div id="post-7316-score" class="comment-score"></div><div class="comment-text"><p>well, gawk is Linux utility actually, cygwin is just it's Windows port. basically it's just a matter of writting the script, you can use your favourite tool, Perl, Python, even Wscript will do just fine. unfortunately, googling around does not show up ready made script, probably because your issue is not very usual, so you'd have to write it on your own or may be throw some bucks @ freelance.com ;)</p></div><div id="comment-7316-info" class="comment-info"><span class="comment-age">(08 Nov '11, 21:51)</span> <span class="comment-user userinfo">ShomeaX</span></div></div></div><div id="comment-tools-7310" class="comment-tools"></div><div class="clear"></div><div id="comment-7310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

