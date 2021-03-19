+++
type = "question"
title = "Convert .txt into .pcap format"
description = '''I have the following from a cisco packet capture as a large text file.  00000000: A1B2C3D4 00020004 00000000 00000000 !2CT .... .... ....  00000010: 000005EE 0000000C 53F608E8 00074B1B ...n .... Sv.h ..K.  00000020: 000000C4 000000C4 450000C4 10160000 ...D ...D E..D ....  I see that there needs to b...'''
date = "2014-08-21T12:28:00Z"
lastmod = "2014-08-25T13:43:00Z"
weight = 35658
keywords = [ "convert", ".txt", ".pcap" ]
aliases = [ "/questions/35658" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Convert .txt into .pcap format](/questions/35658/convert-txt-into-pcap-format)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35658-score" class="post-score" title="current number of votes">0</div><span id="post-35658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following from a cisco packet capture as a large text file.</p><pre><code>00000000:  A1B2C3D4 00020004 00000000 00000000    !2CT .... .... .... 
00000010:  000005EE 0000000C 53F608E8 00074B1B    ...n .... Sv.h ..K. 
00000020:  000000C4 000000C4 450000C4 10160000    ...D ...D E..D ....</code></pre><p>I see that there needs to be spaces between every hex set of characters like this for it to be recognized by wireshark.</p><pre><code>00000000:  A1 B2 C3 D4 00 02 00 04 00 00 00 00 00 00 00 00    !2CT .... .... .... 
00000010:  00 00 05 EE 00 00 00 0C 53 F6 08 E8 00 07 4B 1B    ...n .... Sv.h ..K. 
00000020:  00 00 00 C4 00 00 00 C4 45 00 00 C4 10 16 00 00    ...D ...D E..D ....</code></pre><p>I tested using text2pcap but it wont convert it correctly. The file is huge.</p><p>What do you recommend?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-.txt" rel="tag" title="see questions tagged &#39;.txt&#39;">.txt</span> <span class="post-tag tag-link-.pcap" rel="tag" title="see questions tagged &#39;.pcap&#39;">.pcap</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '14, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/3191f2398bee0a48ad39485442c9ee15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jerryroy1&#39;s gravatar image" /><p><span>jerryroy1</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jerryroy1 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Aug '14, 12:29</strong> </span></p></div></div><div id="comments-container-35658" class="comments-container"></div><div id="comment-tools-35658" class="comment-tools"></div><div class="clear"></div><div id="comment-35658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="35681"></span>

<div id="answer-container-35681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35681-score" class="post-score" title="current number of votes">1</div><span id="post-35681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll probably have to write a small script to insert the space characters, or change the text2pcap code for your needs. It doesn't look complicated, should not be more than half an hour of coding (but I have to admit I'm not famous for getting code effort estimates right :-)).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '14, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35681" class="comments-container"></div><div id="comment-tools-35681" class="comment-tools"></div><div class="clear"></div><div id="comment-35681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35727"></span>

<div id="answer-container-35727" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35727-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35727-score" class="post-score" title="current number of votes">1</div><span id="post-35727-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm sure this can be made more efficient by all of you scripting gurus out there (you know who you are), but here's one solution that seems to work by using <a href="http://linux.die.net/man/1/sed"><code>sed</code></a> and <a href="http://linux.die.net/man/1/xxd"><code>xxd</code></a> to convert the data back to a binary pcap file without the need for <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html"><code>text2pcap</code></a>, which probably wouldn't work anyway because the data looks like it's from a raw libpcap file, and not simply packet data which <code>text2pcap</code> expects:</p><pre><code>sed &#39;s/^[0-9:]*//&#39; file.txt | sed &#39;s/^  //g&#39; | sed &#39;s/    .*$//g&#39; | xxd -r -p &gt; file.pcap</code></pre><p>The <code>A1B2C3D4</code> pretty much gives it away as the magic number of a <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">libpcap file</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '14, 13:43</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '14, 19:27</strong> </span></p></div></div><div id="comments-container-35727" class="comments-container"></div><div id="comment-tools-35727" class="comment-tools"></div><div class="clear"></div><div id="comment-35727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

