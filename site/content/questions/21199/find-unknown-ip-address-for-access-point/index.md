+++
type = "question"
title = "Find unknown IP address for Access Point"
description = '''I have a BelAir 100 Access Point that I set a static IP on and I think I typed it incorrect and now I can&#x27;t log into it. There is no way that I know of to factory reset it. I have tried wireshark and and all I get are some bogus packets when it boots, I think it looks for a proprietary controller on...'''
date = "2013-05-16T22:00:00Z"
lastmod = "2014-03-07T01:09:00Z"
weight = 21199
keywords = [ "ipdiscovery", "unknownipaddress" ]
aliases = [ "/questions/21199" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Find unknown IP address for Access Point](/questions/21199/find-unknown-ip-address-for-access-point)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21199-score" class="post-score" title="current number of votes">0</div><span id="post-21199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a BelAir 100 Access Point that I set a static IP on and I think I typed it incorrect and now I can't log into it. There is no way that I know of to factory reset it. I have tried wireshark and and all I get are some bogus packets when it boots, I think it looks for a proprietary controller on boot up, then it is silent. I can use a wifi device to try to connect to it and I see the DHCP requests come through but no hint as to what IP addess it is set to. Is there a way to make it report to the network what IP address it is set at? I do get the MAC address from the bogus packets.</p><p>Thanks for any help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipdiscovery" rel="tag" title="see questions tagged &#39;ipdiscovery&#39;">ipdiscovery</span> <span class="post-tag tag-link-unknownipaddress" rel="tag" title="see questions tagged &#39;unknownipaddress&#39;">unknownipaddress</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '13, 22:00</strong></p><img src="https://secure.gravatar.com/avatar/0a095f587cc7884054c4edac3d197786?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Pando&#39;s gravatar image" /><p><span>Andy Pando</span><br />
<span class="score" title="12 reputation points">12</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Pando has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Mar '14, 18:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-21199" class="comments-container"><span id="21217"></span><div id="comment-21217" class="comment"><div id="post-21217-score" class="comment-score"></div><div class="comment-text"><p>can you post that capture file somewhere?</p></div><div id="comment-21217-info" class="comment-info"><span class="comment-age">(17 May '13, 03:58)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21199" class="comment-tools"></div><div class="clear"></div><div id="comment-21199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30524"></span>

<div id="answer-container-30524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30524-score" class="post-score" title="current number of votes">0</div><span id="post-30524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you know the subnet, for instance, 192.168.1.x, then you can plug into The device and use nmap to scan the subnet using CIDR as 192.168.1.0/24. This will tell you the devices on the subnet with their mac addresses and IP addresses.</p><p>Using only wireshark, since you know the mac address, you can use a display Filter like eth.addr eq 11:22:33:44:55:66 to only look at traffic to and from you to that device. If the device is set to dhcp instead of static IP it maybe trying to find a dhcp server to get an ip from for itself, which Is what it sounds like from your description.</p><p>Normally a master reset on the device will take it back to factory default ip for setup.</p><p>Im assuming your connected with an ethernet cable and not wireless for configuration.</p><p>Hope this is helpful John</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '14, 01:09</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-30524" class="comments-container"></div><div id="comment-tools-30524" class="comment-tools"></div><div class="clear"></div><div id="comment-30524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

