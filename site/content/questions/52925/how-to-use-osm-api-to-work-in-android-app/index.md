+++
type = "question"
title = "How to use OSM api to work in Android App ?"
description = '''I am beginner trying to use osm api. Are there any resources/documentation which give tutorial about how to implement osm api in android. I have been through osmdroid but find difficult to understand. Are there any other resources.  I want to display the information depending upon the point on the P...'''
date = "2016-11-14T04:44:00Z"
lastmod = "2016-11-17T22:51:00Z"
weight = 52925
keywords = [ "api", "osm2pgsql", "mapnik" ]
aliases = [ "/questions/52925" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to use OSM api to work in Android App ?](/questions/52925/how-to-use-osm-api-to-work-in-android-app)

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
<span id="post-52925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am beginner trying to use osm api. Are there any resources/documentation which give tutorial about how to implement osm api in android. I have been through osmdroid but find difficult to understand. Are there any other resources. I want to display the information depending upon the point on the POI.</p>
<p>Has someone done any project and can you share me the code ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '16, 04:44</strong></p>
<img src="https://secure.gravatar.com/avatar/b8ed410dfe4d99a4aaa89627e0542724?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RahulLab&#39;s gravatar image" />
<p><span>RahulLab</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RahulLab has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Nov '16, 22:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-52925" class="comments-container">
&#10;</div>
<div id="comment-tools-52925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52925-form-container" class="comment-form-container">
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

<span id="53023"></span>

<div id="answer-container-53023" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53023-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Documentation about the main "mapping" API is <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">here</a>. However, for displaying information, I'd suggest that you use an instance of the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> API (there are several). Note that most APIs will have some terms of use that you'll need to abide by.</p>
<p>A quick web search finds a bunch of possible examples such as <a href="http://stackoverflow.com/questions/15719398/overpass-api-android-example">here</a>, but if you've not done much with Android before I'd try and get the basics of calling REST services in that environment first. A web search for "android REST example" claims to find "About 25,700,000 results" so there should be plenty to read...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '16, 22:51</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-53023" class="comments-container">
&#10;</div>
<div id="comment-tools-53023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53023-form-container" class="comment-form-container">
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

