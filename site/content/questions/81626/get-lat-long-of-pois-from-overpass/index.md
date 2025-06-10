+++
type = "question"
title = "Get lat-long of POIs from Overpass?"
description = '''Hi TLDR, I think my question below has possibly been answered here but it&#x27;s too technical for me to understand. I would like to get the lat-long of some POIs in csv format so I can compare them with a published dataset using Excel (that&#x27;s all I can manage!) I get the following result with Overpass T...'''
date = "2021-09-05T15:34:00Z"
lastmod = "2021-09-06T23:40:00Z"
weight = 81626
keywords = [ "overpass", "location" ]
aliases = [ "/questions/81626" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Get lat-long of POIs from Overpass?](/questions/81626/get-lat-long-of-pois-from-overpass)

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
<span id="post-81626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81626-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>TLDR, I think my question below has possibly been answered <a href="https://help.openstreetmap.org/questions/34080/using-r-to-get-lat-and-lon-from-osm_ids-without-assistance-of-external-software-eg-qgis">here</a> but it's too technical for me to understand.</p>
<p>I would like to get the lat-long of some POIs in csv format so I can compare them with a published dataset using Excel (that's all I can manage!)</p>
<p>I get the following result with Overpass Turbo:</p>
<pre><code>&quot;elements&quot;: [
&#10;{
  &quot;type&quot;: &quot;node&quot;,
  &quot;id&quot;: 7841169184,
  &quot;lat&quot;: 52.5786297,
  &quot;lon&quot;: -0.2276290,
  &quot;tags&quot;: {
    &quot;addr:city&quot;: &quot;Peterborough&quot;,
    &quot;addr:postcode&quot;: &quot;PE1 5EH&quot;,
    &quot;addr:street&quot;: &quot;Padholme Road&quot;,
    &quot;amenity&quot;: &quot;place_of_worship&quot;,
    &quot;denomination&quot;: &quot;sunni&quot;,
    &quot;religion&quot;: &quot;muslim&quot;
  }
&#10;    }, 
{
  &quot;type&quot;: &quot;way&quot;,
  &quot;id&quot;: 236058204,
  &quot;nodes&quot;: [
    2441318658,
    5934211602,
    5934211603,
    2441318882,
    2441318621,
    2441318773,
    2441318658
  ],
  &quot;tags&quot;: {
    &quot;addr:city&quot;: &quot;Peterborough&quot;,
    &quot;addr:housenumber&quot;: &quot;116&quot;,
    &quot;addr:postcode&quot;: &quot;PE3 6DD&quot;,
    &quot;addr:street&quot;: &quot;Midland Road&quot;,
    &quot;amenity&quot;: &quot;place_of_worship&quot;,
    &quot;building&quot;: &quot;yes&quot;,
    &quot;denomination&quot;: &quot;sunni&quot;,
    &quot;name&quot;: &quot;Madina Madrassa &amp; Spiritual Centre&quot;,
    &quot;religion&quot;: &quot;muslim&quot;
  }
},</code></pre>
<p>[continues]</p>
<p>Can I efficiently identify the lat-long of the area, either interpolating the centre of the area or using (say) the first-listed node?</p>
<p>Can I force Overpass to output a csv file with one line per POI, rather than the line-separated text above?</p>
<p>Is it even possible for someone who uses iD for map editing, and Excel for database editing, to do this?</p>
<p>Many thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '21, 15:34</strong></p>
<img src="https://secure.gravatar.com/avatar/4f273f48fd8756729fc15f4fcf4aae2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eteb3&#39;s gravatar image" />
<p><span>eteb3</span><br />
<span class="score" title="295 reputation points">295</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eteb3 has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Sep '21, 15:36</strong> </span></p>
</div>
</div>
<div id="comments-container-81626" class="comments-container">
&#10;</div>
<div id="comment-tools-81626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81626-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="81638"></span>

<div id="answer-container-81638" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81638-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-81638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Further to AlaskaDave's post:</p>
<p>"By default all fields are separated by a tab character ("\t")." So isn't required.</p>
<p>If you wish to use another character, such as a comma, pipe etc., the column header display argument (false/true) has to be included:</p>
<pre><code>[out:csv(::id,::lat,::lon,&quot;name&quot;; true; &quot;,&quot;)]
&#10;[out:csv(::id,::lat,::lon,&quot;name&quot;; false; &quot;|&quot;)]</code></pre>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#CSV_output_mode">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#CSV_output_mode</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '21, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '21, 14:57</strong> </span></p>
</div>
</div>
<div id="comments-container-81638" class="comments-container">
&#10;</div>
<div id="comment-tools-81638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81638-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81627"></span>

<div id="answer-container-81627" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81627-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Can I force Overpass to output a csv file with one line per POI, rather than the line-separated text above?</p>
</blockquote>
<p>Yes, you can. Here's a query I used to find trees I had tagged in Chiang Mai</p>
<p><strong>You must put an escaped tab character, "\t", as the last argument). Also, note that all tags you wish returned must be enclosed in quotes.</strong></p>
<p>[out:csv(::id,::lat,::lon,"species","species:en","species:th", "name:en",<strong>"\t"</strong>)][timeout:25];</p>
<p>{{geocodeArea:"Thailand"}}-&gt;.searchArea;</p>
<p>(</p>
<p>node["natural"="tree"](user:"AlaskaDave")(area.searchArea);</p>
<p>);</p>
<p>out qt;</p>
<p>The output is a nice CSV file with latitude/longitude coordinates in separate columns on each line of the output file. I merely select all the output, copy it, and save it as a CSV file. You can then open it in Excel.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '21, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81627" class="comments-container">
<span id="81629"></span>
<div id="comment-81629" class="comment">
<div id="post-81629-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Fantabulous - works perfectly. Thank you!</p>
</div>
<div id="comment-81629-info" class="comment-info">
<span class="comment-age">(05 Sep '21, 22:04)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
<span id="81636"></span>
<div id="comment-81636" class="comment">
<div id="post-81636-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What does the tab do? I'm struggling to see any difference.</p>
</div>
<div id="comment-81636-info" class="comment-info">
<span class="comment-age">(06 Sep '21, 13:07)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="81639"></span>
<div id="comment-81639" class="comment">
<div id="post-81639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re: the tab character</p>
<p>I cannot find the material I used in my example in the Wiki. IIRC, the "/t" argument forced the delimiter characters in the output file to be tabs. However, I noticed that the Overpass Turbo Wizard has changed a lot since I used that query — it's much more powerful now and allows the use of wildcards for key values, for example.</p>
<p>Perhaps that requirement has changed too?</p>
<p>I'm not an Overpass Query expert, far from it. I use the Overpass Turbo Wizard for almost all of my queries. I got the main part of the above query from a friend who knows how to use the standard Overpass better than me.</p>
</div>
<div id="comment-81639-info" class="comment-info">
<span class="comment-age">(06 Sep '21, 14:55)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-81627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81627-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81651"></span>

<div id="answer-container-81651" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81651-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use</p>
<pre><code>out center;</code></pre>
<p>instead of</p>
<p><code>out qt;</code></p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#out</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '21, 20:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '21, 20:12</strong> </span></p>
</div>
</div>
<div id="comments-container-81651" class="comments-container">
<span id="81654"></span>
<div id="comment-81654" class="comment">
<div id="post-81654-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you very much.</p>
<p>Do you know if there's an "Overpass QL for Dummies" page somewhere? I'm reading the wiki and documentation as I come across it, but it's stupendously (meant literally) technical. Maybe there's something like baby-food for a beginner?</p>
</div>
<div id="comment-81654-info" class="comment-info">
<span class="comment-age">(06 Sep '21, 20:58)</span> <span class="comment-user userinfo">eteb3</span>
</div>
</div>
<span id="81659"></span>
<div id="comment-81659" class="comment">
<div id="post-81659-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15711/eteb3">@eteb3</a>: I agree — the standard Overpass API is incredibly opaque for non-programmers. I always use the Overpass Turbo Wizard. It's simpler and although one can't do everything the API can do with it, the barrier to entry is very low.</p>
<p><a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a></p>
</div>
<div id="comment-81659-info" class="comment-info">
<span class="comment-age">(06 Sep '21, 23:12)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="81660"></span>
<div id="comment-81660" class="comment">
<div id="post-81660-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You're correct about the wiki reference pages. You have to understand OP fully to be able to decipher the OP wiki! An inline example or two wouldn't go amiss. Unfortunately that's always the case when the people who wrote the code also write the euphemistically named 'help' pages.</p>
<p>There's <a href="https://dev.overpass-api.de/blog/index.html,">https://dev.overpass-api.de/blog/index.html,</a> but the weird chapter names also makes it hard to follow. Plus it's not google searchable.</p>
<p>This one's a bit better <a href="https://dev.overpass-api.de/overpass-doc/en/index.html">https://dev.overpass-api.de/overpass-doc/en/index.html</a></p>
<p>This one is the nearest to a tutorial &amp; probably the bes tplace to start <a href="https://osm-queries.ldodds.com/">https://osm-queries.ldodds.com/</a></p>
<p>Plus there's Stack Exchange family of sites to search for previously asked questions, but again, I've found you need to know a bit about the subject to ascertain the usefulness of the responses.</p>
</div>
<div id="comment-81660-info" class="comment-info">
<span class="comment-age">(06 Sep '21, 23:40)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-81651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81651-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81645"></span>

<div id="answer-container-81645" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81645-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is all great on the csv output.</p>
<p>Could I flag here (or maybe I should ask again separately) the part of the question about getting the lat-lon of an area? Overpass will give me those for a node, but not otherwise. I only need it approximately - so lat-lon of a single node in the area or relation would be fine.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '21, 17:54</strong></p>
<img src="https://secure.gravatar.com/avatar/4f273f48fd8756729fc15f4fcf4aae2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eteb3&#39;s gravatar image" />
<p><span>eteb3</span><br />
<span class="score" title="295 reputation points">295</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eteb3 has one accepted answer">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '21, 17:56</strong> </span></p>
</div>
</div>
<div id="comments-container-81645" class="comments-container">
&#10;</div>
<div id="comment-tools-81645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81645-form-container" class="comment-form-container">
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

