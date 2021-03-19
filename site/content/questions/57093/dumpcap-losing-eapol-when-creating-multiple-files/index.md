+++
type = "question"
title = "Dumpcap losing eapol when creating multiple files"
description = '''Hi,  I&#x27;m trying to use dumpcap to do long term captures on a wifi network.  Got everything setup right and it records perfectly for the files files with all data decrypted. when it reaches the 300meg mark and then creates the second file it loses the eapol handshake (or more like doesn&#x27;t remember it...'''
date = "2016-11-07T13:40:00Z"
lastmod = "2016-12-15T02:53:00Z"
weight = 57093
keywords = [ "eapol", "dumpcap" ]
aliases = [ "/questions/57093" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Dumpcap losing eapol when creating multiple files](/questions/57093/dumpcap-losing-eapol-when-creating-multiple-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57093-score" class="post-score" title="current number of votes">0</div><span id="post-57093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm trying to use dumpcap to do long term captures on a wifi network. Got everything setup right and it records perfectly for the files files with all data decrypted. when it reaches the 300meg mark and then creates the second file it loses the eapol handshake (or more like doesn't remember it), so the second file is just broadcast frames. is there anyway around this so that it keeps the eapol for all files or anything i can do to make this work?</p><p>Currently using the below command</p><p>dumpcap -i mon0 -a duration:30000 -b filesize:300535 -a files:32 -w \home\msriptide\test</p><p>Many thanks guys</p><p>Mark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '16, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/02ee5258c47902d7e590a0eea45d5d0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msriptide&#39;s gravatar image" /><p><span>msriptide</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msriptide has no accepted answers">0%</span></p></div></div><div id="comments-container-57093" class="comments-container"></div><div id="comment-tools-57093" class="comment-tools"></div><div class="clear"></div><div id="comment-57093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58134"></span>

<div id="answer-container-58134" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58134-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58134-score" class="post-score" title="current number of votes">0</div><span id="post-58134-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="msriptide has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><blockquote><p>second file is just broadcast frames</p></blockquote></blockquote><p>The presence or absence of EAPOL frames should have nothing to do with whether you are able to capture only broadcast frames or not.</p><p>Long term wireless captures like this are painful to work with, one of the reasons being exactly the issue you present.</p><p>A couple of options:</p><ol><li><p>Use wired traffic wherever possible. It's not that often we actually need decrypted wireless traces to troubleshoot a problem. Many times, wired traces will do. However, some problems certainly do need decrypted wireless traces. Usually this is related to subtle timing issues between wired and wireless networks, especially with power save behavior due to buffering. Many straight up wireless issues can be looked at with encrypted data - if the issue is 802.11 handling, encrypted data has little to do with this as probing, ACK mechanism, powersave handling, etc., are all in plain text.</p></li><li><p>If you really need the data, setup a second, sometimes a third, wireless capture of the system to reduce probability that packet loss from capture system will prevent proper analysis.<br />
</p></li><li><p>Setup a separate capture for EAPOL frames, separate from the main capture. Something like this on Windows or the equivalent in Linux or with Omnipeek (dumpcap would be fine too):</p></li></ol><p>C:\tmp&gt;windump -i 1 -s 1600 -w EAPOL -W 200 -C 200 ether proto 0x888e</p><p>This way, I can quickly see the EAPOLl frames from the system during the test process and determine if I have all four for decryption. If we don't get them all we can't decrypt, so that's where the duplicate mechanism comes into play: check there too.<br />
</p><ol><li>As <span><span>@Amato</span></span> indicates, strip out the fourway handshake appropriate for the period under review wherever you may have found it (e.g. export specified packet option) and then merge the traces. This usually works, though group keys can be a little tougher as a group rekey is usually encrypted so it may take some work to find them after decryption takes place.</li></ol><p>It's a lot of work to manage this slicing of traces and inserting packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '16, 02:53</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Dec '16, 02:55</strong> </span></p></div></div><div id="comments-container-58134" class="comments-container"></div><div id="comment-tools-58134" class="comment-tools"></div><div class="clear"></div><div id="comment-58134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58094"></span>

<div id="answer-container-58094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58094-score" class="post-score" title="current number of votes">0</div><span id="post-58094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could you use the mergecap function to combine the files?</p><p><a href="https://www.wireshark.org/docs/man-pages/mergecap.html">https://www.wireshark.org/docs/man-pages/mergecap.html</a></p><p>For example: mergecap -w c:\temp\mergedfile.pcap c:\temp\inout1.pcap c:\temp\input2.pcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '16, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-58094" class="comments-container"></div><div id="comment-tools-58094" class="comment-tools"></div><div class="clear"></div><div id="comment-58094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

