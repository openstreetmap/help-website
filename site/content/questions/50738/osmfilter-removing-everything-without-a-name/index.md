+++
type = "question"
title = "OSMFilter removing everything without a name"
description = '''Hello, I want to filter anything from a OSM file without a name, as I noticed there is alot of unnamed data in the planet files and I don&#x27;t need them for my particular project. I thought I could achieve this with --keep=&quot;name=&quot; with osmfilter.exe unfortunately, when I imported the data into a DB I f...'''
date = "2016-07-08T22:00:00Z"
lastmod = "2019-11-01T16:36:00Z"
weight = 50738
keywords = [ "osmfilter", "osm2pgsql" ]
aliases = [ "/questions/50738" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSMFilter removing everything without a name](/questions/50738/osmfilter-removing-everything-without-a-name)

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
<span id="post-50738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50738-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I want to filter anything from a OSM file without a name, as I noticed there is alot of unnamed data in the planet files and I don't need them for my particular project. I thought I could achieve this with --keep="name=" with osmfilter.exe unfortunately, when I imported the data into a DB I found I still have data with no names. (using osm2pgsql) Am I doing this wrong or is there a better way to do this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jul '16, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/417fcaa49419f2ef008ab5ab60bd3981?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AwDogsGo2Heaven&#39;s gravatar image" />
<p><span>AwDogsGo2Heaven</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AwDogsGo2Heaven has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50738" class="comments-container">
<span id="71412"></span>
<div id="comment-71412" class="comment">
<div id="post-71412-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, have you managed to solve this, please?</p>
</div>
<div id="comment-71412-info" class="comment-info">
<span class="comment-age">(01 Nov '19, 15:58)</span> <span class="comment-user userinfo">fofo</span>
</div>
</div>
</div>
<div id="comment-tools-50738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50738-form-container" class="comment-form-container">
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

<span id="71414"></span>

<div id="answer-container-71414" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71414-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Without seeing the entire command being used, it's impossible to tell what's happening.</p>
<p>That being said, it may be doing exactly what you want. Keep in mind that even when you do this, you'll most likely still have some objects with no name because those objects are part of a higher-level object. For example, if you keep a highway with a name, the unnamed nodes that compose that way will also be present in the results. Likewise, if you keep a relation describing the boundary of a country, you'll also get the unnamed ways that create that boundary (as well as the unnamed nodes that compose each of those ways). Therefore, unless you're working solely with nodes, you're probably going to have lots of unnamed objects in your results.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Nov '19, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-71414" class="comments-container">
&#10;</div>
<div id="comment-tools-71414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71414-form-container" class="comment-form-container">
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

