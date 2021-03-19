+++
type = "question"
title = "Playback mp3 rtp packets"
description = '''Hi, I have captured rtp packets containing mp3 data. I would like to play them back. I have already tried several things but with no success (e.g saving payload as raw data). I hope someone can help me finding a solution. Thanks in advance.'''
date = "2014-04-25T03:02:00Z"
lastmod = "2014-04-28T02:45:00Z"
weight = 32172
keywords = [ "playback", "decode_rtp", "udp", "mp3", "rtp" ]
aliases = [ "/questions/32172" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Playback mp3 rtp packets](/questions/32172/playback-mp3-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32172-score" class="post-score" title="current number of votes">0</div><span id="post-32172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have captured rtp packets containing mp3 data. I would like to play them back. I have already tried several things but with no success (e.g saving payload as raw data).</p><p>I hope someone can help me finding a solution.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-playback" rel="tag" title="see questions tagged &#39;playback&#39;">playback</span> <span class="post-tag tag-link-decode_rtp" rel="tag" title="see questions tagged &#39;decode_rtp&#39;">decode_rtp</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-mp3" rel="tag" title="see questions tagged &#39;mp3&#39;">mp3</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '14, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/959f12bcf0d04bb5c93176a58ee331aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jpa&#39;s gravatar image" /><p><span>jpa</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jpa has no accepted answers">0%</span></p></div></div><div id="comments-container-32172" class="comments-container"></div><div id="comment-tools-32172" class="comment-tools"></div><div class="clear"></div><div id="comment-32172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32195"></span>

<div id="answer-container-32195" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32195-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32195-score" class="post-score" title="current number of votes">1</div><span id="post-32195-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do that directly with Wireshark as the RTP player does not support MP3. You can try to use one of the following tools (both written in Perl) to extract the RTP data and the play it with your preferred MP3 player software, <strong>if the extraction creates a valid MP3 file</strong> !!</p><blockquote><p><a href="http://wiki.wireshark.org/RtpDumpScript">http://wiki.wireshark.org/RtpDumpScript</a><br />
<a href="http://cpansearch.perl.org/src/SULLR/Net-Inspect-0.303/tools/rtpxtract.pl">http://cpansearch.perl.org/src/SULLR/Net-Inspect-0.303/tools/rtpxtract.pl</a></p></blockquote><p>See also my answer to a similar question</p><blockquote><p><a href="http://ask.wireshark.org/questions/21193/extracting-rtp-payload-and-dumping-to-a-ts-file">http://ask.wireshark.org/questions/21193/extracting-rtp-payload-and-dumping-to-a-ts-file</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '14, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-32195" class="comments-container"><span id="32237"></span><div id="comment-32237" class="comment"><div id="post-32237-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>Thanks for your hints, I'm gonna try.</p><p>Regards, Julien.</p></div><div id="comment-32237-info" class="comment-info"><span class="comment-age">(28 Apr '14, 02:45)</span> <span class="comment-user userinfo">jpa</span></div></div></div><div id="comment-tools-32195" class="comment-tools"></div><div class="clear"></div><div id="comment-32195-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

