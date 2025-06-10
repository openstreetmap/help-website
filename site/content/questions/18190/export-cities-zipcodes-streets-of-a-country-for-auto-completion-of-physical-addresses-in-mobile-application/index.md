+++
type = "question"
title = "Export Cities-ZipCodes-Streets of a country, for auto-completion of physical addresses in mobile application"
description = '''My question is similar to this one, but the only answer offered over there does not satisfy my requirement.   I need a to create a database containing the required data to auto-complete a postal address filled in by a user in a mobile application. The database must be embed in the application, to al...'''
date = "2012-12-04T14:52:00Z"
lastmod = "2012-12-05T17:44:00Z"
weight = 18190
keywords = [ "autocomplete", "sqlite", "export", "osm2pgsql", "address" ]
aliases = [ "/questions/18190" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export Cities-ZipCodes-Streets of a country, for auto-completion of physical addresses in mobile application](/questions/18190/export-cities-zipcodes-streets-of-a-country-for-auto-completion-of-physical-addresses-in-mobile-application)

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
<span id="post-18190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18190-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My question is similar to <a href="https://help.openstreetmap.org/questions/5473/export-country-state-city-street-zip-code-worldwide-for-use-with-address-auto-completion">this one</a>, but the only answer offered over there does not satisfy my requirement.</p>
<p><br />
</p>
<p>I need a to create a database containing the required data to <strong>auto-complete a postal address</strong> filled in by a user in a mobile application.<br />
The database must be embed in the application, to allow for <strong>offline use</strong> and always snappy auto-completion.</p>
<p>In this context, my technical goal is to create a SQLite database with the <strong>cities, zip code and streets</strong>. I do not need the coordinates of the points. I have no problem converting from a <em>classic</em> SQL flavor database to SQLite. I'm however having trouble going from <code>osm</code> format to <code>SQL</code>.<br />
If an other format usable in a mobile application is more appropriate, I'm of course ok with it too.</p>
<p>I have the feeling that I'm not dealing with the problem with the right strategy and adequate tools.<br />
What steps and tools do you suggest?</p>
<p><br />
</p>
<hr />
<br />
Here is what I tried:<br />
Using an extract from <a href="http://download.geofabrik.de/openstreetmap/">OpenStreetMap Extracts</a>, I have successfully created a SQLite database with <a href="https://github.com/technimad/osm2sqlite">osm2sqlite</a>.<br />
I'm a bit confused about the format of the rows.<br />
And there is a lot of information I don't care about. While I could remove it, it feels backward to import it from <code>osm</code> to <code>SQL</code> to then remove it. Would be much more efficient to not import it in the first place.
<p><strong>Updated to describe an other try:</strong><br />
Using osm2pgsql, I'm loading the file into a Postgres database.</p>
<pre><code>osm2pgsql -c -G -d osm -S /usr/local/share/osm2pgsql/default.style france.osm.pbf</code></pre>
<p>Seems nice, but I can't find the zip code. Is it not available for France in original osm file, or is it the import that skipped it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-autocomplete" rel="tag" title="see questions tagged &#39;autocomplete&#39;">autocomplete</span> <span class="post-tag tag-link-sqlite" rel="tag" title="see questions tagged &#39;sqlite&#39;">sqlite</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Dec '12, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a41a211aed3597a7d55f9b7ca5b32a41?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guillaume&#39;s gravatar image" />
<p><span>Guillaume</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guillaume has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '16, 11:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></br></p>
</div>
</div>
<div id="comments-container-18190" class="comments-container">
&#10;</div>
<div id="comment-tools-18190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18190-form-container" class="comment-form-container">
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

<span id="18196"></span>

<div id="answer-container-18196" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18196-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18196-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18196-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please have a look at the OSM wiki and do a search there for the tools called osmfilter and osmconvert.</p>
<p>If you have your rae OSM source data, do a filtering for any objects to keep addr:* tags</p>
<p>Then process the result file with osmconvert where you can produce CSV data sets easily.</p>
<p>Then import that CSV data in any database you like.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Dec '12, 17:07</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-18196" class="comments-container">
<span id="18200"></span>
<div id="comment-18200" class="comment">
<div id="post-18200-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@stephan75</span> If I want to import everything in the database, do I need to run the osmfilter command (your line "do a filtering for any objects to keep addr:* tags" sounds like you need to explicitly hint you want to keep a specific tag). I will try osmconvert to write a csv. I have also updated my question, to document my latest try with osm2pgsql</p>
</div>
<div id="comment-18200-info" class="comment-info">
<span class="comment-age">(04 Dec '12, 21:40)</span> <span class="comment-user userinfo">Guillaume</span>
</div>
</div>
<span id="18215"></span>
<div id="comment-18215" class="comment">
<div id="post-18215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hi Guillaume, Well, I am not so familiar with OSM import to an SQL database ... but if you want to know whether you NEED to do some filtering before importing: try it on your own!</p>
<p>Take a small raw OSM file from an area, maybe your hometown or similar, and try all features of osmfilter to find out how it works and if you can benefit from it before importing. There are enough examples about filtering on the OSM wiki page of osmfilter.</p>
<p>Tell us when you get stuck somewhere in detail, with adequate examples.</p>
</div>
<div id="comment-18215-info" class="comment-info">
<span class="comment-age">(05 Dec '12, 17:44)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-18196" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18196-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

