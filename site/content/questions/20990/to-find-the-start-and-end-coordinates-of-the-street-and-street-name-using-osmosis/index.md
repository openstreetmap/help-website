+++
type = "question"
title = "To find the start and end coordinates of the street and street name using Osmosis"
description = '''I am using this querry to extract road network used by cars: osmosis --read-xml niedersachsen.osm --tf accept-ways highway=* --tf reject-ways highway=pedestrian,footway,steps,cycleway,bridleway --tf reject-relations --used-node --write-xml niedersachsen_roadnetwork.osm But still I need to find the s...'''
date = "2013-03-26T12:00:00Z"
lastmod = "2013-03-26T15:14:00Z"
weight = 20990
keywords = [ "route_end", "route_start", "streetnames", "coordinates", "osmosis" ]
aliases = [ "/questions/20990" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [To find the start and end coordinates of the street and street name using Osmosis](/questions/20990/to-find-the-start-and-end-coordinates-of-the-street-and-street-name-using-osmosis)

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
<span id="post-20990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20990-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using this querry to extract road network used by cars: osmosis --read-xml niedersachsen.osm --tf accept-ways highway=* --tf reject-ways highway=pedestrian,footway,steps,cycleway,bridleway --tf reject-relations --used-node --write-xml niedersachsen_roadnetwork.osm</p>
<p>But still I need to find the start and end coordinates of the street and street name. Any suggestions? Maybe there is some other more efficient way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route_end" rel="tag" title="see questions tagged &#39;route_end&#39;">route_end</span> <span class="post-tag tag-link-route_start" rel="tag" title="see questions tagged &#39;route_start&#39;">route_start</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Mar '13, 12:00</strong></p>
<img src="https://secure.gravatar.com/avatar/f5d31b13d0fced1a8297e7d9e9385a53?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tfarooqi&#39;s gravatar image" />
<p><span>tfarooqi</span><br />
<span class="score" title="30 reputation points">30</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tfarooqi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Mar '13, 12:06</strong> </span></p>
</div>
</div>
<div id="comments-container-20990" class="comments-container">
<span id="20995"></span>
<div id="comment-20995" class="comment">
<div id="post-20995-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you have programming experience?</p>
</div>
<div id="comment-20995-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 14:53)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="20996"></span>
<div id="comment-20996" class="comment">
<div id="post-20996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I have basic knowlwdge of Python, c++</p>
</div>
<div id="comment-20996-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 14:57)</span> <span class="comment-user userinfo">tfarooqi</span>
</div>
</div>
<span id="21002"></span>
<div id="comment-21002" class="comment">
<div id="post-21002-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe if you read the source code of <a href="http://almien.co.uk/OSM/Routing/">http://almien.co.uk/OSM/Routing/</a> you would find some hints and pointers --- or maybe this is what you want anyway?</p>
</div>
<div id="comment-21002-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 15:14)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20990-form-container" class="comment-form-container">
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

<span id="20994"></span>

<div id="answer-container-20994" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20994-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What kind of analysis you plan on doing on the data? This will be the determinant of the data structure you have to read your data into.</p>
<p>Also, be aware that one street may be mapped as multiple connecting ways, and similar street names may occur in different cities.</p>
<p>I don't know if the first node appearing inside</p>
<pre><code>&lt;way id=&quot;126879680&quot; user=&quot;KartoGrapHiti&quot; uid=&quot;57645&quot; visible=&quot;true&quot; version=&quot;1&quot; changeset=&quot;9072314&quot; timestamp=&quot;2011-08-20T09:01:54Z&quot;&gt;
&lt;nd ref=&quot;1405376824&quot;/&gt;
&lt;nd ref=&quot;1405376826&quot;/&gt;
&lt;nd ref=&quot;1405376827&quot;/&gt;
&lt;nd ref=&quot;1405376829&quot;/&gt;
&lt;nd ref=&quot;1405376832&quot;/&gt;
&lt;tag k=&quot;highway&quot; v=&quot;service&quot;/&gt;
&lt;tag k=&quot;oneway&quot; v=&quot;yes&quot;/&gt;
&lt;/way&gt;</code></pre>
<p>is actually the start of the way, for whatever constitutes the start of a street for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '13, 14:52</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Mar '13, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-20994" class="comments-container">
<span id="20998"></span>
<div id="comment-20998" class="comment">
<div id="post-20998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a database of geo position, and I want to map these coordinates to the nodes(coordinates) of the link/route/street present in the map. For this I have to identify the link, which I think can be done if I find the start and end coordinates of the link/route/street</p>
</div>
<div id="comment-20998-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 15:01)</span> <span class="comment-user userinfo">tfarooqi</span>
</div>
</div>
<span id="21001"></span>
<div id="comment-21001" class="comment">
<div id="post-21001-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just for clarification: you don't want to take the actual course of the street into account, just a line-of-sight-connection between the start and end node of the street? So, for a street shaped like a "C", you would get a line that does not resemble the actual street in any way?</p>
<p>Your question is more of a general GIS question and not one specific to OSM. I would suggest you asked it at <a href="http://gis.stackexchange.com/">http://gis.stackexchange.com/</a> .</p>
</div>
<div id="comment-21001-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 15:10)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20994-form-container" class="comment-form-container">
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

