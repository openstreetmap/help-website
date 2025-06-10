+++
type = "question"
title = "geo-referenced house numbers from OSM through LinkedGeoData"
description = '''I have a question regarding the retrieval of the house numbers from Open Street Map through the Linked Geo Data sparql endpoint: If I run a query to select all the buildings which have a house number located in the city of, for example, of Esino Lario I get only 11 results whereas in OSM seems that ...'''
date = "2016-02-05T17:08:00Z"
lastmod = "2016-02-06T10:55:00Z"
weight = 47958
keywords = [ "linkeddata", "housenumbers", "linkedgeodata", "geocoding", "housenumbering" ]
aliases = [ "/questions/47958" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [geo-referenced house numbers from OSM through LinkedGeoData](/questions/47958/geo-referenced-house-numbers-from-osm-through-linkedgeodata)

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
<span id="post-47958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47958-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a question regarding the retrieval of the house numbers from Open Street Map through the <a href="http://linkedgeodata.org/About">Linked Geo Data</a> <a href="http://linkedgeodata.org/sparql">sparql endpoint</a>:</p>
<p>If I run a query to select all the buildings which have a house number located in the city of, for example, of Esino Lario I get only 11 results whereas in OSM seems that a lot of building of that village have explicitly indicated a housenumber (compare the <a href="http://linkedgeodata.org/sparql?default-graph-uri=http%3A%2F%2Flinkedgeodata.org&amp;query=Select%20*%0D%0AWhere%20%7B%0D%0A%3Fs%0D%0A%20%20%20%20%3Chttp%3A%2F%2Flinkedgeodata.org%2Fontology%2Faddr%253Acity%3E%20%22Esino%20Lario%22%3B%0D%0A%20%20%20%20%3Chttp%3A%2F%2Flinkedgeodata.org%2Fontology%2Faddr%253Ahousenumber%3E%20%3Fhousenumber.%0D%0A%7D&amp;format=text%2Fhtml&amp;timeout=0&amp;debug=on">query result</a> with the <a href="https://www.openstreetmap.org/#map=17/45.99498/9.33471">actual view from OSM</a>).</p>
<p>Even if i expand my search to the whole world broadening the research to include all possibilities I get only 1,176,404 results which seems not reasonable at all (<a href="http://linkedgeodata.org/sparql?default-graph-uri=http%3A%2F%2Flinkedgeodata.org&amp;query=Select%20count%28%3Fhousenumber%20%29%20as%20%3Fn%0D%0A%20%20%20%20Where%20%7B%20%3Fs%20%20%3Chttp%3A%2F%2Flinkedgeodata.org%2Fontology%2Faddr%253Ahousenumber%3E%20%3Fhousenumber%20%7D&amp;format=text%2Fhtml&amp;timeout=0&amp;debug=on">here the query result</a>).</p>
<p>The queries used are the following:</p>
<pre><code>Select *
Where {
?s
    &lt;http://linkedgeodata.org/ontology/addr%3Acity&gt; &quot;Esino Lario&quot;;
    &lt;http://linkedgeodata.org/ontology/addr%3Ahousenumber&gt; ?housenumber.
}</code></pre>
<p>and</p>
<pre><code>Select count(?housenumber ) as ?n
Where { ?s  &lt;http://linkedgeodata.org/ontology/addr%3Ahousenumber&gt; ?housenumber }</code></pre>
<p>Seems that the LGD database is not complete or not updated at Jan 2016 as declared. Or, which is more plausible, I am doing some bad mistakes in the query or I do not understand properly the ontology used.</p>
<p>Can somebody please help me unravel this mystery? Responses that do not involve SPARQL but help me better understand the taxonomy of OSM are also appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-linkeddata" rel="tag" title="see questions tagged &#39;linkeddata&#39;">linkeddata</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span> <span class="post-tag tag-link-linkedgeodata" rel="tag" title="see questions tagged &#39;linkedgeodata&#39;">linkedgeodata</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-housenumbering" rel="tag" title="see questions tagged &#39;housenumbering&#39;">housenumbering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Feb '16, 17:08</strong></p>
<img src="https://secure.gravatar.com/avatar/58d5627ab8324e45c23f4262e3ee7c24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ilTrabucchiere&#39;s gravatar image" />
<p><span>ilTrabucchiere</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ilTrabucchiere has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '16, 13:33</strong> </span></p>
</div>
</div>
<div id="comments-container-47958" class="comments-container">
<span id="47974"></span>
<div id="comment-47974" class="comment">
<div id="post-47974-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>My first intention to get a solution for you was to recommend a direct contact to the guys from LinkedGeoData.org, then I saw your posting in their googlegroup mailinglist ... so lets see where you get better hints.</p>
</div>
<div id="comment-47974-info" class="comment-info">
<span class="comment-age">(06 Feb '16, 10:55)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-47958" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47958-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

