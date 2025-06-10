+++
type = "question"
title = "OsmSharp filtering and completion is slow"
description = '''I&#x27;m not sure I&#x27;m doing this correctly. I&#x27;m trying to get hold of the coastline of a specific little island using OsmSharp and an osm-map of Singapore (xml format).   XmlOsmStreamSource source = new XmlOsmStreamSource(fileStream);   var islandsIncomplete = from osmGeo in source where (osmGeo.Type == ...'''
date = "2020-11-12T12:31:00Z"
lastmod = "2020-11-13T15:24:00Z"
weight = 77523
keywords = [ "filter", "osmsharp" ]
aliases = [ "/questions/77523" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OsmSharp filtering and completion is slow](/questions/77523/osmsharp-filtering-and-completion-is-slow)

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
<span id="post-77523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77523-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm not sure I'm doing this correctly. I'm trying to get hold of the coastline of a specific little island using OsmSharp and an osm-map of Singapore (xml format).</p>
<pre><code>    XmlOsmStreamSource source = new XmlOsmStreamSource(fileStream);
&#10;    var islandsIncomplete = from osmGeo in source where (osmGeo.Type == OsmSharp.OsmGeoType.Relation &amp;&amp; osmGeo.Tags.Contains(&quot;name&quot;, &quot;Pulau Ubin&quot;))
    || (osmGeo.Type == OsmSharp.OsmGeoType.Way &amp;&amp; osmGeo.Tags.Contains(&quot;natural&quot;, &quot;coastline&quot;))
    || (osmGeo.Type == OsmSharp.OsmGeoType.Node)
    select osmGeo;
&#10;    var completes = incompletes.ToComplete();
&#10;    var relations = from osmGeo in completes where osmGeo.Type == OsmSharp.OsmGeoType.Relation select osmGeo;
    return relations.Cast&lt;CompleteRelation&gt;().ToArray();</code></pre>
<p>So I looked into the xml file for these specific keys and values and I think I'm only extracting the necessary objects for completion. Yet, the process takes a really long time to complete. What is it doing that is taking so long? The above example seems to never complete, but even in other examples I try to extract a small amout of specific ways from the file, and it takes many minutes. Maybe there is something I don't understand here. Maybe I should better parse the xml file myself?</p>
<p>Is there any OsmSharp forum?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-osmsharp" rel="tag" title="see questions tagged &#39;osmsharp&#39;">osmsharp</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '20, 12:31</strong></p>
<img src="https://secure.gravatar.com/avatar/2035de0eeacdd19ada2b72c977206ac4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="laban77&#39;s gravatar image" />
<p><span>laban77</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="laban77 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77523" class="comments-container">
&#10;</div>
<div id="comment-tools-77523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77523-form-container" class="comment-form-container">
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

<span id="77535"></span>

<div id="answer-container-77535" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77535-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Also, try opening an issue on the OSMSharp Github at <a href="https://github.com/OsmSharp/core">https://github.com/OsmSharp/core</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '20, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-77535" class="comments-container">
<span id="77537"></span>
<div id="comment-77537" class="comment">
<div id="post-77537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would if I thought that there were something wrong. I have a feeling though that I have just misunderstood the whole thing. It's not stated anywhere that the processing should take such a long time. By the way I found out why the example above never finishes. I had forgotten to check that osmGeo.Tags is not null before checking what it contains. The error is probably swallowed later by the Cast command.</p>
<p>The problem is really a lack of documentation. The best I have found so far is to look through the examples in the source code itself.</p>
</div>
<div id="comment-77537-info" class="comment-info">
<span class="comment-age">(13 Nov '20, 15:24)</span> <span class="comment-user userinfo">laban77</span>
</div>
</div>
</div>
<div id="comment-tools-77535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77535-form-container" class="comment-form-container">
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

