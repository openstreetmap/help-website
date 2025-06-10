+++
type = "question"
title = "OSM in a Java Web Application ?"
description = '''I&#x27;d like to use OSM in a webapp (java) to  a) let the user draw a network topology on a map and record it b) show the topology when requested by the user (i.e. use the recorded coordinates) Here is an example with GoogleMaps: http://docs.zkoss.org/wiki/Construct_A_Telecom_Network_Graph_On_Google_Map...'''
date = "2010-09-21T09:20:00Z"
lastmod = "2010-09-21T11:15:00Z"
weight = 875
keywords = [ "development", "jsp", "zk", "java", "web" ]
aliases = [ "/questions/875" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM in a Java Web Application ?](/questions/875/osm-in-a-java-web-application)

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
<span id="post-875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-875-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'd like to use OSM in a webapp (java) to a) let the user draw a network topology on a map and record it b) show the topology when requested by the user (i.e. use the recorded coordinates)</p>
<p>Here is an example with GoogleMaps: <a href="http://docs.zkoss.org/wiki/Construct_A_Telecom_Network_Graph_On_Google_Maps">http://docs.zkoss.org/wiki/Construct_A_Telecom_Network_Graph_On_Google_Maps</a></p>
<p>I'd like to understand what is possible with current API's, and I can contribute to OSM by developing a ZK-component that uses OSM in stead of gM</p>
<p>Thanks for any useful hints and pointers!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-jsp" rel="tag" title="see questions tagged &#39;jsp&#39;">jsp</span> <span class="post-tag tag-link-zk" rel="tag" title="see questions tagged &#39;zk&#39;">zk</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-web" rel="tag" title="see questions tagged &#39;web&#39;">web</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '10, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/9eae6ad83f966bbaf40705eba6d33cfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mhogendoorn&#39;s gravatar image" />
<p><span>mhogendoorn</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mhogendoorn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-875" class="comments-container">
&#10;</div>
<div id="comment-tools-875" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-875-form-container" class="comment-form-container">
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

<span id="877"></span>

<div id="answer-container-877" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-877-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Generally, such questions should better be asked on the <a href="http://lists.openstreetmap.org/listinfo/dev">OSM developer mailing list</a> where they will reach a wider technical audience.</p>
<p>It seems to me that the quick answer to your question is that you'll need OSM tiles (freely available), the OpenLayers JavaScript library (to display tiles and allow the user to draw stuff - requires some Javascript coding on your part to make things happen) plus some server-side component that stores whatever you have drawn (e.g. FeatureServer). Or you might be able to use a complete framework like MapFish. I don't know what "zk" is or in how far this might already have some of the components you need. All of this has, however, little to do with OSM as the only thing you'll use from OSM are the map tiles; all the other "API" stuff you'll be using is not OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '10, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-877" class="comments-container">
&#10;</div>
<div id="comment-tools-877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-877-form-container" class="comment-form-container">
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

