+++
type = "question"
title = "Street names not exporting in XML"
description = '''I&#x27;m trying to export streets in Saint-Marc, Haiti so I can use them in ArcGIS for a map. I did the XML output and it only seems to export some street names, the rest are blank. However, they all seem to be named on the OSM website. Why is that? Is there something else I can do to get the exports wit...'''
date = "2012-07-09T20:04:00Z"
lastmod = "2012-07-10T16:21:00Z"
weight = 14118
keywords = [ "xml", "attributes", "export", "names", "streetnames" ]
aliases = [ "/questions/14118" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Street names not exporting in XML](/questions/14118/street-names-not-exporting-in-xml)

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
<span id="post-14118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14118-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to export streets in Saint-Marc, Haiti so I can use them in ArcGIS for a map. I did the XML output and it only seems to export some street names, the rest are blank. However, they all seem to be named on the OSM website. Why is that? Is there something else I can do to get the exports with all the attributes? Geofabrik.de and Cloudmade don't include street names either.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '12, 20:04</strong></p>
<img src="https://secure.gravatar.com/avatar/8776e49a74c21df94b072174455fa3ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marion%20Barry&#39;s gravatar image" />
<p><span>Marion Barry</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marion Barry has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14118" class="comments-container">
<span id="14119"></span>
<div id="comment-14119" class="comment">
<div id="post-14119-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please name one concrete OSM object that does not have a name in your export but has one on the OSM map, then we can investigate.</p>
</div>
<div id="comment-14119-info" class="comment-info">
<span class="comment-age">(09 Jul '12, 20:18)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14121"></span>
<div id="comment-14121" class="comment">
<div id="post-14121-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>La Scierie Prolonngée for example. Also it seems that Rue Pierre Toussaint (on the OSM site) is exporting as "La Scirie Bonet Prolongee" in XML. I should be using Highway or highway-ln, right?</p>
</div>
<div id="comment-14121-info" class="comment-info">
<span class="comment-age">(09 Jul '12, 20:36)</span> <span class="comment-user userinfo">Marion Barry</span>
</div>
</div>
<span id="14122"></span>
<div id="comment-14122" class="comment">
<div id="post-14122-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know what you mean by "using Highway or highway-ln", these are not keys that appear in the XML. The road you mention is not called "La Scierie Prolonngée" like you say, but it appears once as "La Scierie Prolongee" (capital s, normal double e) and once as "La scierie Prolongée" (small s, accent). Both of these roads are present in the OSM export as well as in the Geofabrik extract. Is it possible that you postprocess the XML in a program that only shows you part of what's there?</p>
</div>
<div id="comment-14122-info" class="comment-info">
<span class="comment-age">(09 Jul '12, 20:39)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14123"></span>
<div id="comment-14123" class="comment">
<div id="post-14123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Part of the road seems to be present, but not the whole thing when I bring it in. I am taking the XML to ArcGIS via their Data Interoperability extension -- when you do that it has feature classes for highway and highway-ln. Is there a better way to bring the data into ArcGIS then?</p>
</div>
<div id="comment-14123-info" class="comment-info">
<span class="comment-age">(09 Jul '12, 20:46)</span> <span class="comment-user userinfo">Marion Barry</span>
</div>
</div>
<span id="14138"></span>
<div id="comment-14138" class="comment">
<div id="post-14138-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>On your earlier parts, I downloaded the most recent Geofabrik file and it did have a lot more street names. The one I had before was from a month ago, I guess they made a lot of changes in that time.</p>
</div>
<div id="comment-14138-info" class="comment-info">
<span class="comment-age">(10 Jul '12, 16:21)</span> <span class="comment-user userinfo">Marion Barry</span>
</div>
</div>
</div>
<div id="comment-tools-14118" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14118-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

