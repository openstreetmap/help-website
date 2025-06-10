+++
type = "question"
title = "Import of private maps"
description = '''Hi Team, Does openstreetmap support import of map from map providers like LeadDog or DigitalGlobe or we can import only openstreetmap map only. Can you please point me to the guide on importing of other map data, if supported. Thanks'''
date = "2018-05-27T08:39:00Z"
lastmod = "2018-05-27T09:45:00Z"
weight = 63757
keywords = [ "map" ]
aliases = [ "/questions/63757" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Import of private maps](/questions/63757/import-of-private-maps)

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
<span id="post-63757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63757-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Team,</p>
<p>Does openstreetmap support import of map from map providers like LeadDog or DigitalGlobe or we can import only openstreetmap map only. Can you please point me to the guide on importing of other map data, if supported.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 May '18, 08:39</strong></p>
<img src="https://secure.gravatar.com/avatar/1c8154cf6e206c8009a6901c7b2661e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jiten19851985&#39;s gravatar image" />
<p><span>jiten19851985</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jiten19851985 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63757" class="comments-container">
&#10;</div>
<div id="comment-tools-63757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63757-form-container" class="comment-form-container">
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

<span id="63758"></span>

<div id="answer-container-63758" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63758-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-63758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is likely using terminology that has certain meanings in the context of OSM that you probably don't mean.</p>
<p>Could you for starters explain what you mean by "openstreetmap", the website, the OSM data, a third party application?</p>
<p>If you simply want to -display- data from a third party on top of OpenStreetMap derived maps, you could for example use <a href="umap.openstreetmap.fr">umap</a> or roll your own web app with <a href="https://leafletjs.com/">Leaflet</a> or <a href="https://openlayers.org/">openlayers</a>.</p>
<p>If you are building your own mapstyle, you can naturally import the 3rd party data into your rendering database and use from there.</p>
<p>Importing data in to the OSM dataset requires that</p>
<ul>
<li>the data is available under a suitable licence</li>
<li>you have community support for the import</li>
<li>and the data models fetures or properties that actually make sense in a general purpose geo-dataset</li>
</ul>
<p>You can find more on that here <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">Import Guidelines</a> but as already said it seems unlikely that that is what you really want to do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 May '18, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 May '18, 09:47</strong> </span></p>
</div>
</div>
<div id="comments-container-63758" class="comments-container">
&#10;</div>
<div id="comment-tools-63758" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63758-form-container" class="comment-form-container">
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

