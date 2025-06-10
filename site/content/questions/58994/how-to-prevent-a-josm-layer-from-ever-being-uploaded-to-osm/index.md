+++
type = "question"
title = "How to prevent a JOSM layer from ever being uploaded to OSM?"
description = '''When I open a SHP file using the opendata plug-in I want make sure the layer never gets uploaded to OSM.  Right-Clicking on the &quot;layer&quot; gives me a &quot;Discourage upload&quot; option but it seems to have no effect, or I don&#x27;t know how to use it.  I&#x27;d like to have a &quot;Never Upload&quot; option.'''
date = "2017-09-05T22:24:00Z"
lastmod = "2017-09-06T00:23:00Z"
weight = 58994
keywords = [ "layers", "josm", "options", "opendata" ]
aliases = [ "/questions/58994" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to prevent a JOSM layer from ever being uploaded to OSM?](/questions/58994/how-to-prevent-a-josm-layer-from-ever-being-uploaded-to-osm)

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
<span id="post-58994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58994-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I open a SHP file using the opendata plug-in I want make sure the layer never gets uploaded to OSM.</p>
<p>Right-Clicking on the "layer" gives me a "Discourage upload" option but it seems to have no effect, or I don't know how to use it.</p>
<p>I'd like to have a "Never Upload" option.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-options" rel="tag" title="see questions tagged &#39;options&#39;">options</span> <span class="post-tag tag-link-opendata" rel="tag" title="see questions tagged &#39;opendata&#39;">opendata</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Sep '17, 22:24</strong></p>
<img src="https://secure.gravatar.com/avatar/75cc9956f060892f585352e9011cd26e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alan01730&#39;s gravatar image" />
<p><span>Alan01730</span><br />
<span class="score" title="464 reputation points">464</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alan01730 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58994" class="comments-container">
&#10;</div>
<div id="comment-tools-58994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58994-form-container" class="comment-form-container">
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

<span id="58995"></span>

<div id="answer-container-58995" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58995-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58995-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58995-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you save the layer as a OSM file, you can change the &lt;osm&gt; tag to be something like:</p>
<pre><code>&lt;osm version=&#39;0.6&#39; upload=&#39;false&#39; generator=&#39;JOSM&#39;&gt;</code></pre>
<p>That will keep JOSM from nagging you about uploading it. But I am not sure it will prevent you from uploading it (I never wanted to try it in case it let me).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Sep '17, 23:38</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-58995" class="comments-container">
<span id="58997"></span>
<div id="comment-58997" class="comment">
<div id="post-58997-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Recent versions of JOSM also interpret <code>upload='never'</code>, which goes a step further, disabling the upload options for the layer.</p>
<p>The "Discourage Upload" feature mentioned in the question actually just sets the <code>upload='false'</code> flag. The opendata plugin defaults to discourage upload, I don't think there is any way to set a layer to <code>never</code> in JOSM.</p>
</div>
<div id="comment-58997-info" class="comment-info">
<span class="comment-age">(06 Sep '17, 00:23)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-58995" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58995-form-container" class="comment-form-container">
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

