+++
type = "question"
title = "HTTP transmission or not???"
description = '''I found a really weird statistics on wireshark. For a video transmission on Android I opened up the stats for protocol hierarchy, the stats shows that the 3MB video doesn&#x27;t go through HTTP. However, when I clicked &quot;save the objects&quot; , wireshard shows the 3MB as &quot;video/mp4&quot; through HTTP. (It&#x27;s like i...'''
date = "2012-11-13T13:34:00Z"
lastmod = "2012-11-14T02:54:00Z"
weight = 15879
keywords = [ "https" ]
aliases = [ "/questions/15879" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP transmission or not???](/questions/15879/http-transmission-or-not)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15879-score" class="post-score" title="current number of votes">0</div><span id="post-15879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I found a really weird statistics on wireshark. For a video transmission on Android I opened up the stats for protocol hierarchy, the stats shows that the 3MB video doesn't go through HTTP.</p><p>However, when I clicked "save the objects" , wireshard shows the 3MB as "video/mp4" through HTTP. (It's like it resembles the packages).</p><p>Now I'm confused whether the video on Android is sent through HTTP or not.., or HTTPS?</p><p>Thank you !</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '12, 13:34</strong></p><img src="https://secure.gravatar.com/avatar/45c162accca9a3f515287aaf7cf84f78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miramiram&#39;s gravatar image" /><p><span>miramiram</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miramiram has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '12, 03:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-15879" class="comments-container"></div><div id="comment-tools-15879" class="comment-tools"></div><div class="clear"></div><div id="comment-15879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15892"></span>

<div id="answer-container-15892" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15892-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15892-score" class="post-score" title="current number of votes">1</div><span id="post-15892-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Because HTTP re-assembles the TCP stream, most packets are marked as "[TCP segment of a reassembled PDU]". Those packets are not counted as HTTP in the protocol hierarchy.</p><p>You can disable the reassembly of packets by right-clicking on "Transmission Control Protocol" in the packet details pane. Then choose "Protocol Preferences" and deselect "Allow subdissector to reassemble TCP streams".</p><p>Then your HTTP response will not get reassembled and all HTTP packets will be counted as HTTP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '12, 02:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-15892" class="comments-container"></div><div id="comment-tools-15892" class="comment-tools"></div><div class="clear"></div><div id="comment-15892-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

