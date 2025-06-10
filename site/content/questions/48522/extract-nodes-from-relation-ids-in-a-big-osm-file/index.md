+++
type = "question"
title = "extract nodes from relation ids in a big osm file"
description = '''Hello, I have a big osm file and I have the ids of 430 relations (in a text file) and I want to extract the data related to them from the osm file (I understand the hierarchy ( x relation -&amp;gt; x.y0, x.y1...x.yn ways -&amp;gt; x.y[0...n].z[0...t] nodes )) to make my osm file smaller. But I don&#x27;t know wh...'''
date = "2016-03-06T15:40:00Z"
lastmod = "2016-03-08T00:49:00Z"
weight = 48522
keywords = [ "api", "relations", "postgis" ]
aliases = [ "/questions/48522" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [extract nodes from relation ids in a big osm file](/questions/48522/extract-nodes-from-relation-ids-in-a-big-osm-file)

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
<span id="post-48522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48522-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have a big osm file and I have the ids of 430 relations (in a text file) and I want to extract the data related to them from the osm file (I understand the hierarchy ( x relation -&gt; x.y0, x.y1...x.yn ways -&gt; x.y[0...n].z[0...t] nodes )) to make my osm file smaller.</p>
<p>But I don't know where to begin ? I think that I need to import the osm file into postgis and then run queries ? I thought also to use the openstreetmap API and queries for each relations their ways and ... queries for each ways their nodes ... Then merge all of it. But it isn't very powerful...</p>
<p>Is there a better way to create my custom osm file ?</p>
<p>Thanks for your help, best regards,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '16, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/8fc3af157f477c7ccdd53d3d779369f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="syskaw&#39;s gravatar image" />
<p><span>syskaw</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="syskaw has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '16, 15:42</strong> </span></p>
</div>
</div>
<div id="comments-container-48522" class="comments-container">
&#10;</div>
<div id="comment-tools-48522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48522-form-container" class="comment-form-container">
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

<span id="48555"></span>

<div id="answer-container-48555" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48555-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="syskaw has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the <a href="https://github.com/osmcode/osmium-tool">osmium command line tool</a> for this. The "add-refs" subcommand does what you need. You'll have to use the master version from github, the released versions don't have this command yet. Use it like this:</p>
<pre><code>osmium add-refs -s large-osm-file.osm.pbf -i relation-ids -o extract.osm.pbf</code></pre>
<p>with relation-ids file containing one relation id per line preceded by the letter 'r'.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '16, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-48555" class="comments-container">
<span id="48556"></span>
<div id="comment-48556" class="comment">
<div id="post-48556-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it works like a charm, thanks you :)</p>
</div>
<div id="comment-48556-info" class="comment-info">
<span class="comment-age">(08 Mar '16, 00:49)</span> <span class="comment-user userinfo">syskaw</span>
</div>
</div>
</div>
<div id="comment-tools-48555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48555-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48523"></span>

<div id="answer-container-48523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48523-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should not use the OpenStreetMap api to fetch the relations.</p>
<p>It may work to fetch them from Overpass API. It's possible to query by object id, so you could use something like</p>
<pre><code>(
rel(firstid);
rel(secondid);
);
(._;&gt;;);
out meta;</code></pre>
<p>(look at <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">the Overpass QL documentation</a> for more information, especially the sections on "Union" and "By Element Id")</p>
<p>I'm not sure that it would be acceptable to query so many relations, if they are large, the query would have a large result.</p>
<p>Another approach that doesn't need a database is to use whatever programming tools you are familiar with to read through the large file 3 times. The first time, when you encounter a desired relation, extract it and also make a list of the ways that are members of the relation. The second time, extract the list of ways and make a list of the nodes that are members. The third time, extract the list of nodes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '16, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-48523" class="comments-container">
&#10;</div>
<div id="comment-tools-48523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48523-form-container" class="comment-form-container">
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

