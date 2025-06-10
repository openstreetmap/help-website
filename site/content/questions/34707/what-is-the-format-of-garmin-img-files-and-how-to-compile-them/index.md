+++
type = "question"
title = "What is the format of Garmin .img files and how to compile them?"
description = '''I&#x27;m looking for technical details here of how to create my own .img files formatted appropriately for the Garmin. How do you generate these presently via OpenStreetMap?  I assume that I can find the source and methodology behind creating these files somewhere?'''
date = "2014-07-07T21:31:00Z"
lastmod = "2014-07-08T17:00:00Z"
weight = 34707
keywords = [ "gmapsupp", "garmin", "img", "format" ]
aliases = [ "/questions/34707" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What is the format of Garmin .img files and how to compile them?](/questions/34707/what-is-the-format-of-garmin-img-files-and-how-to-compile-them)

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
<span id="post-34707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34707-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-34707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for technical details here of how to create my own .img files formatted appropriately for the Garmin. How do you generate these presently via OpenStreetMap?<br />
</p>
<p>I assume that I can find the source and methodology behind creating these files somewhere?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gmapsupp" rel="tag" title="see questions tagged &#39;gmapsupp&#39;">gmapsupp</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-img" rel="tag" title="see questions tagged &#39;img&#39;">img</span> <span class="post-tag tag-link-format" rel="tag" title="see questions tagged &#39;format&#39;">format</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jul '14, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/13538e5176fda7e559ceed5464d9c401?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bzw&#39;s gravatar image" />
<p><span>bzw</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bzw has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jul '14, 23:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-34707" class="comments-container">
&#10;</div>
<div id="comment-tools-34707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34707-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="34708"></span>

<div id="answer-container-34708" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-34708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34708-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-34708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bzw has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The most widely used software used to create Garmin maps from OSM data is <a href="http://wiki.openstreetmap.org/wiki/Mkgmap">mkgmap</a>. There's lots of information in the OSM wiki, various pre-built styles and many download sites.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '14, 22:28</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-34708" class="comments-container">
<span id="34720"></span>
<div id="comment-34720" class="comment">
<div id="post-34720-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>For an excellent (but slightly out of date) mkgmap tutorial see <a href="http://www.cferrero.net/maps/maps_index.html">http://www.cferrero.net/maps/maps_index.html</a></p>
</div>
<div id="comment-34720-info" class="comment-info">
<span class="comment-age">(08 Jul '14, 11:13)</span> <span class="comment-user userinfo">ligfietser</span>
</div>
</div>
<span id="34734"></span>
<div id="comment-34734" class="comment">
<div id="post-34734-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you!</p>
</div>
<div id="comment-34734-info" class="comment-info">
<span class="comment-age">(08 Jul '14, 17:00)</span> <span class="comment-user userinfo">bzw</span>
</div>
</div>
</div>
<div id="comment-tools-34708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34708-form-container" class="comment-form-container">
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

