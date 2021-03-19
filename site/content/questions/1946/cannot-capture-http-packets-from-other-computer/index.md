+++
type = "question"
title = "Cannot capture HTTP packets from other computer"
description = '''I have set up my network card into monitor mode and I have connected to my WPA2 encrypted network. I have another computer with a wireless network card that is also connected to the same network.  I want to capture HTTP data from that computer and everytime I load a webpage from that computer, my ot...'''
date = "2011-01-26T11:10:00Z"
lastmod = "2011-01-27T09:18:00Z"
weight = 1946
keywords = [ "http", "wpa2", "packet" ]
aliases = [ "/questions/1946" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture HTTP packets from other computer](/questions/1946/cannot-capture-http-packets-from-other-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1946-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1946-score" class="post-score" title="current number of votes">0</div><span id="post-1946-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have set up my network card into monitor mode and I have connected to my WPA2 encrypted network. I have another computer with a wireless network card that is also connected to the same network.</p><p>I want to capture HTTP data from that computer and everytime I load a webpage from that computer, my other computer with Wireshark on seems to capture some data, but the source is my Netgear router and the protocol is LLC.</p><p>I once succeeded to capture the data from my other computer, but I fail now. I have also set the WPA-PSK decryption keys in Wireshark.</p><p>What am I doing wrong?</p><p>EDIT: I can mention that if I turn of the encryption, it all works perfect, but when encryption is enabled, then it cannot read the data.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-wpa2" rel="tag" title="see questions tagged &#39;wpa2&#39;">wpa2</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '11, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/b40d415d5a5ed5142e38ad841b2e176a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rox&#39;s gravatar image" /><p><span>Rox</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rox has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Jan '11, 11:20</strong> </span></p></div></div><div id="comments-container-1946" class="comments-container"></div><div id="comment-tools-1946" class="comment-tools"></div><div class="clear"></div><div id="comment-1946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1947"></span>

<div id="answer-container-1947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1947-score" class="post-score" title="current number of votes">0</div><span id="post-1947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>WPA decryption only works if you captured all the way from the start of the WPA session. So you need to start the capture first and then turn on the wireless adapter on the system you would like to monitor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '11, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1947" class="comments-container"></div><div id="comment-tools-1947" class="comment-tools"></div><div class="clear"></div><div id="comment-1947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1973"></span>

<div id="answer-container-1973" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1973-score" class="post-score" title="current number of votes">0</div><span id="post-1973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>But if I turn off the wireless adapter, then Wireshark cannot find the interface to make the capture on, right?</p><p>This is the procedure:</p><p>I have two computers, let´s call them "A" and "B". Computer "A" is the one with Wireshark installed.</p><p>Borth A and B are disconnected from the network. On A, I run "ifconfig wlan0 up" and then start the capturing session on Wireshark. Then I connect A to the network.</p><p>So far B is still disconnected from the network, so when A is capturing on the network, I connect B to it.</p><p>In wireshark, I can see two EAPOL packets when connecting computer B ("msg 1/4" and "msg 3/4", where are "msg 2/4" and "msg 4/4"???), but nothing is decrypted. I have added a decryption key in Wireshark.</p><p>What is wrong?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '11, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/b40d415d5a5ed5142e38ad841b2e176a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rox&#39;s gravatar image" /><p><span>Rox</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rox has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jan '11, 09:36</strong> </span></p></div></div><div id="comments-container-1973" class="comments-container"></div><div id="comment-tools-1973" class="comment-tools"></div><div class="clear"></div><div id="comment-1973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

