+++
type = "question"
title = "Overpass: Store bounding box in variable"
description = '''Is it possible to declare the variable area and store a bounding box in it? The following works fine: id-query {{nominatimArea:Netherlands}} into=&quot;area&quot; and then i can ask for it with: area-query from=&quot;area&quot; However bbox-query s=&quot;51.92&quot; w=&quot;4.79&quot; n=&quot;52.31&quot; e=&quot;5.64&quot; into=&quot;area&quot; and then ask for it wit...'''
date = "2016-01-28T00:30:00Z"
lastmod = "2016-02-02T23:55:00Z"
weight = 47684
keywords = [ "overpass" ]
aliases = [ "/questions/47684" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: Store bounding box in variable](/questions/47684/overpass-store-bounding-box-in-variable)

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
<span id="post-47684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47684-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to declare the variable <em>area</em> and store a bounding box in it?</p>
<p>The following works fine: <em>id-query {{nominatimArea:Netherlands}} into="area"</em></p>
<p>and then i can ask for it with: <em>area-query from="area"</em></p>
<p>However <em>bbox-query s="51.92" w="4.79" n="52.31" e="5.64" into="area"</em></p>
<p>and then ask for it with: <em>area-query from="area"</em> gives an empty result.</p>
<p>Is it possible store a bounding box in a variable? And if so, what's the correct code for it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '16, 00:30</strong></p>
<img src="https://secure.gravatar.com/avatar/b7a71ee7c9bc8c574ea76486008dea16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steijn&#39;s gravatar image" />
<p><span>Steijn</span><br />
<span class="score" title="61 reputation points">61</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steijn has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47684" class="comments-container">
&#10;</div>
<div id="comment-tools-47684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47684-form-container" class="comment-form-container">
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

<span id="47705"></span>

<div id="answer-container-47705" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47705-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Steijn has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It is possible in Overpass Turbo, using the custom shortcut syntax:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo/Extended_Overpass_Queries#Custom_Shortcuts">http://wiki.openstreetmap.org/wiki/Overpass_turbo/Extended_Overpass_Queries#Custom_Shortcuts</a></p>
<p>But this feature is coming from Overpass Turbo and won't work on queries sent directly to Overpass API, only on queries made using the Turbo interface.</p>
<p>Depending on what you are retrieving, it may also work to set the bounding box on the osm-script element.</p>
<p>Something like (untested): <code>&lt;osm-script bbox="1,2,3,4" output="json"&gt;</code>, it will then apply to all queries in the script.</p>
<p>Another solution would be to use a script written in another language (like Python or Ruby or ...) to generate your Overpass script from a template.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '16, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '16, 13:39</strong> </span></p>
</div>
</div>
<div id="comments-container-47705" class="comments-container">
<span id="47837"></span>
<div id="comment-47837" class="comment">
<div id="post-47837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>thank you for your response. :)</p>
<p>I decided to keep it simple and repeat the bounding box in each query. But thanks anyway as I now realise there is a difference between Overpass Turbo and Overpass API.</p>
</div>
<div id="comment-47837-info" class="comment-info">
<span class="comment-age">(02 Feb '16, 23:55)</span> <span class="comment-user userinfo">Steijn</span>
</div>
</div>
</div>
<div id="comment-tools-47705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47705-form-container" class="comment-form-container">
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

