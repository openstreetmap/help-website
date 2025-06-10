+++
type = "question"
title = "postgis &amp; osm2pgsql  vs osmconvert &amp; -filter: which methods are the best"
description = '''what should i use:  PostGis as a solution for getting a database populated by osm2pgsql  or osmconvert / -filter to create csv-sheets  aimed is to transform data out of German osm-pbf-files - in order to get the data (not to creat maps again)  see the source (s)= http://download.geofabrik.de/europe/...'''
date = "2014-05-12T14:25:00Z"
lastmod = "2014-05-12T18:09:00Z"
weight = 33112
keywords = [ "osmfilter", "osmconvert", "osm", "postgis", "linux" ]
aliases = [ "/questions/33112" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [postgis & osm2pgsql vs osmconvert & -filter: which methods are the best](/questions/33112/postgis-osm2pgsql-vs-osmconvert-filter-which-methods-are-the-best)

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
<span id="post-33112-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33112-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33112-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>what should i use:</p>
<p>PostGis as a solution for getting a database populated by osm2pgsql or osmconvert / -filter to create csv-sheets</p>
<p>aimed is to transform data out of German osm-pbf-files - in order to get the data (not to creat maps again)</p>
<p>see the source (s)= <a href="http://download.geofabrik.de/europe/germany.html">http://download.geofabrik.de/europe/germany.html</a> ranging form 10 MB (Bremen) to 390 MB (Nordrhein Westfalen) the osm.pbf-files are not too big; Question: which method is the best - the most appropiate? - to store the results in a mysql-db or just have big calc-sheets (with csv-data)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 May '14, 14:25</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33112" class="comments-container">
<span id="33113"></span>
<div id="comment-33113" class="comment">
<div id="post-33113-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>What data do you actually want? Could you describe it in a bit more detail, using words? That way people will be able to see how well that concept maps to OSM data and what manipulation would be needed at your end.</p>
<p>Also (given that you've asked a few questions here) perhaps a more interactive mechanism for asking questions (like the #osm IRC channel) might be a better option?</p>
</div>
<div id="comment-33113-info" class="comment-info">
<span class="comment-age">(12 May '14, 14:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33114"></span>
<div id="comment-33114" class="comment">
<div id="post-33114-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear Someone elsenode i want to have id="20" lat="574" lon="3.0"&gt; &lt;tag k="addr:housenumber" v="9"/&gt; &lt;tag k="addr:street" v="Marktplaats"/&gt; &lt;tag k="amenity" v="cafe"/&gt; &lt;tag k="email" v="vandaelekoen67@skynet.be"/&gt; &lt;tag k="name" v="Paviljoentje"/&gt; &lt;tag k="opening_hours" v="Mo-Su 09:00+; Tu off; Th 09:00-14:00"/&gt; &lt;tag k="phone" v="+3251636211"/&gt; &lt;tag k="website" v="http://www.paviljoentjestaden.be"/&gt; &lt;/node&gt; &lt;node id="244312208" lat="51.2461401" lon="5.4390455"&gt; &lt;tag k="amenity" v="cafe"/&gt; &lt;tag k="created_by" v="JOSM"/&gt; &lt;tag k="name" v="De Club"/&gt; &lt;/node&gt;</p>
<p>what do you think?</p>
</div>
<div id="comment-33114-info" class="comment-info">
<span class="comment-age">(12 May '14, 16:08)</span> <span class="comment-user userinfo">tagtheworld</span>
</div>
</div>
<span id="33115"></span>
<div id="comment-33115" class="comment">
<div id="post-33115-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is XML, not CSV. Please explain exactly what data you are trying to extract and what your desired output format is.</p>
</div>
<div id="comment-33115-info" class="comment-info">
<span class="comment-age">(12 May '14, 16:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33118"></span>
<div id="comment-33118" class="comment">
<div id="post-33118-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@tagtheworld</span> So you only want the XML for one node? What information do you have that you want to use to obtain that node (e.g. its ID in the OSM database, its location, its name, or something else)? Is this related to <span>@say_hello_to_the_world</span> 's question or something else?</p>
</div>
<div id="comment-33118-info" class="comment-info">
<span class="comment-age">(12 May '14, 17:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="33119"></span>
<div id="comment-33119" class="comment">
<div id="post-33119-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello you both - thx alot for posting. well the final formate is calc-based or to view the data in phpmyadmin (or thelike). so i want to gather data out of the osm-data (the map-data) and need to have an oferview on e.g. the restaurants of germany. goal : to have a valid dataset with the adress etc. data of e.g. the restaurants. Question: which tool (set) is the best and which mehtod should be used? - love to hear from you both - btw. say-hello is identical. soorry - i wont repost a similarquestion onaother board again...</p>
</div>
<div id="comment-33119-info" class="comment-info">
<span class="comment-age">(12 May '14, 18:09)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-33112" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33112-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

