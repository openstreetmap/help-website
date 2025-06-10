+++
type = "question"
title = "Cannot see GPS track on map using OpenLayers vector layer"
description = '''Sorry for the bad formatting as I am new to this. I am using the code from here: http://wiki.openstreetmap.org/wiki/Openlayers_Track_example and I have used the GPX data from here: http://forum.openstreetmap.org/viewtopic.php?id=17278 and stored it in a static file on disk c:&#92;tracks.gpx And this is ...'''
date = "2013-04-17T09:10:00Z"
lastmod = "2013-04-19T02:59:00Z"
weight = 21619
keywords = [ "gpx", "openlayers" ]
aliases = [ "/questions/21619" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Cannot see GPS track on map using OpenLayers vector layer](/questions/21619/cannot-see-gps-track-on-map-using-openlayers-vector-layer)

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
<span id="post-21619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21619-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sorry for the bad formatting as I am new to this.</p>
<p>I am using the code from here: <a href="http://wiki.openstreetmap.org/wiki/Openlayers_Track_example">http://wiki.openstreetmap.org/wiki/Openlayers_Track_example</a></p>
<p>and I have used the GPX data from here: <a href="http://forum.openstreetmap.org/viewtopic.php?id=17278">http://forum.openstreetmap.org/viewtopic.php?id=17278</a> and stored it in a static file on disk c:\tracks.gpx</p>
<p>And this is how I create the layer:</p>
<pre><code>var lgpx = new OpenLayers.Layer.Vector(&quot;Lakeside cycle ride&quot;, &quot;c:/tracks.gpx&quot;,{
                strategies: [new OpenLayers.Strategy.Fixed()],
                protocol: new OpenLayers.Protocol.HTTP({
                    format: new OpenLayers.Format.GPX()
                }),
                style: {strokeColor: &quot;green&quot;, strokeWidth: 5, strokeOpacity: 0.5},
                projection: new OpenLayers.Projection(&quot;EPSG:4326&quot;)
            });
            map.addLayer(lgpx);</code></pre>
<p>What am I doing wrong ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Apr '13, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/c3c0019d2e50e99bfa1560c6aa07c560?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CarTay&#39;s gravatar image" />
<p><span>CarTay</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CarTay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Apr '13, 12:27</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-21619" class="comments-container">
&#10;</div>
<div id="comment-tools-21619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21619-form-container" class="comment-form-container">
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

<span id="21621"></span>

<div id="answer-container-21621" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21621-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-21621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="CarTay has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>have a look in your JavaScript error console (ctrl+shift+J in Firefox and some other browsers).</p>
<p>I could imagine that the read access to that local file via JavaScript in your browser is not allowed by your browser (even if your user may have read access). Try to place the html file and the gpx file on a web server.</p>
<p>Mention what your problem was if you solved it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Apr '13, 12:35</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '13, 02:26</strong> </span></p>
</div>
</div>
<div id="comments-container-21621" class="comments-container">
<span id="21653"></span>
<div id="comment-21653" class="comment">
<div id="post-21653-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the suggestion, will try it out and post the results.</p>
</div>
<div id="comment-21653-info" class="comment-info">
<span class="comment-age">(19 Apr '13, 01:45)</span> <span class="comment-user userinfo">CarTay</span>
</div>
</div>
<span id="21654"></span>
<div id="comment-21654" class="comment">
<div id="post-21654-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>By moving the file to my web server the map now displays the contents of the .px file. Awesome !</p>
<p>Thanks aseerel4c26 !</p>
</div>
<div id="comment-21654-info" class="comment-info">
<span class="comment-age">(19 Apr '13, 02:41)</span> <span class="comment-user userinfo">CarTay</span>
</div>
</div>
<span id="21655"></span>
<div id="comment-21655" class="comment">
<div id="post-21655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the feedback. You really may see helpful errors/messages in the console (clear before running the script).</p>
<p>I have <span>clarified the wiki page</span> a bit.</p>
</div>
<div id="comment-21655-info" class="comment-info">
<span class="comment-age">(19 Apr '13, 02:59)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-21621" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21621-form-container" class="comment-form-container">
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

