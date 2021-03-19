+++
type = "question"
title = "about RTP .raw file"
description = '''Hi, I captured some telephony call packets using wireshark. The RTP payload types include PCMU and CN(comfort noise) I can play the voice packets using wireshark-&amp;gt;VOIP However,It is not possible to save the payload as .au files using wireshark-&amp;gt;RTP and I can only save them as .raw files. When ...'''
date = "2010-11-22T07:28:00Z"
lastmod = "2012-11-01T02:45:00Z"
weight = 1062
keywords = [ ".raw", "rtp", "voip", ".au" ]
aliases = [ "/questions/1062" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [about RTP .raw file](/questions/1062/about-rtp-raw-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1062-score" class="post-score" title="current number of votes">0</div><span id="post-1062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I captured some telephony call packets using wireshark. The RTP payload types include PCMU and CN(comfort noise) I can play the voice packets using wireshark-&gt;VOIP However,It is not possible to save the payload as .au files using wireshark-&gt;RTP and I can only save them as .raw files. When I play the .raw files using goldwave, the sound is in a mess. what is wrong with the .raw files? thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-.raw" rel="tag" title="see questions tagged &#39;.raw&#39;">.raw</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-.au" rel="tag" title="see questions tagged &#39;.au&#39;">.au</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Nov '10, 07:28</strong></p><img src="https://secure.gravatar.com/avatar/2edef74a36aba8b70b94d9885864e7b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="esolve&#39;s gravatar image" /><p><span>esolve</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="esolve has no accepted answers">0%</span></p></div></div><div id="comments-container-1062" class="comments-container"></div><div id="comment-tools-1062" class="comment-tools"></div><div class="clear"></div><div id="comment-1062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15450"></span>

<div id="answer-container-15450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15450-score" class="post-score" title="current number of votes">0</div><span id="post-15450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have to decode the .raw file with the corresponding codec decoder, and save to .pcm format.</p><p>then open that .pcm file audacity as import--&gt;rawdata, then play the audio.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '12, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/215d9378b10901b1233ef89a5d7cd496?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Binu%20Babu&#39;s gravatar image" /><p><span>Binu Babu</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Binu Babu has one accepted answer">33%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Nov '12, 02:46</strong> </span></p></div></div><div id="comments-container-15450" class="comments-container"></div><div id="comment-tools-15450" class="comment-tools"></div><div class="clear"></div><div id="comment-15450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

