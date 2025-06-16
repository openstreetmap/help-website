+++
type = "question"
title = "How to show cursor position in degrees in OpenLayers?"
description = '''I&#x27;d like to place a simple map on a page, and the cursor location should be shown. I can do this but the location is shown in meters instead of degrees. How can I change the units to degrees? &amp;lt;!DOCTYPE HTML&amp;gt; &amp;lt;title&amp;gt;OpenLayers Mouse Location Test&amp;lt;/title&amp;gt; &amp;lt;div id=&quot;demoMap&quot; style=&quot;...'''
date = "2014-01-13T21:09:00Z"
lastmod = "2014-01-15T10:23:00Z"
weight = 29815
keywords = [ "cursor", "degrees", "meters", "mouseposition", "openlayers" ]
aliases = [ "/questions/29815" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to show cursor position in degrees in OpenLayers?](/questions/29815/how-to-show-cursor-position-in-degrees-in-openlayers)

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
<span id="post-29815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29815-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to place a simple map on a page, and the cursor location should be shown. I can do this but the location is shown in meters instead of degrees.</p>
<p>How can I change the units to degrees?</p>
<pre><code>&lt;!DOCTYPE HTML&gt;
&lt;title&gt;OpenLayers Mouse Location Test&lt;/title&gt;
&lt;div id=&quot;demoMap&quot; style=&quot;height:250px&quot;&gt;&lt;/div&gt;
&lt;script src=&quot;OpenLayers.js&quot;&gt;&lt;/script&gt;
&#10;&lt;script&gt;
    map = new OpenLayers.Map(&quot;demoMap&quot;);
    map.addLayer(new OpenLayers.Layer.OSM());
    map.addControl(new OpenLayers.Control.MousePosition());
    map.zoomToMaxExtent();
&lt;/script&gt;</code></pre>
<p>Edit. Here's a screenshot clip of the map from the code above shown in Firefox:</p>
<p><img src="/upfiles/Screenshot-OpenLayers_Mouse_Location_Test_-_Mozilla_Firefox.png" alt="Example map. Cursor is between Spain and Italy, and the widget displays &quot;694659.71296, 4921321.62843&quot;." /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-cursor" rel="tag" title="see questions tagged &#39;cursor&#39;">cursor</span> <span class="post-tag tag-link-degrees" rel="tag" title="see questions tagged &#39;degrees&#39;">degrees</span> <span class="post-tag tag-link-meters" rel="tag" title="see questions tagged &#39;meters&#39;">meters</span> <span class="post-tag tag-link-mouseposition" rel="tag" title="see questions tagged &#39;mouseposition&#39;">mouseposition</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '14, 21:09</strong></p>
<img src="https://secure.gravatar.com/avatar/74350d6288ba179b756f3b37346e52ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gibbousmoon&#39;s gravatar image" />
<p><span>gibbousmoon</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gibbousmoon has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '14, 12:37</strong> </span></p>
</div>
</div>
<div id="comments-container-29815" class="comments-container">
&#10;</div>
<div id="comment-tools-29815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29815-form-container" class="comment-form-container">
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

<span id="29834"></span>

<div id="answer-container-29834" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29834-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29834-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-29834-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gibbousmoon has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This isn't a question for openstreetmap - it's purely an openlayers question. You'd be better asking on the <a href="http://trac.osgeo.org/openlayers/wiki/MailingLists">openlayers mailing lists</a> or on <a href="http://gis.stackexchange.com/">gis.stackexchange.com</a></p>
<p>In saying that, I know the answer since I've done this in the past :-) You need to set the projection of your map, and the displayProjection too. Controls like permalink and mouseposition use the displayProjection but often go wrong if the map projection isn't set too. Try something like:</p>
<pre><code>map = new OpenLayers.Map(divName,
      { maxExtent: new OpenLayers.Bounds(-20037508,-20037508,20037508,20037508),
        numZoomLevels: 19,
        maxResolution: 156543,
        units: &#39;m&#39;,
        projection: &quot;EPSG:900913&quot;,
        controls: [
          new OpenLayers.Control.LayerSwitcher({roundedCornerColor: &quot;#575757&quot;}),
          new OpenLayers.Control.Permalink(&#39;permalink&#39;),
          new OpenLayers.Control.Permalink(&#39;editlink&#39;, &#39;https://www.openstreetmap.org/edit.html&#39;),
          new OpenLayers.Control.Attribution(),
          new OpenLayers.Control.PanZoomBar(),
          new OpenLayers.Control.Navigation()
        ],
        displayProjection:  new OpenLayers.Projection(&quot;EPSG:4326&quot;) });</code></pre>
<p>(taken from the OpenCycleMap source code)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '14, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-29834" class="comments-container">
<span id="29848"></span>
<div id="comment-29848" class="comment">
<div id="post-29848-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thank you so much for the answer! :) Problem solved.</p>
<p>My apologies for posting this question here. To be honest, I didn't quite see how close this thing called OpenLayers is related to OSM.</p>
</div>
<div id="comment-29848-info" class="comment-info">
<span class="comment-age">(15 Jan '14, 10:23)</span> <span class="comment-user userinfo">gibbousmoon</span>
</div>
</div>
</div>
<div id="comment-tools-29834" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29834-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29828"></span>

<div id="answer-container-29828" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29828-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The position <em>is</em> shown in degrees and not meters. Perhaps you want degrees.minutes.seconds or some other format instead of decimal degrees ? Which one ?</p>
<p>Sorry there <a href="http://dev.openlayers.org/docs/files/OpenLayers/Control/MousePosition-js.html">doesn't seem to be an option</a> to change the unit displayed in mouseposition. You could try patching mouseposition.js to get your prefered format.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jan '14, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-29828" class="comments-container">
<span id="29829"></span>
<div id="comment-29829" class="comment">
<div id="post-29829-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That said, non-decimal lat/long formats really should be forgoten about. Many people are used to them, but they are just pointlessly complicated, inherited from the time when a sextan was the best way to measure your location. Decimal degrees are <em>better</em>.</p>
<p>Decimal degrees (decimal units in general) really should be the only kind you use. Consider changing all your tools (including your brain) to decimal instead of the other way around.</p>
</div>
<div id="comment-29829-info" class="comment-info">
<span class="comment-age">(14 Jan '14, 09:36)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="29830"></span>
<div id="comment-29830" class="comment">
<div id="post-29830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer but it's not at all about deg:min:sec vs. decimal degs.</p>
<p>I had a many hours battle with OpenLayers but still cannot figure out how to change the units. The units are lying somewhere in class map or layer or projection. There must be a simple solution to this problem. I hope this a relevant question in this help center.</p>
</div>
<div id="comment-29830-info" class="comment-info">
<span class="comment-age">(14 Jan '14, 13:03)</span> <span class="comment-user userinfo">gibbousmoon</span>
</div>
</div>
</div>
<div id="comment-tools-29828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29828-form-container" class="comment-form-container">
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

