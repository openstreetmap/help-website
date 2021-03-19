+++
type = "question"
title = "Source  or destination is an address Mac"
description = '''Hello, I have used Wireshark for a few days and I noticed each connection is related to a Mac Address : Cisco_ec:ba:92 (00:0d:29:ec:ba:92). It appears as destination if I initiate the connection or as source if not. I contacted my ISP (Videotron) and they don&#x27;t identify their equipment by their mac ...'''
date = "2011-08-04T15:50:00Z"
lastmod = "2011-08-09T18:49:00Z"
weight = 5507
keywords = [ "macaddress" ]
aliases = [ "/questions/5507" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Source or destination is an address Mac](/questions/5507/source-or-destination-is-an-address-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5507-score" class="post-score" title="current number of votes">0</div><span id="post-5507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have used Wireshark for a few days and I noticed each connection is related to a Mac Address : Cisco_ec:ba:92 (00:0d:29:ec:ba:92). It appears as destination if I initiate the connection or as source if not. I contacted my ISP (Videotron) and they don't identify their equipment by their mac addresses and they don't seem to understand what is going on. I'm intrigued. I'm actually connected via modem (Aris) so I have nothing to do with Cisco. Is there any explanation ? Thank you for your help. Danielle Massé</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macaddress" rel="tag" title="see questions tagged &#39;macaddress&#39;">macaddress</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '11, 15:50</strong></p><img src="https://secure.gravatar.com/avatar/eacb6a86ce38d3415ab3d0becc30485d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coccinaile&#39;s gravatar image" /><p><span>coccinaile</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coccinaile has no accepted answers">0%</span></p></div></div><div id="comments-container-5507" class="comments-container"><span id="5508"></span><div id="comment-5508" class="comment"><div id="post-5508-score" class="comment-score"></div><div class="comment-text"><p>I.e., for packets being sent by your machine to your cable modem to initiate a connection, the destination MAC address is a Cisco address?</p></div><div id="comment-5508-info" class="comment-info"><span class="comment-age">(04 Aug '11, 16:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-5507" class="comment-tools"></div><div class="clear"></div><div id="comment-5507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="5523"></span>

<div id="answer-container-5523" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5523-score" class="post-score" title="current number of votes">1</div><span id="post-5523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>All IP packets to/from IP addresses outside of your local subnet will be sent to/received from your default gateway. So the symptoms you describe would suggest that the device with mac address 00:0d:29:ec:ba:92 is your default gateway.</p><p>You can check that by looking up which IP adress is your default gateway address (assuming you're using windows: ipconfig in a cmd window). You can then check which mac address is listed for your gateway address with "arp -a" (also in the cmd window). I am sure this will point to the cisco mac address.</p><p>As you say you don't have any cisco device in your network, my bet is that your Arris cable modem is in bridging mode, which means it is not your local gateway, it just forwards your packets to a device at your provider which acts as your default gateway. This is a normal setup and nothing to worry about :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '11, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5523" class="comments-container"><span id="5544"></span><div id="comment-5544" class="comment"><div id="post-5544-score" class="comment-score"></div><div class="comment-text"><p>Hello, you're quite right arp -a gives me the very same Mac Address.Is there a way to find out this bridgind mode ? Thank you very much.</p></div><div id="comment-5544-info" class="comment-info"><span class="comment-age">(06 Aug '11, 09:06)</span> <span class="comment-user userinfo">coccinaile</span></div></div><span id="5545"></span><div id="comment-5545" class="comment"><div id="post-5545-score" class="comment-score"></div><div class="comment-text"><p>Hello, you're quite right arp -a gives me the very same Mac Address for my ip gateway. Thank you very much.</p></div><div id="comment-5545-info" class="comment-info"><span class="comment-age">(06 Aug '11, 10:42)</span> <span class="comment-user userinfo">coccinaile</span></div></div><span id="5554"></span><div id="comment-5554" class="comment"><div id="post-5554-score" class="comment-score"></div><div class="comment-text"><p>(converted your "answer" to a "comment", please see the FAQ)</p><p>Well, the fact that you get the Mac-Address of a device that is not in your network, but behind the Cable modem is kind of proof that it is in bridging mode :-)</p></div><div id="comment-5554-info" class="comment-info"><span class="comment-age">(07 Aug '11, 06:56)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5523" class="comment-tools"></div><div class="clear"></div><div id="comment-5523-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5563"></span>

<div id="answer-container-5563" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5563-score" class="post-score" title="current number of votes">0</div><span id="post-5563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just read about the man in the middle intervention and there is some similarity her : intercepting the traffic between two ip addresses using another Mac Address ? Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '11, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/eacb6a86ce38d3415ab3d0becc30485d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coccinaile&#39;s gravatar image" /><p><span>coccinaile</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coccinaile has no accepted answers">0%</span></p></div></div><div id="comments-container-5563" class="comments-container"><span id="5566"></span><div id="comment-5566" class="comment"><div id="post-5566-score" class="comment-score"></div><div class="comment-text"><p>If there is some man-in-the-middle attack going on, you will see arp packets that you normally don't see.</p></div><div id="comment-5566-info" class="comment-info"><span class="comment-age">(07 Aug '11, 23:36)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5563" class="comment-tools"></div><div class="clear"></div><div id="comment-5563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5571"></span>

<div id="answer-container-5571" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5571-score" class="post-score" title="current number of votes">-1</div><span id="post-5571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello, in this case, would you be kind enough to tell me where and what I should be looking for in order to be certain ? Thanks a lot for your help</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '11, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/eacb6a86ce38d3415ab3d0becc30485d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coccinaile&#39;s gravatar image" /><p><span>coccinaile</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coccinaile has no accepted answers">0%</span></p></div></div><div id="comments-container-5571" class="comments-container"></div><div id="comment-tools-5571" class="comment-tools"></div><div class="clear"></div><div id="comment-5571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5572"></span>

<div id="answer-container-5572" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5572-score" class="post-score" title="current number of votes">-1</div><span id="post-5572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>P.S. My computer is a Mac OS 10.6</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '11, 06:16</strong></p><img src="https://secure.gravatar.com/avatar/eacb6a86ce38d3415ab3d0becc30485d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coccinaile&#39;s gravatar image" /><p><span>coccinaile</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coccinaile has no accepted answers">0%</span></p></div></div><div id="comments-container-5572" class="comments-container"></div><div id="comment-tools-5572" class="comment-tools"></div><div class="clear"></div><div id="comment-5572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5573"></span>

<div id="answer-container-5573" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5573-score" class="post-score" title="current number of votes">-1</div><span id="post-5573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Update : there is a change in the wireshark report : instead of displaying the mac address as source and destination like it did, it displays the ip of the ISP (and the mac address) as source or destination so I guess there is nothing to be concerned about : the mac address belongs to the ISP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '11, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/eacb6a86ce38d3415ab3d0becc30485d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coccinaile&#39;s gravatar image" /><p><span>coccinaile</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coccinaile has no accepted answers">0%</span></p></div></div><div id="comments-container-5573" class="comments-container"><span id="5605"></span><div id="comment-5605" class="comment"><div id="post-5605-score" class="comment-score"></div><div class="comment-text"><p>Please read the <a href="http://ask.wireshark.org/faq/">FAQ</a>, especially the first item, which indicates that this is not a discussion forum. If you want to add more information or clarify something, either edit your question or do so with a comment block, as I'm doing now, and not as a new answer, which you've now done 4 times incorrectly. If this Q&amp;A format doesn't really fit, then please try the wireshark developer and/or user mailing lists instead.</p></div><div id="comment-5605-info" class="comment-info"><span class="comment-age">(09 Aug '11, 18:49)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-5573" class="comment-tools"></div><div class="clear"></div><div id="comment-5573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

