+++
type = "question"
title = "Create Network Dataset with OSM data"
description = '''I am trying to use OSM data to create a network dataset in ArcGIS. I am able to load the file as a feature class in ArcGIS using the Load OSM File tool, but when I try to use the Create Network Dataset Tool I keep getting an error (shown below). Do I need to edit the data itself? If so how do I go a...'''
date = "2018-12-12T18:29:00Z"
lastmod = "2018-12-13T00:28:00Z"
weight = 67149
keywords = [ "tools", "networkanalysis", "arcmap" ]
aliases = [ "/questions/67149" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Create Network Dataset with OSM data](/questions/67149/create-network-dataset-with-osm-data)

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
<span id="post-67149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67149-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to use OSM data to create a network dataset in ArcGIS. I am able to load the file as a feature class in ArcGIS using the Load OSM File tool, but when I try to use the Create Network Dataset Tool I keep getting an error (shown below). Do I need to edit the data itself? If so how do I go about doing this for an OSM file?</p>
<p>Thanks for the ideas or help!</p>
<pre><code>Populating Turn Features from OSM Relations
The row contains a bad value. [RestrictionType]
   at ESRI.ArcGIS.Geodatabase.IFeature.Store()
   at ESRI.ArcGIS.OSM.GeoProcessing.NetworkTurns.CreateTurnFeature_NO(TurnFeatureClassWrapper turnFCW, OSMTurnInfo osmTurn)
   at ESRI.ArcGIS.OSM.GeoProcessing.NetworkTurns.PopulateTurnsFromRelations()
   at ESRI.ArcGIS.OSM.GeoProcessing.RunTaskManager.ExecuteTask(String messageName, Action task)
   at ESRI.ArcGIS.OSM.GeoProcessing.NetworkTurns.ExtractTurnRestrictions()
   at ESRI.ArcGIS.OSM.GeoProcessing.NetworkDataset.ExtractTurnRestrictions()
   at ESRI.ArcGIS.OSM.GeoProcessing.RunTaskManager.ExecuteTask(String messageName, Action task)
   at ESRI.ArcGIS.OSM.GeoProcessing.NetworkDataset.CreateNetworkDataset()
   at ESRI.ArcGIS.OSM.GeoProcessing.OSMGPCreateNetworkDataset.Execute(IArray paramvalues, ITrackCancel TrackCancel, IGPEnvironmentManager envMgr, IGPMessages message)
Failed to execute (OSMGPCreateNetworkDataset).
Failed at Mon Dec 10 22:24:01 2018 (Elapsed Time: 23 minutes 42 seconds)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tools" rel="tag" title="see questions tagged &#39;tools&#39;">tools</span> <span class="post-tag tag-link-networkanalysis" rel="tag" title="see questions tagged &#39;networkanalysis&#39;">networkanalysis</span> <span class="post-tag tag-link-arcmap" rel="tag" title="see questions tagged &#39;arcmap&#39;">arcmap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Dec '18, 18:29</strong></p>
<img src="https://secure.gravatar.com/avatar/af45d14681e42f217775b7fba91b0264?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="girlfromdc&#39;s gravatar image" />
<p><span>girlfromdc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="girlfromdc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67149" class="comments-container">
<span id="67151"></span>
<div id="comment-67151" class="comment">
<div id="post-67151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What object is it getting stuck on? It looks like it's a turn restriction relation, but it would be helpful to see exactly how it's tagged in the OSM database.</p>
</div>
<div id="comment-67151-info" class="comment-info">
<span class="comment-age">(12 Dec '18, 22:52)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="67152"></span>
<div id="comment-67152" class="comment">
<div id="post-67152-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for responding. I don't know which object it is getting stuck on. Is there a way I could figure this out? There are about 32k entries in the attribute table so I can't look through it too much...</p>
</div>
<div id="comment-67152-info" class="comment-info">
<span class="comment-age">(13 Dec '18, 00:28)</span> <span class="comment-user userinfo">girlfromdc</span>
</div>
</div>
</div>
<div id="comment-tools-67149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67149-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

