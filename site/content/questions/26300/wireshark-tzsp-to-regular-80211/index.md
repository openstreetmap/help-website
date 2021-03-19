+++
type = "question"
title = "Wireshark TZSP to regular 802.11 ?"
description = '''Hello, as you know , the captured files with TZSP is not usefull for Aircrack-NG. is there anyway to convert TZSP to something that Aircrack can use it. when i want use tzsp captured files in aircrack it give me this error This file is not a regular 802.11 (wireless) capture. Read 0 packets. No netw...'''
date = "2013-10-22T17:00:00Z"
lastmod = "2013-10-29T04:13:00Z"
weight = 26300
keywords = [ "tzsp", "wireshark" ]
aliases = [ "/questions/26300" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark TZSP to regular 802.11 ?](/questions/26300/wireshark-tzsp-to-regular-80211)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26300-score" class="post-score" title="current number of votes">0</div><span id="post-26300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, as you know , the captured files with TZSP is not usefull for Aircrack-NG. is there anyway to convert TZSP to something that Aircrack can use it.</p><p>when i want use tzsp captured files in aircrack it give me this error</p><p>This file is not a regular 802.11 (wireless) capture. Read 0 packets. No networks found, exiting.</p><p><a href="http://i.imgur.com/np3Au6E.png">http://i.imgur.com/np3Au6E.png</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tzsp" rel="tag" title="see questions tagged &#39;tzsp&#39;">tzsp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Oct '13, 17:00</strong></p><img src="https://secure.gravatar.com/avatar/cd9e8474468cd8179f094673d15473df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="itboys&#39;s gravatar image" /><p><span>itboys</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="itboys has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '13, 17:00</strong> </span></p></div></div><div id="comments-container-26300" class="comments-container"><span id="26302"></span><div id="comment-26302" class="comment"><div id="post-26302-score" class="comment-score"></div><div class="comment-text"><p>i found one tools</p><p><a href="http://code.google.com/p/tzsp2cap/">http://code.google.com/p/tzsp2cap/</a></p><p>but there is no file for download now!</p></div><div id="comment-26302-info" class="comment-info"><span class="comment-age">(22 Oct '13, 17:28)</span> <span class="comment-user userinfo">itboys</span></div></div></div><div id="comment-tools-26300" class="comment-tools"></div><div class="clear"></div><div id="comment-26300-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26479"></span>

<div id="answer-container-26479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26479-score" class="post-score" title="current number of votes">1</div><span id="post-26479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is there anyway to convert TZSP to something that Aircrack can use it.</p></blockquote><p>You can strip the unwanted headers (ethernet up to UDP) with bittwiste.</p><blockquote><p>bittwiste -I tzsp.pcap -O tzsp-stripped.pcap -D 0-4F</p></blockquote><p><strong>Hint 1:</strong> I'm not sure about the range 0-4F. If you are able to post a small pcap file with TZSP somewhere (google drive, dropbox, cloudshark.org), I'll check it.</p><p>The resulting file will only contain IEEE 802.11 frames, actually anything that was encapsulated in TZSP.</p><p><strong>Hint 2:</strong> There is no simple way to generate a radiotap header from the values of the TZSP header, so you'll probably loose that information!</p><p>bittwiste is part of the Bit-Twist tool package</p><blockquote><p><a href="http://bittwist.sourceforge.net/">http://bittwist.sourceforge.net/</a></p></blockquote><p>See also here:</p><p><a href="http://www.lovemytool.com/blog/2011/05/bittwiste-pcap-capture-file-editor-by-joke-snelders.html">http://www.lovemytool.com/blog/2011/05/bittwiste-pcap-capture-file-editor-by-joke-snelders.html</a></p><blockquote><p><a href="http://code.google.com/p/tzsp2cap/">http://code.google.com/p/tzsp2cap/</a><br />
but there is no file for download now!</p></blockquote><p>There is code. Please run these commands on a linux system</p><ul><li>git clone <a href="https://code.google.com/p/tzsp2cap/">https://code.google.com/p/tzsp2cap/</a></li><li>gcc -lpcap tzsp2cap.c -o tzsp2cap</li></ul><p><strong>Hint 3:</strong> A libpcap devel package needs to be installed on your linux system to be able to build the tool!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 09:17</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '13, 09:22</strong> </span></p></div></div><div id="comments-container-26479" class="comments-container"><span id="26495"></span><div id="comment-26495" class="comment"><div id="post-26495-score" class="comment-score"></div><div class="comment-text"><p>nice reply mate, yes tzsp2cap work fine.</p></div><div id="comment-26495-info" class="comment-info"><span class="comment-age">(28 Oct '13, 19:09)</span> <span class="comment-user userinfo">itboys</span></div></div><span id="26501"></span><div id="comment-26501" class="comment"><div id="post-26501-score" class="comment-score"></div><div class="comment-text"><p>Your "answer" has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-26501-info" class="comment-info"><span class="comment-age">(29 Oct '13, 02:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="26506"></span><div id="comment-26506" class="comment"><div id="post-26506-score" class="comment-score"></div><div class="comment-text"><blockquote><p>nice reply mate, yes tzsp2cap work fine.</p></blockquote><p>Yep. It does basically what I tried to describe with bittwiste (would work too), only the number of bytes I was using (4F) is wrong. According to the tool it's 3F. So, you would run bittwiste like this:</p><blockquote><p>bittwiste -I tzsp.pcap -O tzsp-stripped.pcap -D 0-3F</p></blockquote></div><div id="comment-26506-info" class="comment-info"><span class="comment-age">(29 Oct '13, 04:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-26479" class="comment-tools"></div><div class="clear"></div><div id="comment-26479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

