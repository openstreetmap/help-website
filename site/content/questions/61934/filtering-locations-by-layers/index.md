+++
type = "question"
title = "Filtering Locations by Layers"
description = '''Hi all, I would like to filter locations in a map with regard of multiple values. With &quot;Filtering&quot; I mean to blend out layers / locations which are not of interest. For instance, I want to find all places in my map which have a size of 21-50sqm AND can host 51-100 people.  My desired structure of la...'''
date = "2018-02-02T16:25:00Z"
lastmod = "2018-02-03T09:45:00Z"
weight = 61934
keywords = [ "filter", "layers", "sublayers" ]
aliases = [ "/questions/61934" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering Locations by Layers](/questions/61934/filtering-locations-by-layers)

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
<span id="post-61934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61934-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I would like to filter locations in a map with regard of multiple values. With "Filtering" I mean to blend out layers / locations which are not of interest. For instance, I want to find all places in my map which have a size of 21-50sqm AND can host 51-100 people.</p>
<p>My desired structure of layers looks like this:</p>
<p><strong>1. Size</strong></p>
<p><strong>1.1</strong> 1-20 sqm <em>(disabled)</em></p>
<p><strong>1.2</strong> 21-50 sqm <em>(visible)</em></p>
<p><strong>1.3</strong> 51-100 sqm <em>(disabled)</em></p>
<p><strong>2. Capacity</strong></p>
<p><strong>2.1</strong> 10-50 people <em>(disabled)</em></p>
<p><strong>2.2</strong> 51-100 people <em>(visible)</em></p>
<p><strong>2.3</strong> 101-200 <em>(disabled)</em></p>
<p>I have found a tool which can solve this issue but doesn't support other features that I will need. Nevertheless, I want to share it with you to express better my need: <a href="https://www.geosheets.com/map/s:L5J0wAYM/real-estate-analysis">https://www.geosheets.com/map/s:L5J0wAYM/real-estate-analysis</a></p>
<p>Can you help me, how I could realise this with OSM + uMAP?</p>
<p>Thanks a lot, Anne</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-sublayers" rel="tag" title="see questions tagged &#39;sublayers&#39;">sublayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Feb '18, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/75dae34fb2138a92113aec8084ca8720?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aboenemann&#39;s gravatar image" />
<p><span>aboenemann</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aboenemann has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61934" class="comments-container">
<span id="61936"></span>
<div id="comment-61936" class="comment">
<div id="post-61936-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you clarify what you mean when you say "find all places"? What do you define as a place in this context? Restaurants? Residential buildings? Any building that has been mapped? Capacity could be difficult, because this isn't something that's typically recorded for most POIs.</p>
</div>
<div id="comment-61936-info" class="comment-info">
<span class="comment-age">(02 Feb '18, 16:38)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="61942"></span>
<div id="comment-61942" class="comment">
<div id="post-61942-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Let's say, I have 100 places. Only 20 of these 100 have a size of 21-50sqm. And 15 of these 20 have a capacity of 51-100 people. The overlap of places which have as well a size of 21-50sqm and a capacity of 51-100 is 15. Consequently, I want to "find all these 15 places".</p>
<p>It is not important of which type these places are. They are place marks that I set myself. Also the Capacity is a value that I add myself.</p>
</div>
<div id="comment-61942-info" class="comment-info">
<span class="comment-age">(03 Feb '18, 09:45)</span> <span class="comment-user userinfo">aboenemann</span>
</div>
</div>
</div>
<div id="comment-tools-61934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61934-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

