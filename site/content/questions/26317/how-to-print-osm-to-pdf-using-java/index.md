+++
type = "question"
title = "How to print OSM to pdf using java"
description = '''I&#x27;m new to OSM can anyone tell me how can i print a OSM to pdf file, i have found a printservlet.war file in the mapfish website i have downloaded it and placed it in my tomcat folder and run the server, when i make a request to print org.mapfish.print.InvalidJsonValueException: spec.layers[0].type ...'''
date = "2013-09-13T07:34:00Z"
lastmod = "2013-09-16T16:48:00Z"
weight = 26317
keywords = [ "openstreetmap", "java", "openlayers" ]
aliases = [ "/questions/26317" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to print OSM to pdf using java](/questions/26317/how-to-print-osm-to-pdf-using-java)

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
<span id="post-26317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26317-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM can anyone tell me how can i print a OSM to pdf file, i have found a printservlet.war file in the mapfish website i have downloaded it and placed it in my tomcat folder and run the server, when i make a request to print</p>
<pre><code>org.mapfish.print.InvalidJsonValueException: spec.layers[0].type has an invalid value: OSM</code></pre>
<p>Then i get the above exception, is it a correct way or anyone please point me in the right direction.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '13, 07:34</strong></p>
<img src="https://secure.gravatar.com/avatar/60e21c77c89cb038a0ae6b15e49047cd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lokesh39&#39;s gravatar image" />
<p><span>Lokesh39</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lokesh39 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '13, 11:45</strong> </span></p>
</div>
</div>
<div id="comments-container-26317" class="comments-container">
&#10;</div>
<div id="comment-tools-26317" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26317-form-container" class="comment-form-container">
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

<span id="26320"></span>

<div id="answer-container-26320" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26320-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a quick investigation, it seems that mapfish supports osm tiles:</p>
<p><a href="http://www.mapfish.org/doc/print/protocol.html#layers-params">http://www.mapfish.org/doc/print/protocol.html#layers-params</a></p>
<p>Your may have a version problem (older library) or a case sensitivity problem ('OSM' and not 'osm') ?</p>
<p>Also be careful that OSM has limited resources and a tile usage policy:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">https://wiki.openstreetmap.org/wiki/Tile_usage_policy</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '13, 09:35</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-26320" class="comments-container">
<span id="26335"></span>
<div id="comment-26335" class="comment">
<div id="post-26335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Pieren</span> thanks for the reply, i have gone through layers-params but that didn't help....is there any other way excluding mapfish to print OSM using java from my tomcat server</p>
</div>
<div id="comment-26335-info" class="comment-info">
<span class="comment-age">(14 Sep '13, 07:33)</span> <span class="comment-user userinfo">Lokesh39</span>
</div>
</div>
<span id="26397"></span>
<div id="comment-26397" class="comment">
<div id="post-26397-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>maybe a solution or a helpful link is hidden at <a href="https://wiki.openstreetmap.org/wiki/Frameworks">https://wiki.openstreetmap.org/wiki/Frameworks</a> ?</p>
</div>
<div id="comment-26397-info" class="comment-info">
<span class="comment-age">(16 Sep '13, 16:48)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-26320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26320-form-container" class="comment-form-container">
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

