+++
type = "question"
title = "Why does rows=&quot;...&quot; in JOSM Preset not work?"
description = '''I created a Preset for JOSM (version 7777) that includes the following lines: A. &amp;lt;text key=&quot;description&quot; text=&quot;Description&quot; default=&quot;&quot; delete_if_empty=&quot;true&quot; rows=&quot;3&quot;/&amp;gt; B. &amp;lt;multiselect key=&quot;amenity&quot; delimiter=&quot;,&quot; text=&quot;Amenity&quot; values=&quot;restaurant,bar&quot; default=&quot;&quot; delete_if_empty=&quot;true&quot; rows=...'''
date = "2014-12-27T16:55:00Z"
lastmod = "2015-02-12T23:33:00Z"
weight = 39854
keywords = [ "josm", "rows", "preset" ]
aliases = [ "/questions/39854" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does rows="..." in JOSM Preset not work?](/questions/39854/why-does-rows-in-josm-preset-not-work)

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
<span id="post-39854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39854-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I created a Preset for JOSM (version 7777) that includes the following lines:</p>
<p>A. &lt;text key="description" text="Description" default="" delete_if_empty="true" rows="3"/&gt; B. &lt;multiselect key="amenity" delimiter="," text="Amenity" values="restaurant,bar" default="" delete_if_empty="true" rows="3"/&gt;</p>
<p>A. always gives 1 row, B. always 8, whatever value I use in rows.</p>
<p>What am I doing wrong?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-rows" rel="tag" title="see questions tagged &#39;rows&#39;">rows</span> <span class="post-tag tag-link-preset" rel="tag" title="see questions tagged &#39;preset&#39;">preset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Dec '14, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/9bf33603772d166237e50ace6c6e57f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jan%20van%20Bekkum&#39;s gravatar image" />
<p><span>Jan van Bekkum</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jan van Bekkum has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-39854" class="comments-container">
<span id="39864"></span>
<div id="comment-39864" class="comment">
<div id="post-39864-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Where did you learn about the rows attribute ? I cannot find an example in the default JOSM presets. AFAIK the UI for a description is a text box with 1 line, never seen one with multiple lines.</p>
<p>Perhaps those numbers cannot be changed.</p>
</div>
<div id="comment-39864-info" class="comment-info">
<span class="comment-age">(28 Dec '14, 07:32)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="40985"></span>
<div id="comment-40985" class="comment">
<div id="post-40985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>rows is only valid for &lt;multiselect&gt; so only B. should work. See <a href="https://josm.openstreetmap.de/wiki/TaggingPresets#XML">Tagging Presets</a></p>
<p><del>If not please fill a bug.</del> Was fixed see <a href="https://josm.openstreetmap.de/ticket/10941">https://josm.openstreetmap.de/ticket/10941</a></p>
<p>By the way, be careful with changing the delimiter from default semi-colon. It is only useful in special cases and the delimiter will be used also in the value if more than one is used.</p>
</div>
<div id="comment-40985-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 23:33)</span> <span class="comment-user userinfo">skyper</span>
</div>
</div>
</div>
<div id="comment-tools-39854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39854-form-container" class="comment-form-container">
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

<span id="39878"></span>

<div id="answer-container-39878" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39878-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-39878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The rows attribute doesn't seem to occur anywhere in the <a href="https://josm.openstreetmap.de/browser/trunk/data/tagging-preset.xsd#L166">presets xml template definition</a> (linked from <a href="https://josm.openstreetmap.de/wiki/TaggingPresets#Developanewpreset">here</a>).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '14, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-39878" class="comments-container">
<span id="40984"></span>
<div id="comment-40984" class="comment">
<div id="post-40984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Documentation is now in the JOSM wiki under <a href="https://josm.openstreetmap.de/wiki/TaggingPresets#XML">Tagging Presets</a> and rows does exist for quite some time now.</p>
</div>
<div id="comment-40984-info" class="comment-info">
<span class="comment-age">(12 Feb '15, 23:23)</span> <span class="comment-user userinfo">skyper</span>
</div>
</div>
</div>
<div id="comment-tools-39878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39878-form-container" class="comment-form-container">
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

