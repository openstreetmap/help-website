+++
type = "question"
title = "strange web download behavior"
description = '''When downloading sql developer tools from oracle.com(using IE or Chrome) users are experiencing an issue where the download will start and just die at about 520k. From the captures i can see the client ACKing at about the 520K mark and then nothing from the server, followed up by several keep-alives...'''
date = "2014-01-13T15:26:00Z"
lastmod = "2014-01-14T07:06:00Z"
weight = 28850
keywords = [ "downloads", "slow", "http" ]
aliases = [ "/questions/28850" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [strange web download behavior](/questions/28850/strange-web-download-behavior)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28850-score" class="post-score" title="current number of votes">0</div><span id="post-28850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When downloading sql developer tools from oracle.com(using IE or Chrome) users are experiencing an issue where the download will start and just die at about 520k. From the captures i can see the client ACKing at about the 520K mark and then nothing from the server, followed up by several keep-alives from the client to the server. Since I have no way of doing a capture at the server, i can't tell if the server is sending more data after the ACK or if the ACK ever gets to the server. If this download is attempted from a mac it works fine, also, once in awhile the download will actually work but not until you try it multiple times. Another strange behavior I see during these download attempts is the browser actually sends several SYN packets to the server to try and establish a connection, so there are several TCP streams between the same IP's, most of them just RST or FIN,ACK, FIN,ACK, ACK normally. I usually don't see this behavior during downloads from other sites that aren't having issues. Just looking to see if anyone else has had this issue with the oracle site as it seems to be isolated to that particular domain.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-downloads" rel="tag" title="see questions tagged &#39;downloads&#39;">downloads</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '14, 15:26</strong></p><img src="https://secure.gravatar.com/avatar/4607b37c5d283726a623b70d042eebd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="msemkiw&#39;s gravatar image" /><p><span>msemkiw</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="msemkiw has no accepted answers">0%</span></p></div></div><div id="comments-container-28850" class="comments-container"></div><div id="comment-tools-28850" class="comment-tools"></div><div class="clear"></div><div id="comment-28850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28861"></span>

<div id="answer-container-28861" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28861-score" class="post-score" title="current number of votes">0</div><span id="post-28861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>From the captures i can see the client ACKing at about the 520K mark and <strong>then nothing from the server</strong>,</p></blockquote><p>well, it could be the server, but it an also be some piece of security software and/or device that blocks the download after some time, because it believes it has found some malware.</p><p>Did you <strong>thoroughly</strong> check the logs and alerts of your security software on the client and your internet firewall?</p><p>If you captured solely on the client, you should consider to capture off-box to detect if local software on the client and/or the network firewall stops frames from the server.</p><ul><li><strong>detect client security software problem:</strong> capture on a mirror port of the switch (or with a TAP) to see if the server really does not answer at a certain point in the conversation. If yes: it could be the server <strong>or</strong> your internet firewall</li><li><strong>detect internet firewall problems:</strong> capture on the WAN side of your firewall (sometimes hard, if the firewall has an integrated DSL modem), to check if the server really does not answer, or if the firewall dropped the connection</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '14, 07:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28861" class="comments-container"></div><div id="comment-tools-28861" class="comment-tools"></div><div class="clear"></div><div id="comment-28861-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

