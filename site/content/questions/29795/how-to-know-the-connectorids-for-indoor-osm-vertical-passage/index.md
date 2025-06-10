+++
type = "question"
title = "How to know the connector:ids for indoor OSM (vertical passage)?"
description = '''Hi all, we currently are modelling an indoor osm map following the Indoor Schema. There is also a part in which vertical passages are described. It connects the doors of elevators, stairs and others with the doors above and below it. That means you have to know the doors&#x27; ids of both &quot;neighboring&quot; d...'''
date = "2014-01-13T12:07:00Z"
lastmod = "2014-01-13T12:13:00Z"
weight = 29795
keywords = [ "josm", "indoor", "osm" ]
aliases = [ "/questions/29795" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to know the connector:ids for indoor OSM (vertical passage)?](/questions/29795/how-to-know-the-connectorids-for-indoor-osm-vertical-passage)

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
<span id="post-29795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29795-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all, we currently are modelling an indoor osm map following the <a href="http://wiki.openstreetmap.org/wiki/IndoorOSM">Indoor Schema</a>. There is also a part in which <a href="http://wiki.openstreetmap.org/wiki/IndoorOSM#Modeling_connections_between_different_levels">vertical passages</a> are described. It connects the doors of elevators, stairs and others with the doors above and below it. That means you have to know the doors' ids of both "neighboring" doors. The connection is done by the tag connector:ids:</p>
<pre><code>      &lt;node id=&#39;-245&#39; action=&#39;modify&#39; visible=&#39;true&#39; lat=&#39;52.39349018473089&#39; lon=&#39;13.130163004646104&#39;&gt;
      &lt;tag k=&#39;connector:ids&#39; v=&#39;&lt;id_door_above&gt;, &lt;id_door_below&gt;&#39; /&gt;
      &lt;tag k=&#39;door&#39; v=&#39;yes&#39; /&gt;
   &lt;/node&gt;</code></pre>
<p>We model our buildings in JOSM. JOSM gives negative IDs to each new element and those IDs will be replaced by positive ones when the data gets uploads. The IDs in the tag (written by hand) won't be replaced which makes the file inconsistent. (Though I cannot verify at the moment because currently I'm not allowed to upload any indoor data for legal reasons).</p>
<p>A solution would be to upload the floors one after the other, but to me it doesn't seem to be a good solution.</p>
<p>Has anyone ever run into this problem? Have I missed to read the best practice?</p>
<p>Thank you for your time and any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-indoor" rel="tag" title="see questions tagged &#39;indoor&#39;">indoor</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jan '14, 12:07</strong></p>
<img src="https://secure.gravatar.com/avatar/34c0a69c5e95a6e56de49aa65cf845e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Henry%20Moews&#39;s gravatar image" />
<p><span>Henry Moews</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Henry Moews has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29795" class="comments-container">
&#10;</div>
<div id="comment-tools-29795" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29795-form-container" class="comment-form-container">
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

<span id="29796"></span>

<div id="answer-container-29796" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29796-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29796-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29796-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do not, under any circumstances, use the IDs of other objects in tag values. This is asking for trouble - IDs could change at any time, e.g. if someone were to delete and re-create an object.</p>
<p>Instead, use relations to model links between objects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jan '14, 12:13</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-29796" class="comments-container">
&#10;</div>
<div id="comment-tools-29796" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29796-form-container" class="comment-form-container">
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

