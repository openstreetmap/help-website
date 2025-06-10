+++
type = "question"
title = "live GPS Trace"
description = '''Howdy everyone!  I am currently working on a project where I would like to overlay a live GPS trail onto a blank background, to create an effect similar to the &#x27;GPS traces&#x27; on this website. I was just wondering if this is at all possible, and if so, how I should go about doing this.  I know its a bi...'''
date = "2010-12-02T14:55:00Z"
lastmod = "2011-03-10T16:58:00Z"
weight = 1705
keywords = [ "live", "traces", "gps" ]
aliases = [ "/questions/1705" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [live GPS Trace](/questions/1705/live-gps-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Howdy everyone!</p>
<p>I am currently working on a project where I would like to overlay a live GPS trail onto a blank background, to create an effect similar to the 'GPS traces' on this website. I was just wondering if this is at all possible, and if so, how I should go about doing this.</p>
<p>I know its a bit vague, but any help/suggestions would be much appreciated!</p>
<p>Thanks, Roy</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-live" rel="tag" title="see questions tagged &#39;live&#39;">live</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-gps" rel="tag" title="see questions tagged &#39;gps&#39;">gps</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Dec '10, 14:55</strong></p>
<img src="https://secure.gravatar.com/avatar/8045ceb7bee6696ca6376a288b6fbce3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Royrog&#39;s gravatar image" />
<p><span>Royrog</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Royrog has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1705" class="comments-container">
<span id="3304"></span>
<div id="comment-3304" class="comment">
<div id="post-3304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would you add some more details? It is your project Web based or is an application intended for a desktop computer, mobile phone, etc? When you say "live" do you mean a live signal coming from a GPS or animating a previous recorded GPS track?</p>
</div>
<div id="comment-3304-info" class="comment-info">
<span class="comment-age">(23 Feb '11, 10:27)</span> <span class="comment-user userinfo">temporalista</span>
</div>
</div>
<span id="3698"></span>
<div id="comment-3698" class="comment">
<div id="post-3698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't forget to accept an answer (the round checkmark button).</p>
</div>
<div id="comment-3698-info" class="comment-info">
<span class="comment-age">(10 Mar '11, 16:58)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-1705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1705-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1709"></span>

<div id="answer-container-1709" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1709-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1709-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1709-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Roy,</p>
<p>Many GPS receivers can be made to behave like serial devices. They will provide position information every so often, and you can generally configure how often. So yes, you can capture that serial data, and provide it you whatever tools you wish to work with, to consume the data and plot a location on screen, or paper, or whatever your output device of choice might be.<br />
</p>
<p>Some navigation software will accept live gps data to place your position on a moving map. Perhaps have a look at <a href="http://wiki.openstreetmap.org/wiki/Gpsdrive">GPSDrive</a> to see if that gives you any ideas.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '10, 17:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d90ea04df82d77f534659f08894dd889?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Weait&#39;s gravatar image" />
<p><span>Richard Weait</span><br />
<span class="score" title="3044 reputation points"><span>3.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="34 badges"><span class="silver">●</span><span class="badgecount">34</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Weait has 8 accepted answers">17%</span> </br></br></p>
</div>
</div>
<div id="comments-container-1709" class="comments-container">
&#10;</div>
<div id="comment-tools-1709" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1709-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3316"></span>

<div id="answer-container-3316" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3316-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-3316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The Garmin Oregon, and presumably Colorado, and their lowest-end trail-user models that aren't capable of navigation, can all do this out of the box. With the Colorado and Oregon units, you may have to turn off all map layers first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Feb '11, 22:13</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-3316" class="comments-container">
&#10;</div>
<div id="comment-tools-3316" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3316-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

