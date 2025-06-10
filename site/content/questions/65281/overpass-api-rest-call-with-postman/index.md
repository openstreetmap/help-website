+++
type = "question"
title = "Overpass API: REST call with Postman"
description = '''I&#x27;m trying to retrieve all cinemas in the world for a project.  I found out that I can do it through Postman using this REST call: http://www.overpass-api.de/api/xapi?*[amenity=cinema]  I can also retrieve all cinemas from a specific square this way: http://www.overpass-api.de/api/xapi?*[amenity=cin...'''
date = "2018-08-12T02:01:00Z"
lastmod = "2018-08-12T02:01:00Z"
weight = 65281
keywords = [ "overpassapi", "api", "overpass-turbo", "rest" ]
aliases = [ "/questions/65281" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: REST call with Postman](/questions/65281/overpass-api-rest-call-with-postman)

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
<span id="post-65281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65281-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to retrieve all cinemas in the <strong>world</strong> for a project.</p>
<p>I found out that I can do it through <a href="https://www.getpostman.com/">Postman</a> using this REST call:</p>
<pre><code>http://www.overpass-api.de/api/xapi?*[amenity=cinema]</code></pre>
<p>I can also retrieve all cinemas from a specific square this way:</p>
<pre><code>http://www.overpass-api.de/api/xapi?*[amenity=cinema][bbox=-180,-90,180,90]</code></pre>
<p>What I would like to do now is to retrieve all cinemas for a <strong>country</strong> or a <strong>city</strong>. All I know is that I can use <code>area["name"="New Zealand"]</code> or <code>geocodeArea:California</code> but if I stick those value on the query I receive an error.</p>
<p>This is how I'm using geocodeArea right now and is not working:</p>
<pre><code>http://www.overpass-api.de/api/xapi?*[amenity=cinema][geocodeArea=California]</code></pre>
<p>On your documentation I don't see examples of REST call so I'm bit stock.</p>
<p>Can you please provide an example, please?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-rest" rel="tag" title="see questions tagged &#39;rest&#39;">rest</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '18, 02:01</strong></p>
<img src="https://secure.gravatar.com/avatar/edd9cbb506e3d4c26c63f8b8a5558f02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="francesco_mantovani&#39;s gravatar image" />
<p><span>francesco_ma...</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="francesco_mantovani has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Aug '18, 02:02</strong> </span></p>
</div>
</div>
<div id="comments-container-65281" class="comments-container">
&#10;</div>
<div id="comment-tools-65281" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65281-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

