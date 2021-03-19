+++
type = "question"
title = "WLAN capturing"
description = '''Hello I&#x27;m not a computer nor a network specialist, but I can fly Airbuses :).  We are running a small privat house LAN with two WLAN access points, one of them is them modem. I have system administrator rights.  Even after changing the password, after a few days somebody is again in our WLAN, we sus...'''
date = "2012-03-03T21:43:00Z"
lastmod = "2012-03-06T17:22:00Z"
weight = 9337
keywords = [ "wlan", "capturing" ]
aliases = [ "/questions/9337" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [WLAN capturing](/questions/9337/wlan-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9337-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I'm not a computer nor a network specialist, but I can fly Airbuses :). We are running a small privat house LAN with two WLAN access points, one of them is them modem. I have system administrator rights. Even after changing the password, after a few days somebody is again in our WLAN, we suspect with a iPhone. We would like to see what traffic is going trough our Access Point. How to do that? If a specialist is able to help us, even at some cost, please contact [email protected]<a href="http://bluewin.ch">bluewin.ch</a> Martin</p></div><div id="question-tags" class="tags-container tags">wlan capturing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '12, 21:43</strong></p><img src="https://secure.gravatar.com/avatar/73cfaab42e0ee9f3342ecc0e9109696e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Martin%20Gautschi&#39;s gravatar image" /><p>Martin Gautschi<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Martin Gautschi has no accepted answers">0%</span></p></div></div><div id="comments-container-9337" class="comments-container"></div><div id="comment-tools-9337" class="comment-tools"></div><div class="clear"></div><div id="comment-9337-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9339"></span>

<div id="answer-container-9339" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9339-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all, when you say "password" do you mean the password that you use to log in to your modem/accesspoints? Or do you mean the WEP/WPA key?</p><p>I assume you mean the key used to encrypt the wireless traffic. When you configure a wireless key, make sure to use WPA2. WEP encryption can be cracked within a few minutes nowadays and also WPA is less secure than WPA2.</p><p>Now for capturing the traffic, have a look at the scenarios on the wiki:</p><ul><li><a href="http://wiki.wireshark.org/CaptureSetup">CaptureSetup</a>: How to setup your network to successfully capture packets</li><li><a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">CaptureSetup/Ethernet</a>: Discusses capturing on switched Ethernet networks</li><li><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">CaptureSetup/WLAN</a>: Frequently asked WLAN capture setup info</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '12, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9339" class="comments-container"></div><div id="comment-tools-9339" class="comment-tools"></div><div class="clear"></div><div id="comment-9339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9412"></span>

<div id="answer-container-9412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9412-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unfortunetly WLAN Capture is not possible under Windows. You can boot a live Linux (e.g. Linux Backtrack), put your wireless card in monitor mode and see, who is associated to your AP. it looks like this</p><p><img src="http://vpoint7.files.wordpress.com/2008/12/bt3-4.jpg" alt="http://vpoint7.files.wordpress.com/2008/12/bt3-4.jpg" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '12, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/c241cfce7680c690b68422163a98c0d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="contradictor_&#39;s gravatar image" /><p>contradictor_<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="contradictor_ has no accepted answers">0%</span></p></img></div></div><div id="comments-container-9412" class="comments-container"></div><div id="comment-tools-9412" class="comment-tools"></div><div class="clear"></div><div id="comment-9412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

