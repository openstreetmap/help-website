+++
type = "question"
title = "How to avoid duplicating information when tagging a power plant"
description = '''The Forney Energy Center west of Dallas has an outer perimeter with the following tags: &quot;landuse&quot;: &quot;industrial&quot;,  &quot;name&quot;: &quot;Forney Energy Center&quot;,  &quot;plant:output:electricity&quot;: &quot;1824 MW&quot;,  &quot;power&quot;: &quot;plant&quot; And several inner perimeters with demarcating the turbine hall, cooling fans, etc. I noticed tha...'''
date = "2019-12-11T23:44:00Z"
lastmod = "2019-12-12T13:21:00Z"
weight = 72077
keywords = [ "infrastructure", "power", "industrial_plant" ]
aliases = [ "/questions/72077" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to avoid duplicating information when tagging a power plant](/questions/72077/how-to-avoid-duplicating-information-when-tagging-a-power-plant)

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
<span id="post-72077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72077-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The <a href="https://www.openstreetmap.org/#map=17/32.75663/-96.48942">Forney Energy Center west of Dallas</a> has an outer perimeter with the following tags:</p>
<p><code>"landuse": "industrial", "name": "Forney Energy Center", "plant:output:electricity": "1824 MW", "power": "plant"</code></p>
<p>And several inner perimeters with demarcating the turbine hall, cooling fans, etc. I noticed that on the turbine hall it had the tag of <code>"source": "gas"</code>. Most other power plants I've looked at have this tagged at the top level. Are there conventions to follow? Note that I have (now I think erroneously) added operator and start date to the turbine hall but these <em>I think</em> these should be added to the polygon describing the perimeter of the plant. Thoughts on what to do / how to avoid duplicating info / link to suggested best practice(s ;) ) please.</p>
<p>Perhaps additionally the <a href="https://www.openstreetmap.org/way/39952924">turbine hall #39952924</a> should be tagged as a relation or subnode/ child of <a href="https://www.openstreetmap.org/way/39952915">the perimeter 39952915</a>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-infrastructure" rel="tag" title="see questions tagged &#39;infrastructure&#39;">infrastructure</span> <span class="post-tag tag-link-power" rel="tag" title="see questions tagged &#39;power&#39;">power</span> <span class="post-tag tag-link-industrial_plant" rel="tag" title="see questions tagged &#39;industrial_plant&#39;">industrial_plant</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '19, 23:44</strong></p>
<img src="https://secure.gravatar.com/avatar/688a8eb05930e8c8cd2606aa27ff8888?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TFJamMan&#39;s gravatar image" />
<p><span>TFJamMan</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TFJamMan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '19, 00:33</strong> </span></p>
</div>
</div>
<div id="comments-container-72077" class="comments-container">
&#10;</div>
<div id="comment-tools-72077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72077-form-container" class="comment-form-container">
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

<span id="72081"></span>

<div id="answer-container-72081" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72081-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-72081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TFJamMan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Don't avoid. Tagging both the plant and generator is the best practice.</p>
<ol>
<li><p>There could be generators of other sources not for power transmission, eg: emergency, start-up, facility use. <code>plant:source=</code> needs to be consistent with <code>generator:source=</code> for power output, same with <code>plant:output</code> == <code>generator:output</code></p></li>
<li><p>A power plant can have multiple power sources, value colon-separated in <code>plant:sourc=e</code>. <code>generator:source=</code> absolutely must be tagged explicitly for these. In time, there could be changes, renovations, and expansion in the plant in the future; or that there may be edits going on in OSM, like yours. Redundancy allows for easy reference, without questions needing to be asked every time.</p></li>
<li><p>Finally, tagging <code>generator:source</code> completes the info of the generator itself. This data would be direct and simple to use. No need to further query and infer from the enclosing area, for info as basic and inherent as this.</p></li>
</ol>
<p>Same for <code>opening_date=</code>. A generator could similarly have a different value. If you have the knowledge, certainly fill out as much as possible.</p>
<p>The area vs relation issue is long-standing. You are free to map so; surely welcomed and thanked if there's such an incomplete tagging of objects that, perhaps you aren't sure or are unable to totally sort it out yet. Usually this is done for more complicated cases, so I probably won't here.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Dec '19, 13:21</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Dec '19, 13:45</strong> </span></p>
</div>
</div>
<div id="comments-container-72081" class="comments-container">
&#10;</div>
<div id="comment-tools-72081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72081-form-container" class="comment-form-container">
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

