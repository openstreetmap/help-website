+++
type = "question"
title = "overpass doesn&#x27;t find all banks"
description = '''Hello, I am new to using the overpass page, I am trying to extract the number of banks that are in an area of Bogota, Colombia. The problem is that I cannot find all the banks that are in a box. For example, Bancolombia, although when entering the open street map website, it appears in the category ...'''
date = "2020-09-05T00:33:00Z"
lastmod = "2020-09-06T00:49:00Z"
weight = 76442
keywords = [ "overpassapi", "overpass", "overpass-turbo" ]
aliases = [ "/questions/76442" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [overpass doesn't find all banks](/questions/76442/overpass-doesnt-find-all-banks)

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
<span id="post-76442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76442-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I am new to using the overpass page, I am trying to extract the number of banks that are in an area of Bogota, Colombia. The problem is that I cannot find all the banks that are in a box. For example, Bancolombia, although when entering the open street map website, it appears in the category of amaneity bank. Thanks for any suggestions.</p>
<p>Your query in pretty Overpass QL: <a href="http://overpass-turbo.eu/s/XIn">overpass</a></p>
<pre><code>node
  [&quot;amenity&quot;=&quot;bank&quot;]
  (4.6304414673187,-74.075607061386,4.6332058140013,-74.072549343109);
out;</code></pre>
<p><a href="https://www.openstreetmap.org/way/392010374#map=18/4.63169/-74.07486">Open street map - Bancolombia (392010374)</a></p>
<pre><code>Etiquetas 
_____________________________________
addr:city         | Bogotá 
addr:country      | CO 
addr:district     | Teusaquillo 
addr:housenumber  | 40-95
addr:state        | Distrito Capital
addr:street       | Carrera 24
addr:suburb       | La Soledad
amenity           | bank
atm               | yes
brand             | Bancolombia
_____________________________________</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '20, 00:33</strong></p>
<img src="https://secure.gravatar.com/avatar/e5f5e2b902f3ef1991c190295c84e794?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rafael%20Eduardo%20Diaz&#39;s gravatar image" />
<p><span>Rafael Eduar...</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rafael Eduardo Diaz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76442" class="comments-container">
&#10;</div>
<div id="comment-tools-76442" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76442-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="76450"></span>

<div id="answer-container-76450" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76450-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rafael Eduardo Diaz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Rafael, I think the problem is that your query is only looking for banks mapped as nodes, and some of the banks in your search area are mapped as ways. These are both valid methods of mapping banks, depending on the circumstances, so if you're searching for all banks you'll have to check nodes and ways.</p>
<p>Try this search instead:</p>
<pre><code>nwr[&quot;amenity&quot;=&quot;bank&quot;](4.6304414673187,-74.075607061386,4.6332058140013,-74.072549343109);
out body;
&gt;;
out skel qt;</code></pre>
<p>The "nwr" command will search for both nodes and ways. It will also search for relations, which might be used to represent, for instance, a bank building with a courtyard. (Here's a bank mapped as a relation: <a href="https://www.openstreetmap.org/relation/2544819">https://www.openstreetmap.org/relation/2544819</a>.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '20, 03:45</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-76450" class="comments-container">
&#10;</div>
<div id="comment-tools-76450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76450-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76443"></span>

<div id="answer-container-76443" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76443-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I find the straight Qverpass Query code too difficult so I used the Overpass Turbo Wizard to find banks with name=Bancolumbia in Bogota and it produced many nodes and polygons. Try it yourself — the link below will be a starting point. Your example asked only for nodes but some of the banks may be mapped as polygons so I did not restrict the query at all.</p>
<p>amenity=bank and brand=Bancolombia in Bogotá</p>
<p><a href="http://overpass-turbo.eu/s/XIq">http://overpass-turbo.eu/s/XIq</a></p>
<p>Note I used name=Bancolombia rather than brand=Bancolumbia. To obtain banks that had the brand tag but not the name tag, or vice-versa, just add the extra condition enclosed in parentheses with an or operation.</p>
<p>amenity=bank and (name=Bancolombia or brand=Bancolumbia) in Bogotá</p>
<p><a href="http://overpass-turbo.eu/s/XIs">http://overpass-turbo.eu/s/XIs</a></p>
<p>You could also restrict your query to your area of interest by using the bounding box data or enclosing the area in your view and deleting the "in Bogotá" part of the query.</p>
<p>Hope this helps.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '20, 01:14</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Sep '20, 01:20</strong> </span></p>
</div>
</div>
<div id="comments-container-76443" class="comments-container">
<span id="76445"></span>
<div id="comment-76445" class="comment">
<div id="post-76445-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello thank you, how could I find all the banks in the polygon, which is what I need.</p>
</div>
<div id="comment-76445-info" class="comment-info">
<span class="comment-age">(05 Sep '20, 01:18)</span> <span class="comment-user userinfo">Rafael Eduar...</span>
</div>
</div>
<span id="76446"></span>
<div id="comment-76446" class="comment">
<div id="post-76446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you could add type:relation connected with an AND to the previous examples:</p>
<p>type:relation and amenity=bank and (name=Bancolombia or brand=Bancolumbia) in Bogotá</p>
</div>
<div id="comment-76446-info" class="comment-info">
<span class="comment-age">(05 Sep '20, 01:22)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="76449"></span>
<div id="comment-76449" class="comment">
<div id="post-76449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>However, the AV Villas bank is yet to be found in this polygon. <a href="https://www.openstreetmap.org/way/392010458#map=19/4.63106/-74.07539">https://www.openstreetmap.org/way/392010458#map=19/4.63106/-74.07539</a></p>
</div>
<div id="comment-76449-info" class="comment-info">
<span class="comment-age">(05 Sep '20, 02:13)</span> <span class="comment-user userinfo">Rafael Eduar...</span>
</div>
</div>
</div>
<div id="comment-tools-76443" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76443-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76470"></span>

<div id="answer-container-76470" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76470-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76470-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76470-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"extract the number of banks that are in an area of Bogota"</p>
<p>This is the answer to question as written:</p>
<pre><code>{{geocodeArea:Bogotá}};
nwr[amenity=bank](area);
out count;
out meta center;</code></pre>
<p><a href="https://overpass-turbo.eu/s/XJT">https://overpass-turbo.eu/s/XJT</a></p>
<p>It searches for an area with the name Bogotá. It then searches for all banks within the boundary of that area. It outputs a visual representation ('map' tab) &amp; a count of all the banks broken down into how they're mapped ('data' tab).</p>
<p>If you wish to show the boundary:</p>
<pre><code>{{geocodeArea:Bogotá}};
rel(pivot)-&gt;.District;
nwr[amenity=bank](area);
out count;
out meta center;
way(r.District);
out geom;</code></pre>
<p><a href="https://overpass-turbo.eu/s/XJU">https://overpass-turbo.eu/s/XJU</a></p>
<p>You can filter for specific banks by using the name tag, but use the '~' symbol instead of '=' which searches for all names that <strong>includes</strong> 'Bancolombia' It returns more items</p>
<pre><code>{{geocodeArea:Bogotá}};
nwr[amenity=bank][name~Bancolombia](area);
out count;
out meta center;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '20, 00:49</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '20, 00:54</strong> </span></p>
</div>
</div>
<div id="comments-container-76470" class="comments-container">
&#10;</div>
<div id="comment-tools-76470" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76470-form-container" class="comment-form-container">
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

