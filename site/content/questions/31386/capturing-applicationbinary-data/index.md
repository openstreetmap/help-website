+++
type = "question"
title = "Capturing application/binary data"
description = '''I&#x27;m running wireshark Version 1.10.6 (v1.10.6 from master-1.10) on Windows Server 2008 R2. I am trying to check the contents of some data from a proprietary application that is sent with a POST request, as application/binary data. I am seeing the POST data headers:  POST /eddSrv/EddRcvr?x=832893 HTT...'''
date = "2014-04-02T06:19:00Z"
lastmod = "2014-04-03T05:36:00Z"
weight = 31386
keywords = [ "binary", "post", "data" ]
aliases = [ "/questions/31386" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing application/binary data](/questions/31386/capturing-applicationbinary-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31386-score" class="post-score" title="current number of votes">0</div><span id="post-31386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running wireshark Version 1.10.6 (v1.10.6 from master-1.10) on Windows Server 2008 R2.</p><p>I am trying to check the contents of some data from a proprietary application that is sent with a POST request, as application/binary data. I am seeing the POST data headers:<br />
</p><pre><code>POST /eddSrv/EddRcvr?x=832893 HTTP/1.0
Accept: */*
Connection: Keep-alive
Content-Type: application/binary
User-Agent: WRA 3787
Host: &lt;myserver.com&gt;:55023
Content-Length: 92</code></pre><p>But I am trying to see the 92 bytes specified in Content-Length, and even with a ton of googling, cannot figure out how to look at them. Any help would be greatly appreciated.</p><p>Dave</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-binary" rel="tag" title="see questions tagged &#39;binary&#39;">binary</span> <span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '14, 06:19</strong></p><img src="https://secure.gravatar.com/avatar/561059d1915785de772a29cb007785ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="archer&#39;s gravatar image" /><p><span>archer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="archer has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Apr '14, 12:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-31386" class="comments-container"><span id="31388"></span><div id="comment-31388" class="comment"><div id="post-31388-score" class="comment-score"></div><div class="comment-text"><p>Can you share the capture somewhere, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-31388-info" class="comment-info"><span class="comment-age">(02 Apr '14, 06:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="31389"></span><div id="comment-31389" class="comment"><div id="post-31389-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid not; there is proprietary information in the data. Nothing as sensitive as HIPAA or PCI-DSS, but I can't post it publicly.</p></div><div id="comment-31389-info" class="comment-info"><span class="comment-age">(02 Apr '14, 07:23)</span> <span class="comment-user userinfo">archer</span></div></div></div><div id="comment-tools-31386" class="comment-tools"></div><div class="clear"></div><div id="comment-31386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31426"></span>

<div id="answer-container-31426" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31426-score" class="post-score" title="current number of votes">0</div><span id="post-31426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you see the payload bytes in the following POST request (you can download the file and analyze it in Wireshark)?</p><blockquote><p><a href="https://www.cloudshark.org/captures/5254ad47c670">https://www.cloudshark.org/captures/5254ad47c670</a></p></blockquote><p><strong>If yes:</strong> Please post the payload. If it is correct (I will check ;-)), something is 'wrong' with the POST request in your capture file. Probably you did not capture the full frame length and thus the payload is simply not in the capture file.</p><p><strong>If no:</strong> You need a better understanding how Wireshark and/or HTTP POST works. If so, please follow up here and I'll give you some hints, like 'Follow TCP Stream' if you right click the frame with the POST request.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '14, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31426" class="comments-container"><span id="31427"></span><div id="comment-31427" class="comment"><div id="post-31427-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the help! Yes, I see your "123456789012345678901234567890". However, you're using application/x-www-form-urlencoded, not application/binary as I am. Would that make a difference? I have tried the Follow TCP Stream function; that's where I got the data in my original post.<br />
</p><p>Re cloudshark (I've never used it): If I post a packet and let it analyze it, will I be able to delete it after I'm done with it?</p></div><div id="comment-31427-info" class="comment-info"><span class="comment-age">(02 Apr '14, 13:04)</span> <span class="comment-user userinfo">archer</span></div></div><span id="31428"></span><div id="comment-31428" class="comment"><div id="post-31428-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Re cloudshark (I've never used it): If I post a packet and let it analyze it, will I be able to delete it after I'm done with it?</p></blockquote><p>with a paid account: yes. Otherwise: no.</p><blockquote><p>Would that make a difference?</p></blockquote><p>Hm.. I guess, it shouldn't. But maybe you discovered a problem with 'Follow TCP stream'.</p><p>What do you see, if you look directly into the POST frame, <strong>not</strong> with 'Follow TCP stream'.</p><p>If you look at the 'Frame' layer in the frame, what do you see for 'bytes on wire' and 'bytes captured'? The values should be identical.</p></div><div id="comment-31428-info" class="comment-info"><span class="comment-age">(02 Apr '14, 13:08)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="31476"></span><div id="comment-31476" class="comment"><div id="post-31476-score" class="comment-score"></div><div class="comment-text"><p>Yes, I'm seeing "bytes on wire" == "bytes captured". But I'm not seeing anything that appears to correspond to the amount of data in the content-length field. I'm beginning to wonder if there's a bug in Wireshark's handling of application/binary data when it doesn't correspond to a specific object type like an attachment. I know the data is there, because our app is working properly and the server is receiving all the data it is supposed to.</p></div><div id="comment-31476-info" class="comment-info"><span class="comment-age">(03 Apr '14, 05:36)</span> <span class="comment-user userinfo">archer</span></div></div></div><div id="comment-tools-31426" class="comment-tools"></div><div class="clear"></div><div id="comment-31426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

