+++
type = "question"
title = "New to Maperitive, Trying to Get Relation to Display"
description = '''I have a relation (https://www.openstreetmap.org/relation/295355) I want to load into Maperitive. I&#x27;m really struggling though. At the link above, I use the Download XML button and manage to save a file in .osm format. I remove the XML tag at the top of the OSM file, because that&#x27;s the only way Mape...'''
date = "2020-10-30T17:02:00Z"
lastmod = "2023-12-16T21:30:00Z"
weight = 77328
keywords = [ "relations", "how-to" ]
aliases = [ "/questions/77328" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [New to Maperitive, Trying to Get Relation to Display](/questions/77328/new-to-maperitive-trying-to-get-relation-to-display)

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
<span id="post-77328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77328-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a relation (<a href="https://www.openstreetmap.org/relation/295355)">https://www.openstreetmap.org/relation/295355)</a> I want to load into Maperitive. I'm really struggling though.</p>
<p>At the link above, I use the Download XML button and manage to save a file in .osm format. I remove the XML tag at the top of the OSM file, because that's the only way Maperitive will recognize and open the file. i.e. see below.</p>
<p>I load it to Maperitive (v2.4.3), seemingly successfully. It's listed and gold-starred in the Map Sources lists. But for the life of me, I can't get the boundary to display. What am I missing? I've read something about topmost-layer property, but this thing isn't too user friendly...</p>
<pre><code>&lt;osm version=&quot;0.6&quot; generator=&quot;CGImap 0.8.3 (2320392 spike-08.openstreetmap.org)&quot; copyright=&quot;OpenStreetMap and contributors&quot; attribution=&quot;https://www.openstreetmap.org/copyright&quot; license=&quot;http://opendatacommons.org/licenses/odbl/1-0/&quot;&gt;
&#10;&lt;relation id=&quot;295355&quot; visible=&quot;true&quot; version=&quot;44&quot; changeset=&quot;68619793&quot; timestamp=&quot;2019-03-28T10:31:19Z&quot; user=&quot;This Is A Display Name Desu&quot; uid=&quot;196051&quot;&gt;
&lt;member type=&quot;way&quot; ref=&quot;128565169&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128651122&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128650417&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;582704525&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;582706226&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;582706227&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128648174&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128648180&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128642791&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128642785&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128642793&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128642789&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128565194&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128664044&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128663151&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128663153&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128663154&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128663152&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;574890206&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128657132&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128651805&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128651806&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128651288&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128651124&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;way&quot; ref=&quot;128651119&quot; role=&quot;outer&quot;/&gt;
&lt;member type=&quot;node&quot; ref=&quot;20971094&quot; role=&quot;admin_centre&quot;/&gt;
&lt;tag k=&quot;admin_level&quot; v=&quot;8&quot;/&gt;
&lt;tag k=&quot;boundary&quot; v=&quot;administrative&quot;/&gt;
&lt;tag k=&quot;council_name&quot; v=&quot;Cambridge City Council&quot;/&gt;
&lt;tag k=&quot;name&quot; v=&quot;Cambridge&quot;/&gt;
&lt;tag k=&quot;name:zh&quot; v=&quot;劍橋&quot;/&gt;
&lt;tag k=&quot;ons_code&quot; v=&quot;12UB&quot;/&gt;
&lt;tag k=&quot;ref:gss&quot; v=&quot;E07000008&quot;/&gt;
&lt;tag k=&quot;source:ons_code&quot; v=&quot;OS_OpenData_CodePoint Codelist.txt&quot;/&gt;
&lt;tag k=&quot;type&quot; v=&quot;boundary&quot;/&gt;
&lt;tag k=&quot;wikidata&quot; v=&quot;Q21713103&quot;/&gt;
&lt;tag k=&quot;wikipedia&quot; v=&quot;en:Cambridge&quot;/&gt;
&lt;/relation&gt;
&#10;&lt;/osm&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-how-to" rel="tag" title="see questions tagged &#39;how-to&#39;">how-to</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Oct '20, 17:02</strong></p>
<img src="https://secure.gravatar.com/avatar/bb4a96818219ef4d7ac338f922f02437?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike_302&#39;s gravatar image" />
<p><span>mike_302</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike_302 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77328" class="comments-container">
&#10;</div>
<div id="comment-tools-77328" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77328-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="77333"></span>

<div id="answer-container-77333" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77333-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I know nothing about Maperative, but if that is the entirety of your OSM file you appear to be missing the actual geometry. Relations reference other geometry types, so unless you have included the referenced elements in your file the software will have very little to go on. See <a href="https://wiki.openstreetmap.org/wiki/Elements">this page</a> for more information about the three element types that are used within OSM.</p>
<p>If you export the result of for example <a href="https://overpass-turbo.eu/s/ZyR">this Overpass query</a> as and load that into Maperative, do you get the desired effect?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '20, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '20, 00:17</strong> </span></p>
</div>
</div>
<div id="comments-container-77333" class="comments-container">
<span id="77334"></span>
<div id="comment-77334" class="comment">
<div id="post-77334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, it's the entirety of the Relation, as far as I understand these things (which is not very much...) Maperitive initializes with an OSM Map (OSM Mapnik). Then, as I understand the mechanics, you load in additional Map data (like Relations). My reference is the Loading Map Data heading on this page: <a href="http://maperitive.net/docs/TenMinutesIntro.html">http://maperitive.net/docs/TenMinutesIntro.html</a></p>
</div>
<div id="comment-77334-info" class="comment-info">
<span class="comment-age">(31 Oct '20, 09:26)</span> <span class="comment-user userinfo">mike_302</span>
</div>
</div>
<span id="77335"></span>
<div id="comment-77335" class="comment">
<div id="post-77335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Relations have no geometry of their own, so yes it is all of the relation, but unless you download the geometry it refers to ( <code>member type="way" ref="128565169" role="outer"/</code> etc.) Maperative will have no geometry to render.</p>
<p>The xml generated by the query I linked is 1660 lines long rather than the 47 lines for the relation itself as it includes all of the members. If you follow the link I provided and select <em>Run</em> then <em>Export</em> &gt; <em>download/copy as raw OSM data</em>, does the resulting file load correctly in Maperative?</p>
</div>
<div id="comment-77335-info" class="comment-info">
<span class="comment-age">(31 Oct '20, 10:21)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-77333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77333-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="88058"></span>

<div id="answer-container-88058" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-88058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-88058-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-88058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="/upfiles/IMG_20231126_053945.jpg" alt="alt text" />This XML file does not appear to have any style information associated with it. The document tree is shown below. &lt;osm version="0.6" generator="CGImap 0.8.10 (3607142 spike-06.openstreetmap.org)" copyright="OpenStreetMap and contributors" attribution="https://www.openstreetmap.org/copyright" license="http://opendatacommons.org/licenses/odbl/1-0/"&gt; &lt;relation id="10249598" visible="true" version="4" changeset="143225600" timestamp="2023-10-27T18:59:32Z" user="ramseraph1" uid="13327813"&gt; &lt;member type="way" ref="741276431" role="outer"/&gt; &lt;member type="way" ref="741917457" role="outer"/&gt; &lt;member type="way" ref="741311834" role="outer"/&gt; &lt;member type="way" ref="741311788" role="outer"/&gt; &lt;member type="way" ref="741311817" role="outer"/&gt; &lt;member type="way" ref="741311815" role="outer"/&gt; &lt;member type="node" ref="245747076" role="admin_centre"/&gt; &lt;tag k="admin_level" v="6"/&gt; &lt;tag k="boundary" v="administrative"/&gt; &lt;tag k="&amp;lt;img alt=" alt="" text"="" src="http://Mehsi,Bihar.com"/&gt;name" v="Mehsi"/&gt; &lt;tag k="town" v="Kaswa Mehsi"/&gt; &lt;tag k="type" v="boundary"/&gt; &lt;/relation&gt; &lt;/osm&gt;</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '23, 21:30</strong></p>
<img src="https://secure.gravatar.com/avatar/eb7ad479f7c100444177e8afbcce5b31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Motiharicity&#39;s gravatar image" />
<p><span>Motiharicity</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Motiharicity has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '23, 21:52</strong> </span></p>
</div>
</div>
<div id="comments-container-88058" class="comments-container">
&#10;</div>
<div id="comment-tools-88058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-88058-form-container" class="comment-form-container">
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

