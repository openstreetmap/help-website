+++
type = "question"
title = "Capture Appliance"
description = '''We have a long term application performance problem. We need to get a packet capture of when the application misbehaves. Pretty standard stuff. Due to a lot of factors, we anticipate running the capture continously for a few months. (We don&#x27;t need to store this stuff more than 4 days). Running windo...'''
date = "2015-12-22T13:20:00Z"
lastmod = "2016-01-06T06:20:00Z"
weight = 48675
keywords = [ "capture", "appliance", "ringbuffer", "remote-capture" ]
aliases = [ "/questions/48675" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Capture Appliance](/questions/48675/capture-appliance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48675-score" class="post-score" title="current number of votes">0</div><span id="post-48675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a long term application performance problem. We need to get a packet capture of when the application misbehaves. Pretty standard stuff. Due to a lot of factors, we anticipate running the capture continously for a few months. (We don't need to store this stuff more than 4 days).</p><p>Running windows boxes, with wireshark configured with a ring buffer usually gets the job done, but requires quite a bit of care and feeding. (checking it's running, didn't crash, windows didn't do a windows update, etc..)</p><p>Inexpensive being a relative term, are there any packet capture appliances that people have used with great success? We have about 10 devices, spread across 4 closets. (Some have one device we're interested in, most have two devices). We're only looking at 100Mbit copper connections, pretty low data rates.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-appliance" rel="tag" title="see questions tagged &#39;appliance&#39;">appliance</span> <span class="post-tag tag-link-ringbuffer" rel="tag" title="see questions tagged &#39;ringbuffer&#39;">ringbuffer</span> <span class="post-tag tag-link-remote-capture" rel="tag" title="see questions tagged &#39;remote-capture&#39;">remote-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '15, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/d87d2173daa97e7292d8c556d8fafb8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mpking&#39;s gravatar image" /><p><span>Mpking</span><br />
<span class="score" title="8 reputation points">8</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mpking has no accepted answers">0%</span></p></div></div><div id="comments-container-48675" class="comments-container"><span id="48847"></span><div id="comment-48847" class="comment"><div id="post-48847-score" class="comment-score"></div><div class="comment-text"><p>Christian_R, can you post that as an answer? That was exactly what I was looking for, and will mark it as the "answer" if you post it.</p></div><div id="comment-48847-info" class="comment-info"><span class="comment-age">(04 Jan '16, 10:24)</span> <span class="comment-user userinfo">Mpking</span></div></div><span id="48850"></span><div id="comment-48850" class="comment"><div id="post-48850-score" class="comment-score"></div><div class="comment-text"><p><span>@Mpking</span> : No problem. I have done it.</p></div><div id="comment-48850-info" class="comment-info"><span class="comment-age">(04 Jan '16, 10:45)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-48675" class="comment-tools"></div><div class="clear"></div><div id="comment-48675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48690"></span>

<div id="answer-container-48690" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48690-score" class="post-score" title="current number of votes">1</div><span id="post-48690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mpking has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I suggest you to have a look at this similar question: <a href="https://ask.wireshark.org/questions/47868/looking-on-recommendationsbest-practices-on-ws-deployment-at-large-data-centers?page=1&amp;focusedAnswerId=47877#47877">https://ask.wireshark.org/questions/47868/looking-on-recommendationsbest-practices-on-ws-deployment-at-large-data-centers?page=1&amp;focusedAnswerId=47877#47877</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '15, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-48690" class="comments-container"></div><div id="comment-tools-48690" class="comment-tools"></div><div class="clear"></div><div id="comment-48690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48681"></span>

<div id="answer-container-48681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48681-score" class="post-score" title="current number of votes">0</div><span id="post-48681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I suggest use of <a href="https://openwrt.org/">OpenWrt</a> here so often that I am afraid of getting a ban for that :-)</p><p>It is a linux distribution for devices with small flash memory, typically home routers, and if you choose a hardware which is equipped with USB ports, you can connect an external disk to it. OpenWrt <em>never</em> checks for updates or automatically reboots, so you may run tcpdump in circular mode forever on it (or at least until the disk gets worn).</p><p>I suppose you capture on monitoring ports of switches in your closets already now, so you do not need to push the captured traffic through the capturing box. If this <em>is</em> your intention, you would need a setup with independent network cards you could set up as a software bridge together, and the total volume of traffic may be important too, with regard to the available CPU power needed for the software bridging. Both these requirements would push you towards a PC hardware, i.e. losing the advantage of small mechanical footprint and power consumption, but keeping the software advantages of OpenWrt. Use of USB network adaptors is not a good idea for the purpose.</p><p>If we stay with the plastic boxes, by experience the weakest part of the chain are the external switching power adaptors, so you can feel safe during first year of operation if there is not above 30 °C in the closets and if you power the external disk by its own adaptor, not from the USB. You can extend that period by replacing the adaptors delivered with the router and disk by ones with 1.5 - 2 times higher current rating, as these won't run at their limit 24/7 and thus they will not kill themselves by heat production so quickly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '15, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48681" class="comments-container"><span id="48907"></span><div id="comment-48907" class="comment"><div id="post-48907-score" class="comment-score"></div><div class="comment-text"><p>Thanks, but I was looking for a more an off the shelf solution, as opposed to rolling my own hardware.</p></div><div id="comment-48907-info" class="comment-info"><span class="comment-age">(06 Jan '16, 06:20)</span> <span class="comment-user userinfo">Mpking</span></div></div></div><div id="comment-tools-48681" class="comment-tools"></div><div class="clear"></div><div id="comment-48681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

