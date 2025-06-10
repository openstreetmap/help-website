+++
type = "question"
title = "How to Get User Contribution Stats By Area"
description = '''I&#x27;m interested of getting user contribution statistics for a particular region. For example, like it is done on http://osm.svimik.com/. I looked through related questions, but all seems to be about contributions for particular user. It looks like that using newer keyword for Overpass API should almo...'''
date = "2017-10-25T21:19:00Z"
lastmod = "2017-10-26T16:41:00Z"
weight = 60301
keywords = [ "overpassapi", "overpass", "contribution", "statistics", "overpass-turbo" ]
aliases = [ "/questions/60301" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to Get User Contribution Stats By Area](/questions/60301/how-to-get-user-contribution-stats-by-area)

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
<span id="post-60301-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60301-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60301-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm interested of getting user contribution statistics for a particular region. For example, like it is done on <a href="http://osm.svimik.com/">http://osm.svimik.com/</a>.</p>
<p>I looked through related questions, but all seems to be about contributions for particular user.</p>
<p>It looks like that using <code>newer</code> keyword for Overpass API should almost do the trick:</p>
<pre><code>node
  (newer:&quot;2017-10-24T07:00:00Z&quot;)     // adjust date as needed
  ({{bbox}})-&gt;.newnodes;
&#10;// Output
.newnodes out meta;</code></pre>
<p>But how to tell the API to look for changes only for particular country? It is connected with <code>area</code> keyword, but it's not clear how to use it (the Overpass API is tricky). Also it is not clear, how to detect what was really done in resulting data:</p>
<pre><code> &lt;node id=&quot;33191091&quot; lat=&quot;54.6025991&quot; lon=&quot;25.3133923&quot; version=&quot;8&quot; timestamp=&quot;2017-10-25T10:45:54Z&quot; changeset=&quot;53232321&quot; uid=&quot;60129&quot; user=&quot;...&quot;/&gt;
  &lt;node id=&quot;34224031&quot; lat=&quot;54.6878381&quot; lon=&quot;25.4908757&quot; version=&quot;5&quot; timestamp=&quot;2017-10-25T17:00:45Z&quot; changeset=&quot;53240840&quot; uid=&quot;60129&quot; user=&quot;...&quot;/&gt;</code></pre>
<p>It's only a list of nodes (and tags sometimes) and it's not clear if those nodes (tags, etc.) were just created, or edited, or moved.</p>
<p>On the whole, does anybody have a good example for something similar or a good explanation of how to use such queries. Also these queries are performance-consuming for the server, so probably I need to manage to run them locally somehow.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-contribution" rel="tag" title="see questions tagged &#39;contribution&#39;">contribution</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '17, 21:19</strong></p>
<img src="https://secure.gravatar.com/avatar/7beec6d85fed7bf5255d6657d7609ad0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sergey%20Karavay&#39;s gravatar image" />
<p><span>Sergey Karavay</span><br />
<span class="score" title="539 reputation points">539</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sergey Karavay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60301" class="comments-container">
&#10;</div>
<div id="comment-tools-60301" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60301-form-container" class="comment-form-container">
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

<span id="60302"></span>

<div id="answer-container-60302" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60302-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60302-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60302-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An example of how to search in a given country: <a href="http://overpass-turbo.eu/s/sBo">http://overpass-turbo.eu/s/sBo</a></p>
<p>To discover what was changed, you'll probably want to use <a href="https://wiki.openstreetmap.org/wiki/Achavi">Achavi</a> or similar on individual changesets (for geometries at least).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '17, 00:52</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Oct '17, 01:00</strong> </span></p>
</div>
</div>
<div id="comments-container-60302" class="comments-container">
<span id="60316"></span>
<div id="comment-60316" class="comment">
<div id="post-60316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! Seems to be a good direction to start.</p>
</div>
<div id="comment-60316-info" class="comment-info">
<span class="comment-age">(26 Oct '17, 16:41)</span> <span class="comment-user userinfo">Sergey Karavay</span>
</div>
</div>
</div>
<div id="comment-tools-60302" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60302-form-container" class="comment-form-container">
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

