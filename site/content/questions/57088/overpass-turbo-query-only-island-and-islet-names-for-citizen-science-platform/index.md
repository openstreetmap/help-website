+++
type = "question"
title = "Overpass turbo: Query only Island and Islet names for Citizen Science platform"
description = '''Hi! We have developed a Citizen Science platform where people can upload pictures of coasts to a world map to help Science study the risks of sea-level rise (www.coastwards.org). The images are placed automatically with help of the embedded GPS data - if available. If not, we ask the participant to ...'''
date = "2017-07-14T11:40:00Z"
lastmod = "2017-07-14T19:00:00Z"
weight = 57088
keywords = [ "islets", "islands", "overpass-turbo" ]
aliases = [ "/questions/57088" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass turbo: Query only Island and Islet names for Citizen Science platform](/questions/57088/overpass-turbo-query-only-island-and-islet-names-for-citizen-science-platform)

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
<span id="post-57088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57088-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi!</p>
<p>We have developed a Citizen Science platform where people can upload pictures of coasts to a world map to help Science study the risks of sea-level rise (<a href="http://www.coastwards.org">www.coastwards.org</a>). The images are placed automatically with help of the embedded GPS data - if available. If not, we ask the participant to place the image for us. And here lies the problem: Small islands and islets are very hard to find on the map because the name labels appear too late for people to orient themselves in the vast blue oceans.</p>
<p>We use Mapbox to style and display the world map on the website. Their support pointed us to Overpass Turbo saying we could query the OSM database to create a new layer of island and islet names to appear at an earlier zoom level. However, I am having trouble building the query as I am new to OSM QL. This is what I have so far:</p>
<pre><code>way[&quot;natural&quot;=&quot;coastline&quot;]({{bbox}});
node
(around:100)
[&quot;place&quot;=&quot;island&quot;]
[name];
out body;
&#10;way[&quot;natural&quot;=&quot;coastline&quot;]({{bbox}});
node
(around:100)
[&quot;place&quot;=&quot;islet&quot;]
[name];
out body;</code></pre>
<p>As you can imagine, this query is rejected by the server depending on the bounding box I use which makes me doubt if there is a way to query this kind of information for the entire world at all. Also, since this layer already exists in the OSM base map, isn't there a faster way to get hold of it?</p>
<p>I hope someone can point me in the right direction as to how to solve this problem. Any comment or indication will be very much appreciated. Thank you so much!</p>
<p>Maureen</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-islets" rel="tag" title="see questions tagged &#39;islets&#39;">islets</span> <span class="post-tag tag-link-islands" rel="tag" title="see questions tagged &#39;islands&#39;">islands</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '17, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/9a8f5111aef88fb6ed8f14f5abee7e3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coastwards&#39;s gravatar image" />
<p><span>coastwards</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coastwards has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57088" class="comments-container">
&#10;</div>
<div id="comment-tools-57088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57088-form-container" class="comment-form-container">
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

<span id="57091"></span>

<div id="answer-container-57091" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57091-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you really need to retrieve this information via the overpass-api?</p>
<p>As the data should be fairly static a one time (or seldom updated) extract from a planet dump or asking somebody to give you the results of querying their database would seem to be good enough.</p>
<p>See for example <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">http://wiki.openstreetmap.org/wiki/Osmfilter</a> and <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">http://wiki.openstreetmap.org/wiki/Osmfilter</a> for the planet dumps. Naturally there are many ways to skin a cat and this is just one of them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '17, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-57091" class="comments-container">
<span id="57092"></span>
<div id="comment-57092" class="comment">
<div id="post-57092-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No I don't, you're absolutely right, I only need to query this information once. (I'm still lost in the OSM world and discovering what's possible) I will investigate osmfilter. Thanks for pointing me in the right direction!</p>
</div>
<div id="comment-57092-info" class="comment-info">
<span class="comment-age">(14 Jul '17, 12:29)</span> <span class="comment-user userinfo">coastwards</span>
</div>
</div>
</div>
<div id="comment-tools-57091" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57091-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57093"></span>

<div id="answer-container-57093" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57093-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you "use Mapbox to style and display the world map on the website" couldn't you just display island names a bit sooner?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '17, 12:39</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-57093" class="comments-container">
<span id="57101"></span>
<div id="comment-57101" class="comment">
<div id="post-57101-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also thought that was possible but support told me "the zoom level range is automatically chosen based on your data's features and isn't customizable. We do this with your custom tilesets as well as our Mapbox Streets tilesets in order minimize the amount of data included and ensure these layers are is as fast as possible."</p>
</div>
<div id="comment-57101-info" class="comment-info">
<span class="comment-age">(14 Jul '17, 19:00)</span> <span class="comment-user userinfo">coastwards</span>
</div>
</div>
</div>
<div id="comment-tools-57093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57093-form-container" class="comment-form-container">
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

