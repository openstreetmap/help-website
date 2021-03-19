+++
type = "question"
title = "What does &quot;linear predictive encoding from xeroc park&quot; mean ? Does it mean voice encoder ?"
description = '''Hi  I found one of the RTP packet has this text &quot;linear predictive encoding from xeroc park&quot;. I am trying to find which encoder might have been used during this communication. Can you please suggest me if it refers to the encoder and if there is any decoder to decode it . Any suggestion appreciated.'''
date = "2015-05-11T00:36:00Z"
lastmod = "2015-05-11T02:24:00Z"
weight = 42292
keywords = [ "encoder", "rtp", "decoder" ]
aliases = [ "/questions/42292" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does "linear predictive encoding from xeroc park" mean ? Does it mean voice encoder ?](/questions/42292/what-does-linear-predictive-encoding-from-xeroc-park-mean-does-it-mean-voice-encoder)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42292-score" class="post-score" title="current number of votes">0</div><span id="post-42292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I found one of the RTP packet has this text "linear predictive encoding from xeroc park". I am trying to find which encoder might have been used during this communication. Can you please suggest me if it refers to the encoder and if there is any decoder to decode it . Any suggestion appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-encoder" rel="tag" title="see questions tagged &#39;encoder&#39;">encoder</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-decoder" rel="tag" title="see questions tagged &#39;decoder&#39;">decoder</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '15, 00:36</strong></p><img src="https://secure.gravatar.com/avatar/4ec917e3556fb6d9c03cc0e39ec7732a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shas&#39;s gravatar image" /><p><span>Shas</span><br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shas has no accepted answers">0%</span></p></div></div><div id="comments-container-42292" class="comments-container"></div><div id="comment-tools-42292" class="comment-tools"></div><div class="clear"></div><div id="comment-42292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42294"></span>

<div id="answer-container-42294" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42294-score" class="post-score" title="current number of votes">0</div><span id="post-42294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To quote <a href="http://tools.ietf.org/html/rfc1890">RFC 1890</a>, "RTP Profile for Audio and Video Conferences with Minimal Control":</p><pre><code>4.4.9 LPC

  LPC designates an experimental linear predictive encoding contributed
  by Ron Frederick, Xerox PARC, which is based on an implementation
  written by Ron Zuckerman, Motorola, posted to the Usenet group
  comp.dsp on June 26, 1992.</code></pre><p>and</p><pre><code>LPC

   An implementation is available at

            ftp://parcftp.xerox.com/pub/net-research/lpc.tar.Z</code></pre><p>although that FTP server doesn't seem to be working.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '15, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-42294" class="comments-container"><span id="42295"></span><div id="comment-42295" class="comment"><div id="post-42295-score" class="comment-score"></div><div class="comment-text"><p><span>@Guy Harris</span>, Thanks. This session was captured during voip communication by a reputed app. I am surprised, some apps still using it. Isnt it too old to use ?</p></div><div id="comment-42295-info" class="comment-info"><span class="comment-age">(11 May '15, 02:24)</span> <span class="comment-user userinfo">Shas</span></div></div></div><div id="comment-tools-42294" class="comment-tools"></div><div class="clear"></div><div id="comment-42294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

