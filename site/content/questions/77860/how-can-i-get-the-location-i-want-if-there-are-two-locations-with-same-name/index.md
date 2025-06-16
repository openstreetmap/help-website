+++
type = "question"
title = "How can I get the location I want if there are two locations with same name?"
description = '''I am searching for a map of sub-districts (admin level 6) within a district(admin level 5) in which each sub-dist will be clickable on my webpage. The problem is there are some districts with one of its sub-district having same name as the district itself. when I search for the district I get the su...'''
date = "2020-12-06T17:36:00Z"
lastmod = "2020-12-07T21:47:00Z"
weight = 77860
keywords = [ "output", "input" ]
aliases = [ "/questions/77860" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get the location I want if there are two locations with same name?](/questions/77860/how-can-i-get-the-location-i-want-if-there-are-two-locations-with-same-name)

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
<span id="post-77860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am searching for a map of sub-districts (admin level 6) within a district(admin level 5) in which each sub-dist will be clickable on my webpage. The problem is there are some districts with one of its sub-district having same name as the district itself. when I search for the district I get the sub-district instead.</p>
<p>Sub District with same name <img src="/upfiles/2020-12-06_23_02_52-overpass_turbo_-_Brave.png" alt="alt text" /></p>
<p>What i want<img src="/upfiles/2020-12-06_23_02_44-overpass_turbo_-_Brave.png" alt="alt text" /></p>
<pre><code>[out:json];
&#10;{{geocodeArea: chittoor, Andhra Pradesh, india}}-&gt;.searchArea;
&#10;(
&#10;  relation[&quot;type&quot;=&quot;boundary&quot;][admin_level = 6](area.searchArea);
&#10;);
out;
&#10;(
    relation[admin_level = 6];
);
out skel;</code></pre>
<p>Here i am trying to use output of one set as input for next set? How can i archive this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span> <span class="post-tag tag-link-input" rel="tag" title="see questions tagged &#39;input&#39;">input</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Dec '20, 17:36</strong></p>
<img src="https://secure.gravatar.com/avatar/203cf23bc7b343ffbec5dbb92c2857f6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PramodG&#39;s gravatar image" />
<p><span>PramodG</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PramodG has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '20, 18:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</img>
</div>
</div>
<div id="comments-container-77860" class="comments-container">
&#10;</div>
<div id="comment-tools-77860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77860-form-container" class="comment-form-container">
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

<span id="77861"></span>

<div id="answer-container-77861" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77861-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you cant rely on geocodeArea for this type of operation. Instead you will need an unambiguous search string using standard overpass syntax (for instance possibly based on the wikidata item) and convert that to an area using the overpass statement which can then be assigned to the .searchArea set, something like area[wikidata="Q11103437"]-&gt;.searchArea;. (Of course if you know the object's OSM Id you can access the area by adding a magic number to the id).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Dec '20, 18:55</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-77861" class="comments-container">
<span id="77862"></span>
<div id="comment-77862" class="comment">
<div id="post-77862-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am doing something like that in python, but geocode return list (geo_result VARIABLE) of location matching the district name so both the sub-district and district are returned. How can i select the right one?</p>
<p>geolocator = Nominatim(user_agent="city_compare") geo_results = geolocator.geocode(dist_name, exactly_one=False)</p>
<h1 id="searching-for-relation-in-result-set">Searching for relation in result set</h1>
<p>for r in geo_results: #print(r.address, r.raw.get("osm_type")) if r.raw.get("osm_type") == "relation" and r.raw.get('type')=='administrative': city = r break # Calculating area id area_id = int(city.raw.get("osm_id")) + 3600000000 #print(area_id) # Excecuting overpass call query2 = """ [out:json]; area({})-&gt;.searchArea;</p>
<pre><code>       (
           relation[&quot;type&quot;=&quot;boundary&quot;][admin_level = 6](area.searchArea);
        );
      out geom;&quot;&quot;&quot;.format(area_id)
   url = &#39;https://overpass-api.de/api/interpreter&#39;
   r= requests.get(url, params={&#39;data&#39;: query2})</code></pre>
</div>
<div id="comment-77862-info" class="comment-info">
<span class="comment-age">(06 Dec '20, 19:10)</span> <span class="comment-user userinfo">PramodG</span>
</div>
</div>
<span id="77865"></span>
<div id="comment-77865" class="comment">
<div id="post-77865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, my approach gets round this Nominatim issue in Overpass, but does not resolve the actual Nominatim issue.</p>
</div>
<div id="comment-77865-info" class="comment-info">
<span class="comment-age">(07 Dec '20, 13:03)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="77866"></span>
<div id="comment-77866" class="comment">
<div id="post-77866-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It will probably work to use the <code>place_rank</code> in the Nominatim results. If it doesn't, query Nominatim or Overpass-API for the details of each candidate (at which point you will have the admin_level tag).</p>
</div>
<div id="comment-77866-info" class="comment-info">
<span class="comment-age">(07 Dec '20, 21:47)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-77861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77861-form-container" class="comment-form-container">
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

