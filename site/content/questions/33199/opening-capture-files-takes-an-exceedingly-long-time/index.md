+++
type = "question"
title = "Opening capture files takes an exceedingly long time"
description = '''Good morning. We&#x27;ve recently built a new server [Xeon E5-2440 hexcore+HT, 32 GB memory, 2 RAID arrays] running Windows 2012 and installed Wireshark [x64]. We&#x27;ve found, however, that opening .pcap files on this server is taking much longer than anticipated: over 20 minutes for a 188 MB .pcap file. Wh...'''
date = "2014-05-30T06:14:00Z"
lastmod = "2014-05-30T07:19:00Z"
weight = 33199
keywords = [ "loading", "pcap", "opening", "capturefile" ]
aliases = [ "/questions/33199" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Opening capture files takes an exceedingly long time](/questions/33199/opening-capture-files-takes-an-exceedingly-long-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33199-score" class="post-score" title="current number of votes">0</div><span id="post-33199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good morning. We've recently built a new server [Xeon E5-2440 hexcore+HT, 32 GB memory, 2 RAID arrays] running Windows 2012 and installed Wireshark [x64]. We've found, however, that opening .pcap files on this server is taking much longer than anticipated: over 20 minutes for a 188 MB .pcap file. Whereas on a comparatively shabby PC [Intel Q9550, 6 GB memory], the file opens in 2 minutes.</p><p>Can anyone think of reasons why capture-file loading would take so much longer on the server?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-loading" rel="tag" title="see questions tagged &#39;loading&#39;">loading</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-opening" rel="tag" title="see questions tagged &#39;opening&#39;">opening</span> <span class="post-tag tag-link-capturefile" rel="tag" title="see questions tagged &#39;capturefile&#39;">capturefile</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '14, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/21c18114cd4bf0f9b45ead46b862386d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MHPark&#39;s gravatar image" /><p><span>MHPark</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MHPark has no accepted answers">0%</span></p></div></div><div id="comments-container-33199" class="comments-container"></div><div id="comment-tools-33199" class="comment-tools"></div><div class="clear"></div><div id="comment-33199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33200"></span>

<div id="answer-container-33200" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33200-score" class="post-score" title="current number of votes">0</div><span id="post-33200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can anyone think of reasons why capture-file loading would take so much longer on the server?</p></blockquote><p>DNS resolution!</p><p>Please disable the following option and then try again:</p><blockquote><p>Edit -&gt; Preferences -&gt; Name Resolution -&gt; Resolve Network (IP) addresses</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '14, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33200" class="comments-container"></div><div id="comment-tools-33200" class="comment-tools"></div><div class="clear"></div><div id="comment-33200-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

