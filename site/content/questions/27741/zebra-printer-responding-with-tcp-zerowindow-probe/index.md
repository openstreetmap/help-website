+++
type = "question"
title = "Zebra Printer responding with TCP ZeroWindow Probe"
description = '''We are having some issues with several zebra printers that are printers that continue to release labels as they are sent. What we are seeing is that printer will error out in the windows print queue. These jobs are sent from a unix server to a unix/samba share that hands off to the windows print que...'''
date = "2013-12-03T19:49:00Z"
lastmod = "2013-12-04T02:42:00Z"
weight = 27741
keywords = [ "zero-window", "zerowindowprobe" ]
aliases = [ "/questions/27741" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Zebra Printer responding with TCP ZeroWindow Probe](/questions/27741/zebra-printer-responding-with-tcp-zerowindow-probe)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27741-score" class="post-score" title="current number of votes">0</div><span id="post-27741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are having some issues with several zebra printers that are printers that continue to release labels as they are sent. What we are seeing is that printer will error out in the windows print queue. These jobs are sent from a unix server to a unix/samba share that hands off to the windows print queue. Windows is to manage all the print queue.</p><p>This has become an issue since our volume is now heavier.</p><p>I have taken a small sample from a larger packket capture. What do we need to do to fix this, is this a problem on the zebra printer, windows print server, unix/samba hand off?</p><p>I have also captured infromation from the windows print queue and from the zebra tool.</p><p><a href="http://sdrv.ms/1bf1NaI">Packet capture here</a></p><p><a href="http://sdrv.ms/188QS3m">Full 6mb packet capture</a></p><p>Need some suggestions</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-zero-window" rel="tag" title="see questions tagged &#39;zero-window&#39;">zero-window</span> <span class="post-tag tag-link-zerowindowprobe" rel="tag" title="see questions tagged &#39;zerowindowprobe&#39;">zerowindowprobe</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '13, 19:49</strong></p><img src="https://secure.gravatar.com/avatar/d6ab836d8d5b02419d3329328bc76aab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="indy_dude&#39;s gravatar image" /><p><span>indy_dude</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="indy_dude has no accepted answers">0%</span></p></div></div><div id="comments-container-27741" class="comments-container"></div><div id="comment-tools-27741" class="comment-tools"></div><div class="clear"></div><div id="comment-27741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27747"></span>

<div id="answer-container-27747" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27747-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27747-score" class="post-score" title="current number of votes">1</div><span id="post-27747-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I can tell from the MAC addresses the device sending the Zero Window is a Zebra Printer. Which means that the Printer tells the other system to pause sending further data, which means that it is not able to cope with the amount of incoming packets. So yes, this is a problem with the Zebra printer - it needs to either print faster (which usually means to replace the device with a newer one), or be upgraded with more RAM to buffer incoming print jobs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '13, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-27747" class="comments-container"><span id="27749"></span><div id="comment-27749" class="comment"><div id="post-27749-score" class="comment-score"></div><div class="comment-text"><p>Jasper, thank you so much for looking at it, this helped with what I thought. We will increase the speed of the printer from 2ips to 6ips and see if it can keep up.</p></div><div id="comment-27749-info" class="comment-info"><span class="comment-age">(04 Dec '13, 02:35)</span> <span class="comment-user userinfo">indy_dude</span></div></div><span id="27753"></span><div id="comment-27753" class="comment"><div id="post-27753-score" class="comment-score"></div><div class="comment-text"><p><span>@indy_dude</span>: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-27753-info" class="comment-info"><span class="comment-age">(04 Dec '13, 02:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-27747" class="comment-tools"></div><div class="clear"></div><div id="comment-27747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

