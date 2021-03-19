+++
type = "question"
title = "Monitoring a wireless network?"
description = '''To Whom It May Concern, I am trying to find a software that will allow me to &quot;snif&quot; my wireless network to monitor what my teenagers are doing on their laptops. Ideally, I want to download the software to my laptop and get updates when they log in (to include passwords). Would Wireshark do this or c...'''
date = "2011-03-29T12:56:00Z"
lastmod = "2011-03-30T05:05:00Z"
weight = 3209
keywords = [ "sniffer" ]
aliases = [ "/questions/3209" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Monitoring a wireless network?](/questions/3209/monitoring-a-wireless-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3209-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>To Whom It May Concern, I am trying to find a software that will allow me to "snif" my wireless network to monitor what my teenagers are doing on their laptops. Ideally, I want to download the software to my laptop and get updates when they log in (to include passwords). Would Wireshark do this or can anyone recommend another product that is relatively easy to do? Thank you in advance for your assistance.</p><p>R/S CBW</p></div><div id="question-tags" class="tags-container tags">sniffer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '11, 12:56</strong></p><img src="https://secure.gravatar.com/avatar/e29313ebf76c5cb482794be11a37bd85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ddweer&#39;s gravatar image" /><p>ddweer<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ddweer has no accepted answers">0%</span></p></div></div><div id="comments-container-3209" class="comments-container"></div><div id="comment-tools-3209" class="comment-tools"></div><div class="clear"></div><div id="comment-3209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3214"></span>

<div id="answer-container-3214" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3214-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I doubt Wireshark is the product for you even though it may be an option to capture what your teenagers are doing on the network. Keep in mind that you'll need to buy at least one AirPCAP USB WiFi adapter if you're about to capture WiFi running Wireshark on Windows.</p><p>I have no idea what kind of passwords you want to sniff (and why), but I guess you won't be able to see them in at least some if not most cases. Most logins teenagers do today will be web page logins and those are usually SSL encrypted which you can't break unless you are in possession of the private server key (which I doubt you are).</p><p>Maybe an alternative option (if you really have to spy on the network traffic) is to install a transparent HTTP proxy that is between your teenagers and the internet. It can be setup to intercept and forward any call to web servers while recording the URL and access time in the proxy logs. Those logs could then be inspected/analyzed by hand or log analyzer software.</p><p>Another software you might find usefull is Cain &amp; Abel, but it is to be considered a hacking tool (or, a "security" tool if you want to call it that :-)). It can capture and (often but not always) decrypt passwords on the fly, but it is a little complicated to handle since the GUI is an impressive example of being quite non-intuitive for some activities.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Mar '11, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3214" class="comments-container"></div><div id="comment-tools-3214" class="comment-tools"></div><div class="clear"></div><div id="comment-3214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3226"></span>

<div id="answer-container-3226" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3226-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'll add that you may wish to look at a different router. If you have the inclination I believe that you can do a lot of what you're looking for by using a router running dd-wrt. There is no, real, dummies guide for it and it can be very complicated. I'm running an Asus RT-N16 with dd-wrt and it has great logging capabilities. Jasper's suggestion of Cain&amp;Abel is great, however, as he mentions, setup is complicated. Good Luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '11, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p>GeonJay<br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span></p></div></div><div id="comments-container-3226" class="comments-container"></div><div id="comment-tools-3226" class="comment-tools"></div><div class="clear"></div><div id="comment-3226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

