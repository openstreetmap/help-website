+++
type = "question"
title = "How to conver downloaded element of map( .xml) in kml or any other format appropriate for google?"
description = '''I went to the link  https://www.openstreetmap.org/relation/3198047#map=6/21.384/97.027&amp;amp;layers=T then at the end of members list, I have pressed &quot;Download XML&quot;. I have tried to covert downloaded file by https://mygeodata.cloud/converter/  it didn&#x27;t help.'''
date = "2019-09-11T10:57:00Z"
lastmod = "2019-09-11T15:49:00Z"
weight = 70735
keywords = [ "xml", "convert", "kml", "road", "element" ]
aliases = [ "/questions/70735" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to conver downloaded element of map( .xml) in kml or any other format appropriate for google?](/questions/70735/how-to-conver-downloaded-element-of-map-xml-in-kml-or-any-other-format-appropriate-for-google)

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
<span id="post-70735-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70735-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70735-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I went to the link <a href="https://www.openstreetmap.org/relation/3198047#map=6/21.384/97.027&amp;layers=T">https://www.openstreetmap.org/relation/3198047#map=6/21.384/97.027&amp;layers=T</a> then at the end of members list, I have pressed "Download XML". I have tried to covert downloaded file by <a href="https://mygeodata.cloud/converter/">https://mygeodata.cloud/converter/</a> it didn't help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-element" rel="tag" title="see questions tagged &#39;element&#39;">element</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '19, 10:57</strong></p>
<img src="https://secure.gravatar.com/avatar/25389f4eeccc273f33399195e32b8e01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dizzymezz&#39;s gravatar image" />
<p><span>Dizzymezz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dizzymezz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70735" class="comments-container">
&#10;</div>
<div id="comment-tools-70735" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70735-form-container" class="comment-form-container">
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

<span id="70738"></span>

<div id="answer-container-70738" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70738-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-70738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "Download XML" link mentioned in the question just gives the relation members (ways), and not their member nodes so there will be no latitudes and longitudes. I think you can add /full on the end, but wouldn't recommend it for this rather long relation due to the load on the API. See perhaps instead this question:</p>
<p><a href="https://help.openstreetmap.org/questions/23679/how-to-export-a-route-relation-as-gpx-or-kml">https://help.openstreetmap.org/questions/23679/how-to-export-a-route-relation-as-gpx-or-kml</a></p>
<p>The accepted answer there is to use Overpass Turbo, like this:</p>
<p><a href="http://overpass-turbo.eu/s/Meo">http://overpass-turbo.eu/s/Meo</a></p>
<p>Run the query, then choose an export option.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '19, 15:49</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-70738" class="comments-container">
&#10;</div>
<div id="comment-tools-70738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70738-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="70737"></span>

<div id="answer-container-70737" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70737-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>see</p>
<ul>
<li><a href="https://help.openstreetmap.org/questions/10503/simple-convert-osm-to-kml">https://help.openstreetmap.org/questions/10503/simple-convert-osm-to-kml</a></li>
<li><a href="https://help.openstreetmap.org/questions/849/how-to-convert-osm-to-kml-format">https://help.openstreetmap.org/questions/849/how-to-convert-osm-to-kml-format</a></li>
</ul>
<p>or perhaps</p>
<p><a href="https://www.gpsvisualizer.com/gpsbabel/">https://www.gpsvisualizer.com/gpsbabel/</a> (if OpenStreetMap data files are indeed the format you downloaded)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '19, 14:44</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '19, 14:44</strong> </span></p>
</div>
</div>
<div id="comments-container-70737" class="comments-container">
&#10;</div>
<div id="comment-tools-70737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70737-form-container" class="comment-form-container">
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

