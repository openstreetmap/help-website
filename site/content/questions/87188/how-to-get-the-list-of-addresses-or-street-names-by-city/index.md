+++
type = "question"
title = "How to get the list of addresses or street names by city?"
description = '''Hi everyone,  I am trying a way to get a valid address or street name using the name city/zipcode. I am trying to use the OneStreetMap API to get this information. To be clear, I will present an example of what I am trying to achieve: Selecting a city from my select box, like Milano, I would like to...'''
date = "2023-04-29T13:13:00Z"
lastmod = "2023-12-23T17:30:00Z"
weight = 87188
keywords = [ "openstreetmap", "city", "api", "street", "address" ]
aliases = [ "/questions/87188" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get the list of addresses or street names by city?](/questions/87188/how-to-get-the-list-of-addresses-or-street-names-by-city)

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
<span id="post-87188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87188-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone, I am trying a way to get a valid address or street name using the name city/zipcode. I am trying to use the OneStreetMap API to get this information. To be clear, I will present an example of what I am trying to achieve: Selecting a city from my select box, like Milano, I would like to receive (by API) the list of the addresses or street names that Milano has.</p>
<p>Thank you in advance Achille</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Apr '23, 13:13</strong></p>
<img src="https://secure.gravatar.com/avatar/25ef16609c6769a05247bce8664a735b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aki87&#39;s gravatar image" />
<p><span>Aki87</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aki87 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87188" class="comments-container">
&#10;</div>
<div id="comment-tools-87188" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87188-form-container" class="comment-form-container">
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

<span id="87190"></span>

<div id="answer-container-87190" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87190-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Aki87 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> would be your best bet for this (note usage policy).</p>
<p>An example query giving a csv of all streets and paths in Milano with names (adapted from <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#CSV_output_mode">the documentation</a>):</p>
<pre><code>[out:csv(::id,::type,&quot;highway&quot;,&quot;name&quot;)];
{{geocodeArea:Milano}}-&gt;.searchArea;
 ( 
    way[&quot;highway&quot;][&quot;name&quot;](area.searchArea);    
  );
out;
out count;</code></pre>
<p>See example live in Overpass Turbo <a href="https://overpass-turbo.eu/s/1up6">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '23, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-87190" class="comments-container">
<span id="87193"></span>
<div id="comment-87193" class="comment">
<div id="post-87193-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thank you so much to help me. Just another question, I am using the API in this way: <a href="https://nominatim.openstreetmap.org/search?X-Requested-With=overpass-ide&amp;format=json&amp;q=Milano.">https://nominatim.openstreetmap.org/search?X-Requested-With=overpass-ide&amp;format=json&amp;q=Milano.</a></p>
<p>I am not getting the same result in the example <a href="https://overpass-turbo.eu/">here</a></p>
<p>Maybe I am not using the API in the correct way. How I can integrate the API in my backend code.</p>
<p>Thank you in advance. Achille</p>
</div>
<div id="comment-87193-info" class="comment-info">
<span class="comment-age">(30 Apr '23, 19:01)</span> <span class="comment-user userinfo">Aki87</span>
</div>
</div>
<span id="87211"></span>
<div id="comment-87211" class="comment">
<div id="post-87211-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To be clear, I would like to integrate the API in my app and to show the list of the streen name or addresses.</p>
<p>Is it possible with actual API? I have read the documentation, but maybe I did not catch this case or for me it is little bit difficult to understand.</p>
<p>However, may you help me?</p>
<p>Regards, Achille</p>
</div>
<div id="comment-87211-info" class="comment-info">
<span class="comment-age">(02 May '23, 08:20)</span> <span class="comment-user userinfo">Aki87</span>
</div>
</div>
<span id="87212"></span>
<div id="comment-87212" class="comment">
<div id="post-87212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Technical details aside, I would like to draw your attention to Nominatim Usage Policy.</p>
<p>Conducting bulk geocoding is discouraged, and it is preferable for you to run your own version of Nominatim if you want to implement this in your app.</p>
</div>
<div id="comment-87212-info" class="comment-info">
<span class="comment-age">(02 May '23, 14:55)</span> <span class="comment-user userinfo">bxl-forever</span>
</div>
</div>
<span id="87213"></span>
<div id="comment-87213" class="comment">
<div id="post-87213-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/22967/aki87"></a><a href="https://help.openstreetmap.org/users/22967/aki87">@Aki87</a> The example I gave is for Overpass as you asked about a list of streets, the link you have provided is to Nominatim which is a different service.</p>
<ul>
<li>Overpass API is documented <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">here</a>.</li>
<li>Nominatim is documented <a href="https://wiki.openstreetmap.org/wiki/Nominatim">here</a>.</li>
</ul>
<p>If what you actually want is a Geocoding service like Nominatim then you can see a list of options <a href="https://wiki.openstreetmap.org/wiki/Geocoding">here</a>.</p>
</div>
<div id="comment-87213-info" class="comment-info">
<span class="comment-age">(02 May '23, 15:32)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="88077"></span>
<div id="comment-88077" class="comment">
<div id="post-88077-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how to get the same result by zip code/postal code, instead Milano</p>
<p>For example zip code=80131. Is a Napoli location from Italy</p>
</div>
<div id="comment-88077-info" class="comment-info">
<span class="comment-age">(23 Dec '23, 17:30)</span> <span class="comment-user userinfo">salvatore</span>
</div>
</div>
</div>
<div id="comment-tools-87190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87190-form-container" class="comment-form-container">
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

