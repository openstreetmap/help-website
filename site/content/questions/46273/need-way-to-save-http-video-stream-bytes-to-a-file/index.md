+++
type = "question"
title = "Need way to save http video stream bytes to a file..."
description = '''Using Wireshark Version 1.12.7 on Windows, after capture of UDP video stream packets, saving the video to a file may be done by:  Right-click on a video packet, and select &quot;Follow UDP stream&quot; When the dialog appears, click the &quot;Save As&quot; button, and name the file with a .ts extension  After doing so,...'''
date = "2015-09-29T17:45:00Z"
lastmod = "2015-10-02T10:04:00Z"
weight = 46273
keywords = [ "saveas", "videostream", "save", "http" ]
aliases = [ "/questions/46273" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Need way to save http video stream bytes to a file...](/questions/46273/need-way-to-save-http-video-stream-bytes-to-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46273-score" class="post-score" title="current number of votes">0</div><span id="post-46273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using Wireshark Version 1.12.7 on Windows, after capture of UDP video stream packets, saving the video to a file may be done by:</p><ol><li>Right-click on a video packet, and select "Follow UDP stream"</li><li>When the dialog appears, click the "Save As" button, and name the file with a .ts extension</li></ol><p>After doing so, the .ts file may be opened in VLC.</p><p>My question: Is there a way to accomplish the equivalent on a capture of http video stream? This DOESN'T work:</p><ol><li>Right-click on a video packet, and select "Follow TCP stream"</li><li>When the dialog appears, click the "Save As" button, and name the file with a .ts extension</li></ol></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-saveas" rel="tag" title="see questions tagged &#39;saveas&#39;">saveas</span> <span class="post-tag tag-link-videostream" rel="tag" title="see questions tagged &#39;videostream&#39;">videostream</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '15, 17:45</strong></p><img src="https://secure.gravatar.com/avatar/0e669f5129ac13bdba3262abcfbaa92b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfbaker&#39;s gravatar image" /><p><span>mfbaker</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfbaker has no accepted answers">0%</span></p></div></div><div id="comments-container-46273" class="comments-container"><span id="46278"></span><div id="comment-46278" class="comment"><div id="post-46278-score" class="comment-score"></div><div class="comment-text"><p>Couleur you provide us an example trace of the TCP case, in a public accessible place ?</p></div><div id="comment-46278-info" class="comment-info"><span class="comment-age">(30 Sep '15, 04:15)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="46295"></span><div id="comment-46295" class="comment"><div id="post-46295-score" class="comment-score"></div><div class="comment-text"><p>Yes, here's an example capture of an http video stream: <a href="https://drive.google.com/file/d/0B1O8tPh9Cozjd1BFTzFzRWdhNGs/view?usp=sharing">https://drive.google.com/file/d/0B1O8tPh9Cozjd1BFTzFzRWdhNGs/view?usp=sharing</a></p><p>When you click the link, a page will appear with a download button. Upon clicking the button, it should save as a file named "20150930_httpVideoStream.pcapng".</p><p>Thanks! -Mike</p></div><div id="comment-46295-info" class="comment-info"><span class="comment-age">(30 Sep '15, 18:16)</span> <span class="comment-user userinfo">mfbaker</span></div></div><span id="46296"></span><div id="comment-46296" class="comment"><div id="post-46296-score" class="comment-score"></div><div class="comment-text"><p>I was able to extract the video stream and play it, but there wasn't any audio. Was there audio in the original stream, or it was video only? If there wasn't any audio, then my procedure worked and I will post it. If there was audio, it wasn't present when I extracted the stream.</p></div><div id="comment-46296-info" class="comment-info"><span class="comment-age">(30 Sep '15, 18:51)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="46297"></span><div id="comment-46297" class="comment"><div id="post-46297-score" class="comment-score"></div><div class="comment-text"><p>Thanks much, Jim! The capture I posted had no audio, so yes, please post your procedure.</p><p>Tomorrow I will try to post another capture with audio, just to make sure that will work, too.</p><p>-Mike</p></div><div id="comment-46297-info" class="comment-info"><span class="comment-age">(30 Sep '15, 19:25)</span> <span class="comment-user userinfo">mfbaker</span></div></div></div><div id="comment-tools-46273" class="comment-tools"></div><div class="clear"></div><div id="comment-46273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46298"></span>

<div id="answer-container-46298" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46298-score" class="post-score" title="current number of votes">1</div><span id="post-46298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mfbaker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to Edit &gt; Preferences &gt; Protocols &gt; TCP. Enable "Allow subdissector to reassemble TCP streams." Then go to File &gt; Export Objects &gt; HTTP. Select the video stream, then click on "Save As" and save with an appropriate extension, .ts in the case of the stream extracted from the capture file you supplied.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '15, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-46298" class="comments-container"><span id="46299"></span><div id="comment-46299" class="comment"><div id="post-46299-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, Jim -- your procedure worked! Wow, wireshark has such an amazingly number of capabilities -- kudos also to the wireshark developers!</p></div><div id="comment-46299-info" class="comment-info"><span class="comment-age">(30 Sep '15, 21:20)</span> <span class="comment-user userinfo">mfbaker</span></div></div><span id="46345"></span><div id="comment-46345" class="comment"><div id="post-46345-score" class="comment-score"></div><div class="comment-text"><p>Jim, just to follow up, I confirmed that "File -&gt; Export Objects -&gt; HTTP" on a http video stream with audio also worked great -- thanks again!</p></div><div id="comment-46345-info" class="comment-info"><span class="comment-age">(02 Oct '15, 10:04)</span> <span class="comment-user userinfo">mfbaker</span></div></div></div><div id="comment-tools-46298" class="comment-tools"></div><div class="clear"></div><div id="comment-46298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

