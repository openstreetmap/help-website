+++
type = "question"
title = "Why not displayed the elevation data in the osm in the converted map?"
description = '''Using Java OpenStreetMap - Editor, I convert contour.osm into contour.map. As plugins, I use mapsforge-map-writer-master-20180501.133614-216-jar-with-dependencies.jar. The elevation data in the contour.osm is not displayed in the converted contour.map . What&#x27;s the problem? Do you have any solution a...'''
date = "2018-05-17T12:51:00Z"
lastmod = "2018-05-17T13:52:00Z"
weight = 63535
keywords = [ "elevation", "data", "contour" ]
aliases = [ "/questions/63535" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why not displayed the elevation data in the osm in the converted map?](/questions/63535/why-not-displayed-the-elevation-data-in-the-osm-in-the-converted-map)

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
<span id="post-63535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63535-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Using Java OpenStreetMap - Editor, I convert contour.osm into contour.map. As plugins, I use mapsforge-map-writer-master-20180501.133614-216-jar-with-dependencies.jar. The elevation data in the contour.osm is not displayed in the converted contour.map . What's the problem? Do you have any solution about this?</p>
<pre><code>*Some of contour.osm is as following;</code></pre>
&lt;osm version="0.6" generator="Global Mapper"&gt; &lt;bounds minlat="33.728736" minlon="126.356245" maxlat="33.730543" maxlon="126.359227"/&gt; &lt;node id="-534648673" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7293008513" lon="126.3562448712"/&gt; &lt;node id="-534648674" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7292933559" lon="126.3562449265"/&gt; &lt;node id="-534648672" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7293158565" lon="126.3562477517"/&gt; &lt;node id="-534648675" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7292883733" lon="126.3562479546"/&gt; &lt;node id="-534648676" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7292846400" lon="126.3562509735"/&gt; &lt;node id="-534648668" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7293783469" lon="126.3562532728"/&gt; &lt;node id="-534648669" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7293733500" lon="126.3562533097"/&gt; &lt;node id="-534648677" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7292809067" lon="126.3562539924"/&gt; &lt;node id="-534648667" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7293846074" lon="126.3562562179"/&gt; &lt;node id="-534648666" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7293958649" lon="126.3562591261"/&gt; &lt;node id="-534648671" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1" lat="33.7293433971" lon="126.3562595136"/&gt;
<p>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>
<p>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</p>
<p>&lt;way id="-52607" timestamp="2018-04-23T20:09:19Z" uid="217598" user="ajiandachi" version="1"&gt; &lt;nd ref="-534650507"/&gt; &lt;nd ref="-534650508"/&gt; &lt;nd ref="-534650509"/&gt; &lt;nd ref="-534650510"/&gt; &lt;nd ref="-534650511"/&gt; &lt;nd ref="-534650512"/&gt; &lt;nd ref="-534650513"/&gt; &lt;nd ref="-534650514"/&gt; &lt;nd ref="-534650515"/&gt; &lt;nd ref="-534650516"/&gt; &lt;nd ref="-534650517"/&gt; &lt;nd ref="-534650518"/&gt; &lt;nd ref="-534650519"/&gt; &lt;nd ref="-534650520"/&gt; &lt;nd ref="-534650521"/&gt; &lt;nd ref="-534650522"/&gt; &lt;nd ref="-534650523"/&gt; &lt;nd ref="-534650524"/&gt; &lt;nd ref="-534650525"/&gt; &lt;nd ref="-534650526"/&gt; &lt;nd ref="-534650527"/&gt; &lt;nd ref="-534650528"/&gt; &lt;nd ref="-534650529"/&gt; &lt;nd ref="-534650507"/&gt; &lt;tag k="contour_ext" v="elevation_major"/&gt; &lt;tag k="ele" v="80"/&gt; &lt;tag k="contour" v="elevation"/&gt; &lt;/way&gt; &lt;/osm&gt;</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-contour" rel="tag" title="see questions tagged &#39;contour&#39;">contour</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '18, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/cf91f75edb02df465842ccc0e8f49cf1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DjIm&#39;s gravatar image" />
<p><span>DjIm</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DjIm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '18, 13:50</strong> </span></p>
</div>
</div>
<div id="comments-container-63535" class="comments-container">
<span id="63536"></span>
<div id="comment-63536" class="comment">
<div id="post-63536-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That snippet of your .osm file doesn't have any elevation data in it. Can you give an example of something (and OSM object ID, perhaps) that does have elevation data?</p>
</div>
<div id="comment-63536-info" class="comment-info">
<span class="comment-age">(17 May '18, 13:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63539"></span>
<div id="comment-63539" class="comment">
<div id="post-63539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Elevation data inserted</p>
</div>
<div id="comment-63539-info" class="comment-info">
<span class="comment-age">(17 May '18, 13:52)</span> <span class="comment-user userinfo">DjIm</span>
</div>
</div>
</div>
<div id="comment-tools-63535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63535-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

