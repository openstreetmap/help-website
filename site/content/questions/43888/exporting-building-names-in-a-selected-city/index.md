+++
type = "question"
title = "Exporting building names in a selected city"
description = '''Hello, i&#x27;m new to OpenStreetMap world and i would like to know if it woud be possible and how to extract all building names in a selected city (my requirement is Ploiesti, PH, Romania). I need those in order to integrate them as POIs in a specialized application. P.S: When stating &quot;building names&quot; i...'''
date = "2015-07-01T18:39:00Z"
lastmod = "2015-07-02T07:57:00Z"
weight = 43888
keywords = [ "buildings", "nominatim", "export" ]
aliases = [ "/questions/43888" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Exporting building names in a selected city](/questions/43888/exporting-building-names-in-a-selected-city)

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
<span id="post-43888-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43888-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43888-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, i'm new to OpenStreetMap world and i would like to know if it woud be possible and how to extract all building names in a selected city (my requirement is Ploiesti, PH, Romania). I need those in order to integrate them as POIs in a specialized application.</p>
<p>P.S: When stating "building names" i mean block of flats/appartment buildings numbers</p>
<p>An example building for better understanding: <a href="http://nominatim.openstreetmap.org/details.php?place_id=75757510">http://nominatim.openstreetmap.org/details.php?place_id=75757510</a></p>
<p>I need this data in a very simple form like a csv or plain text file for eg.:</p>
<pre><code>Bl. 42,Cameliei
Bl. 71,Cameliei
Bl. 2A2, Aleea Codrului</code></pre>
<p>Is this achievable?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '15, 18:39</strong></p>
<img src="https://secure.gravatar.com/avatar/4486a29d4923ab42022a31892634306c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrei_teopop&#39;s gravatar image" />
<p><span>andrei_teopop</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrei_teopop has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '15, 18:43</strong> </span></p>
</div>
</div>
<div id="comments-container-43888" class="comments-container">
<span id="43903"></span>
<div id="comment-43903" class="comment">
<div id="post-43903-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Note that the tagging of the building in your example is wrong. Building numbers don't belong into the building name.</p>
</div>
<div id="comment-43903-info" class="comment-info">
<span class="comment-age">(02 Jul '15, 07:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43888" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43888-form-container" class="comment-form-container">
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

<span id="43889"></span>

<div id="answer-container-43889" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43889-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You may need to tune the script to account for additional tags being used for the building names and do some post filtering, but Overpass API and/or Overpass Turbo is a good tool to look at for this:</p>
<p><a href="http://overpass-turbo.eu/s/adr">http://overpass-turbo.eu/s/adr</a></p>
<p>(click "Run" to see the results.)</p>
<p>As the text there says, I generated the script using the Wizard, with the input</p>
<pre><code>building=* and name=* in &quot;Ploiesti, Romania&quot;</code></pre>
<p>but I then edited the output configuration to have it generate csv instead of json. The query language is documented here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a></p>
<p>To add a tag like "addr:housename" to the results, you would need to add additional lines to the main body of the script, like <code>way["building"]["addr:housename"](area.searchArea);</code>, with a node, way and relation query for each additional tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '15, 19:57</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-43889" class="comments-container">
<span id="43890"></span>
<div id="comment-43890" class="comment">
<div id="post-43890-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>First, thank you very much for the answer. I see that the list does not contain all the buildings listed in nominatim. Do you know the cause of this behaviour? Also, would it be possible to add geographical coordinates (longitude and latitude) to every entry in that generated output?</p>
</div>
<div id="comment-43890-info" class="comment-info">
<span class="comment-age">(01 Jul '15, 20:26)</span> <span class="comment-user userinfo">andrei_teopop</span>
</div>
</div>
<span id="43891"></span>
<div id="comment-43891" class="comment">
<div id="post-43891-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here's an amended script for lat lon: <a href="http://overpass-turbo.eu/s/adv">http://overpass-turbo.eu/s/adv</a></p>
<p>The coordinates are the center returned by Overpass and may not lie inside of the building (search the docs for 'center'), also take a look at the docs for "Output Format" to see what you can get as far as the output (you can also get various other structured formats like json, xml).</p>
<p>As far as the buildings that are not returned, as I said in my answer, it depends on the tagging in use in the area (I based the example on the building you linked and didn't look at any others), if buildings are also having addr:housenumber or addr:housename, you will need to add those to the script, both in the output specification and as queries, and then presumably do some post processing to consolidate those columns.</p>
</div>
<div id="comment-43891-info" class="comment-info">
<span class="comment-age">(01 Jul '15, 20:43)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-43889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43889-form-container" class="comment-form-container">
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

