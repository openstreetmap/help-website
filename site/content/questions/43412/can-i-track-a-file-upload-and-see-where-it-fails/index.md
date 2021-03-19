+++
type = "question"
title = "Can I track a file upload and see where it fails?"
description = '''I apologize for the probably complete noob question. This is my problem and what I need to do. I am currently unable to upload files &amp;gt;100kb in size to any other website (dropbox, work server, send email with an attachment, etc) during my ISPs (Windstream) prime time. What is happening is that fil...'''
date = "2015-06-21T11:16:00Z"
lastmod = "2015-06-21T13:00:00Z"
weight = 43412
keywords = [ "track", "fragmented", "upload" ]
aliases = [ "/questions/43412" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I track a file upload and see where it fails?](/questions/43412/can-i-track-a-file-upload-and-see-where-it-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43412-score" class="post-score" title="current number of votes">0</div><span id="post-43412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I apologize for the probably complete noob question. This is my problem and what I need to do.</p><p>I am currently unable to upload files &gt;100kb in size to any other website (dropbox, work server, send email with an attachment, etc) during my ISPs (Windstream) prime time. What is happening is that files that must be fragmented to transmit are failing somewhere along the route and the upload fail.</p><p>Windstream refuses to acknowledge any problem. Their stance is since I can get online and surf the internet there is no problem</p><p>Can Wireshark track a file upload over the internet and let me know where along the path the upload fails? If not, is there anything that can?</p><p>Thank you for your help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-track" rel="tag" title="see questions tagged &#39;track&#39;">track</span> <span class="post-tag tag-link-fragmented" rel="tag" title="see questions tagged &#39;fragmented&#39;">fragmented</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '15, 11:16</strong></p><img src="https://secure.gravatar.com/avatar/0677ea443eb9175b539ec56f2bf09cb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cortilian&#39;s gravatar image" /><p><span>Cortilian</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cortilian has no accepted answers">0%</span></p></div></div><div id="comments-container-43412" class="comments-container"></div><div id="comment-tools-43412" class="comment-tools"></div><div class="clear"></div><div id="comment-43412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43414"></span>

<div id="answer-container-43414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43414-score" class="post-score" title="current number of votes">1</div><span id="post-43414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Can Wireshark track a file upload over the internet and let me know where along the path the upload fails?</p></blockquote><p>you can capture the upload and figure out what's causing the failure (RESET, timeout, packet loss, etc.) <strong>however</strong> there is <strong>no way</strong> to figure out <strong>where</strong> the error/problem occurs! The only thing you can say: It's <strong>somewhere</strong> between your client and the servers on the internet. Could be your network, could be the last mile to your home, could be your ISP, could be another ISP, your traffic has to cross, etc.</p><blockquote><p>If not, is there anything that can?</p></blockquote><p>No, there isn't.</p><p>If the problem is indeed your ISP, then you'd have to capture at several points within their network to find the bottleneck, but I guess that's not going to happen.</p><blockquote><p>Windstream refuses to acknowledge any problem. Their stance is since I can get online and surf the internet there is no problem</p></blockquote><p>well, what else do you expect to hear from their first line support ;-) There is never a problem on the ISP network :-)</p><p>BTW: If you have a work server (you mentioned it), you could capture at your client and at your server at the same time. In that capture file you should see packet loss. With that "evidence" you can try to talk to their support people again, but based on my experience, I'm telling you, that's going to lead nowhere (<a href="https://ask.wireshark.org/questions/43024/can-we-pin-the-tail-on-charter-dsl-using-wireshark">see a similar discussion with <span><span>@Lucidcryotank</span></span></a>)</p><p>So, what can you do?</p><ul><li>switch to a better ISP, even if it costs you more money!</li><li>upload your files outside their "prime time"</li><li><a href="https://ask.wireshark.org/questions/43024/can-we-pin-the-tail-on-charter-dsl-using-wireshark">team up with <span><span>@Lucidcryotank</span></span> and file a FCC complaint if you're in the U.S.</a> ;-))</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '15, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '15, 14:02</strong> </span></p></div></div><div id="comments-container-43414" class="comments-container"><span id="43415"></span><div id="comment-43415" class="comment"><div id="post-43415-score" class="comment-score"></div><div class="comment-text"><p>Thanks a bunch for the info.</p></div><div id="comment-43415-info" class="comment-info"><span class="comment-age">(21 Jun '15, 12:13)</span> <span class="comment-user userinfo">Cortilian</span></div></div><span id="43416"></span><div id="comment-43416" class="comment"><div id="post-43416-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-43416-info" class="comment-info"><span class="comment-age">(21 Jun '15, 13:00)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-43414" class="comment-tools"></div><div class="clear"></div><div id="comment-43414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

