+++
type = "question"
title = "AirBnB dataset: suitable for import?"
description = '''I&#x27;ve founnd a CC0 dataset by AirBnB.  Here&#x27;s an excerpt: id,name,host_name,latitude,longitude,room_type,minimum_nights,number_of_reviews,last_review 77958,BRERA LOVELY WHITE BOAT STUDIO 2,Silvia,45.47117,9.19135,Entire home/apt,2,70,2019-02-25T00:00:00Z  Geocoord quality isn&#x27;t very high (see umap 2)...'''
date = "2019-05-23T13:22:00Z"
lastmod = "2019-05-25T13:10:00Z"
weight = 69279
keywords = [ "airbnb", "import", "guest_house", "chalet", "tourism" ]
aliases = [ "/questions/69279" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [AirBnB dataset: suitable for import?](/questions/69279/airbnb-dataset-suitable-for-import)

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
<span id="post-69279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69279-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've founnd a CC0 dataset by <a href="http://insideairbnb.com/get-the-data.html">AirBnB</a>. Here's an excerpt:</p>
<pre><code>id,name,host_name,latitude,longitude,room_type,minimum_nights,number_of_reviews,last_review
77958,BRERA  LOVELY WHITE BOAT STUDIO 2,Silvia,45.47117,9.19135,Entire home/apt,2,70,2019-02-25T00:00:00Z</code></pre>
<p>Geocoord quality isn't very high (see umap <a href="https://umap.openstreetmap.fr/en/map/airbnb-open-data_329527">2</a>), maybe OSM acceptable, but my doubts are about name (which I guess doesn't show outside): should we map only verifiable elements?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-airbnb" rel="tag" title="see questions tagged &#39;airbnb&#39;">airbnb</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-guest_house" rel="tag" title="see questions tagged &#39;guest_house&#39;">guest_house</span> <span class="post-tag tag-link-chalet" rel="tag" title="see questions tagged &#39;chalet&#39;">chalet</span> <span class="post-tag tag-link-tourism" rel="tag" title="see questions tagged &#39;tourism&#39;">tourism</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 May '19, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/d33efa30f05d8f3604e7210c48b24a8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cascafico&#39;s gravatar image" />
<p><span>Cascafico</span><br />
<span class="score" title="283 reputation points">283</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cascafico has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69279" class="comments-container">
&#10;</div>
<div id="comment-tools-69279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69279-form-container" class="comment-form-container">
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

<span id="69280"></span>

<div id="answer-container-69280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69280-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-69280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, we should only add verifiable elements to OSM. Just because something is CC0 licenced doesn't mean it's appropriate to add here.</p>
<p>You've said yourself that the quality isn't very good so that is another good reason not to add it.</p>
<p>A number of OSM communities around the world are struggling with low quality but liberally licensed crap that was imported in the early days of OSM. Please don't add more!</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 May '19, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-69280" class="comments-container">
<span id="69289"></span>
<div id="comment-69289" class="comment">
<div id="post-69289-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>In addition to concerns about verifiability, the disclaimer on that page says that the locations have been anonymised and may be 150m from the true location, which is quite a large discrepancy.</p>
<p>Also, I don't understand the licensing/copyright/database rights. When I first read your post I thought you meant that AirBnB had made the data available under CC0. But in fact it is anothet website that is making that claim, not AirBnB - wouldn't OpenStreetMap need the licence to be confirmed directly by AirBnB?</p>
</div>
<div id="comment-69289-info" class="comment-info">
<span class="comment-age">(23 May '19, 19:58)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="69297"></span>
<div id="comment-69297" class="comment">
<div id="post-69297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>But in fact it is anothet website that is making that claim, not AirBnB - wouldn't OpenStreetMap need the licence to be confirmed directly by AirBnB?</p>
</blockquote>
<p>Yes, and it is unlikely that we would touch this data even then as it is problematic from other aspects too.</p>
</div>
<div id="comment-69297-info" class="comment-info">
<span class="comment-age">(25 May '19, 13:10)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69280-form-container" class="comment-form-container">
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

