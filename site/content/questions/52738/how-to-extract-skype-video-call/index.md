+++
type = "question"
title = "how to extract skype video call"
description = '''Hi, there, I sniffed a trace of skype video call which was with my friend, how can I extract the video out and save it as mp4?  I used wireshark v2.0.2 on WIN7 64bit with service pack 1. thank you.'''
date = "2016-05-18T09:15:00Z"
lastmod = "2016-05-19T07:49:00Z"
weight = 52738
keywords = [ "call", "video", "extract", "skype" ]
aliases = [ "/questions/52738" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to extract skype video call](/questions/52738/how-to-extract-skype-video-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52738-score" class="post-score" title="current number of votes">0</div><span id="post-52738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, there,</p><p>I sniffed a trace of skype video call which was with my friend, how can I extract the video out and save it as mp4? I used wireshark v2.0.2 on WIN7 64bit with service pack 1. thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-call" rel="tag" title="see questions tagged &#39;call&#39;">call</span> <span class="post-tag tag-link-video" rel="tag" title="see questions tagged &#39;video&#39;">video</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-skype" rel="tag" title="see questions tagged &#39;skype&#39;">skype</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/97a9c875023d779173deb3a7fa4d17c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="metz2086&#39;s gravatar image" /><p><span>metz2086</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="metz2086 has no accepted answers">0%</span></p></div></div><div id="comments-container-52738" class="comments-container"></div><div id="comment-tools-52738" class="comment-tools"></div><div class="clear"></div><div id="comment-52738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52740"></span>

<div id="answer-container-52740" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52740-score" class="post-score" title="current number of votes">0</div><span id="post-52740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Short answer: you can't.</p><p>Skype is a proprietary protocol which no one has yet fully <a href="https://en.wikipedia.org/wiki/Reverse_engineering">reverse engineered</a>. There is a <a href="https://wiki.wireshark.org/Skype">Skype page</a> on Wireshark's wiki to describe and collect information about the protocol.</p><p>Even if we did understand the protocol better, Skype communications are (so they say) encrypted (meaning you still wouldn't be able to extract the video--unless one could break the encryption).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 May '16, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52740" class="comments-container"><span id="52766"></span><div id="comment-52766" class="comment"><div id="post-52766-score" class="comment-score"></div><div class="comment-text"><p>thanks for the comments. i was meant to say that i had a video call directly with my friend and i sniffed that call with wireshark, i was not the third person and was not outside of the call. suppose that call was decrypted in my pc, wireshark should be able to get all the traffic of that call, including UDP and RTP packets, so how can i get the video stream out and save it as mp4?</p></div><div id="comment-52766-info" class="comment-info"><span class="comment-age">(19 May '16, 07:08)</span> <span class="comment-user userinfo">metz2086</span></div></div><span id="52768"></span><div id="comment-52768" class="comment"><div id="post-52768-score" class="comment-score"></div><div class="comment-text"><p>Wireshark will capture the traffic seen by your network interface, which will still have been encrypted. The Skype client application on your PC will have decrypted the traffic, and at that point it's out of reach of Wireshark (or any <strong>network</strong> sniffer).</p></div><div id="comment-52768-info" class="comment-info"><span class="comment-age">(19 May '16, 07:17)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="52770"></span><div id="comment-52770" class="comment"><div id="post-52770-score" class="comment-score"></div><div class="comment-text"><p>The reason why a capture from network interface can be decrypted in case of e.g. https is that, in contrary to skype, the encryption method is publicly known and if you are one of the conversation parties (the client or the server), you can obtain the data used as encryption key for the tls session. In case of Skype, you lack both the knowledge of the encryption method and the key material even if you are one of the conversation parties. Which btw also means that you cannot learn what else, in addition to your audio and video, Skype sends out from your PC.</p></div><div id="comment-52770-info" class="comment-info"><span class="comment-age">(19 May '16, 07:49)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-52740" class="comment-tools"></div><div class="clear"></div><div id="comment-52740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

