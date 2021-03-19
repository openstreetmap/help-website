+++
type = "question"
title = "help identifying network issues"
description = '''I&#x27;ve been running into a bit of a wall as I am not a savvy wireshark user but this seems to be my next step to identify issues and was hoping someone might be able to point me in the right direction or take a look at my capture log and be able to see what the issue might be. Running a simple home ne...'''
date = "2016-08-31T16:58:00Z"
lastmod = "2016-08-31T16:58:00Z"
weight = 55256
keywords = [ "traffic-analysis" ]
aliases = [ "/questions/55256" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [help identifying network issues](/questions/55256/help-identifying-network-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55256-score" class="post-score" title="current number of votes">-1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been running into a bit of a wall as I am not a savvy wireshark user but this seems to be my next step to identify issues and was hoping someone might be able to point me in the right direction or take a look at my capture log and be able to see what the issue might be. Running a simple home network multiple times in an hour I will lose internet connectivity through my wired pc. At that point I can check my phone on the wifi and also will still be connected yet no internet pages will load. After 20 seconds or so my connection will come back and all works well. I can assume no faulty hardware due to both the modem and router being less than a month old. Any help would be appreciated. I saved a capture log and witnessed the issue occur and waited for connectivity to be restored and then stopped to save the log. <a href="https://drive.google.com/open?id=0B9evkOC7pgrRajJ0YTFFT1B4VlU">Capture log</a></p></div><div id="question-tags" class="tags-container tags">traffic-analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '16, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/8b93563470867af48f09673c6432ee18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="godsplague&#39;s gravatar image" /><p>godsplague<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="godsplague has no accepted answers">0%</span></p></div></div><div id="comments-container-55256" class="comments-container"><span id="55263"></span><div id="comment-55263" class="comment"><div id="post-55263-score" class="comment-score"></div><div class="comment-text"><p>If you have already checked that all cables between the router and modem, and between the modem and the wall outlet are OK, I'd suggest you to do the following on your PC:</p><ul><li>take a <code>traceroute</code> (<code>tracert</code> on Windows) of 8.8.8.8 (Google's easy-to-remember DNS server IP address)</li><li>start capturing (do not use any capture filter as not only icmp is interesting)</li><li>start a continuous ping of the first IP on the hop list, which should be your home router's IP</li><li>in another window, start a continuous ping of the second IP on the hop list, which should be your ISP's first router</li><li>if your modem is configured to routing mode as well (i.e. the wireless router does not get its WAN side IP address from the ISP but from the modem which itself gets it from the ISP), start a continuous ping to the third IP on the list as well, as in such case, that one is the first one to belong to the ISP</li><li>in yet another window, start a continuous ping of 8.8.8.8.</li></ul><p>Then continue your normal use of the PC until the issue occurs and disappears, and then stop and save the capture and stop all three pings.</p><p>This should show whether the issue exists between your PC and the home router, or between the home router and the ISP (or modem), or between the router and the modem, or between the ISP's first router and the rest of the world.</p><p>Maybe even before doing that, you should have a look at eventual logs of your router and modem whether you can find something interesting there.</p></div><div id="comment-55263-info" class="comment-info"><span class="comment-age">(01 Sep '16, 04:10)</span> sindy</div></div><span id="55276"></span><div id="comment-55276" class="comment"><div id="post-55276-score" class="comment-score"></div><div class="comment-text"><p>Thank you Sindy, I will try this as soon as I have some time to sit down and watch it</p></div><div id="comment-55276-info" class="comment-info"><span class="comment-age">(01 Sep '16, 17:02)</span> godsplague</div></div></div><div id="comment-tools-55256" class="comment-tools"></div><div class="clear"></div><div id="comment-55256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

