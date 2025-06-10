+++
type = "question"
title = "feature and popup"
description = '''Hi, I&#x27;m trying to use feature, marker and popup but cannot access the popup properties.  var feature = new OpenLayers.Feature(markers, lonLat);  feature.closeBox = false; feature.popupClass = OpenLayers.Class(OpenLayers.Popup.Anchored, {  &#x27;autoSize&#x27;: true  }); feature.data.popupContentHTML = infoWin...'''
date = "2012-03-22T13:05:00Z"
lastmod = "2012-03-26T13:22:00Z"
weight = 11409
keywords = [ "marker", "popup", "openlayers", "feature" ]
aliases = [ "/questions/11409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [feature and popup](/questions/11409/feature-and-popup)

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
<span id="post-11409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm trying to use feature, marker and popup but cannot access the popup properties.</p>
<pre><code>    var feature = new OpenLayers.Feature(markers, lonLat); 
feature.closeBox = false;
feature.popupClass = OpenLayers.Class(OpenLayers.Popup.Anchored, {
        &#39;autoSize&#39;: true
    });
feature.data.popupContentHTML = infoWindow;</code></pre>
<p>How do I get access to 'backgroundColor' for example? Thanks :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-marker" rel="tag" title="see questions tagged &#39;marker&#39;">marker</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-feature" rel="tag" title="see questions tagged &#39;feature&#39;">feature</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '12, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/079431abbe8de735208cf50b92bbbafe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lowfreq78&#39;s gravatar image" />
<p><span>lowfreq78</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lowfreq78 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '12, 15:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-11409" class="comments-container">
&#10;</div>
<div id="comment-tools-11409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11409-form-container" class="comment-form-container">
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

<span id="11503"></span>

<div id="answer-container-11503" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11503-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11503-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11503-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What do you mean by "access"?</p>
<p>If you want only set the value of the "backgroundColor" properties, you can simply add it with the "autosize", ie:</p>
<pre><code>feature.popupClass = OpenLayers.Class(OpenLayers.Popup.Anchored, {
    &#39;autoSize&#39;: true,&#39;backgroundColor&#39;=&#39;#aaccee&#39;;
});</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '12, 13:22</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-11503" class="comments-container">
&#10;</div>
<div id="comment-tools-11503" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11503-form-container" class="comment-form-container">
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

