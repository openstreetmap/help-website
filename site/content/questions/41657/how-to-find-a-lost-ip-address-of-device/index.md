+++
type = "question"
title = "How to find a lost IP address of device"
description = '''I have a device that can be IP managed through the network. The IP address of the device is lost along with network @ so i don&#x27;t know the network the device belongs to. I&#x27;m trying to use Wireshark to get it back. The only thing i was able to retrieve was the MAC@ of the device and that was from the ...'''
date = "2015-04-21T23:55:00Z"
lastmod = "2015-04-22T06:14:00Z"
weight = 41657
keywords = [ "iplostfindlost" ]
aliases = [ "/questions/41657" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to find a lost IP address of device](/questions/41657/how-to-find-a-lost-ip-address-of-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41657-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41657-score" class="post-score" title="current number of votes">0</div><span id="post-41657-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a device that can be IP managed through the network. The IP address of the device is lost along with network @ so i don't know the network the device belongs to. I'm trying to use Wireshark to get it back.</p><p>The only thing i was able to retrieve was the <span class="__cf_email__" data-cfemail="d994989a99">[email protected]</span> of the device and that was from the Spanning Tree frames. By the way i'm using a direct cable connection to the device so i can capture anything that goes out of the port.</p><p>Any Ideas are very much appreciated.</p><p>Thnx</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iplostfindlost" rel="tag" title="see questions tagged &#39;iplostfindlost&#39;">iplostfindlost</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '15, 23:55</strong></p><img src="https://secure.gravatar.com/avatar/cb84a5d8464ef5ca8c41928d3b0e3ed1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dannykaadan&#39;s gravatar image" /><p><span>dannykaadan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dannykaadan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Apr '15, 23:58</strong> </span></p></div></div><div id="comments-container-41657" class="comments-container"><span id="41675"></span><div id="comment-41675" class="comment"><div id="post-41675-score" class="comment-score"></div><div class="comment-text"><p>what type of device is that (brand and model)?</p></div><div id="comment-41675-info" class="comment-info"><span class="comment-age">(22 Apr '15, 05:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-41657" class="comment-tools"></div><div class="clear"></div><div id="comment-41657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41669"></span>

<div id="answer-container-41669" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41669-score" class="post-score" title="current number of votes">2</div><span id="post-41669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dannykaadan has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on the type of device, it may try and communicate with it's default gateway or other configured LAN peer.</p><p>You can try rebooting the device while running an unfiltered capture and looking for ARP packets. These should show you the source IP address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/7addf8865ef7a9819162afe977458460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NickR&#39;s gravatar image" /><p><span>NickR</span><br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NickR has one accepted answer">50%</span></p></div></div><div id="comments-container-41669" class="comments-container"><span id="41682"></span><div id="comment-41682" class="comment"><div id="post-41682-score" class="comment-score">1</div><div class="comment-text"><p>I got it finally! I just let Wireshark collect everything for about 5 miniutes then, as NickR suggested, i filtered the ARP frames and i got the one from the device showing IP @. Thnx NickR</p></div><div id="comment-41682-info" class="comment-info"><span class="comment-age">(22 Apr '15, 06:14)</span> <span class="comment-user userinfo">dannykaadan</span></div></div></div><div id="comment-tools-41669" class="comment-tools"></div><div class="clear"></div><div id="comment-41669-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41665"></span>

<div id="answer-container-41665" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41665-score" class="post-score" title="current number of votes">0</div><span id="post-41665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Unless the device transmits its IP address in a packet, you're in trouble. Usually I would try to do a factory reset, which should be possible as long as you have physical access (and don't care about the config of the device being lost in the process).</p><p>You could also do an nmap ping scan over all private IP address ranges if you assume that the switch had an IP from that range, but you should only do this while it is not in a production network. This can still fail if someone configured the switch to not have an IP address on the port you're connected to.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Apr '15, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-41665" class="comments-container"></div><div id="comment-tools-41665" class="comment-tools"></div><div class="clear"></div><div id="comment-41665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

