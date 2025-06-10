+++
type = "question"
title = "Write 17th century street and building names over the modern ones?"
description = '''Hi all! I am trying to make a map of an area of Rome with 17th century street names and buildings. Can I do this over the actual map? Thanks!'''
date = "2022-03-07T23:52:00Z"
lastmod = "2022-03-09T08:22:00Z"
weight = 83748
keywords = [ "rome" ]
aliases = [ "/questions/83748" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Write 17th century street and building names over the modern ones?](/questions/83748/write-17th-century-street-and-building-names-over-the-modern-ones)

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
<span id="post-83748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83748-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all! I am trying to make a map of an area of Rome with 17th century street names and buildings. Can I do this over the actual map? Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rome" rel="tag" title="see questions tagged &#39;rome&#39;">rome</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '22, 23:52</strong></p>
<img src="https://secure.gravatar.com/avatar/e49ab863f10397bc025d450ebb085d25?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baroquerome&#39;s gravatar image" />
<p><span>baroquerome</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baroquerome has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83748" class="comments-container">
&#10;</div>
<div id="comment-tools-83748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83748-form-container" class="comment-form-container">
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

<span id="83750"></span>

<div id="answer-container-83750" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83750-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This would seem to be a bit difficult in OSM itself. While it is completely possible to store an old_name attribute for a street or building, there is no time dimension as such, so there can really be only one such tag per object currently.</p>
<p>Possible solutions:</p>
<ul>
<li>customize a local extract of OSM data, replacing the value of name tags with the ones of your choice. This is reasonably easy, but you will have to render the data yourself (which would be quite easy with tilemaker for vector tiles).</li>
<li>investigate using <a href="https://openhistoricalmap.org/">https://openhistoricalmap.org/</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '22, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Mar '22, 14:08</strong> </span></p>
</div>
</div>
<div id="comments-container-83750" class="comments-container">
<span id="83753"></span>
<div id="comment-83753" class="comment">
<div id="post-83753-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! I will look into it. Hopefully, there is a way to do it along with demarcating the shape of old buildings. I am new to this and don't understand much but I'm a fast learner. Thanks again!</p>
</div>
<div id="comment-83753-info" class="comment-info">
<span class="comment-age">(08 Mar '22, 15:36)</span> <span class="comment-user userinfo">baroquerome</span>
</div>
</div>
<span id="83758"></span>
<div id="comment-83758" class="comment">
<div id="post-83758-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Technically, it's possible to extend date ranges to <code>old_name</code> like e.g. <code>old_name:1921-1932=abc</code>. But there would be many unanswered questions on how to treat historic dates in different calendars. You would also just attach the old name to the current streets without any adjustment of position or adjacent building structure. So looking at OpenHistoricalMap is probably the better option.</p>
</div>
<div id="comment-83758-info" class="comment-info">
<span class="comment-age">(09 Mar '22, 08:22)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-83750" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83750-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83754"></span>

<div id="answer-container-83754" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83754-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'd recommend to contact <a href="https://wiki.openstreetmap.org/wiki/User:Dieterdreist">https://wiki.openstreetmap.org/wiki/User:Dieterdreist</a> (his personal website is <a href="https://23maps.it/en">https://23maps.it/en</a> ) as he has done this in a wonderful way in his nolli-app (<a href="https://www.nolli-app.com">https://www.nolli-app.com</a> ).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '22, 16:07</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83754" class="comments-container">
&#10;</div>
<div id="comment-tools-83754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83754-form-container" class="comment-form-container">
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

