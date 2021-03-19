+++
type = "question"
title = "What device on the network was responsible for the most data transfer ?"
description = '''Does anybody know how I could use Wireshark to find the device on my network that transfers the most data?'''
date = "2016-01-17T13:44:00Z"
lastmod = "2016-01-17T14:11:00Z"
weight = 49307
keywords = [ "wireshark" ]
aliases = [ "/questions/49307" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What device on the network was responsible for the most data transfer ?](/questions/49307/what-device-on-the-network-was-responsible-for-the-most-data-transfer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49307-score" class="post-score" title="current number of votes">0</div><span id="post-49307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anybody know how I could use Wireshark to find the device on my network that transfers the most data?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jan '16, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/18e5e60158b9cc6f0397b7f257942488?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Balter%20Wenjamin&#39;s gravatar image" /><p><span>Balter Wenjamin</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Balter Wenjamin has no accepted answers">0%</span></p></div></div><div id="comments-container-49307" class="comments-container"><span id="49309"></span><div id="comment-49309" class="comment"><div id="post-49309-score" class="comment-score"></div><div class="comment-text"><ul><li>what kind of network? Wired, wireless...</li><li>can you capture the total traffic of that network at a single place at the same time? (requires monitor mode for wireless networks and special arrangement for wired networks)</li><li>do the devices in your network talk to each other or only to the internet through a gateway device?</li></ul><p>Wireshark provides summary information, so once you capture the complete traffic, it is enough to sort the conversations by amount of packets or bytes transferred, but the key is not to miss a part of the total traffic flow.</p></div><div id="comment-49309-info" class="comment-info"><span class="comment-age">(17 Jan '16, 13:53)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="49310"></span><div id="comment-49310" class="comment"><div id="post-49310-score" class="comment-score"></div><div class="comment-text"><p>I'm on a wireless network connected to the internet through a 802.11n wireless router. If I captured traffic for say five minutes what should I look at to find the device, on my network that transferred the most data?</p></div><div id="comment-49310-info" class="comment-info"><span class="comment-age">(17 Jan '16, 13:57)</span> <span class="comment-user userinfo">Balter Wenjamin</span></div></div></div><div id="comment-tools-49307" class="comment-tools"></div><div class="clear"></div><div id="comment-49307-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49311"></span>

<div id="answer-container-49311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49311-score" class="post-score" title="current number of votes">0</div><span id="post-49311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming you've captured using <em>monitor</em> mode (don't confuse it with <em>promiscuous</em> mode), you should go <code>Statistics -&gt; Conversations</code>, and in the right bottom part of the window which opens, click <code>Conversation types</code> and put a checkmark to <code>IEEE 802.11</code>. This will create a corresponding tab in that window. Select that tab and click the column header named "Bytes" (4th from the left, sum of Tx and Rx traffic of the device) twice to sort the rows of the table by the number of packets with highest values on top.</p><p>Then, one of address A and address B columns of the topmost row contains the AP's MAC address, and the other one contains the MAC address of the device responsible for the biggest deal of the traffic.</p><p>Higher protocol layers, such as IP, are likely inaccessible unless your wireless network uses no encryption, so you'll not be able to see any other than MAC addresses. If that is an issue for you, you'd have to configure Wireshark to decrypt the wireless traffic and to reconnect all your devices to the AP while capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '16, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jan '16, 14:12</strong> </span></p></div></div><div id="comments-container-49311" class="comments-container"></div><div id="comment-tools-49311" class="comment-tools"></div><div class="clear"></div><div id="comment-49311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

