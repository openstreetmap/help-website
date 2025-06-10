+++
type = "question"
title = "How to get the hierarchical tree structure for a city, prefereably using OSM on AWS Athena?"
description = '''For a particular city, is it possible to get a tree structure? Eg:  New York City  | --------------------------------------------------------------- | | | |  Manhattan...........Brooklyn................Bronx .............Queens |  NoHo |  Washington Square Park'''
date = "2019-06-20T09:59:00Z"
lastmod = "2019-06-23T07:00:00Z"
weight = 69678
keywords = [ "parent", "polygons", "trees" ]
aliases = [ "/questions/69678" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the hierarchical tree structure for a city, prefereably using OSM on AWS Athena?](/questions/69678/how-to-get-the-hierarchical-tree-structure-for-a-city-prefereably-using-osm-on-aws-athena)

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
<span id="post-69678-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69678-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69678-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For a particular city, is it possible to get a tree structure?</p>
<p>Eg:</p>
<pre><code>                New York City
                     |
---------------------------------------------------------------
|                    |                     |                   |</code></pre>
<p>Manhattan...........Brooklyn................Bronx .............Queens</p>
<pre><code>|</code></pre>
<p>NoHo</p>
<pre><code>|</code></pre>
<p>Washington Square Park</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-parent" rel="tag" title="see questions tagged &#39;parent&#39;">parent</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span> <span class="post-tag tag-link-trees" rel="tag" title="see questions tagged &#39;trees&#39;">trees</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jun '19, 09:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ba4d08ac7a54dfbc248117485ba1c23f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chiiz&#39;s gravatar image" />
<p><span>chiiz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chiiz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69678" class="comments-container">
<span id="69685"></span>
<div id="comment-69685" class="comment">
<div id="post-69685-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>OSM doesn't have a clean hierarchy of settlements (largely because the real world doesn't). I'd suggest you spend some time exploring what OSM data there is in the area you're interested in, and how each object is tagged.</p>
</div>
<div id="comment-69685-info" class="comment-info">
<span class="comment-age">(20 Jun '19, 14:09)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="69707"></span>
<div id="comment-69707" class="comment">
<div id="post-69707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Richard, Thank you for your comment. How do I start with something simple. For example get a list of coordinates for all the city districts in say, Jeddah, Saudi Arabia.</p>
</div>
<div id="comment-69707-info" class="comment-info">
<span class="comment-age">(23 Jun '19, 07:00)</span> <span class="comment-user userinfo">chiiz</span>
</div>
</div>
</div>
<div id="comment-tools-69678" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69678-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

