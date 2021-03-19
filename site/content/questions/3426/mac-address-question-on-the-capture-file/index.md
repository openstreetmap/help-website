+++
type = "question"
title = "MAC address Question on the capture file"
description = '''Hello. My professor gave us an homework about wireshark so i am kinda new to this application. I dowloaded the wireshark. My professor sent a .pcap (capture file) to answer the following questions on the homework. So my question is, how do you check the MAC address for the wireless network card in a...'''
date = "2011-04-10T12:36:00Z"
lastmod = "2011-04-10T23:14:00Z"
weight = 3426
keywords = [ "0201" ]
aliases = [ "/questions/3426" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [MAC address Question on the capture file](/questions/3426/mac-address-question-on-the-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3426-score" class="post-score" title="current number of votes">0</div><span id="post-3426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. My professor gave us an homework about wireshark so i am kinda new to this application. I dowloaded the wireshark. My professor sent a .pcap (capture file) to answer the following questions on the homework. So my question is, how do you check the MAC address for the wireless network card in an IP address on the .pcap (captured file) sent by my professor? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-0201" rel="tag" title="see questions tagged &#39;0201&#39;">0201</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '11, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/10384556eba509bd0867e78e9dd47fdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alvnfer&#39;s gravatar image" /><p><span>alvnfer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alvnfer has no accepted answers">0%</span></p></div></div><div id="comments-container-3426" class="comments-container"></div><div id="comment-tools-3426" class="comment-tools"></div><div class="clear"></div><div id="comment-3426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3430"></span>

<div id="answer-container-3430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3430-score" class="post-score" title="current number of votes">0</div><span id="post-3430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not exactly sure what your task actually is (maybe my english isn't good enough to understand it), but I'll try to give you some hints:</p><p>If you know the IP address and want to know which MAC address it was used by you can just filter on the ip address using <code>ip.addr==w.x.y.z</code> with w.x.y.z being the IPv4 address. Then you just open the ethernet layer in the decode pane to find everything you might need. Keep in mind that the MAC you'll find might not always be the one the IP is directly associated with, for example if the IP packet was captured coming from a router, but here you said it's coming from a wireless card so you should be fine.</p><p>If my answer isn't helping let us know, and maybe try to clarify the question like this:</p><ol><li>what do you know about the trace?</li><li>what are you supposed to find out?</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '11, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3430" class="comments-container"><span id="3433"></span><div id="comment-3433" class="comment"><div id="post-3433-score" class="comment-score"></div><div class="comment-text"><p>This is my first time using wireshark so i have low knowlegde of tracing.</p><p>I am looking for something like this "6E:51:F5:c1:11:00" which the MAC add on the capture i think.</p><p>This is the actual question: <strong>What is the MAC address for my wireless network card with an IP address of 879.125.8.3?</strong></p><p>I just do not understand what he meant for wireless network card. i cannot trace those</p></div><div id="comment-3433-info" class="comment-info"><span class="comment-age">(10 Apr '11, 17:03)</span> <span class="comment-user userinfo">alvnfer</span></div></div><span id="3436"></span><div id="comment-3436" class="comment"><div id="post-3436-score" class="comment-score"></div><div class="comment-text"><p>Uh, the IP address "879.125.8.3" is not exactly a valid IP, the first octet may not exceed 255. But anyway, if it were a valid IP you'd filter for "ip.src==879.125.8.3" by entering that into the filter bar right on top of the packet list. That will only give you packets comming from your professors IP (which happens to "live" on his wireless card). Look into one of the packets and write down the source MAC address as specified in the ethernet header.</p></div><div id="comment-3436-info" class="comment-info"><span class="comment-age">(10 Apr '11, 23:14)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-3430" class="comment-tools"></div><div class="clear"></div><div id="comment-3430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

