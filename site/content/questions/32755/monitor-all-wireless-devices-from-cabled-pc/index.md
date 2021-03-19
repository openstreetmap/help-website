+++
type = "question"
title = "Monitor all wireless devices from cabled PC"
description = '''Hi All, I have a PC running Linux Mint 16 that connects to my Virgin Media supper &quot;hub&quot; via Ethernet cable -  I have Wire shark installed and run gksudo wireshark via the command line to access the gui. on the network are other devises all connected to the hub via WiFi... I would like to be able to ...'''
date = "2014-05-13T04:55:00Z"
lastmod = "2014-05-14T00:54:00Z"
weight = 32755
keywords = [ "noob", "wireshark" ]
aliases = [ "/questions/32755" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor all wireless devices from cabled PC](/questions/32755/monitor-all-wireless-devices-from-cabled-pc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32755-score" class="post-score" title="current number of votes">0</div><span id="post-32755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have a PC running Linux Mint 16 that connects to my Virgin Media supper "hub" via Ethernet cable - I have Wire shark installed and run gksudo wireshark via the command line to access the gui.</p><p>on the network are other devises all connected to the hub via WiFi...</p><p>I would like to be able to monitor my phone - Samsung S3 - to see what emails/websites and any thing else it looks at.</p><p>Is this set up possible to work?</p><p>I'm very new to the world of Linux -</p><p>Is there s a step by step guide for noobs?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-noob" rel="tag" title="see questions tagged &#39;noob&#39;">noob</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '14, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/656dea592f414d22f7e9960ca4a3fda0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HexHunt&#39;s gravatar image" /><p><span>HexHunt</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HexHunt has no accepted answers">0%</span></p></div></div><div id="comments-container-32755" class="comments-container"></div><div id="comment-tools-32755" class="comment-tools"></div><div class="clear"></div><div id="comment-32755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32769"></span>

<div id="answer-container-32769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32769-score" class="post-score" title="current number of votes">0</div><span id="post-32769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You say "hub" but it sounds more like you're describing a "router". Can you confirm the model number for this device? The difference between these two terms is very important for what you're trying to do.</p><p>If it is a typical wireless router, then no as it is right now you can't monitor everything the S3 is doing because the S3's traffic will go from the router to the Internet, and the router has no reason to send that traffic toward your wired computer.</p><p>If you want to capture the traffic from the S3, there are a few things you can do. One is to run wireshark on something that is connecting to your network via Wifi, and monitor all the radio messages on that network (including those of the S3). Another way is to connect to an <em>actual</em> hub that the S3's traffic is passing through, or a switch with "port mirroring" or "SPAN" configured to forward all the S3's traffic out to an interface that you are connected to and running wireshark off of.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '14, 15:29</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-32769" class="comments-container"><span id="32780"></span><div id="comment-32780" class="comment"><div id="post-32780-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Its the Virgin Media "Super Hub" called so as its a all in one - <a href="http://help.virginmedia.com/system/selfservice.controller?CMD=VIEW_ARTICLE&amp;ARTICLE_ID=3859&amp;CURRENT_CMD=SEARCH&amp;CONFIGURATION=1001&amp;PARTITION_ID=1&amp;USERTYPE=1&amp;LANGUAGE=en&amp;COUNTY=us&amp;VM_CUSTOMER_TYPE=Cable">http://help.virginmedia.com/system/selfservice.controller?CMD=VIEW_ARTICLE&amp;ARTICLE_ID=3859&amp;CURRENT_CMD=SEARCH&amp;CONFIGURATION=1001&amp;PARTITION_ID=1&amp;USERTYPE=1&amp;LANGUAGE=en&amp;COUNTY=us&amp;VM_CUSTOMER_TYPE=Cable</a> I believe the the model number is Netgear VMDG480</p><p>I'm a bit of a noob as i have been working with Windows for all of my life but only in the last month or so moved to Linux-</p><p>I'm looking for a easy set up where my pc connects to the hub via a Ethernet cabal and can see all the traffic from the S3. (the PC has NOT got a wireless card in it.)</p><p>I've looked long and hard at versus tutorials on how to set up Wire-shark and and they all seem to assume you know everything ells.... and this is where i fall down... I'm looking for a simple set up that may return packets that are easy to understand...</p><p>Thanks,</p></div><div id="comment-32780-info" class="comment-info"><span class="comment-age">(14 May '14, 00:54)</span> <span class="comment-user userinfo">HexHunt</span></div></div></div><div id="comment-tools-32769" class="comment-tools"></div><div class="clear"></div><div id="comment-32769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

