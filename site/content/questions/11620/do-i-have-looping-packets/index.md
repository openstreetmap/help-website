+++
type = "question"
title = "Do I have looping packets?"
description = '''I have an iSCSI performance problem. So I&#x27;m just going thru my checklist. One thing mentioned on page 336 is using IP ID to identify looping packets. So i did a tshark dump of the ip.id and created a Perl script to check for duplicates. Once I identified these I looked at the packets to see if Don&#x27;t...'''
date = "2012-06-04T07:32:00Z"
lastmod = "2012-06-04T08:12:00Z"
weight = 11620
keywords = [ "flags", "ip.id" ]
aliases = [ "/questions/11620" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Do I have looping packets?](/questions/11620/do-i-have-looping-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11620-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an iSCSI performance problem. So I'm just going thru my checklist. One thing mentioned on page 336 is using IP ID to identify looping packets. So i did a tshark dump of the <a href="http://ip.id">ip.id</a> and created a Perl script to check for duplicates. Once I identified these I looked at the packets to see if Don't Fragment is set. I found a case where I have duplicate IDs and the DF is set. See displayed frames 10 and 11 of the following trace. I have a DF bit flag set and from the same host I'm seeing the same IP ID. Note the time display is set to display seconds since beginning of capture. As a matter of fact all of the packets displayed here have the same IP ID. But many of them don't have the DF flag set. Please advise if I'm missing something. But this doesn't look right. <a href="http://cloudshark.org/captures/bfd12b3b02d9">http://cloudshark.org/captures/bfd12b3b02d9</a></p></div><div id="question-tags" class="tags-container tags">flags ip.id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '12, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/a472d068843eefd8a4ef69c4f94e4160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gipper&#39;s gravatar image" /><p>gipper<br />
<span class="score" title="30 reputation points">30</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gipper has no accepted answers">0%</span></p></div></div><div id="comments-container-11620" class="comments-container"></div><div id="comment-tools-11620" class="comment-tools"></div><div class="clear"></div><div id="comment-11620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11622"></span>

<div id="answer-container-11622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11622-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will see "looping" packets, if they are forwarded between systems (e.g. router) several times, due to a routing loop. In that case you'll see the same packet (same IP ID, same src/dst IP, same ports, same SEQ/ACK, same payload) with different src/dst MAC addresses (those of the routers forwarding the packets). So, just looking for the same IP ID does not help to detect "looping" packets, as long as you ignore the other parameters of the packets.</p><p>According to that definition of looping packets, there are only two matching pairs in your (stripped) capture file: Frame #1/#2 and #4/#5. Those are probaly just a (very fast) re-transmissions, or a problem during capturing the packets.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '12, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jun '12, 11:58</p></div></div><div id="comments-container-11622" class="comments-container"><span id="11623"></span><div id="comment-11623" class="comment"><div id="post-11623-score" class="comment-score"></div><div class="comment-text"><p>Sorry page 336 of Wireshark Network Analysis. Laura Chappel. So this IP ID which is a hex 4 digit number which can be up to 65,535 values to uniquely identify an IP packet could be the same number from the same host within 1.5 seconds would loop thru 64k values? That doesn't make sense.</p></div><div id="comment-11623-info" class="comment-info"><span class="comment-age">(04 Jun '12, 08:14)</span> gipper</div></div><span id="11625"></span><div id="comment-11625" class="comment"><div id="post-11625-score" class="comment-score">2</div><div class="comment-text"><p>see comment below (the one with the screenshot).</p></div><div id="comment-11625-info" class="comment-info"><span class="comment-age">(04 Jun '12, 08:36)</span> Kurt Knochner ♦</div></div><span id="11629"></span><div id="comment-11629" class="comment"><div id="post-11629-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt that makes perfect sense. Thanks for the help. I'm still trying to come up to speed on this.</p></div><div id="comment-11629-info" class="comment-info"><span class="comment-age">(04 Jun '12, 08:48)</span> gipper</div></div><span id="11630"></span><div id="comment-11630" class="comment"><div id="post-11630-score" class="comment-score"></div><div class="comment-text"><p>it makes perfect sense. Here is an IO graph based on traffic in an iSCSI network.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/screenshot-ipid-1a.jpg" alt="IP.ID wrap around" /></p><p>This is just 2,6 Mbit/s and you see a wrap around of the <a href="http://ip.id">ip.id</a> after ~ 15 seconds. So, multiply that throughput by 10 (26 Mbit/s) and you will have a wrap around after 1,5 seconds. The <a href="http://IP.ID">IP.ID</a> in the capture was increased in steps of 6!! in this sample (OS dependant).</p><p>Let's also calculate it:</p><blockquote><p><code>65535 * 800 * 8 = 419424000 Bit = 419 MBit</code></p></blockquote><p>800 is the arithmetic average of the packet size (please consider data + ACK + other).</p><p>That's the amount of data needed for a wrap around. Divide that by the number of seconds and you get the required throughput. 419 Mbit / 1,5 s = 279 Mbit/s. Not so uncommon in a iSCSI network. If you change the arithmetic average, the number will change! Some OS increase the value by 2,4 or 6. You will get an even faster wrap around.</p><p>Regards<br />
Kurt</p></div><div id="comment-11630-info" class="comment-info"><span class="comment-age">(04 Jun '12, 08:49)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-11622" class="comment-tools"></div><div class="clear"></div><div id="comment-11622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11621"></span>

<div id="answer-container-11621" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11621-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On the contrary - in my eyes and on a quick glance your trace does look quite normal (with big holes in it because of the filtering).</p><p>I have no idea why you think that looking for packets with the same IP ID on a general scope would help you tracking a loop problem (unless it happens on a really large scale, but then it'd be obvious). The IP ID is usually (which means, there are some OSes that do it differently, e.g. OpenBSD) incremented by 1 for each new IP packet, and it has a 16 bit range - meaning, that after getting to the number 65535 it will start again at 0 and count up again. So if you wait long enough (and believe me, when waiting on a busy iSCSI transfer with tons of data being transfered it doesn't take long) you'll see the same IP ID over and over again.</p><p>By the way, what "page 336" do you refer to? It's not much use to tell us a page number and not which book it is ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '12, 07:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></img></div></div><div id="comments-container-11621" class="comments-container"></div><div id="comment-tools-11621" class="comment-tools"></div><div class="clear"></div><div id="comment-11621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

