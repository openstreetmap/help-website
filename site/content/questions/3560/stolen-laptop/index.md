+++
type = "question"
title = "Stolen laptop"
description = '''Hey Guys Someone stole my wifes laptop, and it so happens theyre somewhere within range of my wireless Dlink router and are currently accessing internet off me... I was hoping to remote in and take a picture via the laptop camera though remoting seems to be disabled nor can i access anythign through...'''
date = "2011-04-18T07:21:00Z"
lastmod = "2011-04-20T11:09:00Z"
weight = 3560
keywords = [ "wireshark" ]
aliases = [ "/questions/3560" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Stolen laptop](/questions/3560/stolen-laptop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3560-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3560-score" class="post-score" title="current number of votes">0</div><span id="post-3560-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey Guys Someone stole my wifes laptop, and it so happens theyre somewhere within range of my wireless Dlink router and are currently accessing internet off me...</p><p>I was hoping to remote in and take a picture via the laptop camera though remoting seems to be disabled nor can i access anythign through teh UNC paths...</p><p>So my current plan is to see email addresses or facebook links of the theif so that i can send police his way...</p><p>Do you have any recommendations on how I can achieve this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/d1c2c219e2e2283730da40d666b707d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SKM&#39;s gravatar image" /><p><span>SKM</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SKM has no accepted answers">0%</span></p></div></div><div id="comments-container-3560" class="comments-container"></div><div id="comment-tools-3560" class="comment-tools"></div><div class="clear"></div><div id="comment-3560-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3561"></span>

<div id="answer-container-3561" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3561-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3561-score" class="post-score" title="current number of votes">1</div><span id="post-3561-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure they are in Range of your DLink Router? That would mean they're pretty close to your location since wireless ranges are very limited. How do you know they are close?</p><p>You can try to capture the wireless traffic if your network card is able to enter monitor mode (usually not possible on Windows unless you own an AirPCAP adapter). Otherwise you might try to capture the wired network going out to your provider, but that is usually difficult unless your router can mirror the data to a monitor port.</p><p>IF you can capture their data you can try to filter on HTTP traffic, and possibly identify communications containing web pages with personal information, but you'd need to be lucky to capture those. Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Apr '11, 07:29</strong> </span></p></div></div><div id="comments-container-3561" class="comments-container"><span id="3565"></span><div id="comment-3565" class="comment"><div id="post-3565-score" class="comment-score"></div><div class="comment-text"><p>I bought a DC to AC power converter for the car...plugged the router in, assumed the guy hadnt removed the wireless profile and thought if i can get the router close enough then the laptop should connect. Which it did a few houses down from mine, though today i checked DHCP clients on my router at home and it seems the laptop is able to connect from wherever it is. Ive pinged it and I get replies...</p><p>So as you say, they must be pretty close...really disappointing to know a neighbours broken into our place.</p><p>Thanks Jasper... I wonder if i can setup internet connection sharing on my PC ...have the wireless router receiving the signal run it through teh PC and then from PC to modem</p><p>Ill play around as youve suggested first. Thanks</p></div><div id="comment-3565-info" class="comment-info"><span class="comment-age">(18 Apr '11, 07:37)</span> <span class="comment-user userinfo">SKM</span></div></div></div><div id="comment-tools-3561" class="comment-tools"></div><div class="clear"></div><div id="comment-3561-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3619"></span>

<div id="answer-container-3619" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3619-score" class="post-score" title="current number of votes">1</div><span id="post-3619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I wonder if it would be possible to locate it using SNMP. If you could query the device for RSSI, then presumably the closer you got to it, the higher the RSSI would be.</p><p>There are likely many free MIB browsers available that might be able to help you with this. One such free one that I have used in the past is available from <a href="http://ireasoning.com/mibbrowser.shtml">iReasoning</a>.</p><p>By the way, I got the basic idea from the paper available from <a href="http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.79.2963&amp;rank=1">http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.79.2963&amp;rank=1</a>.</p><p>You might also try something as basic as <code>ping</code> and look for small changes in average round-trip service response times. It <em>might</em> be possible to detect small differences in SRT's that could help locate the laptop. In theory, the closer you are to the laptop, the smaller the SRT's should be. This is likely not going to be very practical though as the time deltas will likely be only very, very small and probably not measurable with any level of certainty or confidence.</p><p>To help narrow things down, another idea might be to reduce the transmit power output of your WAP if you can. Some WAPs allow you to do this; others don't. But, if you can, then you'd have to be that much closer to the stolen laptop before it could still connect. If you can't reduce the tx output power, you could try disconnecting the antenna[e] altogether.</p><p>Another possible way to find out more information about who might be using your wife's laptop is to place a hub between your cable/dsl/other modem and your WAP, then connect your Wireshark sniffing PC to the hub as well. You might be able to learn something more from that. You wouldn't necessarily need a hub in between if your WAP allows you to mirror your wireless traffic to one of your LAN ports, but I doubt most consumer-grade WAPs support that capability.</p><p>There might be other possibilities too. For example, you could change the WAP settings so that its default gateway points to your laptop, which could proxy everything out. But now you're a man-in-the-middle and can easily log and sniff away at will. This would likely require 2 Ethernet interfaces on your PC though, one for the WAN and one to connect to your WAP. Your PC would then IP forward everything from LAN to WAN.</p><p>Well, just a few more ideas to consider. In any case, I would be curious to know what happens and if you're able to find the culprit, so do update us!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '11, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Apr '11, 16:10</strong> </span></p></div></div><div id="comments-container-3619" class="comments-container"></div><div id="comment-tools-3619" class="comment-tools"></div><div class="clear"></div><div id="comment-3619-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3643"></span>

<div id="answer-container-3643" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3643-score" class="post-score" title="current number of votes">0</div><span id="post-3643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Whereas I don't know anything about this subject, I am hesitant to post this link. But just wanted to share in case it's of use. I stumbled on to it. Hope it helps.<br />
</p><p>http://securitystartshere.org/page-training-oswa-assistant.htm#moocherhunter</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/96f7c51993c68391c0929d0f35f464d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KSK&#39;s gravatar image" /><p><span>KSK</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KSK has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Apr '11, 11:09</strong> </span></p></div></div><div id="comments-container-3643" class="comments-container"></div><div id="comment-tools-3643" class="comment-tools"></div><div class="clear"></div><div id="comment-3643-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

