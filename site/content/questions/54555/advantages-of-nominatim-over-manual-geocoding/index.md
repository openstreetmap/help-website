+++
type = "question"
title = "Advantages of nominatim over manual geocoding ?"
description = '''My task is simple that is to geocode the addresses. As I googled to this, suggestions were to use nominatim. But using nominatim requires a web server. Besides that what are the advantages of geocoding through nominatim instead of doing manual geocoding ? There is not much help to do manual geocodin...'''
date = "2017-02-08T19:00:00Z"
lastmod = "2017-02-13T19:57:00Z"
weight = 54555
keywords = [ "openstreetmap", "nominatim" ]
aliases = [ "/questions/54555" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Advantages of nominatim over manual geocoding ?](/questions/54555/advantages-of-nominatim-over-manual-geocoding)

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
<span id="post-54555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54555-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My task is simple that is to geocode the addresses. As I googled to this, suggestions were to use nominatim. But using nominatim requires a web server. Besides that what are the advantages of geocoding through nominatim instead of doing manual geocoding ? There is not much help to do manual geocoding.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '17, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/2a95229b87eba17c63a633a8fe609aa2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="3yK&#39;s gravatar image" />
<p><span>3yK</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="3yK has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54555" class="comments-container">
<span id="54556"></span>
<div id="comment-54556" class="comment">
<div id="post-54556-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you explain what you mean by "manual geocoding"? It's not really very clear...</p>
</div>
<div id="comment-54556-info" class="comment-info">
<span class="comment-age">(08 Feb '17, 19:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="54557"></span>
<div id="comment-54557" class="comment">
<div id="post-54557-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>manual geocoding in the sense, we query the address and get the lat lon from the tables.</p>
</div>
<div id="comment-54557-info" class="comment-info">
<span class="comment-age">(08 Feb '17, 19:15)</span> <span class="comment-user userinfo">3yK</span>
</div>
</div>
</div>
<div id="comment-tools-54555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54555-form-container" class="comment-form-container">
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

<span id="54558"></span>

<div id="answer-container-54558" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54558-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54558-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-54558-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="3yK has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You seem to be under the impression that every address is present in OSM as one record, with the columns "house number", "street", "post code", "city", "country" nicely filled out. (Or to be precise, the <code>addr:*</code> columns.)</p>
<p>This is not the case.</p>
<p>First of all, only a fraction of existing houses/addresses actually are in OSM. Second, only roughly a third of these have a house number mapped, and even fewer have addr:street or addr:city.</p>
<p>Therefore your "manual geocoding" would be much more than "select coordinates from table where city='a' and street='b' and housenumber='c'". You'd have to make sure those objects that only have house numbers are still matched to the nearest street, and those that don't have a city or post code specification are matched to whatever polygon they are in (and if there's not even a city polygon but just some <code>place=city</code> node three kilometres away, maybe that's the city for this address). You'd also have to evaluate interpolation ranges, where OSM just has a range of house numbers and not individual numbers.</p>
<p>You <em>can</em> do all this, but you would essentially be re-inventing Nominatim.</p>
<p>Hence the suggestion to simply use it. A web server is not required, you can call the PHP code from the command line, or even adapt the PHP code to read input from a file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '17, 19:35</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54558" class="comments-container">
<span id="54559"></span>
<div id="comment-54559" class="comment">
<div id="post-54559-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>+1 for Frederik's answer but you may also want to look at Pelias <a href="https://github.com/pelias/pelias">https://github.com/pelias/pelias</a></p>
<p>As best I can tell the publicly available Nominatim and Pelias servers typically include more sources than just OSM which is good as the address data in OSM can be spotty.</p>
<p>In either case you should be able to programmatically query the server. It seems that the publicly available servers for both have some usage restrictions so you may want to setup your own server.</p>
</div>
<div id="comment-54559-info" class="comment-info">
<span class="comment-age">(08 Feb '17, 21:37)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="54566"></span>
<div id="comment-54566" class="comment">
<div id="post-54566-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there a good source where I can learn about all these polygons, interpolations, roads, lines, points, ways etc in detail and how its built ?</p>
</div>
<div id="comment-54566-info" class="comment-info">
<span class="comment-age">(09 Feb '17, 11:50)</span> <span class="comment-user userinfo">3yK</span>
</div>
</div>
<span id="54571"></span>
<div id="comment-54571" class="comment">
<div id="post-54571-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am new to php and scripting. Is there any guides or tutorials around, on how to geocode using these osm2pgsql tables using nominatim php files ?</p>
</div>
<div id="comment-54571-info" class="comment-info">
<span class="comment-age">(09 Feb '17, 16:17)</span> <span class="comment-user userinfo">3yK</span>
</div>
</div>
<span id="54622"></span>
<div id="comment-54622" class="comment">
<div id="post-54622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also see <a href="https://wiki.openstreetmap.org/wiki/Search_engines">https://wiki.openstreetmap.org/wiki/Search_engines</a> for more possibilites, maybe some serverless ones?</p>
</div>
<div id="comment-54622-info" class="comment-info">
<span class="comment-age">(13 Feb '17, 19:57)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-54558" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54558-form-container" class="comment-form-container">
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

