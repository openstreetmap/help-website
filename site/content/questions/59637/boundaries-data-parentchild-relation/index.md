+++
type = "question"
title = "Boundaries Data Parent/Child Relation"
description = '''Hello Guys, I want to get Multi polygon boundaries from OSM. When I checked OSM documentation, I didn&#x27;t see anything about parent/child relation. for example; Germany/Berlin/Pankow.  When I investigated this topic, I found following projects,  https://wambachers-osm.website/boundaries/ (API service ...'''
date = "2017-09-14T20:52:00Z"
lastmod = "2017-09-15T07:44:00Z"
weight = 59637
keywords = [ "osm" ]
aliases = [ "/questions/59637" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Boundaries Data Parent/Child Relation](/questions/59637/boundaries-data-parentchild-relation)

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
<span id="post-59637-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59637-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-59637-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Guys,</p>
<p>I want to get Multi polygon boundaries from OSM. When I checked OSM documentation, I didn't see anything about parent/child relation. for example; Germany/Berlin/Pankow.</p>
<p>When I investigated this topic, I found following projects,</p>
<ul>
<li><a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a> (API service is not working)</li>
<li><a href="https://github.com/whosonfirst-data/whosonfirst-data">https://github.com/whosonfirst-data/whosonfirst-data</a> (multi polygon data is incorrect)</li>
</ul>
<p>but these projects are not stable, that's why I didn't use.</p>
<p>How can I get Parent/Child information from OSM?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '17, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/be5a07d5cee3af36acbf3c66aa60c932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnalen&#39;s gravatar image" />
<p><span>johnalen</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnalen has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '17, 20:53</strong> </span></p>
</div>
</div>
<div id="comments-container-59637" class="comments-container">
&#10;</div>
<div id="comment-tools-59637" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59637-form-container" class="comment-form-container">
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

<span id="59641"></span>

<div id="answer-container-59641" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59641-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-59641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Typically you need to do spatial queries one way or the other to retrieve "sub"-admin entities of a given admin entity in OSM. You can do this with your own database or for example with overpass-turbo/overpass, example <a href="http://overpass-turbo.eu/s/rJ0">http://overpass-turbo.eu/s/rJ0</a> (Note doing this in a larger way with a public overpass instance is likely going to get you in trouble).</p>
<p>whosonfirst is a product of mapzen and uses something between little and no OSM data. We obviously cannot help you with non-OSM based projects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '17, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '17, 22:16</strong> </span></p>
</div>
</div>
<div id="comments-container-59641" class="comments-container">
&#10;</div>
<div id="comment-tools-59641" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59641-form-container" class="comment-form-container">
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

