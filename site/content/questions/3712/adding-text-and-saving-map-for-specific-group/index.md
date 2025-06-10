+++
type = "question"
title = "Adding text and saving map for specific group"
description = '''I know very little about Open Street Map, but wondered if it would be a good vehicle for getting local residents to map their own resources for emergency response preparedness. If I wanted to indicate a &quot;command center&quot; in a neighborhood (such as a school) how would I do that? (Insert my own text la...'''
date = "2011-03-11T03:45:00Z"
lastmod = "2011-03-11T07:33:00Z"
weight = 3712
keywords = [ "adding", "group", "customization", "text" ]
aliases = [ "/questions/3712" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding text and saving map for specific group](/questions/3712/adding-text-and-saving-map-for-specific-group)

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
<span id="post-3712-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3712-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3712-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I know very little about Open Street Map, but wondered if it would be a good vehicle for getting local residents to map their own resources for emergency response preparedness. If I wanted to indicate a "command center" in a neighborhood (such as a school) how would I do that? (Insert my own text label.)</p>
<p>Would it be possible to customize for one group of people (such as a neighborhood association) with a password if not all the data was for the public, but might be kept private for the group making the map?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-adding" rel="tag" title="see questions tagged &#39;adding&#39;">adding</span> <span class="post-tag tag-link-group" rel="tag" title="see questions tagged &#39;group&#39;">group</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span> <span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '11, 03:45</strong></p>
<img src="https://secure.gravatar.com/avatar/23288c10e028d30cbf127fe6cbac2d96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Curious5&#39;s gravatar image" />
<p><span>Curious5</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Curious5 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '11, 07:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-3712" class="comments-container">
&#10;</div>
<div id="comment-tools-3712" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3712-form-container" class="comment-form-container">
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

<span id="3713"></span>

<div id="answer-container-3713" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3713-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-3713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most of that data like "use this school for the command center" and "here lives old Bert who will need help leaving his house" do not belong in OpenStreetMap. They exist only be consensus in the group, are not objectively verifiable by other mappers and might violate Bert's right to privacy if available to the whole world. (And data in OpenStreetMap is always available to the whole world for reading and editing, no exceptions.)</p>
<p>But that doesn't mean that you can't use OpenStreetMap. You can use OpenStreetMap as a base layer, store the additional data you want in an own database (or even just a text file) and display them as an overlay in your map. For a simple solution you would save the coordinates of all the locations you need (you can use OpenStreetMap to derive them) and then use a password protected website that shows tiles from OpenStreetMap and markers from your private database using OpenLayers.</p>
<p>For online editing capabilities you would have to create a website that offers either a custom build of potlatch 2 or using an OpenLayers installation with an OpenStreetMap base layer and an interactive vector layer like <a href="http://latlon.org/sketch">http://latlon.org/sketch</a> has. This is obviously quite a bit more work but would allow easy edits by others in your neighborhood.</p>
<p>PS: Some information that is objectively verifiable like the position of fire hydrants is suitable for OpenStreetMap.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '11, 07:33</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '11, 09:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-3713" class="comments-container">
&#10;</div>
<div id="comment-tools-3713" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3713-form-container" class="comment-form-container">
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

