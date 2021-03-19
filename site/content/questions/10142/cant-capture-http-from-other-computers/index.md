+++
type = "question"
title = "Can&#x27;t Capture HTTP from other computers"
description = '''I have my PC with wireshark on it, and my laptop (the target) connected via ethernet to a dumb hub, which in turn is connected to my XFINITY router. The hub is a true dumb hub, and I also used a small network tap and got the same results, so the hub is not the problem. I can surf the internet from m...'''
date = "2012-04-13T18:19:00Z"
lastmod = "2012-04-15T00:43:00Z"
weight = 10142
keywords = [ "ssdp", "http", "cant" ]
aliases = [ "/questions/10142" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't Capture HTTP from other computers](/questions/10142/cant-capture-http-from-other-computers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10142-score" class="post-score" title="current number of votes">0</div><span id="post-10142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have my PC with wireshark on it, and my laptop (the target) connected via ethernet to a dumb hub, which in turn is connected to my XFINITY router.</p><p>The hub is a true dumb hub, and I also used a small network tap and got the same results, so the hub is not the problem.</p><p>I can surf the internet from my PC and from my laptop.</p><p>When I surf from my PC which has Wireshark I can capture everything as normal. But when I surf from my laptop with Wireshark running on my PC, Wireshark doesn't get any HTTP packets, instead I get a bunch of 'SSDP' packets.</p><p>What is the problem?</p><p>EDIT: extra details: I have promiscuous mode enabled on Wireshark; The only card availible to the PC is "SiS NIC SISNIC Microsoft's Packet Scheduler"; This PC is pretty old, about 2006; I tried disabling the PC's firewall and virus scanner to no avail; I have the router's firewall on low security.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssdp" rel="tag" title="see questions tagged &#39;ssdp&#39;">ssdp</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-cant" rel="tag" title="see questions tagged &#39;cant&#39;">cant</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '12, 18:19</strong></p><img src="https://secure.gravatar.com/avatar/c3aa4e90f7bb89581b0c505311da089d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnsands&#39;s gravatar image" /><p><span>johnsands</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnsands has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Apr '12, 21:40</strong> </span></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-10142" class="comments-container"><span id="10150"></span><div id="comment-10150" class="comment"><div id="post-10150-score" class="comment-score"></div><div class="comment-text"><p>Should this setup work, or am I making a basic mistake? Has anyone else experienced this issue?</p><p>I made a diagram of my setup so it is easier to understand, I would really appreciate any help:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Untitled_1.jpg" alt="alt text" /></p></div><div id="comment-10150-info" class="comment-info"><span class="comment-age">(14 Apr '12, 16:30)</span> <span class="comment-user userinfo">johnsands</span></div></div></div><div id="comment-tools-10142" class="comment-tools"></div><div class="clear"></div><div id="comment-10142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10158"></span>

<div id="answer-container-10158" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10158-score" class="post-score" title="current number of votes">0</div><span id="post-10158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The most common problem in this scenario is that most "dumb hubs" nowadays are really switches or at least a switching hub (a 10 Mbit/s hub and a 100 Mbit/s hub, connected through a 2-port switch). What speed are all devices connected with? If the speeds are different, please try to set all devices to the same speed. See also: <a href="http://wiki.wireshark.org/HubReference">http://wiki.wireshark.org/HubReference</a></p><p>OK, if the hub really is a dumb hub (meaning, the packets indeed get sent to all attached devices), then the problem lies on the capturing system. What happens when you surf from your PC and use wirehark on your laptop?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '12, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></img></div></div><div id="comments-container-10158" class="comments-container"></div><div id="comment-tools-10158" class="comment-tools"></div><div class="clear"></div><div id="comment-10158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

