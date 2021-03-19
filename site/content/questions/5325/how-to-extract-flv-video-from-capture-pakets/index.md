+++
type = "question"
title = "How to extract flv video from capture pakets."
description = '''Hello Everyone, I have captured a few packets of a video file(flv, from youtube). I stopped capturing the packets after playing a few seconds of it. from the captured packets how can i extract the chunk of video seen. ? Thanks, Arjun '''
date = "2011-07-27T11:13:00Z"
lastmod = "2014-09-16T05:03:00Z"
weight = 5325
keywords = [ "capture", "flv", "packets", "youtube", "wireshark" ]
aliases = [ "/questions/5325" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract flv video from capture pakets.](/questions/5325/how-to-extract-flv-video-from-capture-pakets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5325-score" class="post-score" title="current number of votes">1</div><span id="post-5325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Everyone, I have captured a few packets of a video file(flv, from youtube). I stopped capturing the packets after playing a few seconds of it. from the captured packets how can i extract the chunk of video seen. ?</p><p>Thanks, Arjun</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-flv" rel="tag" title="see questions tagged &#39;flv&#39;">flv</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-youtube" rel="tag" title="see questions tagged &#39;youtube&#39;">youtube</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '11, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/9efda729ccf3d60a6241f17ef05291b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arjun&#39;s gravatar image" /><p><span>Arjun</span><br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arjun has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Sep '11, 11:21</strong> </span></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span></p></div></div><div id="comments-container-5325" class="comments-container"><span id="5335"></span><div id="comment-5335" class="comment"><div id="post-5335-score" class="comment-score"></div><div class="comment-text"><p>Sorry if I haven't made my question clear. I don't want to download it from the source(i.e. youtube). I want to get the chunk of the flv file by joining the capture packets only. If anyone knows about any tool or process. please explain...</p><p>Thanks, Arjun</p></div><div id="comment-5335-info" class="comment-info"><span class="comment-age">(27 Jul '11, 22:04)</span> <span class="comment-user userinfo">Arjun</span></div></div></div><div id="comment-tools-5325" class="comment-tools"></div><div class="clear"></div><div id="comment-5325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5353"></span>

<div id="answer-container-5353" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5353-score" class="post-score" title="current number of votes">3</div><span id="post-5353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Arjun,<br />
<br />
Then you need to <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChIOExportSection.html#ChIOExportObjectsDialog">Export HTTP Objects</a>:<br />
<br />
Go to:<br />
File | Export | Object | HTTP<br />
Look for Content Type: video/x-flv<br />
Select: video/x-flv<br />
Click Save As and save as .flv file<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '11, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-5353" class="comments-container"><span id="32892"></span><div id="comment-32892" class="comment"><div id="post-32892-score" class="comment-score"></div><div class="comment-text"><p>This doesn't work anymore. The traffic is now encrypted and the flash video is broken into streams</p></div><div id="comment-32892-info" class="comment-info"><span class="comment-age">(19 May '14, 06:16)</span> <span class="comment-user userinfo">MikeC</span></div></div><span id="32912"></span><div id="comment-32912" class="comment"><div id="post-32912-score" class="comment-score"></div><div class="comment-text"><p>Yes, I know. I have posted this answer last year on Stackoverflow: <a href="http://stackoverflow.com/questions/17114202/wireshark-getting-flv-video-url-of-youtube/17305321#17305321">http://stackoverflow.com/questions/17114202/wireshark-getting-flv-video-url-of-youtube/17305321#17305321</a> I have to look into it again.</p></div><div id="comment-32912-info" class="comment-info"><span class="comment-age">(19 May '14, 11:39)</span> <span class="comment-user userinfo">joke</span></div></div><span id="36357"></span><div id="comment-36357" class="comment"><div id="post-36357-score" class="comment-score"></div><div class="comment-text"><p>I am trying to do the same now. Youtube streams in TCP packets and the TCP DATA SEGMENT contains the fragmented video files. Has anyone figured out how to combine and play these? I am actually looking for a method to determine the length of each fragment. Any help?</p></div><div id="comment-36357-info" class="comment-info"><span class="comment-age">(16 Sep '14, 05:03)</span> <span class="comment-user userinfo">Qazi</span></div></div></div><div id="comment-tools-5353" class="comment-tools"></div><div class="clear"></div><div id="comment-5353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5326"></span>

<div id="answer-container-5326" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5326-score" class="post-score" title="current number of votes">0</div><span id="post-5326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Watch this video at YouTube:<br />
<a href="http://www.youtube.com/watch?v=5miqHkco7rU">Wireshark tutorial: find yt flv file.</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '11, 11:50</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-5326" class="comments-container"></div><div id="comment-tools-5326" class="comment-tools"></div><div class="clear"></div><div id="comment-5326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

