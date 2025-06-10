+++
type = "question"
title = "Newbie javascript question"
description = '''Can I get data from the OSM by sending a javascript request for it ? I mean data like what is shown when you do a search on the OSM map? (any data is welcome). Can that be done based on lat/lon ? If yes, where can I find the documentation how to do that? &amp;lt;/blush&amp;gt;'''
date = "2023-09-15T14:20:00Z"
lastmod = "2023-09-18T07:58:00Z"
weight = 87848
keywords = [ "map", "javascript", "data", "newbie" ]
aliases = [ "/questions/87848" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Newbie javascript question](/questions/87848/newbie-javascript-question)

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
<span id="post-87848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87848-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can I get data from the OSM by sending a javascript request for it ? I mean data like what is shown when you do a search on the OSM map? (any data is welcome). Can that be done based on lat/lon ?</p>
<p>If yes, where can I find the documentation how to do that? &lt;/blush&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '23, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/dc3a157b24af4900a422c9e93896f9f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Treklov&#39;s gravatar image" />
<p><span>Treklov</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Treklov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87848" class="comments-container">
<span id="87849"></span>
<div id="comment-87849" class="comment">
<div id="post-87849-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is quite vague. What kind of query do you want to run?</p>
</div>
<div id="comment-87849-info" class="comment-info">
<span class="comment-age">(16 Sep '23, 22:15)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="87851"></span>
<div id="comment-87851" class="comment">
<div id="post-87851-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am looking for something similar as with google maps places in javascript for android, like the following, but then for OSM.</p>
<p>function getPlacesData(query) { const url = <a href="https://maps.googleapis.com/maps/api/place/textsearch/json?query=$%7Bquery%7D&amp;key=$%7BapiKey%7D"><code>https://maps.googleapis.com/maps/api/place/textsearch/json?query=${query}&amp;key=${apiKey}</code></a>;</p>
<p>fetch(url) .then(response =&gt; response.json()) .then(data =&gt; { // Extract relevant information from the API response const places = data.results.map(result =&gt; { return { name: result.name, address: result.formatted_address, rating: result.rating, phone_number: result.formatted_phone_number, website: result.website, types: result.types, opening_hours: result.opening_hours, photos: result.photos, geometry: result.geometry.location, // lat/lan }; }); }) .catch(error =&gt; { // Handle errors console.error(error); }); }</p>
<p>Can someone tell me if something like this exists for OSM and where I can find it?</p>
</div>
<div id="comment-87851-info" class="comment-info">
<span class="comment-age">(17 Sep '23, 03:24)</span> <span class="comment-user userinfo">Treklov</span>
</div>
</div>
</div>
<div id="comment-tools-87848" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87848-form-container" class="comment-form-container">
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

<span id="87852"></span>

<div id="answer-container-87852" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87852-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you can. An app that I use quite often is GPS Prune. I needs Java to operate and displays a GPX over a map drawn from OSM data. I think the source code, of the app, is available. It may give you a good starting point for what you wish to do. see <a href="https://activityworkshop.net/software/gpsprune/">https://activityworkshop.net/software/gpsprune/</a></p>
<p>The JOSm editor and the latest version of the Potlatch editor also use Java and they certainly shows OSM data. I'm not sure if OSM object to us disassembling either of these tools.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '23, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '23, 15:05</strong> </span></p>
</div>
</div>
<div id="comments-container-87852" class="comments-container">
<span id="87854"></span>
<div id="comment-87854" class="comment">
<div id="post-87854-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've never looked, but I suspect that all the Potlatches are ActionScript (for Flash). It's successor, iD, is written using JavaScript.</p>
</div>
<div id="comment-87854-info" class="comment-info">
<span class="comment-age">(17 Sep '23, 15:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-87852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87852-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87855"></span>

<div id="answer-container-87855" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87855-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short (but unhelpful) answer is "yes".</p>
<p>However, OSM is not like Google - you do not have to interact with it through the keyhole of an API;you can just download it and extract what you want with it (subject to copyright restrictions, which for you probably means accreditation).</p>
<p>There are APIs available from third-parties that allow you to query their extract of OSM data, but we won't know which will be useful to you because we don't know what you actually want to do.</p>
<p>I'm guessing, but I'd suggest that "overpass" might be a possible starting point. Have a look in the OSM wiki for that.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '23, 15:09</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '23, 15:09</strong> </span></p>
</div>
</div>
<div id="comments-container-87855" class="comments-container">
&#10;</div>
<div id="comment-tools-87855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87855-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87856"></span>

<div id="answer-container-87856" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87856-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Great ! Thanks very much sofar.</p>
<p>I had a look at GpsPrune, but it uses Java and my webpage(s) does everything with coordinates and positioning in javascript. The web site is/are a few pages that are loaded in webviews into an android app. I have little Java coding in the app, just for permissions, intent processing and back buttons ;-) So the logic I have mostly in Javascript.</p>
<p>I will have a look at the he JOSm editor, when not Potlatches with ActionScript then iD and the overpass in the OSM wiki too. Third party software..maybe.</p>
<p>I will tell you soon.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '23, 16:20</strong></p>
<img src="https://secure.gravatar.com/avatar/dc3a157b24af4900a422c9e93896f9f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Treklov&#39;s gravatar image" />
<p><span>Treklov</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Treklov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87856" class="comments-container">
&#10;</div>
<div id="comment-tools-87856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87856-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87857"></span>

<div id="answer-container-87857" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87857-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87857-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87857-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am looking for a way to detect a difference in color on a map, but I can't find it or get it to work (yet) on a google map with a canvas.</p>
<p>So I was thinking of using an api to just get the color at a certain coordinate with an Open Street Map. That would also be a good start to detect areas with water btw. But I haven't found a simple solution yet. If OSM would give the data like if something is a building or a forest at a certain coordinate, that could also work for me. I have google maps set up, but with a coordinate I could do something with OSM in parallel.</p>
<p>I will keep looking. If I find something, I will post it. Thank you!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Sep '23, 07:58</strong></p>
<img src="https://secure.gravatar.com/avatar/dc3a157b24af4900a422c9e93896f9f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Treklov&#39;s gravatar image" />
<p><span>Treklov</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Treklov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87857" class="comments-container">
&#10;</div>
<div id="comment-tools-87857" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87857-form-container" class="comment-form-container">
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

