+++
type = "question"
title = "How to render Maps using KML file in OpenStreetMaps"
description = '''Hi, I have downloaded a Shape file from naturalearthdata.com and converted this shape file to KML file using QGIS tool. I want to render my maps using OSM API and this KML file.and vary the color for each of the state from the KML file Can any one guide me to achieve this functionality? Thank you !!'''
date = "2011-11-16T13:21:00Z"
lastmod = "2011-11-18T11:30:00Z"
weight = 9033
keywords = [ "kml" ]
aliases = [ "/questions/9033" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to render Maps using KML file in OpenStreetMaps](/questions/9033/how-to-render-maps-using-kml-file-in-openstreetmaps)

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
<span id="post-9033-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9033-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9033-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have downloaded a Shape file from <a href="http://naturalearthdata.com">naturalearthdata.com</a> and converted this shape file to KML file using QGIS tool.</p>
<p>I want to render my maps using OSM API and this KML file.and vary the color for each of the state from the KML file</p>
<p>Can any one guide me to achieve this functionality?</p>
<p>Thank you !!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-kml" rel="tag" title="see questions tagged &#39;kml&#39;">kml</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '11, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c330e0454ebc0cf055159a5962e4f6ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VenuGopal&#39;s gravatar image" />
<p><span>VenuGopal</span><br />
<span class="score" title="16 reputation points">16</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VenuGopal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9033" class="comments-container">
&#10;</div>
<div id="comment-tools-9033" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9033-form-container" class="comment-form-container">
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

<span id="9040"></span>

<div id="answer-container-9040" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9040-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "OpenStreetMap API" generally refers to the API for editing software. That's something different from what you're after. You can display KML as an overlay on a slippy map (which may be showing OpenStreetMap as a baselayer) Some information about doing that is linked from <a href="http://wiki.openstreetmap.org/wiki/KML">the KML page on the wiki</a>.</p>
<p>However you <em>may</em> have a problem that the KML file you have created is gigantic and will fail to load in the browser (I dont know if that will be a problem, it's just a hunch based on your description) A sensible sanity check might be to try loading it with google earth first of all, before trying a web overlay.</p>
<p>"color for each of the states" could be achieved within the KML definitions. Perhaps QGIS doesn't give you that flexibility with its KML output (anyone know?). You may be able to achieve this by fiddling with the XML file by hand.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '11, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-9040" class="comments-container">
<span id="9065"></span>
<div id="comment-9065" class="comment">
<div id="post-9065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Harry, Thanks a lot for your reply,I am able to load the data from KML file as an overlay. However the polygons defined in the KML file,has a color and I am not getting any color updated over them,I am always getting a default color loaded on to them.</p>
<p>I am not sure How can we make a change,so that it would change the color for that polygon.</p>
<p>Please let me know if you come across this scenario like this.</p>
</div>
<div id="comment-9065-info" class="comment-info">
<span class="comment-age">(17 Nov '11, 09:51)</span> <span class="comment-user userinfo">VenuGopal</span>
</div>
</div>
<span id="9071"></span>
<div id="comment-9071" class="comment">
<div id="post-9071-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you tried editing the KML file directly?</p>
</div>
<div id="comment-9071-info" class="comment-info">
<span class="comment-age">(17 Nov '11, 11:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="9073"></span>
<div id="comment-9073" class="comment">
<div id="post-9073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes,I tried that and modified the KML file as below I kept like this under PlaceMark element and also,I tried with fill and outlibne elements.Still noluck :( &lt;style&gt; &lt;polystyle&gt; &lt;color&gt;44ff0000&lt;/color&gt; &lt;/polystyle&gt; &lt;/style&gt;</p>
<p>Even editing the KML file that did not solved my problem and I gone through few of the forums and they suggested that KML file might have been cached and they want to append "?123" at the end of the KML file URL in Javascript.</p>
<p>I tried that as well,still no luck</p>
<p>Please let me know if you come across any situation</p>
</div>
<div id="comment-9073-info" class="comment-info">
<span class="comment-age">(17 Nov '11, 12:29)</span> <span class="comment-user userinfo">VenuGopal</span>
</div>
</div>
<span id="9105"></span>
<div id="comment-9105" class="comment">
<div id="post-9105-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting thing is ,when I loaded the KML file in the QGis Tool,I am able to see the color for that state,but when I am using with OSM API,I always see the default color(Orange)</p>
</div>
<div id="comment-9105-info" class="comment-info">
<span class="comment-age">(18 Nov '11, 11:30)</span> <span class="comment-user userinfo">VenuGopal</span>
</div>
</div>
</div>
<div id="comment-tools-9040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9040-form-container" class="comment-form-container">
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

