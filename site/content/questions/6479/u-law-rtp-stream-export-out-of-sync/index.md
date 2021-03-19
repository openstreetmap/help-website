+++
type = "question"
title = "U-Law RTP Stream export out of Sync"
description = '''Hi, i capture Voip Traffic and export the U-Law encoded payload to an au file as described in the online manual. Unfortunately forward and reverse directions are not in sync. The incoming channel is always significantly shorter than the outgoing channel. From the quality analysis it sounds like the ...'''
date = "2011-09-21T09:56:00Z"
lastmod = "2011-09-28T02:34:00Z"
weight = 6479
keywords = [ "voip", "sip", "synchron", "rtp", "analysis" ]
aliases = [ "/questions/6479" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [U-Law RTP Stream export out of Sync](/questions/6479/u-law-rtp-stream-export-out-of-sync)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6479-score" class="post-score" title="current number of votes">0</div><span id="post-6479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>i capture Voip Traffic and export the U-Law encoded payload to an au file as described in the online manual.</p><p>Unfortunately forward and reverse directions are not in sync. The incoming channel is always significantly shorter than the outgoing channel. From the quality analysis it sounds like the incoming channel is missing the silence packets. Or in other words. In the incoming channel, the silence periods are much shorter than they have been in the actual conversation. I believe, that silence Supression is used in this case.</p><p>Is there a way to export the RTP Payload and make sure that the exported Soundfile is in sync?</p><p>If the conversation is encoded using G711 A-law or G721, then the export is always in sync.</p><p>Anyone knows what the issue is?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-voip" rel="tag" title="see questions tagged &#39;voip&#39;">voip</span> <span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-synchron" rel="tag" title="see questions tagged &#39;synchron&#39;">synchron</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '11, 09:56</strong></p><img src="https://secure.gravatar.com/avatar/b654bf7fd90c1cdaeeb7437621820963?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rocket&#39;s gravatar image" /><p><span>Rocket</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rocket has no accepted answers">0%</span></p></div></div><div id="comments-container-6479" class="comments-container"></div><div id="comment-tools-6479" class="comment-tools"></div><div class="clear"></div><div id="comment-6479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6482"></span>

<div id="answer-container-6482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6482-score" class="post-score" title="current number of votes">0</div><span id="post-6482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Only standard G.711 A-law and µ-law streams are supported. Otherwise you'll have to save the RTP payloads and process the offline.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '11, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6482" class="comments-container"><span id="6610"></span><div id="comment-6610" class="comment"><div id="post-6610-score" class="comment-score"></div><div class="comment-text"><p>I understand that.</p><p>My Question is, why are u-law streams not in Sync, while A-Law streams are.</p><p>I'm not asking how to process them offline. I know how to do it.</p><p>I want to know what causes the streams to go out of sync.</p></div><div id="comment-6610-info" class="comment-info"><span class="comment-age">(28 Sep '11, 02:00)</span> <span class="comment-user userinfo">Rocket</span></div></div><span id="6612"></span><div id="comment-6612" class="comment"><div id="post-6612-score" class="comment-score"></div><div class="comment-text"><p>There is no difference based on the encoding, there's a difference when the RTP streams are different. Somehow your observed installation behaves differently under different circumstances.</p></div><div id="comment-6612-info" class="comment-info"><span class="comment-age">(28 Sep '11, 02:34)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-6482" class="comment-tools"></div><div class="clear"></div><div id="comment-6482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

