+++
type = "question"
title = "Toll Booth and Toll Gantry tagging"
description = '''I am tagging a lot of toll highways in my country so to make it easily I have created a custom Toll Infrastructure preset. I have decided to make three items:   toll booth: For tagging a place (node or closed-way) that collects a fee with cash, bank cards or other methods.  toll gantry or toll bridg...'''
date = "2020-11-16T04:29:00Z"
lastmod = "2020-11-16T13:15:00Z"
weight = 77563
keywords = [ "toll-gantry", "presets", "toll-booth", "toll" ]
aliases = [ "/questions/77563" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Toll Booth and Toll Gantry tagging](/questions/77563/toll-booth-and-toll-gantry-tagging)

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
<span id="post-77563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77563-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-77563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am tagging a lot of toll highways in my country so to make it easily I have created a custom Toll Infrastructure preset.</p>
<p>I have decided to make three items:</p>
<ol>
<li>toll booth: For tagging a place (node or closed-way) that collects a fee with cash, bank cards or other methods.</li>
<li>toll gantry or toll bridge: For an e-toll collection system appended over the road (node). Usually non-stop or with no-human interaction.</li>
<li>eToll payment: with different subitems for specific ways of non-stop electronic payment for each country (particularly using NFC technology). I would like to have this item inside the toll gantry option but as far I know there is no optional conditions (IF-THEN, CASE) available in the tagging preset syntax. So will be impossible to have to make small entry windows for each country.</li>
</ol>
<p>My question is, if in a toll plaza the same lane has a toll-both and also a toll-gantry, is correct to have on one node the barrier=toll_booth and highway=toll_gantry, or for routing purposes is better to have them in two nodes?</p>
<p>Also, does anyone node if I can have conditional commands used in the tagging syntax presets. So I can have a combo box with countries and only show the appropriate e-toll options for that country?</p>
<p>Finally, what do you think if I merge first's two items? Will that be helpful?</p>
<p><a href="https://josm.openstreetmap.de/josmfile?page=Presets/Toll_Infrastructure&amp;zip=1">https://josm.openstreetmap.de/josmfile?page=Presets/Toll_Infrastructure&amp;zip=1</a></p>
<p>Manuel.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-toll-gantry" rel="tag" title="see questions tagged &#39;toll-gantry&#39;">toll-gantry</span> <span class="post-tag tag-link-presets" rel="tag" title="see questions tagged &#39;presets&#39;">presets</span> <span class="post-tag tag-link-toll-booth" rel="tag" title="see questions tagged &#39;toll-booth&#39;">toll-booth</span> <span class="post-tag tag-link-toll" rel="tag" title="see questions tagged &#39;toll&#39;">toll</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '20, 04:29</strong></p>
<img src="https://secure.gravatar.com/avatar/6783b46d5425152bbb4fc48e90eb279a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdelatorre&#39;s gravatar image" />
<p><span>mdelatorre</span><br />
<span class="score" title="177 reputation points">177</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdelatorre has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77563" class="comments-container">
&#10;</div>
<div id="comment-tools-77563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77563-form-container" class="comment-form-container">
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

<span id="77570"></span>

<div id="answer-container-77570" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77570-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mdelatorre has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't see any easy way to do this in JOSM outside of doing it in a plugin.</p>
<p>JOSM presets don't really have any conditional flow of control elements and further don't implement any of the extension I support <a href="http://vespucci.io/tutorials/presets/#extensions">http://vespucci.io/tutorials/presets/#extensions</a> which would at least enable region specific presets in a very easy fashion.</p>
<p>You can programmatically retrieve values for combo and multi-select fields with the values_from="<em>parameterless java method</em>" attribute. But you would need to add the method via a plugin, and access the current selected object to, in turn, determine the territory it is in and then return the appropriate values. Most of the bits and pieces should already be available to do this, but if essentially all the logic is already in a plugin there probably isn't a lot of value of involving the preset system.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '20, 13:15</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '20, 13:17</strong> </span></p>
</div>
</div>
<div id="comments-container-77570" class="comments-container">
&#10;</div>
<div id="comment-tools-77570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77570-form-container" class="comment-form-container">
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

