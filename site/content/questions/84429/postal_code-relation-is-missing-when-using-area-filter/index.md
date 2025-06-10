+++
type = "question"
title = "postal_code Relation is Missing When Using Area Filter"
description = '''Hi there, when running this overpass query, all postal_code relations in Germany are returned except for one (78266, relation id 3375856). [out:json]; area[admin_level=&quot;2&quot;][type=&quot;boundary&quot;][&quot;ISO3166-1&quot;=&quot;DE&quot;]-&amp;gt;.country; relation(area.country)[boundary=&quot;postal_code&quot;]; out tags;  Without the area fi...'''
date = "2022-05-10T15:44:00Z"
lastmod = "2022-05-10T19:15:00Z"
weight = 84429
keywords = [ "filter", "area", "postal_code", "relations", "missing" ]
aliases = [ "/questions/84429" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [postal_code Relation is Missing When Using Area Filter](/questions/84429/postal_code-relation-is-missing-when-using-area-filter)

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
<span id="post-84429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84429-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>when running this overpass query, all postal_code relations in Germany are returned except for one (78266, relation id 3375856).</p>
<pre><code>[out:json];
area[admin_level=&quot;2&quot;][type=&quot;boundary&quot;][&quot;ISO3166-1&quot;=&quot;DE&quot;]-&gt;.country;
relation(area.country)[boundary=&quot;postal_code&quot;];
out tags;</code></pre>
<p>Without the area filter, the relation is found and returned. However, I don't want to (and cannot) process all postal_code relations, I only want to get the german ones.</p>
<p>Is there something wrong with Overpass/OSM or am I doing something wrong?</p>
<p>Thanks in advance, Daniel</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-postal_code" rel="tag" title="see questions tagged &#39;postal_code&#39;">postal_code</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '22, 15:44</strong></p>
<img src="https://secure.gravatar.com/avatar/cd39a378f1b549f56889a7114a238e3f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="danielkbx&#39;s gravatar image" />
<p><span>danielkbx</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="danielkbx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84429" class="comments-container">
<span id="84432"></span>
<div id="comment-84432" class="comment">
<div id="post-84432-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <a href="https://www.openstreetmap.org/relation/3375856">offending postal_code</a> is of Büsingen am Hochrhein, a German exclave in Switzerland. The area is included in Germany's admin_level 2 relation.<br />
Maybe there is an issue with the postal code and the country boundary being exactly the same? Just guessing.</p>
</div>
<div id="comment-84432-info" class="comment-info">
<span class="comment-age">(10 May '22, 19:15)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-84429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84429-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

