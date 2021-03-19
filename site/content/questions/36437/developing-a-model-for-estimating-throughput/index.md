+++
type = "question"
title = "Developing a model for estimating throughput"
description = '''Hi all, Before I explan my query I&#x27;d just like to put it out there that I&#x27;m new to Wireshark and protocol analysis. I&#x27;m trying to go about learing this the right way, but am not quite there yet, hence my query. So here goes... We, a large multinational company, are looking to make use of the Microso...'''
date = "2014-09-18T15:46:00Z"
lastmod = "2014-09-18T15:46:00Z"
weight = 36437
keywords = [ "model", "wireshark" ]
aliases = [ "/questions/36437" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Developing a model for estimating throughput](/questions/36437/developing-a-model-for-estimating-throughput)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36437-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>Before I explan my query I'd just like to put it out there that I'm new to Wireshark and protocol analysis. I'm trying to go about learing this the right way, but am not quite there yet, hence my query.</p><p>So here goes...</p><p>We, a large multinational company, are looking to make use of the Microsoft hosted OneDrive for Business application. Now I know not everyone is a fan of Microsoft, that's a different story. What I'm trying to do is to establish a model that estimates the impact the use of this application will have on various WAN circuits around the world. So what do I know? I know that there are an awful lot of varibales that you need to consider, so many that some might suggest it's impossible to estimate (client, network, Internet, server, etc). I've tried explaining this to the business but they want something, even if it only provides a worst case scenario. What I also know is a little about the OneDrive application, it uses TCP (SSL), for every file a user attempts to upload it creates a separate TCP/SSL socket, that application won't attempt to sync a single file that is larger than 3Mb, any file larger than this is chunked up. And the application doesn't permit more than five concurrent uploads...</p><p>So how do you estimate this? I thought about calculating the time it would take to transmit over both wired and wireless lans, the Internet, etc. I've got some basic captures and from what I can see the server is responding well (reasonably large window size), the client too seems to perform well.</p><p>I'm trying to devise a calculation for doing this. I've pulled together many captures but am struggling somewhat on this. Can anybody suggest a way in Wireshark I can pull together what is an average throughput? I guess a lot of this will depend on the number of users uploading at any given time. I've also recently got a licemse for the Steelhead Analyser software. I can see on avergae that clients generally seem to have an average throughput in Mb not Mbps of 1.4Mb. No more.</p><p>If I used the example of a 20Mbps circuit and 10 users can anybody suggest how you would estimate the time it would take to transfer this data, high-level only of course. Just think I might be missing something obvious in my current calculations as my estimates v actuals are way out.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">model wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '14, 15:46</strong></p><img src="https://secure.gravatar.com/avatar/aa9cb2452882c53ab182eb819d527ca6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcarr&#39;s gravatar image" /><p>dcarr<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcarr has no accepted answers">0%</span></p></div></div><div id="comments-container-36437" class="comments-container"></div><div id="comment-tools-36437" class="comment-tools"></div><div class="clear"></div><div id="comment-36437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

