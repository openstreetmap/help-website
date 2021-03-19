+++
type = "question"
title = "How to decode video stream if type is unknown?"
description = '''Hi there, i captured some udp packets while streaming my webcam in order to reassemble them to a video. Unfortunately i even don&#x27;t know the type of that video stream. Wireshark is just defining the packets as UDP and no hint concerning RTP or any other streaming format. How can i proceed with my ana...'''
date = "2013-07-28T15:05:00Z"
lastmod = "2013-08-20T01:33:00Z"
weight = 23416
keywords = [ "webcam", "udp", "video", "stream" ]
aliases = [ "/questions/23416" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode video stream if type is unknown?](/questions/23416/how-to-decode-video-stream-if-type-is-unknown)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23416-score" class="post-score" title="current number of votes">0</div><span id="post-23416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>i captured some udp packets while streaming my webcam in order to reassemble them to a video. Unfortunately i even don't know the type of that video stream. Wireshark is just defining the packets as UDP and no hint concerning RTP or any other streaming format. How can i proceed with my analysis, without knowing the type?</p><p>I followed the UDP Stream with my src ip and extracted it to a raw File. <a href="http://chummersinn.phpnet.us/mystream.raw">Mystream.raw</a></p><p>What would be the next steps? Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-webcam" rel="tag" title="see questions tagged &#39;webcam&#39;">webcam</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-video" rel="tag" title="see questions tagged &#39;video&#39;">video</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '13, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/99c672fafb988ba1be3eeb16f23df20a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yggdrasil&#39;s gravatar image" /><p><span>Yggdrasil</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yggdrasil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Aug '13, 15:22</strong> </span></p></div></div><div id="comments-container-23416" class="comments-container"><span id="23859"></span><div id="comment-23859" class="comment"><div id="post-23859-score" class="comment-score"></div><div class="comment-text"><p>as you updated the link of the file, are there any advances with your problem?</p></div><div id="comment-23859-info" class="comment-info"><span class="comment-age">(20 Aug '13, 01:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-23416" class="comment-tools"></div><div class="clear"></div><div id="comment-23416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23422"></span>

<div id="answer-container-23422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23422-score" class="post-score" title="current number of votes">0</div><span id="post-23422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i captured some udp packets while <strong>streaming my webcam</strong> ... Unfortunately i even <strong>don't know the type of that video stream</strong>.</p></blockquote><p>Well, that's a problem and the vendor of that webcam may well use it's own encoding. There might also be some form of encryption/data scrambling in place to prevent others from intercepting and viewing the video.</p><blockquote><p>I followed the UDP Stream with my src ip and extracted it to a raw File. Mystream.raw</p></blockquote><p>That looks like raw data. I tried to identify it with the <strong>file</strong> command on linux, and it also detects no known format.</p><p>So, either you extracted the wrong thing, not all data, or the data stream is in a proprietary format of that vendor.</p><blockquote><p>What would be the next steps?</p></blockquote><p>Figure out what data format is used by that vendor, by contacting the vendor support.</p><p>BTW: If you are able to post a capture file (on google docs, dropbox, etc.) of a <strong>whole</strong> video streaming session, someone here might be able to help. BEWARE the privacy issues in doing so!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '13, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jul '13, 05:53</strong> </span></p></div></div><div id="comments-container-23422" class="comments-container"></div><div id="comment-tools-23422" class="comment-tools"></div><div class="clear"></div><div id="comment-23422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

