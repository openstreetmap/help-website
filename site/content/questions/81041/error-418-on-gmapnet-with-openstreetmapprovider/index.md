+++
type = "question"
title = "error 418 on Gmap.net with OpenStreetMapProvider"
description = '''Good day. I create a desktop application using gmap.net  GMap.NET.MapProviders.GMapProvider.UserAgent = &quot;cferreira GMap tool 1.0&quot; GMP.MapProvider = GMap.NET.MapProviders.OpenStreetMapProvider.Instance However, I get an error 418, please tell me how to make the map display. Other providers such as go...'''
date = "2021-07-21T12:27:00Z"
lastmod = "2021-07-21T12:47:00Z"
weight = 81041
keywords = [ "gmap" ]
aliases = [ "/questions/81041" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [error 418 on Gmap.net with OpenStreetMapProvider](/questions/81041/error-418-on-gmapnet-with-openstreetmapprovider)

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
<span id="post-81041-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81041-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81041-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good day. I create a desktop application using gmap.net</p>
<p>GMap.NET.MapProviders.GMapProvider.UserAgent = "cferreira GMap tool 1.0" GMP.MapProvider = GMap.NET.MapProviders.OpenStreetMapProvider.Instance</p>
<p>However, I get an error 418, please tell me how to make the map display. Other providers such as google yandex and others work. But I would like to work with OpenStreetMap</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gmap" rel="tag" title="see questions tagged &#39;gmap&#39;">gmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '21, 12:27</strong></p>
<img src="https://secure.gravatar.com/avatar/e6e9361cdaab80ff359ba9fd71713bb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Red_sashka&#39;s gravatar image" />
<p><span>Red_sashka</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Red_sashka has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81041" class="comments-container">
&#10;</div>
<div id="comment-tools-81041" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81041-form-container" class="comment-form-container">
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

<span id="81044"></span>

<div id="answer-container-81044" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81044-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OpenStreetMap's Tile Usage Policy can be found <a href="https://operations.osmfoundation.org/policies/tiles/">here</a>. The error that you are seeing suggests that you are not complying with that policy.</p>
<p>If you don't understand the previous sentence, or what the tile usage policy requires you to do, then you'll need to contact your tool provider, in this case gmap.net, about it.</p>
<p>Note that the policy says "<strong>OpenStreetMap data is free for everyone to use. Our tile servers are not.</strong>". If you're creating some sort of product that relies on accessing OpenStreetMap's tiles then you and your customers can expect to see the error that you are getting.</p>
<p>You are, of course, available to create your own tiles from OpenStreetMap data, or use a third-party provider of tiles.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '21, 12:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81044" class="comments-container">
&#10;</div>
<div id="comment-tools-81044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81044-form-container" class="comment-form-container">
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

