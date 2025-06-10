+++
type = "question"
title = "How to use javascript to display marker for an address?"
description = '''I have a map inside a Confluence wiki page, and using PocketQuery I get the addresses I want to display from my DB.  What&#x27;s the most direct way to do the Nominatim request and the Leaflet marker placement? I can generate code that looks like this:  &amp;lt;script&amp;gt;  #foreach($person in $result)  $.get...'''
date = "2015-11-06T10:13:00Z"
lastmod = "2015-11-14T20:58:00Z"
weight = 46425
keywords = [ "leaflet", "json", "nominatim" ]
aliases = [ "/questions/46425" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use javascript to display marker for an address?](/questions/46425/how-to-use-javascript-to-display-marker-for-an-address)

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
<span id="post-46425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46425-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a map inside a Confluence wiki page, and using PocketQuery I get the addresses I want to display from my DB.</p>
<p>What's the most direct way to do the Nominatim request and the Leaflet marker placement?</p>
<p>I can generate code that looks like this:</p>
<pre><code>    &lt;script&gt;
    #foreach($person in $result)
    $.getJSON(&#39;https://nominatim.openstreetmap.org/search/$person.strasse $person.hausnummer ,$person.plz?format=json&#39;, cbMarker);
    function cbMarker(data){
      L.marker([data.lat, data.lon], {title: &#39;$person.name&#39;}).addTo(map);
    }
    #end
    &lt;/script&gt;</code></pre>
but something is wrong, it seems to crash the template and it falls back to just showing me $result as a table.
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '15, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/79d8a7ff1b12fde8c303ca6e3c925749?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="HeaDCase&#39;s gravatar image" />
<p><span>HeaDCase</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="HeaDCase has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Nov '15, 22:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-46425" class="comments-container">
<span id="46584"></span>
<div id="comment-46584" class="comment">
<div id="post-46584-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Is Conluence supposed to be Confluence?</p>
</div>
<div id="comment-46584-info" class="comment-info">
<span class="comment-age">(14 Nov '15, 08:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46586"></span>
<div id="comment-46586" class="comment">
<div id="post-46586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... this one <a href="https://en.wikipedia.org/wiki/Confluence_%28software%29">https://en.wikipedia.org/wiki/Confluence_%28software%29</a> ? <a href="http://help.openstreetmap.org/users/11659/headcase">@HeaDCase</a></p>
</div>
<div id="comment-46586-info" class="comment-info">
<span class="comment-age">(14 Nov '15, 16:32)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46587"></span>
<div id="comment-46587" class="comment">
<div id="post-46587-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yeah, my typo there. Got it sorted in the meantime, the suggestion about using only the first element of the returned array is right on the money. Thanks!</p>
</div>
<div id="comment-46587-info" class="comment-info">
<span class="comment-age">(14 Nov '15, 20:58)</span> <span class="comment-user userinfo">HeaDCase</span>
</div>
</div>
</div>
<div id="comment-tools-46425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46425-form-container" class="comment-form-container">
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

<span id="46578"></span>

<div id="answer-container-46578" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46578-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="HeaDCase has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your question is difficult to understand (what is Conluence and where does PocketQuery come into it - are we supposed to know?) but your JavaScript looks like it assumes that the Nominatim response will be a hash when indeed it will be an array of search results; you probably need something like <code>data[0].lat</code> instead of <code>data.lat</code>. Which will of course fail if the result set is empty.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '15, 23:00</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46578" class="comments-container">
&#10;</div>
<div id="comment-tools-46578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46578-form-container" class="comment-form-container">
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

