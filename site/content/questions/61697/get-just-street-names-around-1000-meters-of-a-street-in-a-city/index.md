+++
type = "question"
title = "Get just street names around 1000 meters of a street in a city"
description = '''Hi, I need to have a list of just street name around a given street ina given city in a certain range. Is it possible? I wuold need in json format'''
date = "2018-01-18T09:18:00Z"
lastmod = "2018-01-19T04:15:00Z"
weight = 61697
keywords = [ "city", "street", "streetnames", "around" ]
aliases = [ "/questions/61697" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get just street names around 1000 meters of a street in a city](/questions/61697/get-just-street-names-around-1000-meters-of-a-street-in-a-city)

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
<span id="post-61697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61697-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I need to have a list of just street name around a given street ina given city in a certain range. Is it possible? I wuold need in json format</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Jan '18, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/5377ce75ca8fc8f9b5a24116ebc640b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikfaina&#39;s gravatar image" />
<p><span>mikfaina</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikfaina has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jan '18, 09:35</strong> </span></p>
</div>
</div>
<div id="comments-container-61697" class="comments-container">
&#10;</div>
<div id="comment-tools-61697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61697-form-container" class="comment-form-container">
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

<span id="61708"></span>

<div id="answer-container-61708" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61708-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's an example Overpass API script that searches the visible area for a particular named street and then outputs the names of nearby streets:</p>
<p><a href="http://overpass-turbo.eu/s/v4f">http://overpass-turbo.eu/s/v4f</a></p>
<p>Click "Run" there without moving the map much (or "Bluegrass Drive" won't be found). I don't think there is a way to make the output any simpler.</p>
<p>You could adjust the script to use some other method of finding the starting street. There's quite a few options <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jan '18, 04:15</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-61708" class="comments-container">
&#10;</div>
<div id="comment-tools-61708" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61708-form-container" class="comment-form-container">
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

