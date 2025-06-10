+++
type = "question"
title = "Census Block Info for Nominatim"
description = '''Is it possible to get the census block, block group, and tract information for a nominatim query? I know I can get the long/lat and then map back into the census hierarchy but it would be sweet to do both in one step if its possible.'''
date = "2013-11-05T18:34:00Z"
lastmod = "2013-11-21T21:20:00Z"
weight = 27837
keywords = [ "nominatim", "census" ]
aliases = [ "/questions/27837" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Census Block Info for Nominatim](/questions/27837/census-block-info-for-nominatim)

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
<span id="post-27837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27837-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to get the census block, block group, and tract information for a nominatim query? I know I can get the long/lat and then map back into the census hierarchy but it would be sweet to do both in one step if its possible.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-census" rel="tag" title="see questions tagged &#39;census&#39;">census</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '13, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/cedcf7f648595f10a2eff219e1b94922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbryfcz&#39;s gravatar image" />
<p><span>sbryfcz</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbryfcz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Nov '13, 18:35</strong> </span></p>
</div>
</div>
<div id="comments-container-27837" class="comments-container">
<span id="28342"></span>
<div id="comment-28342" class="comment">
<div id="post-28342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you please explain what 'census' means in your opinion? I don't know it from the Nominatim context :/ <a href="http://wiki.openstreetmap.org/wiki/Nominatim">http://wiki.openstreetmap.org/wiki/Nominatim</a></p>
</div>
<div id="comment-28342-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 16:07)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="28351"></span>
<div id="comment-28351" class="comment">
<div id="post-28351-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah. I'm not sure nominatim currently supports it. As you may (or may not be aware), the USA is divided into small groups for purposes of taking the census. There is a hierarchy of census tracts (largest) to census blocks (smallest) that break the USA up into groups. These tend to change much less frequently (and are better defined) than zipcodes. In addition, regular surveys are published for demographic data with these census boundaries. It would be great to get this data from the geocoder so that additional data (ex. Survey data, Demographics) can easily be appended for data analysis.</p>
</div>
<div id="comment-28351-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 16:47)</span> <span class="comment-user userinfo">sbryfcz</span>
</div>
</div>
</div>
<div id="comment-tools-27837" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27837-form-container" class="comment-form-container">
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

<span id="28372"></span>

<div id="answer-container-28372" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28372-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>AFAIK, this kind of census data was not uploaded into the OSM database, and before someone does it, I believe there should be some discussion on the question of if this kind of data is adequate for inclusion. My answer does not discuss this issue, however, even if the data is/was in the OSM database.</p>
<p>I am doing something similar for Brazilian census data - all of the territory is divided into "census sectors" ("Setores Censitários" in portuguese), and one given latitude/longitude falls inside exactly one sector. No sector crosses the boundary between two cities, therefore it is possible to establish some kind of hierarchy (sector - city - state - country).</p>
<p>I am solving the problem of returning the census data using a separate PostGIS schema, loaded with the sector's geometries provided by IBGE in Brazil, and after querying the Nominatim and getting the result's coordinates, I do a second query on the census schema using st_within() or similar functions to get the census sector and upper hierarchies. Then the web server compiles everything into nice JSON strings and sends to the client machine for display...</p>
<p>So far, it has been easier than initially thought, since IBGE provides the sectors in nice SHP/DWG files, easily loadable into a PostGIS database with some custom scripts. Your mileage may vary...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '13, 20:54</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-28372" class="comments-container">
<span id="28373"></span>
<div id="comment-28373" class="comment">
<div id="post-28373-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I like this idea, and I think it may be more appropriate than putting it directly into the OSM schema. A lot of countries have this sort of structure and it seems like a generic approach. Care to share your scripts?</p>
</div>
<div id="comment-28373-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 21:00)</span> <span class="comment-user userinfo">sbryfcz</span>
</div>
</div>
<span id="28374"></span>
<div id="comment-28374" class="comment">
<div id="post-28374-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, while the data (from OSM and IBGE) only requires attribution, the development is internal to my company (and still experimental), can't share the scripts at least until the product is finished and published.</p>
</div>
<div id="comment-28374-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 21:04)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
<span id="28375"></span>
<div id="comment-28375" class="comment">
<div id="post-28375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Completely understand. Thanks for the idea though.</p>
</div>
<div id="comment-28375-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 21:20)</span> <span class="comment-user userinfo">sbryfcz</span>
</div>
</div>
</div>
<div id="comment-tools-28372" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28372-form-container" class="comment-form-container">
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

