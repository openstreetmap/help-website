+++
type = "question"
title = "Integrate OSM in existing Rails App."
description = '''Hi, I am looking for some help setting up openstreetmap in my existing rails app. I am new to the whole maps thing. In my app i am tracking locations of vehicles. now I want to add a feature where I can get the maxspeed, name and type of a road as well. I am considering openstreetmap because I dont ...'''
date = "2017-07-19T13:36:00Z"
lastmod = "2017-07-20T08:35:00Z"
weight = 57179
keywords = [ "postgresql", "private_server", "ruby", "rubyonrails" ]
aliases = [ "/questions/57179" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Integrate OSM in existing Rails App.](/questions/57179/integrate-osm-in-existing-rails-app)

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
<span id="post-57179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57179-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am looking for some help setting up openstreetmap in my existing rails app. I am new to the whole maps thing. In my app i am tracking locations of vehicles. now I want to add a feature where I can get the maxspeed, name and type of a road as well. I am considering openstreetmap because I dont want to make third party api calls for every location I get as the number of locations are greater than 1M per day.</p>
<p>Do I need to duplicate entire schema of OSM? as there are many irrelevant tables in the schema. or simple I should parse the .osm file and create tables for nodes ways and relations only? Also I would need to keep this data updated.</p>
<p>I would really appreciate if any one can point me in the right direction.. or share some links that would help me start?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-private_server" rel="tag" title="see questions tagged &#39;private_server&#39;">private_server</span> <span class="post-tag tag-link-ruby" rel="tag" title="see questions tagged &#39;ruby&#39;">ruby</span> <span class="post-tag tag-link-rubyonrails" rel="tag" title="see questions tagged &#39;rubyonrails&#39;">rubyonrails</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '17, 13:36</strong></p>
<img src="https://secure.gravatar.com/avatar/24fb9e633cb135d94e6a9b4cc4fc6d1f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aitizazk&#39;s gravatar image" />
<p><span>aitizazk</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aitizazk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57179" class="comments-container">
<span id="57182"></span>
<div id="comment-57182" class="comment">
<div id="post-57182-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>crosspost: <a href="https://stackoverflow.com/questions/45190860/integrate-openstreetmap-in-existing-rails-app">https://stackoverflow.com/questions/45190860/integrate-openstreetmap-in-existing-rails-app</a></p>
</div>
<div id="comment-57182-info" class="comment-info">
<span class="comment-age">(19 Jul '17, 16:59)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="57193"></span>
<div id="comment-57193" class="comment">
<div id="post-57193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It would be great if you could help out instead posting crosspost on both platforms...</p>
</div>
<div id="comment-57193-info" class="comment-info">
<span class="comment-age">(20 Jul '17, 08:35)</span> <span class="comment-user userinfo">aitizazk</span>
</div>
</div>
</div>
<div id="comment-tools-57179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57179-form-container" class="comment-form-container">
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

<span id="57180"></span>

<div id="answer-container-57180" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57180-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You definitely don't need to use the OSM API schema and likely a (potentially slimmed down) osm2pgsql schema that actually creates the geometries will be a lot less work than rolling your own.</p>
<p>This will give you an updateable DB that contain as many or as little tags that you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '17, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '17, 15:21</strong> </span></p>
</div>
</div>
<div id="comments-container-57180" class="comments-container">
&#10;</div>
<div id="comment-tools-57180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57180-form-container" class="comment-form-container">
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

