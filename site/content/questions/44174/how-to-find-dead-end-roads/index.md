+++
type = "question"
title = "How to find dead end roads"
description = '''I am developing a sampling technique to do quality assurance checks. One of the things I need for the technique is to find the amount of dead end roads in a certain area. How can this be achieved? I have looked at using JOSM and Overpass-Turbo but I haven&#x27;t been successful so far.  Any help would be...'''
date = "2015-07-14T10:45:00Z"
lastmod = "2015-07-23T10:21:00Z"
weight = 44174
keywords = [ "quality_assurance", "validation", "quality", "josm" ]
aliases = [ "/questions/44174" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to find dead end roads](/questions/44174/how-to-find-dead-end-roads)

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
<span id="post-44174-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44174-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-44174-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am developing a sampling technique to do quality assurance checks. One of the things I need for the technique is to find the amount of dead end roads in a certain area. How can this be achieved? I have looked at using JOSM and Overpass-Turbo but I haven't been successful so far. Any help would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-quality_assurance" rel="tag" title="see questions tagged &#39;quality_assurance&#39;">quality_assurance</span> <span class="post-tag tag-link-validation" rel="tag" title="see questions tagged &#39;validation&#39;">validation</span> <span class="post-tag tag-link-quality" rel="tag" title="see questions tagged &#39;quality&#39;">quality</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Jul '15, 10:45</strong></p>
<img src="https://secure.gravatar.com/avatar/19fd6c1499513907697c5821829c5e83?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BmanS&#39;s gravatar image" />
<p><span>BmanS</span><br />
<span class="score" title="56 reputation points">56</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BmanS has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44174" class="comments-container">
&#10;</div>
<div id="comment-tools-44174" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44174-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="44179"></span>

<div id="answer-container-44179" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44179-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could load the road network data into QGIS and then <a href="http://dominoc925.blogspot.be/2013/11/find-dangles-using-qgis.html">find dangles</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '15, 15:18</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-44179" class="comments-container">
<span id="44184"></span>
<div id="comment-44184" class="comment">
<div id="post-44184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would also be possible, in QGIS, to find roads that intersect but have no node meaning there is no junction between the roads? and to find all the unnamed roads?</p>
</div>
<div id="comment-44184-info" class="comment-info">
<span class="comment-age">(14 Jul '15, 20:53)</span> <span class="comment-user userinfo">BmanS</span>
</div>
</div>
<span id="44191"></span>
<div id="comment-44191" class="comment">
<div id="post-44191-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unnamed roads would be straightforward: you could open the attribute table and select roads with an empty name column. Or you can do the same with a simple query. It would require converting your osm data to a format with a limited number of attributes (like for example a shapefile). I'm not sure on the details of finding the missing nodes, but it will probably not be that hard with the "intersect" tool. If you get that far, ask at e.g. gis.stackexchange.com</p>
</div>
<div id="comment-44191-info" class="comment-info">
<span class="comment-age">(15 Jul '15, 07:13)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-44179" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44179-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44390"></span>

<div id="answer-container-44390" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44390-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>When you load data into GraphHopper you can use the following Java snippet to calculate all coordinates of dead ends in the whole area and do further analysis:</p>
<pre><code>    CmdArgs args = CmdArgs.read(strs);
    GraphHopper hopper = new GraphHopper().init(args);
    hopper.importOrLoad();
    Graph graph = hopper.getGraph();
    NodeAccess nodeAccess = graph.getNodeAccess();
    AllEdgesIterator iter = graph.getAllEdges();
    EdgeExplorer explorer = graph.createEdgeExplorer();
    List&lt;GHPoint&gt; deadEndPoints = new ArrayList&lt;&gt;();
    while (iter.next())
    {
        int node = iter.getAdjNode();
&#10;        // an edge is a connection from junction to junction
        // so if you count all edges from a certain junction
        // and it is exactly 1 you have found a dead end
        if (GHUtility.count(explorer.setBaseNode(node)) == 1)
        {
            deadEndPoints.add(new GHPoint(nodeAccess.getLat(node), nodeAccess.getLon(node)));
        }
        node = iter.getBaseNode();
        if (GHUtility.count(explorer.setBaseNode(node)) == 1)
        {
            deadEndPoints.add(new GHPoint(nodeAccess.getLat(node), nodeAccess.getLon(node)));
        }
    }
    System.out.println(deadEndPoints);
    hopper.close();</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '15, 10:21</strong></p>
<img src="https://secure.gravatar.com/avatar/fec61c70a4cc98b1e84a5dfbde1e9a6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peatar&#39;s gravatar image" />
<p><span>peatar</span><br />
<span class="score" title="351 reputation points">351</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peatar has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-44390" class="comments-container">
&#10;</div>
<div id="comment-tools-44390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44390-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="44175"></span>

<div id="answer-container-44175" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44175-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.44#PostGIS_Tasks_.28Snapshot_Schema.29">pgsnapshot schema from osmosis</a> should be able to help here. You get a SQL version of the OSM data model, and can write SQL queries to find nodes that are only at the start or end of an OSM way with the tags that you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '15, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-44175" class="comments-container">
&#10;</div>
<div id="comment-tools-44175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44175-form-container" class="comment-form-container">
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

