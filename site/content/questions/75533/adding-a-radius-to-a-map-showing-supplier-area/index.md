+++
type = "question"
title = "Adding a radius to a map showing supplier area"
description = '''Can anyone tell me an HTML/CSS method of adding a radius to a map embed code that will put a circle around a central point on that map.  For example, here is my store and I will deliver in this radius (20km for example) I know this can be done in Google maps, but is there a similar option in OSM?'''
date = "2020-07-04T17:00:00Z"
lastmod = "2020-07-05T18:18:00Z"
weight = 75533
keywords = [ "drawn", "map", "radius", "on" ]
aliases = [ "/questions/75533" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding a radius to a map showing supplier area](/questions/75533/adding-a-radius-to-a-map-showing-supplier-area)

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
<span id="post-75533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75533-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-75533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can anyone tell me an HTML/CSS method of adding a radius to a map embed code that will put a circle around a central point on that map. For example, here is my store and I will deliver in this radius (20km for example) I know this can be done in Google maps, but is there a similar option in OSM?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-drawn" rel="tag" title="see questions tagged &#39;drawn&#39;">drawn</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span> <span class="post-tag tag-link-on" rel="tag" title="see questions tagged &#39;on&#39;">on</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jul '20, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/609f5bdfbbfe2c669dd61350d66ebf27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Midrob&#39;s gravatar image" />
<p><span>Midrob</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Midrob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75533" class="comments-container">
<span id="75536"></span>
<div id="comment-75536" class="comment">
<div id="post-75536-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There are a variety of tools used to display OpenStreetMap data on websites. If you could indicate which you intend to use this may help people respond to your query.</p>
</div>
<div id="comment-75536-info" class="comment-info">
<span class="comment-age">(04 Jul '20, 18:42)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="75548"></span>
<div id="comment-75548" class="comment">
<div id="post-75548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The intended use is to have the location of a business centred on a panel onsite, say 800px x 400px wide, and to then have a circle around that location, to a scale, say 20km/miles, and to have the circle with an opacity setting so you can see the map under it. This circle would enclose a delivery area. See how Google do something similar.</p>
<p>Can this be done in OSM ? A circle, not a polygon. <a href="https://indicaonline.zendesk.com/hc/en-us/articles/115012507087-Creating-Delivery-Zones-Using-Google-Maps">Google suggestion on this</a></p>
</div>
<div id="comment-75548-info" class="comment-info">
<span class="comment-age">(05 Jul '20, 16:51)</span> <span class="comment-user userinfo">Midrob</span>
</div>
</div>
</div>
<div id="comment-tools-75533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75533-form-container" class="comment-form-container">
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

<span id="75550"></span>

<div id="answer-container-75550" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75550-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use leafletJS to display the map and than use the following leaflet codeline adjusted to your needs:</p>
<pre><code>L.circle([lat,lng], radius).addTo(map);</code></pre>
<p>See this for more: <a href="https://leafletjs.com/reference-1.6.0.html#circle">https://leafletjs.com/reference-1.6.0.html#circle</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '20, 18:18</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '20, 18:22</strong> </span></p>
</div>
</div>
<div id="comments-container-75550" class="comments-container">
&#10;</div>
<div id="comment-tools-75550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75550-form-container" class="comment-form-container">
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

